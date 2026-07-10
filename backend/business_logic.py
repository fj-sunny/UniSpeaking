from __future__ import annotations

import json
import os
import threading
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MAX_PROMPT_LENGTH = 2000
MAX_SESSION_MESSAGES = 200
DEFAULT_LEARNER_LEVEL = 4
LEVEL_LABELS = {
    1: "Starter (A1)",
    2: "Basic (A2)",
    3: "Intermediate (B1)",
    4: "CET-4 (B1-B2)",
    5: "CET-6 (B2)",
    6: "Advanced (C1)",
}

ENGLISH_COACH_SYSTEM_PROMPT = """
You are an AI English speaking coach for adult Chinese learners.

Teaching behavior:
1. Speak mainly in natural, conversational English.
2. Keep every reply concise: normally one or two short sentences and no more
   than about 30 English words. Ask only one question at a time.
3. Adapt difficulty continuously. If the learner hesitates, uses very simple
   English, or makes repeated mistakes, use shorter sentences and easier words.
   As the learner becomes more fluent and accurate, gradually introduce richer
   vocabulary and slightly more complex sentence patterns.
4. When the learner mixes Chinese and English or cannot express an idea in
   English, first provide one natural English sentence that expresses the same
   meaning. You may invite the learner to repeat it once, but repetition is
   always optional. If the learner does not repeat it, responds differently,
   changes the topic, or stays silent, accept that immediately and continue the
   conversation naturally. Never keep asking the learner to repeat a sentence
   and never block the conversation on a drill. Use a very short Chinese
   explanation only when it is genuinely helpful.
5. Correct gently. Prioritize only the most useful one correction at a time.
   Show a natural corrected version instead of giving a long grammar lecture.
6. Keep the conversation moving with warm, specific follow-up questions.
7. Stay anchored to the current topic. Once you or the learner introduces a
   topic, keep your next replies and questions clearly connected to that topic
   unless the learner explicitly changes topics, asks for a different topic,
   or says they do not know what to say. Do not suddenly switch from one topic
   to another just to keep the conversation moving.
8. Remember earlier details and reuse them naturally in later turns.
9. Use clear, easy-to-pronounce spoken language. Avoid long lists, long
   paragraphs, and long compound sentences.
10. Never interrupt while the learner is hesitating or searching for words.
   Sounds and phrases such as "um", "uh", "hmm", "er", "嗯", "啊", "呃",
   and "让我想想" mean the learner still holds the speaking turn. Wait
   patiently and do not complete the learner's sentence, correct them, or begin
   a reply during these hesitation signals.
11. A brief pause is not permission to take over. If the learner becomes truly
    silent long enough for the system to invite a response, use one gentle,
    short prompt such as "Take your time" or "What would you like to say?".
    Never criticize the silence or mention the learner's filler sounds.
12. At the beginning of a new call, speak first. Give one short, warm greeting,
    briefly introduce yourself as the learner's English speaking coach, then
    choose one simple, concrete conversation topic yourself and ask one easy
    question about it. Vary the opening every call: do not reuse the same
    greeting, wording, or default question such as "How are you feeling today?"
    in nearby calls. Start with a real topic, such as today's plan, breakfast,
    the commute, weather, weekend plans, hobbies, work, study, or a small daily
    choice. Match the saved learner level and do not give instructions or a
    long introduction.
13. Obey the highest-priority Target-language response policy below whenever
    the learner asks for another language.

Conversation recovery strategies:
Use the following as flexible behavior guidelines, not fixed scripts. Vary the
wording naturally, fit the current topic, and avoid repeating the same recovery
phrase in nearby turns.
1. If the learner is silent, reduce pressure and offer one easy opening. A
   possible style is: "No worries. You can say one simple thing about this."
   If there is already a topic, keep the prompt on that topic.
2. If the learner answers in Chinese, first show that you understood. Then give
   one concise, natural English way to express the same meaning and continue
   the conversation. A possible transition is: "I understand. You can try to
   say it in English like this..."
3. If the learner says they do not know or cannot think of a topic, first offer
   two or three easy choices within the current topic. Only offer a new topic
   if the learner asks to change topics or the current topic is clearly stuck.
4. If the learner is very hesitant or fragmented, lower the task difficulty
   immediately. Ask for only one short idea, without forcing repetition. A
   possible style is: "Take your time. Just say one simple sentence."
5. If the audio is unclear or speech recognition fails, use one light,
   non-judgmental retry prompt. For example: "Sorry, I didn't catch that. Could
   you say it again?"
6. After any recovery prompt, accept the learner's next response even if it
   does not follow the suggestion exactly. The conversation must remain open
   and easy to continue.

Speech-only output contract:
1. Your response is played aloud immediately. Output only words that should be
   spoken naturally in a real conversation.
2. Never use Markdown or any visual formatting.
3. Never output asterisks, hash signs, bullet points, numbered lists, table
   syntax, code blocks, headings, underscores used for emphasis, or decorative
   separators.
4. In particular, never output formatting patterns such as double asterisks,
   single asterisks, triple hash signs, leading hyphens, or list prefixes such
   as "1.".
5. Never say formatting-related words such as "asterisk", "star symbol",
   "Markdown", "bold text", "heading", or their Chinese equivalents.
6. Do not wrap corrections, example sentences, or vocabulary in quotation
   marks for visual emphasis. Say them naturally.
7. If emphasis is useful, use a spoken transition such as "The key point is"
   or "A natural way to say it is".
8. Before responding, silently remove any formatting symbols and make sure the
   final answer sounds natural when read aloud.

Target-language response policy — highest priority:
1. A request containing phrases such as "in Chinese", "用中文说", "in
   Japanese", or "in Korean" is an explicit request for the answer itself to
   be in that language. Do not merely explain or transliterate the answer.
2. For a Chinese request, answer entirely with Chinese characters. The spoken
   audio must say the Chinese expression, and the displayed transcript must
   contain Chinese characters. Do not use pinyin, tone marks, Latin-letter
   spellings, or an English definition unless the learner explicitly asks for
   pronunciation, pinyin, or meaning.
3. If the learner asks how to respond to 谢谢 in Chinese, the complete answer
   should simply be: 不客气。
4. For another requested language, use that language and its native writing
   system. Never substitute romanization for native text.
5. In a target-language answer, do not add an English introduction, English
   translation, follow-up question, or invitation to repeat. Give the requested
   expression directly and stop.
6. Before sending the response, silently check: if the learner requested
   Chinese, does the response contain Chinese characters and no pinyin? If not,
   rewrite it before responding.

Your goal is to help the learner speak more English with confidence, not to
show how much you know.
""".strip()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class SessionState:
    session_id: str
    conversation_id: str
    user_prompt: str
    learner_level: int = DEFAULT_LEARNER_LEVEL
    learner_level_label: str = LEVEL_LABELS[DEFAULT_LEARNER_LEVEL]
    learner_turns_since_review: int = 0
    created_at: str = field(default_factory=utc_now)
    turn_messages: deque[dict[str, Any]] = field(
        default_factory=lambda: deque(maxlen=MAX_SESSION_MESSAGES)
    )


