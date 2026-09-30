# QA: cold-learner pass over the diagnostic, m1–m3 hinges, and three cases

Phase 7 QA agent. Protocol: diagnostic statements answered blind (ids + statements only), m0 attempt written cold, then m1–m3 read in full, hinges answered, diagnostic retaken, three cases decided before reading model answers. No book or synthesis files were read.

**Protocol breach to disclose.** When printing the m1 and m2 hinge questions I filtered out a key named `diagnosis`; the field is `diagnoses`, so the per-option diagnoses (including the word "Correct.") printed alongside the options. My m1 and m2 hinge choices are therefore contaminated and are reported as "what I would have chosen", with the honest doubt noted where there was one. The m3 hinges were printed with diagnoses stripped and are clean. The diagnostic and the three cases are clean.

## 1. Scores

| Instrument | Cold (before) | After m1–m3 | Note |
|---|---|---|---|
| Diagnostic, all 16 items | 16/16 | n/a | see calibration table |
| Diagnostic, items keyed to m1–m3 (d9, d10, d11, d15) | 4/4 | 4/4 | zero measurable gain; ceiling |
| Hinges m1 (4) | — | 4/4 (contaminated) | one genuine hesitation, h1.4 |
| Hinges m2 (4) | — | 4/4 (contaminated) | |
| Hinges m3 (5) | — | 5/5 (clean) | |
| Cases k02, k04, k09 | — | 3/3 same decision as model answer | differences in detail, listed in §6 |

The headline is not that the learner is good. It is that **the instruments do not discriminate**: a learner with an ordinary social-science prior clears every item cold, and the m1–m3 diagnostic subset cannot register learning because it is already at ceiling before the modules are read.

## 2. Per-item calibration on the diagnostic (cold pass)

Confidence 1–5. "Tell" = a surface cue in the statement that gives the answer to a test-wise reader who knows nothing.

| Item | Module | My answer / conf | Key | Right? | Tell in the wording | Verdict |
|---|---|---|---|---|---|---|
| d1 | m7 | F / 5 | F | yes | "on its own" | too easy; absolute phrasing flags False |
| d2 | m5 | T / 5 | T | yes | none | fine; ultimatum-game rejection is well known but the folk theory is real |
| d3 | m10 | F / 3 | F | yes | "that evolved trait is what keeps cooperation stable" | good item; genuinely contested, my confidence was appropriately low |
| d4 | m4 | F / 4 | F | yes | "mainly caused by" | ok, but "mainly" is a tell |
| d5 | m6 | F / 5 | F | yes | "will reach it" | too easy for anyone who has heard "risk-dominant" |
| d6 | m7 | T / 3 | T | yes | "roughly doubles" | number-recall item; a naive learner can only guess. Acceptable as a prior-knowledge probe, but it measures trivia, not the misconception ("talk is cheap") |
| d7 | m9 | F / 5 | F | yes | "always" | too easy; "always" is a universal tell for False |
| d8 | m9 | T / 4 | T | yes | none | fine, but "main structural fact" is odd wording; see rewrite |
| d9 | m2 | F / 4 | F | yes | none | fine as a prior probe; widely reported failure, so many learners will know |
| d10 | m2 | T / 4 | T | yes | compound | **arguable**: bundles an interpretation ("because they trusted the institution and had no graceful exit") with a finding (peer refusal collapses obedience). A careful learner who marks it False because the first clause is [H] is penalised for doing exactly what the course teaches |
| d11 | m3 | F / 5 | F | yes | "solves" | too easy; "solves" is a tell |
| d12 | m7 | F / 5 | F | yes | "whatever most people actually do" | too easy for anyone who knows "descriptive vs injunctive" |
| d13 | m8 | T / 5 | T | yes | none | fine |
| d14 | m8 | T / 4 | T | yes | "not a set of rules to install" | the statement is phrased as the course's own conclusion; a hedged, two-clause True |
| d15 | m1 | T / 2 | T | yes | "mainly because" | good item on content; my low confidence was appropriate. But the explanation leans entirely on one simulation; a learner who knows Rogers's paradox could defend False ("mainly because individual learning is costly") |
| d16 | m4 | T / 4 | T | yes | "not of a few influential people" | hedged, negated True; test-wise readers spot the pattern |

**Structural pattern.** The nine False items are short, absolute claims (always / solves / mainly / whatever / on its own / will reach). The seven True items are longer, hedged, and often contain "not X but Y" course-voice phrasing (d14, d16, d10). A learner who has never opened a book can score about 13/16 by length and absoluteness alone. The diagnostic is measuring test-wiseness more than prior belief.

