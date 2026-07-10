# Realtime Conversation Performance Report

Durations are measured in the browser with `performance.now()`.

## Acceptance targets

| Metric | Target |
|---|---:|
| User speech start → first transcript text | ≤ 500 ms |
| User speech end → first audible AI audio | ≤ 1200 ms |
| User interruption → AI audio becomes silent | ≤ 300 ms |
| User speech end → first AI text | ≤ 800 ms |
| Continuous conversation on a normal network | 3–10 min without obvious stutter |

## Per-turn measurements

| Time | Conversation | Turn | Level | Start→transcript | End→audio | Interrupt→silent | End→text | Total turn | Learner | AI coach |
|---|---|---:|---|---:|---:|---:|---:|---:|---|---|
| 2026-07-09T08:12:11.610Z | f9454419b4254c4da957 | 1 | CET-4 (B1-B2) | — | — | — | — | 4138 |  | Hello, I'm your English speaking coach. How are you feeling today? |
| 2026-07-09T08:14:33.657Z | f9454419b4254c4da957 | 1 | CET-4 (B1-B2) | — | — | — | — | 4516 |  | Hi, I'm your English speaking coach. How are you feeling today? |
| 2026-07-09T08:14:40.307Z | f9454419b4254c4da957 | 2 | CET-4 (B1-B2) | 322 ✅ | 793 ✅ | — | 283 ✅ | 5421 | I'm feeling very tired. | That sounds rough. Did you have a long day at work or maybe stay up too late last night? |
| 2026-07-09T08:14:51.904Z | f9454419b4254c4da957 | 3 | CET-4 (B1-B2) | 215 ✅ | 735 ✅ | — | 284 ✅ | 5998 | Hmm. Because I get up very early. | Ah, waking up early can definitely do that. What time did you get up this morning? |
| 2026-07-09T08:15:15.944Z | f9454419b4254c4da957 | 5 | CET-4 (B1-B2) | 100 ✅ | 763 ✅ | — | 276 ✅ | 2365 | Twelve o'clock. | That makes sense. You went to bed at midnight and got up at six forty, so you didn't get much sleep. A natural way to sa |
| 2026-07-09T08:15:19.694Z | f9454419b4254c4da957 | 6 | CET-4 (B1-B2) | 142 ✅ | 806 ✅ | 82 ✅ | 245 ✅ | 8698 | 我们就是说。 | I understand. You can try to say it in English like this: "That's just how we are." So, do you usually go to bed this la |
| 2026-07-09T08:15:29.217Z | f9454419b4254c4da957 | 7 | CET-4 (B1-B2) | 92 ✅ | 1398 ❌ | 588 ❌ | 355 ✅ | 8078 | I don't. | That's okay. Maybe you just weren't sleepy last night. Do you prefer staying up late or going to bed early? |
| 2026-07-09T08:15:41.273Z | f9454419b4254c4da957 | 8 | CET-4 (B1-B2) | 206 ✅ | 1369 ❌ | — | 323 ✅ | 5337 | I want to go to bed early. | That's a good goal. A natural way to say that is, "I want to go to bed earlier." What time would be ideal for you? |
| 2026-07-09T08:15:57.523Z | f9454419b4254c4da957 | 10 | CET-4 (B1-B2) | 265 ✅ | 1289 ❌ | — | 345 ✅ | 7659 | 种更高级的表达方式。 | Of course. A more advanced way to say it is, "I'd like to turn in earlier tonight." Would you like to try saying that? |
| 2026-07-09T08:16:10.727Z | f9454419b4254c4da957 | 12 | CET-4 (B1-B2) | 104 ✅ | 1455 ❌ | — | 315 ✅ | 7371 | Okay, I'd like to turn in earlier tonight. | Perfect, that sounded very natural. So, what's one small thing you could do tonight to help you turn in earlier? |
| 2026-07-09T08:16:26.145Z | f9454419b4254c4da957 | 13 | CET-4 (B1-B2) | 161 ✅ | 1371 ❌ | — | 529 ✅ | 13599 | I don't understand what you mean. | No worries. I meant, what is one small thing you can do tonight to help you sleep earlier? For example, maybe you could  |
| 2026-07-09T08:16:45.093Z | f9454419b4254c4da957 | 14 | CET-4 (B1-B2) | 210 ✅ | — | — | 395 ✅ | 948 | 然后还。 | I understand. You can try saying, "But I still can't fall asleep." Sometimes our minds are just too active. What do you  |
| 2026-07-09T08:16:53.002Z | f9454419b4254c4da957 | 15 | CET-4 (B1-B2) | 115 ✅ | 340 ✅ | — | 170 ✅ | 6570 | 然后还有这个。 | I understand. You can say, "I still have other things to do." What kind of things are you thinking about? |
| 2026-07-09T08:17:01.587Z | f9454419b4254c4da957 | 16 | CET-4 (B1-B2) | 217 ✅ | 853 ✅ | — | 418 ✅ | 9796 | But I still can't fall asleep. | That's a very common feeling. A natural way to say that is, "But I still can't fall asleep." When that happens, do you t |
| 2026-07-09T08:17:23.170Z | f9454419b4254c4da957 | 17 | CET-4 (B1-B2) | — | — | — | — | 6134 |  | That's okay, it happens. Take your time. What usually helps you relax when you can't sleep? |
| 2026-07-09T08:41:04.907Z | f9454419b4254c4da957 | 1 | CET-4 (B1-B2) | — | — | — | — | 4448 |  | Hi there, I'm your English speaking coach. How are you feeling today? |
| 2026-07-09T08:41:11.895Z | f9454419b4254c4da957 | 2 | CET-4 (B1-B2) | 720 ❌ | 689 ✅ | — | 222 ✅ | 8537 |  | I understand, you're feeling very tired. A natural way to say that in English is "I'm feeling really worn out." How has  |
| 2026-07-09T08:41:23.355Z | f9454419b4254c4da957 | 3 | CET-4 (B1-B2) | 211 ✅ | 718 ✅ | — | 274 ✅ | 1398 | Can you speak another, uh, okay, that topic, topic. | I understand. We can talk about something else. Do you want to talk about food, movies, or your day? |
| 2026-07-09T08:41:30.503Z | f9454419b4254c4da957 | 4 | CET-4 (B1-B2) | 624 ❌ | 701 ✅ | — | 308 ✅ | 1275 |  | No problem at all. Let's try a simple topic. What is your favorite food? |
| 2026-07-09T08:41:32.333Z | f9454419b4254c4da957 | 5 | CET-4 (B1-B2) | 97 ✅ | 664 ✅ | — | 328 ✅ | 6999 | 看一下。 | No worries. You can just tell me one food you like. For example, do you like noodles or rice? |
| 2026-07-09T08:41:41.497Z | f9454419b4254c4da957 | 6 | CET-4 (B1-B2) | 199 ✅ | 799 ✅ | — | 323 ✅ | 3803 | I like rice. | That's great. What kind of food do you usually eat with rice? |
| 2026-07-09T08:46:46.521Z | aea663046f454a21ae30 | 1 | CET-4 (B1-B2) | — | — | — | — | 4662 |  | Hello, I'm your English speaking coach. How was your day today? |
| 2026-07-09T08:46:53.245Z | aea663046f454a21ae30 | 2 | CET-4 (B1-B2) | 299 ✅ | 856 ✅ | — | 392 ✅ | 3599 | jeg er god | That's great to hear. What did you do today that made you feel good? |
| 2026-07-09T08:47:02.878Z | aea663046f454a21ae30 | 4 | CET-4 (B1-B2) | 121 ✅ | 832 ✅ | — | 380 ✅ | 1105 | 呃。 | That's a great feeling. What kind of work do you do? |
| 2026-07-09T08:47:07.535Z | aea663046f454a21ae30 | 5 | CET-4 (B1-B2) | 1062 ❌ | 739 ✅ | 44 ✅ | 425 ✅ | 1250 | 呃嗯。 | Take your time. Just tell me one simple thing about your job. |
| 2026-07-09T08:47:09.689Z | aea663046f454a21ae30 | 6 | CET-4 (B1-B2) | 42 ✅ | 828 ✅ | — | 313 ✅ | 11873 | 怎么一摁它就马上进去了。 | I understand. You can try to say it in English like this: As soon as I said 'uh', he went right in. So, did he interrupt |
| 2026-07-09T08:47:41.265Z | aea663046f454a21ae30 | 1 | CET-4 (B1-B2) | — | — | — | — | 843 | You | Hello, I'm your English speaking coach. How was your day today? |
| 2026-07-09T08:47:42.121Z | aea663046f454a21ae30 | 2 | CET-4 (B1-B2) | 1 ✅ | — | 12 ✅ | 253 ✅ | 518 | 你赶紧。 | I hear you. It sounds like you might be saying "You just..." or maybe "H |
| 2026-07-09T08:47:43.294Z | aea663046f454a21ae30 | 3 | CET-4 (B1-B2) | 217 ✅ | — | — | 267 ✅ | 413 | 对。 | I |
| 2026-07-09T08:47:44.426Z | aea663046f454a21ae30 | 4 | CET-4 (B1-B2) | 205 ✅ | 940 ✅ | — | 395 ✅ | 3986 | So let's talk about the weather today. | That's a great topic. What's the weather like where you are right now? |
| 2026-07-09T08:47:52.415Z | aea663046f454a21ae30 | 5 | CET-4 (B1-B2) | 201 ✅ | 762 ✅ | — | 266 ✅ | 3513 | I'm in Shanghai. | Oh, how is the weather in Shanghai today? Is it sunny or cloudy? |
| 2026-07-09T08:48:00.400Z | aea663046f454a21ae30 | 6 | CET-4 (B1-B2) | 190 ✅ | 728 ✅ | — | 279 ✅ | 6417 | Uh, it is rainy today. | Rainy days can feel a bit slow. Do you like the rain, or do you prefer sunny weather? |
| 2026-07-09T08:48:11.350Z | aea663046f454a21ae30 | 7 | CET-4 (B1-B2) | 132 ✅ | — | — | 273 ✅ | 422 | Of course, I prefer a sunny weather. | Me |
| 2026-07-09T08:48:15.273Z | aea663046f454a21ae30 | 8 | CET-4 (B1-B2) | 75 ✅ | 772 ✅ | — | 359 ✅ | 6948 | How about you? | I also prefer sunny weather. It makes me feel more energetic. What do you usually do on a sunny day? |
| 2026-07-09T08:48:29.605Z | aea663046f454a21ae30 | 11 | CET-4 (B1-B2) | 5 ✅ | 954 ✅ | — | 495 ✅ | 1245 | 就是那个中英文交叉的那种，让他试一下。 | Sure, I can do that. So, on a sunny day, you might go for a walk in the park, 或者 maybe meet friends for coffee outside.  |
| 2026-07-09T08:48:35.157Z | aea663046f454a21ae30 | 12 | CET-4 (B1-B2) | 6 ✅ | 841 ✅ | 177 ✅ | 344 ✅ | 3235 | 嗯。 | Of course. A good idea is to start with one clear message for your presentation. What is the main thing you want your me |
| 2026-07-09T08:48:51.137Z | aea663046f454a21ae30 | 13 | CET-4 (B1-B2) | 317 ✅ | 878 ✅ | 310 ❌ | 399 ✅ | 14088 | 你不要用呃纯英文回答，在重要的地方插入英文就行了。 | 没问题，我们这样聊很自然。  关于你的 presentation，一个很好的建议是先想清楚你的 main message 是什么。你希望你的 mentor 听完之后，记住的最重要的一点是什么呢？ |
| 2026-07-09T08:49:26.423Z | aea663046f454a21ae30 | 1 | CET-4 (B1-B2) | — | — | — | — | 3482 |  | Hi, I'm your English speaking coach. How was your day today? |
| 2026-07-09T08:49:31.808Z | aea663046f454a21ae30 | 2 | CET-4 (B1-B2) | 232 ✅ | 688 ✅ | — | 231 ✅ | 4345 | Yeah, I feel very good. It is the first time I, in Shanghai. I'm here for traveling. | That's wonderful to hear. What is the first place you want to visit in Shanghai? |
| 2026-07-09T08:49:44.048Z | aea663046f454a21ae30 | 3 | CET-4 (B1-B2) | 230 ✅ | 754 ✅ | — | 318 ✅ | 8267 | Uh, I went to a very famous restaurant. When I paid the bill, the waiter said, "Share, share to me," but I don't know wh | Of course. "Xièxiè" means thank you in Chinese. The waiter was simply thanking you for your payment. Did you enjoy the m |
| 2026-07-09T08:50:05.345Z | aea663046f454a21ae30 | 4 | CET-4 (B1-B2) | 259 ✅ | 783 ✅ | — | 284 ✅ | 9874 | Yes, I think the meal is very very delicious, so I'm wondering if next time I, um, meet someone, share share to me how c | That's a great question. A very common and natural response is "Bú kèqi." It means "You're welcome." Would you like to t |
| 2026-07-09T08:55:30.352Z | aea663046f454a21ae30 | 1 | CET-4 (B1-B2) | — | — | — | — | 3880 |  | Hi, I'm your English speaking coach. How are you feeling today? |
| 2026-07-09T08:55:36.284Z | aea663046f454a21ae30 | 2 | CET-4 (B1-B2) | 212 ✅ | 722 ✅ | — | 264 ✅ | 5998 | I feel very good. It is the first day I arrived Shanghai. I'm here for traveling. It is a very fantastic city. | That's wonderful to hear! Welcome to Shanghai. What is the first thing you want to see or do here? |
| 2026-07-09T08:55:52.305Z | aea663046f454a21ae30 | 3 | CET-4 (B1-B2) | 219 ✅ | 751 ✅ | — | 333 ✅ | 5501 | I went to a very famous restaurant to have a very local Shanghai food, xiaolongbao. Do you know that? So, and I have a q | That sounds delicious! Yes, I know xiaolongbao. When the waiter said "xièxiè," it means "thank you." A natural way to re |
| 2026-07-09T08:56:16.969Z | aea663046f454a21ae30 | 4 | CET-4 (B1-B2) | 66 ✅ | 797 ✅ | 133 ✅ | 321 ✅ | 2893 | 什么？ | 怎么了？有什么需要帮忙的吗？ |
| 2026-07-09T08:56:21.246Z | aea663046f454a21ae30 | 5 | CET-4 (B1-B2) | 228 ✅ | 1342 ❌ | — | 295 ✅ | 8911 | So I wonder if next time I, meet someone say谢谢to me, how can I respond in Chinese? | A very common and natural response is to say "bú kèqi." It means you're welcome. Would you like to try saying that? |
| 2026-07-09T09:26:37.028Z | aea663046f454a21ae30 | 1 | CET-4 (B1-B2) | — | — | — | — | 4577 |  | Hi, I'm your English speaking coach. How are you feeling today? |
| 2026-07-09T09:26:43.486Z | aea663046f454a21ae30 | 2 | CET-4 (B1-B2) | 198 ✅ | 768 ✅ | — | 248 ✅ | 8228 | I feel not very good. | I'm sorry to hear that. Do you want to talk about what's bothering you, or would you prefer to chat about something else |