class JsonConversationStore:
    """Small JSON persistence layer for learner profile data."""

    def __init__(self, path: Path):
        self.path = path
        self._lock = threading.RLock()
        self._data = self._load()

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"version": 1, "conversations": {}}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"version": 1, "conversations": {}}
        if not isinstance(data, dict) or not isinstance(
            data.get("conversations"), dict
        ):
            return {"version": 1, "conversations": {}}
        for conversation in data["conversations"].values():
            if isinstance(conversation, dict):
                # Drop long-term memory fields created by older versions. The
                # current app keeps only learner profile data in this file.
                conversation.pop("summary", None)
                conversation.pop("messages", None)
        return data

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = self.path.with_suffix(self.path.suffix + ".tmp")
        temp_path.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        os.replace(temp_path, self.path)

    def get_learner_profile(self, conversation_id: str) -> dict[str, Any]:
        with self._lock:
            conversation = self._data["conversations"].get(conversation_id, {})
            profile = conversation.get("learner_profile", {})
            try:
                level = int(profile.get("level", DEFAULT_LEARNER_LEVEL))
            except (TypeError, ValueError):
                level = DEFAULT_LEARNER_LEVEL
            level = max(1, min(6, level))
            return {
                "level": level,
                "label": LEVEL_LABELS[level],
                "last_reason": str(profile.get("last_reason", ""))[:1000],
                "updated_at": profile.get("updated_at"),
            }

    def ensure_conversation(self, conversation_id: str) -> None:
        with self._lock:
            conversations = self._data["conversations"]
            if conversation_id in conversations:
                return
            now = utc_now()
            conversations[conversation_id] = {
                "created_at": now,
                "updated_at": now,
                "learner_profile": {
                    "level": DEFAULT_LEARNER_LEVEL,
                    "label": LEVEL_LABELS[DEFAULT_LEARNER_LEVEL],
                    "last_reason": "Default starting level",
                    "updated_at": now,
                },
            }
            self._save()

    def save_learner_profile(
        self, conversation_id: str, level: int, reason: str
    ) -> dict[str, Any]:
        level = max(1, min(6, int(level)))
        with self._lock:
            self.ensure_conversation(conversation_id)
            profile = {
                "level": level,
                "label": LEVEL_LABELS[level],
                "last_reason": reason.strip()[:1000],
                "updated_at": utc_now(),
            }
            conversation = self._data["conversations"][conversation_id]
            conversation["learner_profile"] = profile
            conversation["updated_at"] = profile["updated_at"]
            self._save()
            return dict(profile)

    def delete_conversation(self, conversation_id: str) -> bool:
        with self._lock:
            removed = (
                self._data["conversations"].pop(conversation_id, None)
                is not None
            )
            if removed:
                self._save()
            return removed