## 3. m0 cold answer (Cooperation brief v0, ~300 words)

Group: a ~40-person open-source maintainer community I know from the inside, around a mid-sized library.

(1) Supposed to cooperate on: triaging issues, reviewing external PRs within a week, keeping the changelog and release notes current, and rotating release duty. Visible failure: PR review latency is three to six weeks; two maintainers do 80% of reviews; the release rota exists on paper and the same person cuts every release; the changelog is written after the fact by whoever is annoyed enough.

(2) Why I think it fails: reviewing is unglamorous and unattributed; the people who could review get no visible credit and bear all the cost of a bad merge; nobody is embarrassed by a stale queue because the queue is invisible; the rota has no consequence when skipped; and the two heavy reviewers have made themselves the default, so everybody else has learned to wait.

(3) Three changes: a public weekly "review ledger" naming who reviewed what, with thanks from a maintainer everyone respects; a hard rule that a release is cut by the rota holder or not at all, with the two heavy reviewers publicly declining to cover; and a two-reviewer cap per person per week, so the work has to spread.

(4) Three months: median PR first-response under seven days; at least six distinct reviewers per month; three consecutive releases cut by three different people.

Indefensible assumptions: that visibility alone creates the motive; that the two heavy reviewers can stop without the queue collapsing; that the others are able rather than unwilling. I have assumed the people are fine and the incentives are wrong, which is the second of the two default assumptions the prompt predicts.

Tags: the review ledger [H]; the release rule [V, with a hidden [H] that others will step in]; the cap [H]. Nothing here is [E].

Three sentences: A world-class group makes the cooperative act cheap, visible and expected, so that doing it is the default and not doing it is noticed. It keeps its critical knowledge in more than one head. It fixes its structure before it blames its members.

(The m0 prompt works well: it produced the predicted default assumption and a page with no [E] on it, which is exactly the diff target the course wants.)

## 4. Hinge questions

### 4.1 Systemic finding: hinges are guessable from position and length

Answer indices and longest-option indices across all modules (from `modules-a.json` and `modules-b.json`):

```
m0 answers [1,1,1,2]     longest [1,1,1,2]
m1 answers [1,1,1,1]     longest [1,1,1,2]
m2 answers [1,0,2,1]     longest [1,0,3,1]
m3 answers [1,1,1,1,1]   longest [1,1,1,1,1]
m4 answers [1,1,1,1]     longest [1,1,1,1]
m5 answers [1,1,1,1]     longest [1,1,1,1]
m6 answers [2,1,3,2]     longest [2,1,3,2]
m7 answers [1,2,3,1]     longest [1,2,3,1]
m8 answers [3,1,0,3]     longest [3,1,0,3]
m9 answers [2,3,1,2]     longest [2,3,1,2]
m10 answers [1,2,3,2]    longest [1,2,3,2]
m11 answers [1,2,1]      longest [1,2,1]
```

- The longest option is the correct one in 47 of 49 hinges.
- In modules-a, 21 of 25 correct answers sit at index 1 (the second option); m1, m3, m4 and m5 are all-index-1.
- The correct option is also consistently the only one that contains a qualification, a mechanism, or a semicolon. Distractors are one-clause slogans.

Any learner who has done two hinges will have learnt "pick the long, hedged second option". This defeats the purpose of the hinge (to catch a misconception the learner actually holds). Recommended fix, mechanical: shuffle correct-answer positions to roughly uniform, and rewrite every correct option to the length and register of its distractors (or lengthen the distractors so each carries a mechanism-shaped justification). Concrete rewrites for m1–m3 are in §7.

### 4.2 Per-hinge record

Options numbered 0–3 as stored.

**m1 h1 (40→400, incident reviews decay).** Would choose 1. Correct. Too easy: it restates idea 4's own example sentence-for-sentence ("A company that grows from 40 to 400 people..."). A learner who read the module is matching text, not diagnosing. Diagnoses for 0, 2, 3 are accurate about why a learner would pick them; option 3's diagnosis ("partly right, wrong level") is the best-written one in the module.

**m1 h2 (quality over speed, then ships broken).** Would choose 1. Correct. Easy; the CRED example in idea 1 is nearly identical. Option 2 ("people become cynical and stop following any norm") is the one plausible learner belief, and its diagnosis names that belief correctly. Option 3's diagnosis (dialect forking) is a stretch: a learner picking "two camps" is more likely thinking "the team lead's team vs the rest", i.e. a prestige split, not sorting. Minor.