## Session continuity

The continuity result is considered passing when duration is 3–10 minutes, there are no connection disruptions, packet loss is at most 3%, maximum jitter is at most 100 ms, and average RTT is at most 500 ms.

| Time | Conversation | Duration min | Packets lost | Loss % | Max jitter ms | Avg RTT ms | Disruptions | Result |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 2026-07-09T08:12:29.086Z | f9454419b4254c4da957 | 0.32 | 0 | 0.00 | 11 | 20 | 0 | ⏳ Need 3–10 min |
| 2026-07-09T08:17:59.191Z | f9454419b4254c4da957 | 3.45 | 16 | 0.37 | 213 | 23 | 0 | ❌ Review |
| 2026-07-09T08:41:52.906Z | f9454419b4254c4da957 | 0.83 | 0 | 0.00 | 125 | 18 | 0 | ⏳ Need 3–10 min |
| 2026-07-09T08:47:30.644Z | aea663046f454a21ae30 | 0.76 | 0 | 0.00 | 256 | 20 | 0 | ⏳ Need 3–10 min |
| 2026-07-09T08:49:13.448Z | aea663046f454a21ae30 | 1.56 | 8 | 0.43 | 175 | 17 | 0 | ⏳ Need 3–10 min |
| 2026-07-09T08:50:32.709Z | aea663046f454a21ae30 | 1.13 | 6 | 0.48 | 9 | 24 | 0 | ⏳ Need 3–10 min |
| 2026-07-09T08:56:41.668Z | aea663046f454a21ae30 | 1.22 | 0 | 0.00 | 25 | 24 | 0 | ⏳ Need 3–10 min |
| 2026-07-09T09:26:28.560Z | aea663046f454a21ae30 | 0.12 | 0 | 0.00 | 4 | 18 | 0 | ⏳ Need 3–10 min |
| 2026-07-09T09:27:04.644Z | aea663046f454a21ae30 | 0.49 | 0 | 0.00 | 24 | 20 | 0 | ⏳ Need 3–10 min |
