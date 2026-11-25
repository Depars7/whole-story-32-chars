# Tell a Whole Story in 32 Characters — DESIGN

Bounty: `u-xvader-tell-a-whole-story-in-32-characters-f86dd978` ($2, winner takes all, closes 27 Nov 2026 00:25 WIB).
Gate (RULES.txt): `/output/entry.txt` must be UTF-8 text of **1 to 32 characters**, not only whitespace. No trailing newline is written, so the character count is exactly the name's length.

Judge (z-ai/glm-5.3-flash, pairwise, criteria in order):
1. A Wi-Fi network name of at most 32 characters that reads as a joke and hints at a story.
2. The joke lands on the first read, with a clear twist or punchline a stranger gets without explanation.
3. It tells a whole story: implies a situation, a character, and something that happened.
4. Fresh: avoids the stock Wi-Fi jokes everyone has seen (FBI Surveillance Van, Pretty Fly for a Wi-Fi, It Burns When IP, VIRUS.EXE, 404 Not Found, LAN Solo, Abraham Linksys, TellMyWiFiLoveHer, No Free WiFi, Skynet...), or turns a familiar one into something new.
5. Tight: every character earns its place, clean, readable, easy to say out loud.

All character counts below were computed with Python `len()` (Unicode code points), not counted by hand.

## Candidates (16)

| # | Candidate | Chars | Notes |
|---|-----------|-------|-------|
| 1 | `MyExTookTheDogAndTheRouter` | 26 | **PICKED.** Breakup: ex took the dog AND the router. Escalating pettiness; the punchline is meta — the router is the very network you are reading. Character + situation + event, fresh, tight. |
| 2 | `SheLeftMeForTheITGuyNextDoor` | 28 | Good twist (IT guy, Wi-Fi-adjacent), but "left me for X" is a well-worn trope; weaker than #1. |
| 3 | `GrandmaUnpluggedMeMidBossFight` | 30 | Funny, clear character + event, but grandma-unplugs-the-router is a known trope. |
| 4 | `SheTookTheKids_TheDog_TheWiFi` | 29 | Escalation list like #1, but underscores hurt readability and "TheWiFi" is a weaker punchline than "TheRouter". |
| 5 | `TheBabyAteTheEthernetCable` | 26 | Cute, situation clear, but the punchline is soft — no twist, just a mishap. |
| 6 | `HeProposedViaWiFiPassword1234` | 29 | Sweet twist, but "password1234" is stock-ish and the story is thin (no conflict). |
| 7 | `ExMovedOut_TookPasswordWithHer` | 30 | Same family as #1, weaker ending (a password vs. the physical router) and underscores. |
| 8 | `GrandmaThinksTheRouterIsHaunted` | 31 | Funny premise, but no event happened — fails criterion 3 (no "something that happened"). |
| 9 | `WiFiDown_BabyBorn_NoSleep2026` | 29 | A list of facts, no twist or punchline. |
| 10 | `DadChangedPasswordAfterMyGrades` | 31 | Clear story, but dad-changes-the-password is a common trope. |
| 11 | `MomUnpluggedItDuringMyFinals` | 28 | Same family as #3/#10; unplug-during-finals is familiar. |
| 12 | `MyCatSatOnTheRouterAgain_404` | 28 | Cat-on-router is a known meme and `404` is a stock Wi-Fi joke. |
| 13 | `RoommateAteMyLeftoversAgain5G` | 29 | Weak punchline; `5G` is tacked on and earns nothing. |
| 14 | `LandlordRaisedRent_KilledWiFi` | 29 | Two grievances, no twist. |
| 15 | `IToldMomItWasJustAPhase_1998` | 28 | Has a time twist, but the story is vague — what was the phase? |
| 16 | `MyExTookTheDogAndTheRouter5G` | 28 | #1 with `5G` appended; the suffix adds nothing and dilutes the punchline. Rejected. |

## Final choice

**`MyExTookTheDogAndTheRouter` — 26 characters.**

Why it wins against the judge's criteria, in order:
1. Wi-Fi name, 26 ≤ 32 characters, reads as a joke.
2. Punchline lands instantly: dog → router, an escalation from sentimental to petty-practical.
3. Whole story: a breakup (situation), the ex (character), she left and took the dog and the router (event). The reader fills in the rest — the empty flat, the silence, the narrator staring at "No networks found".
4. Fresh: not a stock Wi-Fi joke; the meta twist (the stolen router IS this network name) is new.
5. Tight: CamelCase, no filler words, no separators, no tacked-on `5G`/`404`; 6 characters to spare and none needed.

## Program

`main.py` is deterministic: it writes exactly the entry above, with no trailing newline, to `/output/entry.txt` (mode 0644, so the grader can read it as another user), and nothing else. Two local runs must produce byte-identical output.