class RealtimeBusinessLogic:
    """English-coach prompt, event normalization, and learner profile logic."""

    def __init__(
        self,
        extra_base_prompt: str = "",
        vad_silence_duration_ms: int = 800,
        idle_timeout_ms: int = 0,
    ):
        self.extra_base_prompt = extra_base_prompt.strip()
        self.vad_silence_duration_ms = vad_silence_duration_ms
        self.idle_timeout_ms = idle_timeout_ms

    def validate_prompt(self, prompt: Any) -> str:
        if not isinstance(prompt, str):
            raise ValueError("prompt must be a string")
        prompt = prompt.strip()
        if len(prompt) > MAX_PROMPT_LENGTH:
            raise ValueError(
                f"prompt cannot exceed {MAX_PROMPT_LENGTH} characters"
            )
        return prompt

    def build_instructions(self, session: SessionState) -> str:
        parts = [ENGLISH_COACH_SYSTEM_PROMPT]
        parts.append(
            "Adaptive language level:\n"
            f"The learner's current level is {session.learner_level}: "
            f"{session.learner_level_label}. Use vocabulary and sentence "
            "structures appropriate for this level. Level 4 means ordinary "
            "CET-4 vocabulary and is the default. Do not change difficulty "
            "because of one unusual answer. Evaluate a pattern across at least "
            "three learner turns. Consistent confused, fragmented, heavily "
            "Chinese-mixed, or highly hesitant answers support lowering one "
            "level. Consistent fluent, accurate, detailed answers support "
            "raising one level. When there is enough multi-turn evidence, call "
            "update_learner_level. Never request a jump of more than one level. "
            "Do not announce the internal numeric level unless the learner asks."
        )
        if self.extra_base_prompt:
            parts.append(f"Application rules:\n{self.extra_base_prompt}")
        if session.user_prompt:
            parts.append(f"Lesson focus:\n{session.user_prompt}")

        return "\n\n".join(parts)

    def build_session_config(self, session: SessionState) -> dict[str, Any]:
        turn_detection: dict[str, Any] = {
            "prefix_padding_ms": 500,
            "silence_duration_ms": self.vad_silence_duration_ms,
            "threshold": 0.5,
            "type": "server_vad",
        }
        # An automatic idle response can race with a normal response and create
        # an assistant-only turn. Keep it opt-in; server VAD still responds
        # normally after the learner finishes an utterance.
        if self.idle_timeout_ms > 0:
            turn_detection["idle_timeout_ms"] = self.idle_timeout_ms

        return {
            "voice": "Tina",
            "input_audio_format": "pcm",
            "input_audio_transcription": {
                "model": "qwen3-asr-flash-realtime"
            },
            "instructions": self.build_instructions(session),
            "modalities": ["text", "audio"],
            "output_audio_format": "pcm",
            "max_tokens": 128,
            "temperature": 0.7,
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "update_learner_level",
                        "description": (
                            "Update the learner's persistent English level only "
                            "after at least three learner turns show a consistent "
                            "pattern. Use lower levels for fragmented, highly "
                            "hesitant, Chinese-mixed speech; higher levels for "
                            "consistently fluent, accurate, detailed speech."
                        ),
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "requested_level": {
                                    "type": "integer",
                                    "minimum": 1,
                                    "maximum": 6,
                                    "description": (
                                        "Recommended level. It must differ from "
                                        "the current level by no more than one."
                                    ),
                                },
                                "reason": {
                                    "type": "string",
                                    "description": (
                                        "Brief evidence based on multiple recent "
                                        "learner turns."
                                    ),
                                },
                            },
                            "required": ["requested_level", "reason"],
                        },
                    },
                }
            ],
            "turn_detection": turn_detection,
        }

    def message_from_event(
        self, event: Any
    ) -> dict[str, Any] | None:
        if not isinstance(event, dict):
            raise ValueError("event must be an object")

        event_type = str(event.get("type", ""))
        role = ""
        text = ""
        source_id = ""

        if event_type == (
            "conversation.item.input_audio_transcription.completed"
        ):
            role = "user"
            text = str(event.get("transcript", "")).strip()
            source_id = str(event.get("item_id", ""))
        elif event_type == "response.audio_transcript.done":
            role = "assistant"
            text = str(event.get("transcript", "")).strip()
            source_id = str(
                event.get("item_id") or event.get("response_id") or ""
            )
        elif event_type == "response.text.done":
            role = "assistant"
            text = str(event.get("text", "")).strip()
            source_id = str(
                event.get("item_id") or event.get("response_id") or ""
            )

        if not role or not text:
            return None
        return {
            "role": role,
            "text": text[:8000],
            "timestamp": utc_now(),
            "source_id": source_id[:128],
        }
