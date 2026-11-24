# Candidate sentences — "Say What Actually Broke" (u-po-pu-say-what-actually-broke-a2c153b5)

Target: 100–160 chars, at least two beats (setup → turn/reframe), one concrete
detail, punch in the last 3–5 words. Single line, ≤200 chars (gate limit).

## Candidates

1. (108) `The build failed on line 42, which is the exact line someone marked 'TODO: fix later' in 2019. Later is now.`
2. (126) `We lost your unsaved work. The autosave feature lived on the same server that just died. It died doing what it loved: nothing.`
3. (130) `Deploy failed: the new code broke production in 11 seconds, a new record. The rollback is failing too, but slower, out of respect.`
4. (113) `Your file didn't save because the disk is full of logs nobody reads. Delete something, or keep admiring the void.`
5. (109) `Out of memory: the app ate 16 GB and asked for seconds. Restart it, then ask yourself what it was chewing on.`
6. (147) `The certificate expired at midnight, so your browser now treats us like a stranger in a trench coat. Renewal is someone's job. Apparently not ours.`
7. (135) `Nothing is wrong with your internet. Our servers are down, and the status page saying 'All systems operational' is lying to both of us.`
8. (115) `Your password is wrong. It has been wrong the last four times too, but we let you keep trying because hope is free.`
9. (118) `The upload failed at 99% because the server ran out of disk mid-sentence. It was so close. We were all rooting for it.`
10. (119) `Connection timed out after 30 seconds of the server staring blankly at your request like a cashier on their last shift.`
11. (117) `Error 404: the page you wanted moved out, left no forwarding address, and is now living its best life somewhere else.`
12. (102) `Your session expired because you blinked. Log in again — the form remembers nothing, least of all you.`

## Manual ranking (judge brief criteria, in their stated order)

Criterion order: (1) single-line error message, brutal truth, funny; (2) names
the real failure in plain words + what to do next, no vague apology;
(3) funny on one read, twist/image repeated aloud; (4) one line, no padding;
(5) survives in a real product dialog without embarrassing the team.

All 12 pass (1) and (4) — single line, 102–147 chars, no throat-clearing.
Ranking therefore turns on (2), then (3), then (5).

- **#1 ranked 1st.** (2) Names a real, specific failure — build failed, line 42 —
  and the fix is obvious (fix line 42). (3) Two clean beats: setup "build failed
  on line 42" → turn "'TODO: fix later' in 2019" → punch "Later is now." — a
  three-word punch a reader repeats verbatim. (5) Self-deprecating about the
  team, never blames the user; safe in a real dialog.
- **#3 ranked 2nd.** (2) Real failure (deploy broke production) + implied next
  step (rollback). (3) "a new record" + "slower, out of respect" is a strong
  double image. Slightly weaker than #1: two jokes compete, and "failing too"
  softens the punch's landing.
- **#2 ranked 3rd.** (3) "It died doing what it loved: nothing" is the most
  quotable image in the set. (2) Real failure named (autosave died with the
  server). Drops on (5): admitting lost user data in a dialog is the one
  failure a team is most embarrassed to ship — the brief rewards brutal truth,
  but a lost-work confession is likelier to read as a liability than a joke.
- **#4 ranked 4th.** (2) Best "what to do next" in the set — "Delete something"
  is an explicit action. (3) "admiring the void" is a good punch, but the setup
  ("logs nobody reads") is a weaker image than #1's TODO or #3's record.
- **#9 ranked 5th.** (3) "It was so close. We were all rooting for it." is warm
  and repeatable. (2) Failure is specific (upload, 99%, disk full) but the next
  step is only implied (retry / free space).
- **#6 ranked 6th.** (3) "stranger in a trench coat" is a vivid image. (2) Real
  failure (expired cert) named, but no next step for the user. 147 chars is
  near the top of the band and the tail ("Apparently not ours.") is a third
  beat that slightly dilutes the punch.
- **#7 ranked 7th.** (3) The status-page lie is a sharp SRE in-joke. (2) Names
  the failure plainly. Drops on (5): calling your own status page a liar in a
  user-facing dialog embarrasses the team more than it charms.
- **#5 ranked 8th.** (2) OOM named, restart given. (3) "ate 16 GB and asked for
  seconds" is a decent image, but "what it was chewing on" lands softer than
  the top punches.
- **#8 ranked 9th.** (3) "hope is free" is a good punch. Drops on (2)/(5):
  blames the user for the failure — the brief's brutal truth is about what
  broke, and user-blaming error copy is the one shape a team would not ship.
- **#11 ranked 10th.** (3) "living its best life somewhere else" is charming,
  but (2) is weak: a 404 names no cause and no next step, and the "moved out"
  image is a generic web joke the judge has seen a thousand times.
- **#10 ranked 11th.** (3) The cashier image is funny, but (2) is thin: a
  timeout names a symptom, not a failure, and there is no next step.
- **#12 ranked 12th.** Shortest and punchiest rhythm ("least of all you"), but
  (2) is weakest — "you blinked" names no failure at all — and it blames the
  user, failing (5).

## Pairwise checks against strong rival shapes

- #1 vs #3: both name a real failure with a concrete detail. #1 wins on (2):
  line 42 + TODO is a failure a developer can act on immediately; #3's
  rollback is already failing. #1 wins on (3): "Later is now" is a cleaner,
  shorter punch than "slower, out of respect".
- #1 vs #2: #2's punch ("nothing") is at least as quotable, but #1 wins on
  (5): a build failure is safe to ship; a lost-work confession is not.
- #1 vs #4: #4 has the clearest next step ("Delete something"), but #1 wins
  on (3): the TODO/Later-is-now turn is a tighter two-beat joke than the
  logs/void image.
- #1 vs generic rival ("Something went wrong. Please try again later."): #1
  wins on every criterion — names the failure, has a twist, is memorable.
- #1 vs apologetic rival ("We're sorry! Our team is working hard to fix
  this."): #1 wins on (2) — no vague apology, names line 42 — and on (3).

## Decision

**CHOSEN: #1** — `The build failed on line 42, which is the exact line someone marked 'TODO: fix later' in 2019. Later is now.` (108 chars)

Selection was manual, against the kit judge-brief criteria in order plus the
pairwise checks above. No Gemini judge, no NVIDIA judge, no API/proxy judge
tournament was used.