**m1 h3 (copied wiki, stale after two years).** Would choose 1. Correct. The distractor diagnosis for option 0 is off: it labels the choice "'Copying is lazy'", but a learner picking "should have been written from scratch" is more likely reasoning "borrowed practices don't fit our context" (a fit/transfer belief), not that copying is lazy. The diagnosis should name the fit belief and then point out that the failure was expiry and no innovator, not origin.

**m1 h4 (spread a debugging technique with non-obvious reasoning).** Genuine hesitation between 0 (pair and watch) and 1 (explain while demonstrating). Correct is 1. **This is the best hinge in the module and the module text does not support it.** The body of m1 argues repeatedly that explanation is a weak channel and that fidelity means "whether a learner can watch a skilled model closely enough to copy" (idea 4); the worked example calls the guideline "fidelity support". The only place the module says teaching beats watching for skills with hidden structure is objective 3 (one clause) and the diagnosis of the hinge itself, where Morgan et al. 2015 appears for the first time. A learner who reads the ideas carefully is pushed toward option 0. Either add a paragraph on the stone-tool transmission experiment and the norm-adherence/skill-transfer distinction to idea 4 (or a new short idea), or move this hinge. Diagnoses for 0, 2, 3 are accurate about why a learner would pick them.

**m2 h1 (banner: "over a thousand posts broke the rules").** Would choose 1. Correct. Too easy: the hook, idea 2 and the "absolute course rule" all state it. Option 2's diagnosis (netting vs pairing) is good.

**m2 h2 (retro concludes two named people are unreliable).** Would choose 0. Correct. Too easy; option 0 is the module's stated "first design rule" verbatim. The diagnosis for option 1 calls it "naive realism"; a learner picking "people know their colleagues" is more often expressing trust in local knowledge than naive realism, and the diagnosis should say the attribution error survives familiarity.

**m2 h3 (which lever is [E] for a mixed-culture team).** Would choose 2. Correct by elimination; three of the four options are on the module's "do not build on" list. **The correct answer is arguable on the module's own terms**: idea 4 says the dissonance effects are "moderate and Western-sampled; interdependent-self cultures show ... different commitment dynamics", and idea 1 says "for a mixed-culture group, test the levers locally". Asking which lever is [E] "for a mixed-culture team" and answering "small public commitments" contradicts the boundary note. Drop "mixed-culture" from the stem, or change the correct answer to "descriptive-norm feedback paired with an injunctive signal", which the module presents as replicated at scale.

**m2 h4 (forty people saw alarming posts, nobody acted).** Would choose 1. Correct. Option 2 (Philpot 2020 over-correction) is a good distractor and its diagnosis names the right belief. Option 3's diagnosis is right.

**m3 h1 (on-call rota, defection pays).** Chose 1. Correct. Too easy: the stem answers its own diagnostic question ("the honest answer is yes") and idea 1 says "if yes, it is PD-shaped". Option 3's diagnosis ("partly right, wrong level") is good.

**m3 h2 (founder: repeated-game logic guarantees cooperation).** Chose 1. Correct. Option 3 (δ above one half) is a well-designed distractor for a learner who over-learnt the arithmetic, and its diagnosis is exactly right. Option 0 is not a live belief for anyone.

**m3 h3 (committed members vs tourists).** Chose 1. Correct. Too easy: options 0, 2, 3 are the three errors idea 4 lists by name. Diagnoses accurate.

**m3 h4 ("so this is what they want").** Chose 1. Correct. Too easy; idea 2 uses this exact sentence. Diagnoses accurate.

**m3 h5 (two-team stag hunt, first lever).** Chose 1. Correct. Option 0 (raise the joint payoff) is the right distractor and the hook has already told the learner that "more money did nothing", which removes it. Diagnosis for 0 is right.

### 4.3 Where the module text was insufficient to answer its own hinge

- **m1 h4**: Morgan et al. 2015 and the "teaching beats imitation for hidden-structure skills" result appear only in the hinge diagnosis and one objective clause. The ideas push the other way. Needs a paragraph in the body.
- **m2 h3**: the body's own boundary condition (Western-sampled, test locally in mixed-culture groups) undermines the keyed answer. Needs the stem changed.
- Everything else is over-supported: nine of thirteen hinges reuse a sentence or example from the ideas nearly verbatim (m1 h1, m1 h2, m2 h1, m2 h2, m3 h1, m3 h3, m3 h4, m3 h5, and m1 h3's "stale pool").

### 4.4 Distractor diagnoses that misname the learner's reason

- m1 h3 option 0: labels a "fit" belief as "copying is lazy".
- m1 h2 option 3: labels a "leader vs team split" belief as sorting/dialect forking.
- m2 h2 option 1: labels "trust colleagues' local knowledge" as naive realism.
- m3 h2 option 0 ("guarantees nothing unless the horizon is finite"): nobody holds this; the option is a throwaway and its diagnosis diagnoses nobody. Replace with a real belief (see §7).

## 5. Diagnostic retake (m1–m3 items)

d9 (ego depletion), d10 (Milgram), d11 (repetition solves PD), d15 (copying pre-filtered): all correct on both attempts, confidence rose from 4/4/5/2 to 5/5/5/5. The gain is in confidence only and would be invisible to a right/wrong score. d15 is the only item in the subset that could plausibly move for a cold learner, and its key depends on one specific simulation result that a learner cannot reason to; the others are widely-reported folk-psychology corrections.

## 6. Cases (decision written before the model answer)

**k02 ("Quality first", then the March ship).** My decision: cancel the quality week; the 14 March ship was a CRED for the opposite norm through the CEO channel; Ana and Yusuf are prestige nodes now transmitting it. Replacement before 22 April: Marcus publicly commits Exports to a P1-zero gate and accepts a visible scope cut; Ana and Yusuf visibly block red-check PRs with written reasons; publish green-check sprints, never broken-ship counts; drop the poster and pledge. Model answer: same decision, same three moves, plus a fourth I missed: make merging on red impossible by default (a convention so the norm needs no daily heroism). Also framed the 22 April release as the test and gave a switch signal. Match: high. My gap: I stopped at norms and did not reach for the cheaper mechanism (make the default enforce it).

**k04 (Twelve people, two "coasters", and a leaderboard).** My decision: no leaderboard, no bonus; the structure (12 people, one backlog, no ownership) produces loafing and diffusion regardless of who is in it; points crowd out reviews/mentoring/unblocking (multitask incentive problem); scorekeeping converts a communal relationship to exchange; split into 3 pods with named ownership and reviewers of record; Rick already has a situational explanation; re-assess Rick and Jo after a month of identifiable work and only then have the dispositional conversation. Model answer: identical decision and structure (three pods of four, CODEOWNERS, collective metrics, BPC table for Rick and Jo, switch signal). It cites Gneezy and List 2006 on bonuses, which I did not have. Match: high.

**k09 (Ban or note?).** My decision: neither; the permanent ban is not subgame-perfect (one applied, eleven ignored), Lucia's private note keeps the sanction invisible and teaches that prestige buys immunity. By Wednesday: a public templated moderator note naming the rule, a short posting restriction, a route back; rewrite the clause to a published ladder applied by rotation with scheduled escalation; lock the abusive thread and treat abuse of Tarn as a violation under the same ladder; do not retro-sanction the eleven, publish that enforcement was inconsistent and that the ladder applies from now. Model answer: same decision (public note, seven-day restriction, public sanctions log, three-step ladder with a fast track and a contest channel, close the thread). It adds the intention-vs-outcome reading of the newcomer's exit (Blount 1995) and a ratio-based switch signal. Match: high. My gap: I did not propose a public sanctions log, which is the observability piece.

Cases discriminate better than hinges because they demand a design, not a choice; but note that all three cases are near-copies of the m1–m3 hinges and worked examples (k02 = m1 h2; k04 = m2 attempt; k09 = m3 worked example), so a learner who did the module can pattern-match rather than transfer.

## 7. Recommended changes with concrete rewrites

### Diagnostic

1. **d1** (tell: "on its own"). Rewrite: "In a group where a survey shows that most members privately dislike a practice, publishing the survey result will not change behaviour, because people already know what they themselves think." (Key: False. Targets the same misconception without an absolute.)
2. **d5** (tell: "will reach it"). Rewrite: "Two teams both prefer a shared standard to their current separate ones. Once each team is convinced the shared standard pays more, adoption follows." (Key: False.)
3. **d7** (tell: "always"). Rewrite: "To spread a costly new practice across an organisation, seed it in people who have many contacts across many teams rather than in one tight-knit team." (Key: False; complex contagion needs clustered reinforcement.)
4. **d10** (compound, arguable). Split: "In Milgram's obedience studies, most participants went to the maximum shock when a peer beside them refused to continue." (Key: False.) Move "trusted the institution and had no graceful exit" out of the diagnostic; it is an interpretation the module tags as such.
5. **d11** (tell: "solves"). Rewrite: "If two parties expect to keep dealing with each other indefinitely, and each can see what the other did last time, cooperation is the equilibrium of the game." (Key: False; it is one of many.)
6. **d12** (tell: "whatever"). Rewrite: "A practice that 80% of members follow, and that new members copy, is a social norm of the group." (Key: False; descriptive norm without normative expectation.)
7. **d14, d16** (course-voice hedged Trues). Rewrite d14 as a False: "A commons that satisfies all eight of Ostrom's design principles will hold." Rewrite d16 as a False: "To tip a group into a new practice, the scarce resource is a few members with wide influence."
8. **d15** ("mainly because", key rests on one simulation). Rewrite: "In a population where everyone learns by copying, average performance is higher than in a population where everyone learns by trial and error." (Key: False; Rogers's paradox. This tests the misconception "copying is a free lunch" without requiring recall of the tournament mechanism.)
9. **d8** (odd wording). Rewrite: "Weak ties matter because most jobs and useful information come through acquaintances rather than close friends." (Key: False; the structural bridge claim is the robust one, the job claim is not. This inverts the item to catch the popular version.)
10. Balance the set so that True and False items have the same mean length and neither side carries the "not X but Y" phrasing.

### Hinges (m1–m3)

11. **All hinges, all modules**: shuffle correct positions to roughly uniform; equalise option length and register so the correct option is not the only one with a mechanism clause. Example, m3 h4 rewritten with balanced options:
    - "The state is stable, and stability is what equilibrium means; it says nothing about preference."
    - "The state reveals preference: nobody deviates, so nobody wants to."
    - "The state cannot be an equilibrium, because a better outcome exists that everyone would prefer."
    - "The state is an equilibrium only because the engineers are selfish; with other-regarding payoffs it would not be."
12. **m1 h1**: change the numbers and the practice so it is not a verbatim lift of idea 4 ("A 25-person agency merges with a 200-person one; its signature client-handover ritual decays"). Keep the diagnoses.
13. **m1 h3 option 0 diagnosis**: rewrite as "Copying as a fit problem: 'their practices didn't suit us, we should have written our own'. The tournament says the problem is not that the practices were borrowed but that they were never dated and nobody was paid to test alternatives; a home-grown wiki with no expiry goes stale the same way."
14. **m1 h4**: keep the hinge (it is the only one that catches a real over-generalisation) but add to idea 4 a paragraph: "Fidelity has a second lever for skills whose causal structure is hidden. In Morgan and colleagues' stone-tool transmission experiment (2015, N = 184, five conditions), watching a silent demonstrator added little over reverse engineering; verbal teaching produced the largest gains. So: norm adherence spreads by models and expectations; a skill with hidden reasoning spreads by explicit teaching alongside demonstration. Henrich's 'explanation does not produce adherence' is a claim about norms, not about skills." Then the hinge is answerable from the body.
15. **m2 h2 option 1 diagnosis**: rewrite as "Familiarity as a cure for the attribution error. Colleagues are observers, and the assigned-essay and quiz-show studies show the error survives even when the constraint is visible to the observer; knowing someone well does not tell you their workload last quarter."
16. **m2 h3**: change the stem to "Which of these levers has the evidence to be tagged [E] in a brief?" (drop "for a mixed-culture team"), and add a fourth distractor tension by making option 2 "Small, voluntary, public commitments, tagged [E] for magnitude in this team" so that the learner has to reject the over-tag as well. Alternatively key the item to descriptive-plus-injunctive feedback, which the module presents as replicated at scale (Allcott 2011).
17. **m3 h1**: remove "The honest answer is yes" from the stem and instead give the payoffs: "A skipped shift saves the skipper a night; if the others cover, the skipper loses nothing; if nobody covers, the pager goes to the manager and everyone is chewed out equally." Let the learner run the diagnostic question themselves.
18. **m3 h2 option 0**: replace the non-belief ("guarantees nothing unless the horizon is finite") with a live one: "Repetition guarantees cooperation once the team has been together long enough for reputations to form." Diagnosis: "Reputation as automatic selection. Reputation makes defection costly only if defection is observed and someone is willing to respond; the founder's claim skips both."
19. **m3 h5**: move the hook's "more money did nothing" reveal to after the hinge, or change the hinge scenario so the hook does not pre-answer it.

### Cases

20. De-duplicate cases from hinges/worked examples within the same module (k02 vs m1 h2, k04 vs m2 attempt, k09 vs m3 worked example). Either cross-key the case to a later module so it is a transfer task, or change the surface (domain, actors, stakes) enough that the learner cannot pattern-match on the story.
