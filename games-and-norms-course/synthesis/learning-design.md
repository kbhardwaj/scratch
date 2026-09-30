# Learning design for the anabolic phase — Games and Norms

Status: designed against `SPEC.md`, `course.json`, the eleven finished `books/` files and
`synthesis/claims-ledger.md` (section 5 of the ledger is binding on every claim below). Where this
document and a book file disagree, the book file wins; where two book files disagree, the ledger's
resolution wins. The reconciliation log at the end records every place the first draft was
corrected against those sources, the claims checked with no change needed, and what is still open.
Module ids (m0..m11), diagnostic ids (d1..d16) and brief-section ids (s1..s14) are fixed here and
must not be renumbered by downstream files. Tension ids (t01..) and case ids (k01..) below are
proposals; `tensions.md` and `casebook.md` are canonical once written.

Learner profile: software or product background, comfortable with systems, specs and iteration
loops; time-poor; has a real group in mind (a team, a community, a platform, a commons) and wants
to be able to diagnose why it cooperates or coordinates badly and design the fix. Total learner
time budget: about 20 hours over three weeks of scheduled sessions plus about 3 hours of capstone,
against roughly 150 hours of reading for the eleven books (sum of the "reading time saved" lines
in the book files). Floor for a learner who trims retrieval days and the capstone: about 17 hours.

A convention used throughout: numbers quoted as evidence appear in the claims ledger section 4
(status noted where it is "background" or "verified"); payoff numbers in attempts and worked
examples are illustrative constructions, either the ledger's own illustrative rows (stag-hunt
watershed, norm-based utility, cascade threshold) or arithmetic on the book files' worked
examples, and are labelled as such.

---

## 1. Design principles (each tied to the source that justifies it)

The reading list is about cooperation, not about learning, so each principle is tied to the
course source that justifies it where one exists and marked "(learning-science default, not in
the sources)" where the justification comes from outside the list. The learner is told which is
which; this is itself a tagging exercise.

1. **Attempt before instruction, where the learner has priors to activate.** (`06-behavioral-game-theory`,
   ch 1 and ch 6: first-contact behaviour is governed by whatever the person brings to the
   situation, and early rounds lock in the steady state; `03-social-psychology`, ch 7: freely
   chosen, effortful commitments produce belief where handed-down conclusions produce compliance.)
   Every module opens with a real-group scenario the learner tries cold. The point is to surface
   the learner's folk theory of cooperation (usually "wrong people" or "wrong incentives") so
   that the reading lands on a live mistake. Where there are no priors (the formal definition of
   correlated equilibrium, say) the attempt is a short prediction task instead of a design task.

2. **Worked examples first, faded problems second, novel problems last; scaffolding fades across
   modules.** (`04-games-of-strategy`: every chapter's method is a fully worked small game before
   any exercise; learning-science default for the fading.) m1 to m4 each give a complete worked
   decision ending in a tagged policy; m5 to m9 give a case with a partial reasoning chain the
   learner completes; m10 and m11 give a scenario and a rubric only. The capstone is a novel
   problem: the learner's own group.

3. **One or two load-bearing ideas per module; everything else is reference, not memory.**
   (`06-behavioral-game-theory`, ch 5: people reason one or two steps about others on first contact,
   with a mean of about one and a half thinking steps (Camerer, Ho and Chong 2004, verified); the
   same limit applies to the learner holding a module in mind.) Each module names its one or two
   ideas up front; the rest of the book file is a reading map with sections to skip.

4. **Confront the folk theory; do not just supply the correct one.** (`03-social-psychology`,
   ch 1 and ch 5: naive realism and the fundamental attribution error are the default explanations
   for group failure and they survive being told they are wrong; `05-micromotives-and-macrobehavior`,
   ch 1: people infer motives from outcomes and outcomes from motives unless a model is put between
   them.) The diagnostic and every hinge distractor are built from named folk theories drawn from
   the book files' "Common misreadings" sections and the ledger's corrections, so a wrong answer
   says which folk theory is still active.

5. **Retrieve, space, interleave; every third day is a retrieval day.** (`02-darwins-unfinished-symphony`,
   ch 3 and ch 7: the winning tournament strategy discounted stale information, and skills are
   lost below a fidelity threshold; the course treats the learner's own memory as a transmission
   chain that must be re-run. Learning-science default for the spacing intervals.) Cards for a
   module enter the deck the day after it completes; retrieval days pull from at least three
   modules.

6. **Hinge questions gate the next step; a wrong answer routes to a specific five-minute repair.**
   (`09-governing-the-commons`, ch 3: monitoring as a by-product of activity and small, quick,
   graduated first sanctions keep a rule alive; a hinge is a by-product check and a repair path is
   a graduated sanction.) Repair paths point to a book-file section, never "re-read the module".

7. **Mentor tone: high standards, high support, wise feedback; no cheerleading.**
   (`03-social-psychology`, ch 11: the wise-feedback pattern, high standards paired with assurance
   of capability, is [E] at moderate size; ch 7: overpaying for behaviour crowds out the motive.)
   Feedback on the brief says what is wrong and why the learner can fix it; it never says "great
   job" and never softens a mis-tag.

8. **The cooperation brief improves through versioned diffs, each with a prediction.**
   (`09-governing-the-commons`, ch 4: durable institutions are supplied incrementally, each small
   change producing information that lowers the cost of the next; `06-behavioral-game-theory`,
   ch 6: feedback on forgone payoffs speeds learning.) Every module's deliverable is a diff against
   the previous brief version, tagged [E]/[H]/[V], with one prediction the learner could check in
   their group within three months.

9. **Curiosity hooks sit on the module's target, never beside it.** (`01-secret-of-our-success`,
   ch 4: content biases direct attention to norm violations, danger and status; a hook that trades
   on a surprising anecdote beside the target spends that attention on the wrong thing.) Each hook
   is a question whose answer is the module's load-bearing idea.

10. **Every claim carries a tag; the capstone penalises mis-tags.** (`SPEC.md`; `11-bounds-of-reason`,
    evidence section: the book's own weakness is stating argued claims as shown; the tagging
    discipline is the course's defence against doing the same in the brief.) [E] is reserved for
    claims the ledger marks [E]; the most common capstone error is tagging a lab mechanism as
    [E] for the learner's own group, which the ledger (rule 27) says must be [H].

11. **Design for the median case, not the showcase.** (`05-micromotives-and-macrobehavior`, ch 3:
    a cascade is decided by the threshold distribution, not by the most enthusiastic actor;
    `03-social-psychology`, ch 1: situations are underestimated but effect sizes are moderate.)
    The modules assume a learner who does the reading map once, gets one hinge wrong per module,
    and misses one retrieval day; the schedule has slack for that learner, not for the ideal one.

---

## 2. Course architecture

### Four levels, one spine

The unified model (`unified-model.md`, seeded in 4a) reads like a building. Ordered bottom-up,
because each level constrains the one above it:

- **Origins** (m1; `01`, `02`). Humans are cultural learners inside a collective brain, with
  evolved copying rules and a content-neutral norm psychology. Constraint on everything above:
  the levers are models, prestige, visibility and expectations, and explanation is a weak channel.
- **Mechanisms** (m2 to m5; `03`, `04`, `05`, `06`). What individuals actually do in groups, the
  formal language for strategic interaction, how micro-choices aggregate, and where real behaviour
  departs from the formal prediction. Constraint on Order: any norm, institution or network
  intervention has to work on people with one to two steps of reasoning, conditional cooperation,
  a distribution of norm-sensitivities, and a threshold distribution.
- **Order** (m6 to m9; `07`, `08`, `09`, `10`). How populations settle on an equilibrium, what a
  norm is and how to measure it, what institutions durable commons share, and how network
  structure decides where behaviour spreads. This is where the brief's design decisions live.
- **Synthesis under critique** (m10; `11` plus ledger X5). One attempt to unify the levels,
  assessed claim by claim, and the course's own reconciliation of the four accounts of how a group
  settles on a way of behaving.

The opening is top-down: m0 asks the learner to attempt the whole goal (diagnose and fix their
own group) cold, before any content. Certainty drops as one climbs: the Mechanisms-level formal
results are theorems; the Order-level prescriptions are mostly [H] and [V] for any particular
group, and the course says so at every step.

### Module list

| # | Module | Level | Min | Draws on (slugs) |
|---|--------|-------|-----|------------------|
| m0 | Diagnostic and opening cold challenge | (top-down) | 60 | none (cold) |
| m1 | Cultural learners and the collective brain | Origins | 100 (50+50) | `01`, `02` |
| m2 | The psychology of individuals in groups, with the replication rules | Mechanisms | 70 | `03` (ch 1, 5, 7, 9, 12, 14; evidence section) |
| m3 | The formal toolkit: draw the game before arguing about it | Mechanisms | 100 (50+50) | `04` (ch 1-4, 8-12); `10` ch 6 |
| m4 | Micro to macro: thresholds, tipping, sorting | Mechanisms | 70 | `05`; `10` ch 17 and 19 (population models only) |
| m5 | What people actually do: social preferences, coordination, learning | Mechanisms | 70 | `06` (ch 1, 2, 5, 6, 7); `03` ch 14 |
| m6 | How populations settle: risk dominance, correlation, signals | Order | 100 (50+50) | `07`; `06` ch 7; `04` ch 12 |
| m7 | Norms: expectations, measurement, change | Order | 70 | `08`; `03` ch 9; `10` ch 16 |
| m8 | Institutions for the commons: design principles, sanctions, polycentricity | Order | 70 | `09`; `04` ch 8, 10, 11 |
| m9 | Networks: ties, homophily, cascades, small worlds | Order | 70 | `10` (ch 3, 4, 19, 20); `07` Parts I and III |
| m10 | The four accounts reconciled and Gintis assessed | Synthesis | 70 | `11`; ledger X5; `04` ch 4, `07` ch 1, `08` ch 1 |
| m11 | Integration: tensions, decision rules, the diagnostic path | Integration | 75 | all; `tensions.md`, `unified-model.md` seeds |
| R1-R6 | Retrieval sessions (deck, casebook, free recall, re-tag) | — | 40-55 each | ≥3 modules each |
| Capstone | Cooperation brief v6, defence, first ninety days | — | 180 | all |

Scheduled total: 925 minutes of modules plus 275 minutes of retrieval, about 20 hours, plus a
3-hour capstone. See section 5.

### Rationale for the order

- **Origins first, because every later book takes its inputs from there.** `01` (why it is in the
  curriculum): game theory models players who already have preferences; Bicchieri and Ostrom
  study norms that already exist; networks have nodes that already know what they want. The
  learner who has not internalised "levers are models and expectations, not arguments" (`01` ch 4,
  ch 7) will design memos in every later module.
- **`03` before `04`, not after.** The folk theory the learner arrives with is dispositional
  ("the free-riders", "the toxic person"). `03` ch 5 (the fundamental attribution error) has to
  be installed before the learner is handed a payoff matrix, or they will write the matrix with
  villains in it. `03` also supplies the replication rules (ledger rule 20) that the rest of the
  course must obey, so it comes early.
- **`04` before `05` and `06`.** Schelling's binary-choice diagram (`05` ch 7) and Camerer's
  departures (`06` ch 1) both presuppose the vocabulary of equilibrium, dominance and the PD /
  assurance / chicken distinction (`04` ch 4, 11). Ledger rule 13 (classify before prescribing)
  is the single most-used skill in the brief and it is taught here.
- **`05` before `06`.** Schelling is the bridge from a two-player matrix to a population, and his
  tipping point is the same object as `10`'s z' and `07`'s watershed (ledger glossary). Teaching
  the population view before the lab evidence means the learner reads Van Huyck's weak-link
  collapse (`06` ch 7) as a threshold phenomenon, not as a puzzle.
- **`06` closes Mechanisms** because it is the empirical audit of `04`: the learner now knows what
  the theory predicts and can see the three amendments (social preferences, limited reasoning,
  learning) as amendments rather than as a rival theory (`06` common misreadings: "Camerer refutes
  game theory").
- **`07` opens Order** because it answers the question `04` and `06` leave open: which equilibrium
  does a population reach absent intervention, and what structural levers move it. `06` ch 7 is
  re-read here as the lab counterpart, and ledger rule 2 (risk dominance under random mixing) is
  the module's spine.
- **`08` after `07`, not before.** Skyrms's agents have no beliefs; Bicchieri supplies what must be
  true inside the agents for a signal or a handshake to work (ledger X5 ordering). Teaching
  Bicchieri first would make the learner treat expectations as the whole story and miss that
  basin size decides outcomes even with no beliefs at all.
- **`09` after `08`.** Ostrom's quasi-voluntary compliance is Bicchieri's conditional preference
  in field clothing (`09` connections), and her monitoring principle is what keeps empirical
  expectations accurate. The learner needs the expectation vocabulary to see why graduated
  sanctions work.
- **`10` last in Order** because networks are the variable the other three Order books hold
  fixed (`10` why-in-curriculum), and because the cluster-density theorem (`10` ch 19) needs both
  Skyrms's correlation (`07`) and Bicchieri's trendsetters (`08`) to be read correctly
  (ledger rule 3).
- **`11` is read as a critical exercise, after everything it claims to unify.** `11` (level line)
  says so itself. The module is built around the file's claim-by-claim assessment and the
  ledger's X5 resolution, so the learner assesses a synthesis rather than receiving one.
- **Population models from `10` (ch 17, 19) are previewed in m4 rather than held for m9**,
  because Schelling's ch 7 diagram and `10`'s Z-shaped adoption curve are one idea, and the
  learner should meet it once, early, with both notations. m9 then adds the graph. Recorded in the
  reconciliation log as a departure from the proposed spine.

### Pre-course diagnostic (m0 part A, 20 min)

Sixteen true/false statements, each with a confidence rating from 1 (guess) to 5 (certain), taken
before any content. Half are true. Each item names the folk theory it diagnoses, cites the source
that settles it, and keys to one module. Retaken on day 21; the app reports accuracy and the
change in confidence calibration (mean confidence on wrong answers before versus after).

| id | Statement | Answer | folk_theory | explanation (source) | module |
|----|-----------|--------|-------------|----------------------|--------|
| d1 | A team has kept a practice for years that most members, asked privately, say they dislike. The practice can persist indefinitely, because each member reads the others' compliance as approval. | True | disapproval-kills-norms | Pluralistic ignorance: each person infers others' approval from others' compliance, which is itself conformity; disapproval has to become common knowledge (`08` ch 5; ledger C44). | m7 |
| d2 | People will pay out of their own pocket to punish someone who treated them unfairly, even when they will never meet again. | True | people-are-payoff-maximisers | Ultimatum rejections are robust across decades and countries and are driven by inferred intentions (Blount 1995); about half of offers below a fifth of the pie are rejected in Western student samples, background (`06` ch 2; ledger rule 4, 25). | m5 |
| d3 | Humans evolved to punish cheats at personal cost, and that evolved trait is what keeps cooperation stable in real communities. | False | strong-reciprocity-is-settled | Lab willingness to punish is [E]; "evolved strong reciprocity" is [H] (Binmore and Shaked 2010; Guala 2012); real-world sanctioning is mostly cheap and graduated (`11` evidence; `09` ch 3; ledger X4, rule 4). | m10 |
| d4 | Because Schelling's checkerboard produces segregation from mild preferences, a city's observed segregation is evidence that residents' preferences, not discrimination, produced it. | False | Schelling-proved-preferences | The model is a possibility proof: mild preferences plus interdependence can produce extreme sorting; it says nothing about the real-world share due to discrimination, prices or law, and Schelling says so (`05` ch 4; ledger C29, rule 17). | m4 |
| d5 | Two teams both prefer a shared standard to their separate ones, and each knows the other prefers it too. They can still fail to adopt it, because each fears switching while the other does not. | True | efficient-equilibrium-is-rational | Under random mixing and uncertainty the risk-dominant equilibrium has the larger basin and wins; lab play converges to it without communication (`07` ch 1; `06` ch 7 Cooper et al.; ledger X6, rule 2). | m6 |
| d6 | Ten minutes of relevant, non-binding talk before a public-goods decision roughly doubles cooperation in the lab. | True | talk-is-empty | Dawes, McTavish and Shaklee 1977: from roughly a third to roughly seven in ten, background; communication is the strongest lever in the Sally 1995 meta-analysis (`08` ch 4; `03` ch 14; ledger rule 12). | m7 |
| d7 | A costly new practice adopted by a tight-knit sub-team of ten is more likely to survive and spread than the same practice seeded in ten well-connected people scattered across the organisation. | True | clusters-are-bad | A cluster of density above one minus the threshold blocks a cascade entering from outside and protects a behaviour adopted inside; clustered networks spread costly behaviour faster than random ones (Centola 2010, background) (`10` ch 19; ledger X7, rule 3). | m9 |
| d8 | The reason weak ties matter is that an acquaintance is a better source of job leads and useful information than a close friend is. | False | weak-ties-give-jobs | The structural claim (local bridges are weak; Onnela 2007) is robust; the per-tie job claim is not: most jobs arrive via weak ties in aggregate only because there are more of them, a single strong tie is more valuable at the margin (Gee et al. 2017) and moderately weak ties do best (Rajkumar et al. 2022) (`10` ch 3; ledger C51, rule 33). | m9 |
| d9 | A team schedules its hardest cooperative decisions for the morning, on the grounds that self-control is a resource that gets used up over the day. | False | ego-depletion | Registered replication across 23 labs, N = 2,141, d = 0.04 with the interval including zero (Hagger et al. 2016, verified); never build on it (`03` evidence; ledger C11, rule 20). | m2 |
| d10 | In Milgram's obedience studies, most participants went to the maximum shock even when a peer beside them refused to continue. | False | blind-obedience | The baseline replicates (70% continued past 150 V in Burger 2009, verified, versus roughly 82% in Milgram), but a refusing peer cut full obedience to about one in ten (background); the design lesson is exits, peers and legitimacy of refusal (`03` ch 9; ledger C21, rule 22). | m2 |
| d11 | Two parties expect to keep dealing with each other indefinitely, and each can see what the other did last time. Permanent mutual defection is still an equilibrium of their game. | True | repetition-solves-PD | The folk theorem is an existence result: cooperation is one equilibrium among many; the group must also coordinate on it and detect defection fast (`04` ch 10; ledger C27, rule 15). | m3 |
| d12 | A practice that most members follow and that newcomers copy can fail to be a social norm of the group, if nobody expects disapproval for skipping it. | True | norm-equals-majority | That is a descriptive norm; a social norm needs normative expectations and can exist while widely violated (`08` ch 1; ledger C42, rule 11). | m7 |
| d13 | In durable self-governed commons, the first sanction for a rule violation is usually small. | True | deterrence-needs-big-penalties | First-offence sanctions are graduated and small because compliance is contingent and the sanction's job is to signal that the rule is alive (`09` ch 3, principle 5; ledger rule 30). | m8 |
| d14 | A commons whose rules satisfy each of Ostrom's eight design principles can be expected to hold. | False | principles-are-a-recipe | The principles specify no rules and are structural conditions found in durable cases, not a guarantee; the review of 91 studies (Cox et al. 2010, verified) supports association with publication-bias and structure-not-process caveats (`09` ch 3, evidence; ledger C47, rule 29). | m8 |
| d15 | In a population where everyone learns by copying others, average performance is higher than in a population where everyone learns by trial and error. | False | copying-is-a-free-lunch | Copying pays for the individual because demonstrators pre-filter (Rendell et al. 2010, verified, a simulation), but a population of pure copiers sits on a stale pool and is no better off than trial-and-error learners (Rogers's paradox); someone must innovate (`02` ch 3; ledger rule 39). | m1 |
| d16 | To tip a group into a new practice, the scarce resource is a small number of members with wide influence. | False | influencers-cause-tipping | Schelling's tipping point is an unstable equilibrium; the scarce resource is low-threshold actors, not charismatic ones (`05` ch 3; `10` ch 17; ledger C30, rule 18). | m4 |

Baseline free response (unscored, stored for the capstone comparison): "In three sentences, what
makes a group world-class at cooperating?" The capstone asks the learner to rewrite this and
diff it against the day-1 version.

### Opening cold challenge (m0 part B, 40 min)

Prompt, given verbatim:

> Choose one real group you belong to or know from the inside: a team, a community, a platform,
> or a shared resource that people draw on. In 40 minutes and one page, with no research, write:
> (1) what the group is supposed to cooperate or coordinate on, and where it visibly fails;
> (2) why you think it fails; (3) the three changes you would make; (4) how you would know in
> three months whether they worked. Use what you already believe. The point is to generate, not
> to be right; this page will be graded only against your own later versions.

This page becomes **Cooperation brief v0**. Every module's deliverable is a diff against the
current version. Two instructions after the learner finishes, before m1: (a) list the assumptions
on the page that they could not defend to a sceptic (most learners find they have assumed either
that the people are the problem or that an incentive would fix it); (b) mark every decision on
the page [E], [H] or [V] as best they can. They will do this badly, and m11 returns to the v0
tags with a changelog.

---
## 3. Module specifications

Every module has the same nine parts in the same order, so that by m3 the shape costs no working
memory: draws on; learning objectives; load-bearing ideas (the first one or two are the ones to
hold in memory; the rest are supporting and tagged); curiosity hook; attempt (cold, before
content); worked example; hinge questions; repair paths; brief deliverable; deeper pointers.
Session timing for a 70-minute module: hook 3, attempt 12, reading map 20, worked example 10,
hinges 10, deliverable 15. Split modules put the first three parts on day one and the rest on
day two.

> Note (cold-learner QA fixes): the hinge drafts in sections 3.x below are the seed drafts. The app data (`app/data/modules-a.json`, `modules-b.json`) is canonical for option wording, option order and answer keys; every hinge was rebalanced and shuffled there (see the reconciliation log).

### m1: Cultural learners and the collective brain

**Draws on:** `01-secret-of-our-success` (ch 2, 3, 4, 7, 8, 11, 12; evidence section; common
misreadings), `02-darwins-unfinished-symphony` (ch 3, 4, 7, 8, 11; evidence section).

**Learning objectives.** The learner can (a) explain why a group's competence is a property of its
learning network rather than of its members, and name the three levers (pool size that actually
shares, connectivity, transmission fidelity); (b) list the copying rules people run (success,
prestige, conformity, self-similarity, credibility-enhancing displays; copy-when-uncertain,
discount stale information) and say which one is operating in a given failure; (c) state the
difference between spreading norm adherence (models and expectations) and transferring a skill
with hidden structure (explicit teaching), and choose the channel accordingly.

**Load-bearing ideas.**
1. *Hold in memory.* Competence and norms live in the learning network, not in individuals; the
   levers for changing behaviour are who is visibly successful, who is prestigious, what the
   majority appears to do and whether leaders' costly actions match their words. Explanation is a
   weak channel for adherence. [E for the biases and the prestige/dominance distinction (Cheng
   2013, Herrmann 2007); H for their weight in any given group; ledger X1]
2. *Hold in memory.* Copying pays because demonstrators pre-filter: what you observe is what
   others chose to do, so the value of copying is only as good as the demonstrators' incentive to
   show their best; and a population of pure copiers stagnates, so someone must be paid to innovate
   and old exemplars must expire. [E as a simulation result (Rendell et al. 2010, 104 entries,
   verified); ledger rule 39]
3. Norm psychology is content-neutral: people internalise and enforce whatever pattern is first
   and visible, including harmful norms, and will sometimes punish cooperators. Fill the norm slot
   early. [E for the psychology (developmental and cross-cultural games); H as a practice rule]
4. The collective-brain effect is about the connectivity of the learning network, lab-demonstrated
   at small scale and archaeologically contested (Vaesen et al. 2016); Tasmania is a live dispute.
   Silos and turnover can cause skill loss; growth without connection does not help. [H; ledger
   rule 6]
5. Cultural group selection is the Origins books' account of where cooperative norm packages come
   from; it is [H] in this course and never the sole basis for a design claim; the within-group
   mechanisms (reciprocity, reputation, punishment) are the [E] part. [H; ledger rule 5]

**Curiosity hook.** "A well-provisioned, well-led expedition of intelligent adults starves in a
place where the local population has thrived for centuries. Nobody was stupid. What did they lack,
and what is the equivalent in a talented new team that fails in an unfamiliar domain?" (`01` ch 3:
a locally adapted cultural package that took generations to accumulate; the team equivalent is
disconnection from a living lineage of practice.)

**Attempt (cold, before content).** "A twelve-person engineering team has one person who knows
the deployment system end to end. She is respected, quiet and leaves in three months. Adoption of
the team's written runbook is low: people ask her instead. Design the handover in ten lines and
predict what the team can do six months after she leaves." Predictable errors: the learner writes
more documentation and a training session (explanation as the channel), does not name who will
watch her work repeatedly, does not distinguish the parts of the skill that are opaque procedure
(copy faithfully) from the parts with hidden causal structure (teach the reasons), and does not
budget for the loss of the one node that other people copy. The reading explains why documentation
raises fidelity but does not replace modelling (`01` ch 12), why imitation alone added little over
reverse engineering for stone tools while teaching and language helped most (Morgan et al. 2015,
N = 184, verified, one study; `02` ch 8), and why a single copied node is a Tasmania risk.

**Worked example.** *Decision: how should a platform's moderation team get members to flag
misinformation, given adoption of a well-written flagging guideline is in the single digits of
percent?* (1) Explanation has been tried; `01` ch 7 predicts adoption from explanation near zero,
so treat the guideline as fidelity support, not the channel. (2) Ask which copying rules could
carry the behaviour: is a prestigious, self-similar member visibly flagging and visibly benefiting
(success and prestige bias)? Is the interface making flagging look like majority behaviour or
advertising that almost nobody does it (conformist transmission; ledger rule 24 forbids
advertising low adoption)? Do the moderators produce credibility-enhancing displays, or do they
visibly skip flags themselves? (3) Ask about the learning network: can a new member watch a good
flagger flag, or is flagging invisible by design? (4) Ask about norm psychology: is there any
expectation and mild sanction, or only information? Resulting policy: make three respected,
ordinary-looking members' flags visible with attribution and a visible outcome; show the count of
flags reviewed, never the adoption rate; have moderators narrate a flag decision weekly in a
public thread; add a light expectation ("members here flag; here is what happened to last week's
flags"). Tagged: [E] that models and visibility beat explanation for adherence (`01` ch 4, 7; `02`
ch 11); [H] that these three members are the right models and that the effect size in this
community is material; [V] that flagging should be routed through prestige rather than through
moderator dominance, even if dominance would be faster (`01` design implications).

**Hinge questions.**

Q1. A company grows from 40 to 400 people in a year and finds that a practice it was known for
(thorough incident reviews) has decayed. Which diagnosis fits the Origins books best?
- (a) The new hires are lower quality. *Diagnoses: "competence is in the people" (`01` ch 3
  misreading); the fundamental attribution error in organisational form.*
- (b) The effective learning network shrank: new people cannot watch a skilled model do a review,
  and the few who could are diluted. **Correct**: collective-brain effects are about connectivity
  and fidelity, not head-count (`01` ch 12; ledger rule 6).
- (c) The company is bigger, so by the population-size effect it should be innovating more; the
  decay must be a management failure. *Diagnoses: "bigger populations always produce more complex
  culture" (ledger C1); reads census size as learning-network size.*
- (d) The practice was never explained well enough to the new hires. *Diagnoses: explanation as
  the channel for adherence (`01` ch 7); partly right, wrong level, since fidelity support helps
  but modelling is missing.*

Q2. A team leader announces "quality over speed" and the next week ships a known-broken feature to
hit a date. What does the cultural-learning account predict spreads?
- (a) Nothing changes; people follow the stated policy. *Diagnoses: words as the transmission
  channel; ignores credibility-enhancing displays.*
- (b) The costly action transmits "speed over quality" more strongly than the announcement
  transmitted the reverse. **Correct**: a CRED is a costly action that only makes sense if the
  model holds the belief; the visible exception is the CRED (`01` ch 4).
- (c) People become cynical and stop following any norm. *Diagnoses: norm psychology as fragile
  and all-or-nothing; it is content-neutral and attaches to what is visible.*
- (d) The team splits into two camps with opposite norms. *Diagnoses: conflates this with
  sorting or dialect forking (`07` ch 4), which needs local structure, not a single visible model.*

Q3. An organisation copies a rival's "best practices" wiki wholesale and mandates it. Two years
later nobody has updated it and the practices no longer fit. Which tournament finding applies most
directly?
- (a) Copying is inferior to innovating, so the wiki should have been written from scratch.
  *Diagnoses: "copying is lazy"; the tournament found copying wins individually (ledger C9).*
- (b) The winning strategy discounted stale information; a wiki with no expiry copies the wrong
  things, and a population of pure copiers sits on a stale pool. **Correct** (`02` ch 3;
  ledger rule 39).
- (c) The rival's practices were selected by cultural group selection, so they must be adaptive;
  the organisation failed to implement them faithfully. *Diagnoses: cultural group selection as
  [E] and as a guarantee of fit (ledger rule 5); over-imitation of a norm package without
  modification (`01` ch 10 says copy and modify).*
- (d) The tournament shows that people copy whatever they see, so the wiki should have been more
  visible. *Diagnoses: "the tournament was an experiment on people" and copying as indiscriminate
  (`02` misreadings).*

Q4. A team wants to spread a debugging technique with non-obvious reasoning behind it. Which
channel does the evidence favour?
- (a) Pair new people with an expert and let them watch. *Diagnoses: imitation as sufficient for
  skills with hidden structure; Morgan et al. 2015 found imitation added little over reverse
  engineering (`02` ch 8).*
- (b) Have the expert explain the reasons explicitly while demonstrating. **Correct**: teaching and
  language produced the largest gains for a skill with hidden structure; one N = 184 study, so
  [E] modest (ledger rule 8).
- (c) Write it up, since explanation does not work for cultural learners anyway. *Diagnoses:
  collapsing Henrich's "explanation does not produce adherence" into "explanation does not
  work" (ledger X13); wrong scope.*
- (d) Make the technique's use visible on a dashboard so conformity carries it. *Diagnoses:
  confusing norm adherence (spreads by models and expectations) with skill transfer (needs
  teaching); partly right, wrong level.*

**Repair paths.** Wrong on Q1: `01` ch 12 and the evidence section paragraph on the collective
brain. Q2: `01` ch 4 (CREDs) and design implication "route norms through models, not memos". Q3:
`02` ch 3 (tournament, Rogers's paradox) and its common misreadings. Q4: `02` ch 8 (stone-tool
experiment) and ledger X13.

**Brief deliverable (s3, "the collective brain").** Add to the brief: a map of who actually
learns from whom in the group (not the org chart); the single points of failure for critical
skills; the group's visibly successful and prestigious members and whether they are modelling the
target behaviour; one place where leaders' costly actions contradict their stated norm. Tag each
line. Prediction: name one behaviour that will change within three months if one prestigious
member visibly adopts it, and one that will not change however well it is explained.

**Deeper pointers.** `01` ch 8 (prestige vs dominance), ch 10 (cultural group selection, with the
evidence section's caveats); `02` ch 6 (cultural drive), ch 9 (cultural niche construction, for the
"self-built environment" audit in s4); ledger X2, X3, X13, C1-C10.

### m2: The psychology of individuals in groups, with the replication rules

**Draws on:** `03-social-psychology` (ch 1, 5, 7, 9, 12, 14; evidence strength and limits;
common misreadings); ledger C11-C24, rule 20-24.

**Learning objectives.** The learner can (a) diagnose a group failure situationally before
dispositionally, naming the fundamental attribution error and construal; (b) apply the robust
levers (descriptive plus injunctive norms, a visible dissenter, small public commitments,
identifiable effort, structured contact, exits and peers under authority, the five bystander
steps) and refuse the failed ones (ego depletion, social priming, power posing, watching eyes, the
Stanford Prison Experiment, groupthink as a syndrome, IAT training); (c) state the replication
status of a classic before building on it.

**Load-bearing ideas.**
1. *Hold in memory.* Situations are underestimated, and we do not believe it: the default
   diagnosis of a failing group ("wrong people") is usually wrong, and construal (what people
   think the situation is) moves behaviour as much as payoffs do; the "Community Game" label
   roughly doubled PD cooperation versus "Wall Street Game" (Liberman, Samuels and Ross 2004,
   background). Effect sizes are moderate; the claim is that situations are underestimated, not
   all-powerful. [E; ledger C23]
2. *Hold in memory.* Norms have two channels, descriptive (what people do) and injunctive (what
   they approve), and they must point the same way; a visible descriptive norm of defection beats
   any injunctive appeal, and descriptive feedback alone boomerangs for people above the norm
   (Schultz 2007; Allcott 2011, about 2%, background). [E; ledger rule 24]
3. Much of the famous material is folklore: the course's robust list is conformity, obedience,
   attribution error, dissonance, polarization, loafing, minimal groups, contact (moderate),
   bystander (low-risk settings) and cooperation-game effects. [E that the failed ones failed;
   ledger rule 20]
4. Behaviour changes attitudes: small, freely chosen, public commitments produce belief; heavy
   incentives produce compliance without belief and can crowd out the motive. [E, moderate;
   `03` ch 7]
5. Boundaries form on nothing (minimal groups); cooperation across them needs structured,
   equal-status contact around a shared goal with institutional support, not proximity or
   training. [E, moderate (Pettigrew and Tropp 2006; Paluck 2019 field caveat); ledger C63]

**Curiosity hook.** "A sign at a national park said, in effect, 'please do not take the
petrified wood; many visitors do'. Theft went up. What did the sign transmit, and what does your
own group's most recent all-hands announcement transmit?" (`03` ch 9: the descriptive norm
undercut the injunctive one.)

**Attempt (cold, before content).** "A twelve-person team's output per head fell by about a
third after it grew from five. Two people are widely described as coasting. Write, in ten
lines, what you would do in the first month and what you expect to find." Predictable errors:
the learner starts with the two people (dispositional diagnosis), proposes a performance
conversation or a bonus (compliance without belief; overjustification), and does not check
whether effort is identifiable, tasks are owned, or the group deliberates in a way that
extremises (`03` ch 12). The reading explains loafing and diffusion of responsibility as
structural, the attribution error as the reason the "coasters" story formed, and why the fix is
visibility and ownership before any conversation about character. (The one-third drop is a
scenario number, not an evidence claim.)

**Worked example.** *Decision: a homogeneous eight-person hiring committee keeps making
confident, extreme calls that later look wrong; the founder proposes "implicit-bias training for
everyone".* (1) Check the proposed fix against the replication rules: IAT-based training does
not reliably change behaviour (Oswald 2013; Forscher 2019); reject as the main lever (ledger
C17). (2) Name the robust mechanisms in play: group polarization (deliberation pushes a
homogeneous group toward a more extreme version of its lean), informational conformity (early
confident speakers become the group's evidence), and self-censorship. (3) Design against each:
independent written judgments collected before discussion; speaking order reversed so the most
senior speaks last; a rotating assigned critic; criteria fixed before the candidate is seen. (4)
Add the injunctive channel: the committee chair states that dissent is expected and names the
last time it changed a decision. Resulting policy: "No hiring discussion starts before every
member's written score is in; the chair speaks last; one member per meeting is the assigned
critic; criteria are published before the loop." Tagged [E] for polarization, conformity and
structured procedures; [H] for the magnitude of improvement in this committee; [V] that
procedural fairness is worth the slower meeting.

**Hinge questions.**

Q1. A community manager wants to reduce rule-breaking posts and drafts a banner: "Over a
thousand posts broke the rules last month. Please do better." What does `03` predict?
- (a) It works; people respond to being told the facts. *Diagnoses: information as the lever;
  ignores the descriptive channel.*
- (b) It backfires for most users because it advertises that rule-breaking is common. **Correct**:
  descriptive norm contradicts injunctive norm (Petrified Forest; ledger C22).
- (c) It works for rule-breakers and backfires for everyone else, which nets out. *Diagnoses:
  half-right reading of the Schultz boomerang; misses that the injunctive smiley was what removed
  the boomerang, so the fix is pairing, not netting.*
- (d) It has no effect because banners are ignored. *Diagnoses: "situations do not matter"; the
  boomerang is a replicated effect.*

Q2. After a bad quarter, a team's retrospective concludes that two named people are unreliable.
Which correction from `03` should the facilitator apply first?
- (a) Ask whether workload, information and ambiguity were visible to the people making the
  attribution. **Correct**: the fundamental attribution error is the master theme; diagnose
  situationally first (`03` ch 5).
- (b) Accept the diagnosis; people know their colleagues. *Diagnoses: naive realism; observers
  see disposition even when constraints are obvious (Jones and Harris 1967).*
- (c) Reject the diagnosis outright; situations determine everything. *Diagnoses: "people are
  infinitely malleable" (ledger C23); effect sizes are moderate and the correction is a check,
  not a veto.*
- (d) Run a personality assessment to settle it. *Diagnoses: dispositional model of group
  failure with better instruments; still skips the situation.*

Q3. Which of these levers has the evidence to be tagged [E] in a brief for a mixed-culture team?
- (a) Twenty-minute power-posing sessions before difficult negotiations. *Diagnoses: power
  posing as real (Ranehill 2015, N = 200, blinded: felt power only; ledger C13).*
- (b) Eyes printed on the honour-system snack box. *Diagnoses: watching-eyes effect (mostly
  failed replications; ledger C18); use real identifiability instead.*
- (c) Small, voluntary, public commitments before a behaviour change. **Correct**: induced
  compliance and effort justification replicate at moderate size (`03` ch 7).
- (d) Diagnosing "groupthink" and prescribing a cohesion-reduction offsite. *Diagnoses:
  groupthink as a syndrome (ledger C16); the mechanisms are real, the package is not, and
  cohesion is not the cause.*

Q4. A remote community is worried about a member's safety after alarming posts; forty people saw
them and nobody acted. Which reading of the bystander literature is correct?
- (a) Crowds make people passive; the only fix is smaller communities. *Diagnoses: "crowds make
  people passive" and the Genovese story as fact (ledger C20).*
- (b) The effect is robust in ambiguous, low-risk situations and each of the five steps (notice,
  interpret, take responsibility, know how, act) can be engineered; assign named ownership and
  give a script. **Correct** (`03` ch 14; ledger rule 23).
- (c) In real emergencies someone always intervenes, so this is a non-problem. *Diagnoses:
  over-correction from Philpot 2020; the ambiguous online case is exactly where the effect is
  strongest.*
- (d) Make sure such posts are seen by more people, so that someone is bound to act.
  *Diagnoses: "more bystanders means more help"; diffusion of responsibility runs the other way,
  and the fix is a named owner, not a larger audience (`03` ch 14).*

**Repair paths.** Wrong on Q1: `03` ch 9 (Cialdini, Schultz, Allcott) and the misreading
"descriptive-norm messaging always helps". Q2: `03` ch 5 (attribution) and ch 1 (naive realism).
Q3: `03` evidence strength and limits, "weak, contested or failed" list. Q4: `03` ch 14 (five
steps) and ledger C20.

**Brief deliverable (s4, "situational audit and folk-psychology check").** Add: for each failure
named in v0, the situational alternative to the dispositional story (workload, ambiguity,
visibility, ownership, deliberation design); the group's current descriptive and injunctive
signals for the target behaviour and whether they agree; a list of any levers in v0 that appear on
the failed-replication list, struck through with the reason. Prediction: which one structural
change (identifiable effort, named ownership, speaking order) will move the metric the learner
cares about, and by roughly how much in words (small, moderate).

**Deeper pointers.** `03` ch 3 (self and status threat), ch 8 (inoculation), ch 10 (contact
conditions), ch 13 (honour cultures; cite the homicide pattern, not the hormone result, ledger
C4); the "culture" cross-cutting note (independent vs interdependent self, ledger C24).

### m3: The formal toolkit: draw the game before arguing about it

**Draws on:** `04-games-of-strategy` (ch 1-4, 8, 9, 10, 11, 12; evidence section; common
misreadings); `10-networks-crowds-markets` ch 6 (games on graphs framing only).

**Learning objectives.** The learner can (a) write down a group interaction as a game (players,
strategies as contingent plans, payoffs as the players see them, order, information) and classify
it as PD, stag hunt (assurance), chicken, battle of the sexes or pure coordination using the one
diagnostic question "does a member gain by defecting when everyone else cooperates?"; (b) explain
Nash equilibrium as a stability test, not a prediction or an endorsement, and say what the folk
theorem does and does not give; (c) design a credible sanction, a costly signal or a screening
menu and say why each works only under a stated condition.

**Load-bearing ideas.**
1. *Hold in memory.* Draw the matrix first and classify the shape; the shapes are formally
   distinct and need different fixes: PD (payoffs, repetition, sanctions), stag hunt (assurance),
   chicken (assignment or rotation), battle of the sexes (a fair tie-break), coordination (a focal
   point). Treating a stag hunt as a PD produces heavy enforcement where cheap reassurance would
   do. [E for the distinction; H for any group's classification; ledger rule 13]
2. *Hold in memory.* Nash equilibrium is a stability condition: no one gains by deviating alone.
   It is not a prediction (with multiple equilibria it predicts nothing; first-contact play is
   norm- and fairness-driven) and not an endorsement (mutual defection is an equilibrium because it
   is stable). [E; ledger rule 14, 16]
3. Repetition permits cooperation as one equilibrium among many when the future is long, uncertain
   and observable; selection and fast detection are separate problems; the properties "nice,
   retaliatory, forgiving, clear" matter, never tit-for-tat as a rule. [E for the theorem; ledger
   rule 15]
4. Credibility is manufactured, usually by limiting oneself: a sanction that costs the enforcer
   more than ignoring the violation will not be applied and will not deter; make sanctions cheap,
   fast and subgame-perfect. [E for the logic; `04` ch 8]
5. Information asymmetry is solved by costly signals (credible only when cheaper for the type you
   want) and self-selecting menus; equal cost for all types yields pooling and reveals nothing.
   [E for the theory; H that a given ritual has the asymmetry; `04` ch 9]

**Curiosity hook.** "Two teams both say they want a shared tooling standard and both refuse to
move first. A manager offers a bonus for adoption; nothing changes. What shape is this game, and
why did more money do nothing?" (Stag hunt: the payoffs already favour cooperation; the failure
is strategic uncertainty, not payoff; `04` ch 4, `06` ch 7; ledger C37.)

**Attempt (cold, before content).** "A volunteer community needs eight people to run its monthly
event. Everyone wants the event; nobody wants to be one of the eight. Attendance at the
organising call has fallen for three months. Write the game: who the players are, what each can
do, what each gets in the four combinations (I volunteer / I do not, given enough others do / do
not). Then name the cheapest fix." Predictable errors: the learner writes one matrix for what are
two different games (a chicken game if each strictly prefers others do it regardless; an assurance
game if volunteering pays given enough others volunteer), prescribes enforcement or guilt without
classifying, and treats "everyone wants the event" as if it made cooperation an equilibrium. The
reading gives the classification test and the fix per shape (`04` ch 4, 11: conditional pledges
for assurance, rotation or assignment for chicken).

**Worked example.** *Decision: should a community's code-of-conduct violation be met by an
immediate ban?* (1) Write the enforcement game as a sequential move: violator acts, then the
moderator chooses sanction or ignore. (2) Rollback: at the moderator's node, does sanctioning pay
at the moment of enforcement? An immediate ban of an established member costs the moderator a
public fight and possibly the member's contributions; ignoring costs little now. The ban threat
is not subgame-perfect, so it is not credible; violators know it and the rule is a norm with a
penalty nobody would impose (`04` ch 8). (3) Change the enforcer's payoff at the moment of
enforcement rather than the size of the threat: a small, cheap, public first response (a visible
note) costs the moderator almost nothing and is therefore credible; escalation is scheduled and
delegated so that the moderator is not choosing it alone. (4) Check credibility of the promise
side: is there a cheap way for the violator to return to good standing, so the sanction is
"forgiving" and "clear"? Resulting policy: "First violation: a public, templated note within a
day, applied by whoever is on rotation; second: a fixed one-week restriction; third: a review by
three members. Bans are never a first response." Tagged [E] that oversized threats are less
credible and that cheap sanctions are applied (`04` ch 8; `09` ch 3 for the field version);
[H] that the specific ladder fits this community; [V] that reversibility is worth the delay.

**Hinge questions.**

Q1. A team's shared on-call rota is decaying. You ask: "If everyone else did their shifts
faithfully, would one person still gain by skipping theirs?" The honest answer is yes, a skipped
shift is pure gain if covered by others. What follows?
- (a) It is a stag hunt; build assurance through public pledges. *Diagnoses: assurance as the
  default fix for any cooperation problem; misreads the diagnostic question (ledger rule 13).*
- (b) It is a PD-shaped problem; the fix set is payoff change, repetition with observability, or
  credible sanctions. **Correct** (`04` ch 4, 10; `07` ch 1).
- (c) It is a coordination problem that a clear schedule will fix. *Diagnoses: "every group problem
  is coordination that communication fixes" (ledger C31).*
- (d) It is chicken; rotate the burden. *Diagnoses: partly right, wrong level; rotation is already
  the rule and the question is enforcement of it, not assignment.*

Q2. A founder says "our engineers will keep working together for years, so the repeated-game
logic guarantees cooperation." Which correction is right?
- (a) Repetition guarantees nothing unless the horizon is finite. *Diagnoses: reversed; finite
  known horizons unravel cooperation, indefinite ones permit it.*
- (b) Repetition permits cooperation as one equilibrium among many; the group must also coordinate
  on it and detect defection fast. **Correct** (ledger C27, rule 15).
- (c) Repetition works only if the team plays tit-for-tat. *Diagnoses: tit-for-tat as optimal
  (ledger C26); it feuds under noise.*
- (d) Repetition works if the discount factor is above one half. *Diagnoses: quoting the book
  file's illustrative threshold as a general law; the threshold depends on the temptation and the
  cooperative payoff (`04` ch 10 worked example: with payoffs 3 for mutual cooperation, 1 for
  mutual defection and 5 for defecting on a cooperator, the illustrative threshold is one half;
  raise the temptation and it rises).*

Q3. A community wants to tell committed members from tourists before granting privileges. Which
proposal works, and why?
- (a) Ask applicants to state their commitment in a form. *Diagnoses: cheap talk as a signal;
  informative only when interests are aligned (`04` ch 9).*
- (b) Require a multi-week task that is cheap for people who intend to stay and costly for people
  who do not. **Correct**: a separating equilibrium needs cost that differs by type.
- (c) Charge everyone the same joining fee. *Diagnoses: cost as the signal regardless of
  asymmetry; equal cost pools types and reveals nothing.*
- (d) Make the joining task as hard as possible for everyone. *Diagnoses: "bigger cost equals
  better signal"; also screens out the type you want.*

Q4. A team reaches a state where everyone under-invests in shared tooling and nobody can improve
their lot by investing alone. A manager says "so this is what they want." What does `04` say?
- (a) Correct: equilibrium reveals preference. *Diagnoses: equilibrium as endorsement (ledger
  C32).*
- (b) Wrong: the state is stable, not preferred; it may be one of several equilibria and history
  picked it. **Correct** (`04` ch 4; `05` ch 3).
- (c) Wrong: rational people would never be in a bad equilibrium. *Diagnoses: "game theory proves
  rational people cannot cooperate" inverted; rationality means consistent preferences, and mutual
  defection is exactly what consistent preferences produce in a one-shot PD (ledger rule 16).*
- (d) Correct, but only because the engineers are selfish. *Diagnoses: rationality equals
  selfishness (ledger C28).*

Q5. In a two-team stag hunt, what is the best-supported first lever?
- (a) Raise the joint payoff for adoption. *Diagnoses: "coordination failure is a payoff problem"
  (ledger C37); sweetening the joint payoff is the weakest lever (`07` ch 1).*
- (b) Visible conditional pledges or a threshold ("we start when both sign"). **Correct**:
  assurance mechanisms reach the payoff-dominant equilibrium cheaply (`04` ch 11).
- (c) A penalty for the team that fails to adopt. *Diagnoses: treating a stag hunt as a PD;
  enforcement where reassurance would do.*
- (d) Let the teams keep negotiating until they agree. *Diagnoses: expecting rationality to select
  the equilibrium; multiplicity is resolved socially (`11` ch 9; ledger rule 14).*

**Repair paths.** Wrong on Q1: `04` ch 4 (canonical matrices) and ch 11 (collective-action
shapes); Q2: `04` ch 10 and the misreadings "repetition solves the PD" and "tit-for-tat is
optimal"; Q3: `04` ch 9 (signalling, separating vs pooling); Q4: `04` ch 4 and `05` ch 3
("equilibrium is descriptive"); Q5: `04` ch 11 (assurance mechanisms) and `06` ch 7 (payoff to the
safe action).

**Brief deliverable (s2, "diagnosis: the games being played").** Add: for each of the group's two
or three central interactions, a written matrix or two-curve sketch with payoffs as the members
see them, the answer to the defection question, the shape, and the fix set that shape allows;
one sanction or signal currently in use, checked for credibility (would the enforcer apply it at
the moment of enforcement?) or separation (does its cost differ by type?). Tag each. Prediction:
which interaction, if reclassified from PD to stag hunt or the reverse, changes the fix the
learner proposed in v0.

**Deeper pointers.** `04` ch 5 (best-response functions, effort games), ch 7 (mixed strategies and
random audits: required inspection probability is about gain over penalty), ch 13 (brinkmanship
and off-ramps), ch 14 (incentive design and crowd-out), ch 16 (voting rules and agenda control),
ch 17 (bargaining and outside options); `10` ch 6 (a game as a template played on every edge).

### m4: Micro to macro: thresholds, tipping, sorting

**Draws on:** `05-micromotives-and-macrobehavior` (ch 1, 2, 3, 4, 7; evidence section; common
misreadings); `10-networks-crowds-markets` ch 17 (network effects, the Z-shaped curve) and the
threshold notion from ch 19 (population form only; the graph version is m9).

**Learning objectives.** The learner can (a) separate micromotives from macrobehaviour and refuse
to infer intentions from outcomes or outcomes from intentions; (b) draw Schelling's two-curve
binary-choice diagram for a target behaviour and read off whether it is a multi-person PD (needs
rules), a coordination game with a tipping point (needs seeding above critical mass) or a stable
interior mix (leave alone); (c) state precisely what the checkerboard model shows and does not
show, and define a tipping point as an unstable equilibrium in a threshold distribution.

**Load-bearing ideas.**
1. *Hold in memory.* Macro is not micro summed: when behaviour is contingent (my choice depends on
   how many others choose), populations settle at equilibria that may be nobody's preference,
   several may exist, and history picks one. Check arithmetic constraints (musical chairs) before
   motives. [E for the logic; H that it explains any given case]
2. *Hold in memory.* The two-curve diagram is the diagnostic: if the defect curve is above the
   cooperate curve everywhere but all-cooperate beats all-defect, it is a multi-person PD; if the
   curves cross with cooperation winning to the right, there are two stable corners and an
   unstable interior tipping point, and critical mass is the crossing; if they cross the other way,
   the interior mix is stable. Most "culture" interventions fail by treating an MPD as if it were
   coordination. [E for the logic; H for the curve shapes in any real setting; ledger C31]
3. A tipping point is an unstable equilibrium in a threshold distribution or adoption curve; the
   scarce resource is low-threshold actors; a gap at the low end kills a cascade; a half-launch
   below critical mass decays and poisons the next attempt. [E for the model; ledger rule 18]
4. The checkerboard shows that mild preferences plus interdependence *can* produce extreme sorting
   and that homogeneity is weak evidence of intolerance; it does not show that preferences are the
   main real-world cause, that preferences are exogenous, or that the outcome is acceptable;
   empirical tipping in US census tracts is at roughly 5-20% minority share, higher where measured
   tolerance is higher (Card, Mas and Rothstein 2008, verified); fragility to preference shape is
   disputed. [E for the model and the empirical tipping; ledger rule 17]
5. Self-enforcing conventions (unilateral deviation hurts the deviator) need a focal point, not a
   policeman; reserve enforcement budget for genuine MPDs. [E for the distinction; H for which of
   the group's norms are which]

**Curiosity hook.** "Everyone on a team says they want the weekly cross-team demo to survive.
Attendance falls from twelve to seven to three and it dies. Nobody changed their mind. What
killed it?" (A dying-seminar dynamic: attendance contingent on expected attendance, with the
population below critical mass; `05` ch 1, 3.)

**Attempt (cold, before content).** "Adoption of architecture decision records in an
engineering org has sat at fifteen percent for a year despite two reminders and a template. Draw,
for a person deciding whether to write one, the payoff of writing and the payoff of not writing
as the share of others who write goes from none to all. Say which of three shapes you have drawn
and what each implies." Predictable errors: the learner draws one shape without asking whether
the value of writing depends on others reading and writing (contingency), assumes the answer is
"more reminders" (an intervention that moves no curve), and does not consider that fifteen
percent might be a stable interior mix (only some decisions warrant a record) in which case
pushing for full adoption is a mistake. The reading gives the three shapes and the fix per shape
(`05` ch 7). (The fifteen percent is a scenario number.)

**Worked example.** *Decision: how to launch a shared internal tool whose value to each user
rises with the number of other users.* (1) Recognise a network-effect good: adoption has a Z-shaped
willingness curve with equilibria at zero, an unstable interior point and a high stable point
(`10` ch 17; in the file's illustrative model with intrinsic interest falling linearly and value
proportional to adoption, a price of one fifth gives a tipping point near three in ten adopters
and a stable high point near seven in ten; illustrative numbers). (2) Therefore diffuse
encouragement across the whole org leaks away if adoption sits below the tipping point; a
concentrated push in one subgroup can cross it locally. (3) Identify low-threshold people (those
who will use it if almost nobody else does) and guarantee their presence at launch; the cascade
dies at the low end of the threshold distribution (`05` ch 3). (4) Make adoption visible so
perceived adoption tracks real adoption, and avoid announcing a launch the subgroup cannot carry
past the crossing, because a half-launch creates a self-defeating expectation for the next try.
(5) Lower the threshold itself: reduce switching cost (import, compatibility) so the tipping point
moves down. Resulting policy: "Launch in one team of about ten with three committed early users
pre-recruited; publish adoption within that team only; org-wide launch only once that team is past
its crossing; cut switching cost before widening." Tagged [E] for the tipping logic; [H] for this
tool's threshold and for the choice of team; [V] that the slower launch is worth it.

**Hinge questions.**

Q1. A company's most senior engineers have ended up clustered on one team, and juniors on the
others, although no manager ever assigned by seniority and everyone says they value mixed teams.
What does Schelling license you to conclude?
- (a) Managers are lying about their preferences. *Diagnoses: inferring intentions from outcomes
  (`05` ch 1).*
- (b) Mild preferences not to be the least experienced person in a group, plus free movement,
  can produce this sorting without anyone wanting it; the homogeneity is weak evidence about
  attitudes. **Correct** (`05` ch 4, 5; ledger rule 17).
- (c) The sorting proves preferences caused it, so attitude work is the fix. *Diagnoses:
  "Schelling proved segregation is caused by mild preferences" (ledger C29); the model shows
  sufficiency, not cause, and attitudes move the threshold without removing the dynamic.*
- (d) Since the outcome is structural, attitudes are irrelevant. *Diagnoses: the opposite
  over-reading; Card, Mas and Rothstein find higher tipping points where measured tolerance is
  higher.*

Q2. Two curves for "attend the daily standup": the not-attend payoff is above the attend payoff at
every level of others' attendance, but all-attend beats all-skip for everyone. What follows?
- (a) It is a coordination problem; seed attendance above critical mass. *Diagnoses: "every
  group problem is coordination that communication will fix" (ledger C31); this is an MPD.*
- (b) It is a multi-person PD; only a rule, monitoring or a side payment moves it. **Correct**
  (`05` ch 7).
- (c) It is a stable interior mix; stop pushing for full attendance. *Diagnoses: misreading
  "curves do not cross" as an interior equilibrium; there is no interior crossing here.*
- (d) The curves are wrong because everyone says they value the standup. *Diagnoses: inferring
  outcomes from intentions.*

Q3. A colleague proposes to spread a new practice by recruiting "the three most influential
people" to endorse it. What is the Schelling correction?
- (a) Influence is what matters; find the most charismatic. *Diagnoses: the Gladwell reading of
  tipping (ledger C30).*
- (b) The scarce resource is low-threshold actors, people who will adopt when few others have;
  influence is secondary and a gap at the low end kills the cascade. **Correct** (`05` ch 3;
  ledger rule 18).
- (c) Tipping points are not real; adoption is driven by independent preferences. *Diagnoses:
  over-correction; the logic is uncontested, what is contested is how often behaviour is
  contingent enough (`05` evidence).*
- (d) Endorsements from influential people work because of prestige bias, so this is the Henrich
  lever. *Diagnoses: partly right, wrong level; prestige selects whom people copy, but the
  cascade still needs the threshold distribution to have no gap.*

Q4. A team adopts a rule that everyone welcomes, then discovers that several members would not
have complied voluntarily and only follow it because it is now the rule. What does this tell you?
- (a) The rule was unnecessary since everyone welcomed it. *Diagnoses: conflating the preference
  for the rule with the preference to comply alone; the helmet case (`05` ch 7, an anecdote).*
- (b) The behaviour was an MPD: each preferred all-comply to all-defect but defect dominated
  individually, so the rule gives everyone what nobody would choose alone. **Correct** (`05`
  ch 7; design implication "consult on the rule, not on voluntary adoption").
- (c) The members who need the rule are the problem. *Diagnoses: moralising a structural
  outcome (`05` ch 1).*
- (d) The rule will fail because rules only work with buy-in on the behaviour. *Diagnoses:
  buy-in on behaviour as necessary; an MPD rule is welcomed by people who would not comply
  voluntarily.*

**Repair paths.** Wrong on Q1: `05` ch 4 (what the model shows and does not) and ledger C29.
Q2 and Q4: `05` ch 7 (the binary-choice diagram in words). Q3: `05` ch 3 (threshold
distribution) and the misreading on Gladwell.

**Brief deliverable (s5, "threshold and tipping map").** Add: for the group's key target
behaviour, the two-curve sketch and its shape; whether the current state is below or above a
crossing; the group's likely low-threshold members; one arithmetic constraint the v0 plan ignored
(mentors to mentees, reviewers to reviews); one norm that is self-enforcing and one that needs a
rule. Tag each. Prediction: the minimum viable coalition size (Schelling's k) the learner would
need for a pilot, stated as a hypothesis.

**Deeper pointers.** `05` ch 2 (accounting identities, class-size paradox), ch 5 (ordered-attribute
sorting), ch 6 (positional goods), ch 8 (the nuclear taboo as an aged convention); `10` ch 17
worked model and Salganik, Dodds and Watts; ledger open questions on Bruch and Mare vs Van de
Rijt.

### m5: What people actually do: social preferences, coordination experiments, learning

**Draws on:** `06-behavioral-game-theory` (ch 1, 2, 5, 6, 7; evidence section; common
misreadings); `03-social-psychology` ch 14 (cooperation section); ledger rows 4.1-4.12,
rules 9, 25-28.

**Learning objectives.** The learner can (a) say which of the three amendments (social
preferences, limited iterated reasoning, learning) is driving a departure from the formal
prediction and choose the matching fix (payoffs and fairness frame; salience and simplicity; early
experience and feedback); (b) quote the fairness evidence with the ledger's hedges and describe
the group as a distribution of types rather than a representative agent; (c) explain weak-link
collapse, history lock-in and the effect of communication and gradual growth on coordination.

**Load-bearing ideas.**
1. *Hold in memory.* Three amendments, not a rejection: real play departs from equilibrium
   because people care about fairness and reciprocity, reason one or two steps about others
   (beauty-contest first-round average about 35 with p = 2/3, Nagel 1995, verified; mean thinking
   steps about one and a half), and learn their way toward equilibrium so that early rounds lock in.
   Diagnose which is operating before intervening. [E]
2. *Hold in memory.* Fairness and generosity are real, conditional and culturally variable: mean
   ultimatum offers about 40% with a mode at 40-50% (Oosterbeek 2004, verified); people pay to
   punish unfair intentions, not outcomes (Blount 1995); dictator giving averages about 28% with
   about 64% giving something (Engel 2011, verified) but collapses under double-blind anonymity and
   shifts with take options; small-scale societies' mean offers run from about 26% to about 58%
   (Henrich 2001, verified). Model the group as a distribution: roughly three in ten
   self-interested, about half conditional cooperators, a small tail of altruists (background).
   "A taste for fairness of fixed size" is not [E]. [E for cue-dependence; H for any parametric
   model; ledger rule 9, 25, 26]
3. Weak-link coordination fails at scale: groups of 14-16 in minimum-effort games fell to the
   lowest effort within about ten rounds while fixed pairs reached the highest (Van Huyck 1990;
   group-size result verified, rounds background); play converges to the risk-dominant outcome
   without communication; two-way cheap talk, leader communication, gradual growth from a small
   core (Weber 2006, verified, one lab) and a lower payoff to the safe action select the efficient
   equilibrium. [E for the lab; H for the group; ledger rule 2, C60]
4. Lab results transfer as mechanisms and directions, not point estimates: 61% of 18 top-journal
   economics experiments replicated with effects about two-thirds of the originals (Camerer et al.
   2016, verified); high-stakes rejections fall; positive reciprocity to pay is weak and decaying
   (Gneezy and List 2006, verified) while negative reciprocity is strong. [E; ledger rule 27, 28]

**Curiosity hook.** "A responder is offered a fifth of a pie by an anonymous stranger she will
never meet; rejecting leaves both with nothing. About half the time she rejects. When the same
offer is generated by a computer, she mostly accepts. What is she paying to punish?"
(Intentions, not outcomes; `06` ch 2, Blount 1995.)

**Attempt (cold, before content).** "You run a twenty-person on-call rotation whose outcome is
set by the least-prepared engineer on duty; preparation has drifted to the minimum. You have a
small budget. Propose three interventions and rank them by expected effect." Predictable errors:
the learner leads with a bonus (a payoff fix for what is a strategic-uncertainty problem), keeps
the group at twenty, and does not think of the aggregation rule (minimum versus median) or of
growing from a coordinated core with a visible history. The reading explains the weak-link results
and the post-2003 selection devices (`06` ch 7).

**Worked example (partially faded: the learner completes steps 4 and 5).** *Decision: a
platform must split a fixed pool of contributor rewards unequally; complaints and exits follow
each round.* (1) The evidence says people punish intended unfairness far more than unlucky or
rule-based outcomes (`06` ch 2), so the diagnosis is the perceived intention behind the split, not
its inequality as such. (2) Which amendment? Social preferences, with a cue-dependent norm
(ledger X8): the split is seen as a proposer's choice. (3) The fix set is procedural: make the
rule impersonal and public before contributions happen; if some discretion remains, use a
lottery for the discretionary part. The learner writes (4) the prediction (complaints fall, exits
of the top contributors fall, average contribution unchanged or up) and (5) the tags ([E] for
intention-sensitivity in the lab; [H] for the magnitude on this platform, since field effects
are about two-thirds of lab ones or smaller; [V] for the choice of a rule over discretion).

**Hinge questions.**

Q1. A manager cites lab gift-exchange results to justify above-market pay for sustained extra
effort. What does the evidence support?
- (a) The lab result transfers; pay more and effort rises durably. *Diagnoses: lab numbers
  transfer to the field (ledger C35, C36).*
- (b) Positive reciprocity to a pay raise is real but weak and decays within hours in the field
  (Gneezy and List 2006); negative reciprocity to cuts and broken promises is strong. **Correct**
  (ledger rule 28).
- (c) Reciprocity is a lab artefact; only incentives matter. *Diagnoses: over-correction to
  "people are payoff maximisers"; the ultimatum and trust results are robust.*
- (d) It works only if the raise is framed as a gift. *Diagnoses: partly right, wrong level;
  framing matters in the lab, but the field finding is about persistence, which framing does not
  rescue.*

Q2. A new community's first credit-allocation round is contested and the founders say "it will
settle down with experience." Which amendment does `06` invoke, and what should they do?
- (a) Learning: play converges to equilibrium, so wait. *Diagnoses: convergence as automatic;
  learning drifts toward equilibrium and stalls, and its direction depends on early rounds.*
- (b) Learning: the steady state is path-dependent, so seed the first rounds deliberately and
  give feedback on what each choice would have earned. **Correct** (`06` ch 6, 7; median-effort
  lock-in).
- (c) Social preferences: people are altruists and will share. *Diagnoses: "people are
  altruists" (ledger C33); dictator giving is fragile norm compliance.*
- (d) Limited reasoning: explain the equilibrium to them so they can compute it. *Diagnoses:
  expecting deep iterated reasoning on first contact; people reason one to two steps.*

Q3. A group of sixteen reviewers must all sign off before a release; releases slip because one
reviewer is always late, and everyone else has started reviewing less carefully. What is the
best-supported structural fix?
- (a) Pay a bonus for on-time sign-off. *Diagnoses: "coordination failure is a payoff problem"
  (ledger C37); the least-supported first lever.*
- (b) Shrink the set whose minimum matters, or change the aggregation rule from "all must sign" to
  a median or quorum rule. **Correct** (`06` ch 7; weak-link vs median-effort).
- (c) Replace the late reviewer. *Diagnoses: dispositional diagnosis; the collapse pattern is
  structural and recurs with any sixteen.*
- (d) Remind everyone of the standard. *Diagnoses: exhortation without common knowledge; advice
  works when public and common knowledge (Chaudhuri 2009), and reminders are neither.*

Q4. Which statement about fairness may be tagged [E] in a brief?
- (a) People everywhere expect a fifty-fifty split. *Diagnoses: fairness as a universal 50-50
  (ledger C34).*
- (b) Fairness norms are cultural: the disposition to have them is universal, the content varies
  with the economics of daily life. **Correct** (Henrich 2001, verified direction; causality
  unresolved, ledger C59).
- (c) Market exposure makes people fair. *Diagnoses: stating the causal direction the data cannot
  fix (ledger C59).*
- (d) Most people are inequity averse with fixed parameters. *Diagnoses: a single social-
  preference model as [E]; `06`'s own verdict is no model wins (ledger rule 9).*

**Repair paths.** Wrong on Q1: `06` evidence section, gift exchange in the field. Q2: `06` ch 6
(learning regularities) and ch 7 (median-effort games). Q3: `06` ch 7 (weak-link games and
post-2003 additions). Q4: `06` ch 2, cross-cultural results, and ledger C34, C59.

**Brief deliverable (s6, "population of types and fairness baseline").** Add: the learner's
estimate of the group's type mix in words (mostly conditional cooperators? a large selfish
minority?) and what conditional cooperators can currently see of others' contributions; the
group's own fairness reference point for the allocations that matter (not the lab's); any
weak-link process (where the worst performer sets the outcome) and its group size; which of the
three amendments best explains the main v0 failure. Tag each. Prediction: what happens to
contributions if others' contributions become visible.

**Deeper pointers.** `06` ch 3 (mixed strategies as population facts), ch 4 (bargaining and
self-serving fairness), ch 8 (reputation with a homemade prior); the type-distribution caveat
(Bruhin 2019, background); ledger open questions on market integration and framing equivalence.

### m6: How populations settle: risk dominance, correlation, signals

**Draws on:** `07-stag-hunt` (all chapters; evidence section; common misreadings); `06` ch 7
(re-read for the lab counterpart); `04` ch 12 (ESS, basins); ledger X6, X7, X11, X12, rules 2, 3,
12, 13, 36.

**Learning objectives.** The learner can (a) state the risk-dominance rule with its conditions
(random mixing, best-response updating, large groups, no communication or history) and the
levers that make payoff dominance reachable (correlation through small stable groups,
success-visible imitation, public pledges, gradual growth, lower cost of being the lone
cooperator); (b) explain why local interaction helps cooperation only under success-copying and
why a dense cluster both blocks and protects; (c) say what cheap talk does in a stag hunt and
why it does not rescue a true PD, and pace a rollout so structure re-sorts faster than behaviour
is re-evaluated.

**Load-bearing ideas.**
1. *Hold in memory.* Under random mixing a stag-hunt population goes to whichever equilibrium's
   basin it starts in, and the risk-dominant one usually has the larger basin; basin size, not the
   attractiveness of the good outcome, decides. In the illustrative payoffs (stag with stag 4,
   stag with hare 0, hare 3 against anyone) the watershed is three quarters stag hunters; raising
   the lone-cooperator payoff from 0 to 2 moves it to one half. Cutting the cost of being the lone
   cooperator moves the watershed more than sweetening the joint outcome. [E for the model and
   the lab; H for any group's regime; ledger rule 2]
2. *Hold in memory.* Correlation is the master variable: anything that makes cooperators meet
   cooperators more than chance (location, signals, partner choice) expands the cooperative basin.
   Local interaction helps only under imitate-the-best; under best response it accelerates the
   risk-dominant outcome (Ellison 1993) and with noise the risk-dominant equilibrium is the
   long-run stable one (Kandori, Mailath and Rob; Young). [E for the models; ledger rule 3, 36]
3. Cheap talk is a transient handshake that lets stag hunters find each other; it expands the
   stag basin in models and raises stag hunting in the lab, but in a PD a mimic that signals and
   defects invades; expect talk to decay without sanctions where defection dominates. [E for
   models and lab; H for persistence; ledger rule 12]
4. When partnerships re-sort faster than strategies are re-evaluated, cooperators find each
   other, out-earn hare hunters, get imitated, and the population tips to cooperation; when
   behaviour is re-judged while matching is still near random, risk dominance returns. The
   speed ratio is a design variable. [H, grounded in `07` ch 6-7 simulations]
5. Skyrms's agents have no beliefs or motives; the results hold for stag hunts under specific
   learning rules and do not rescue true PDs; pair with Ostrom (institutions) and Bicchieri
   (expectations). [E as a scope statement; ledger C41]

**Curiosity hook.** "Two teams would both be better off adopting a shared standard and both
know it. Left alone, they will not. Nobody is stupid and nobody is selfish. Where does the
outcome come from if not from anyone's preference?" (From the basin of attraction under
uncertainty about the other; `07` ch 1.)

**Attempt (cold, before content).** "Using the illustrative payoffs (stag with stag 4, stag with
hare 0, hare 3 against anyone), a population of one hundred starts with sixty stag hunters under
random matching and success-biased imitation. Predict where it ends. Then propose one change to
the payoffs and one change to the matching that would reverse the outcome." Predictable errors:
the learner predicts all-stag because sixty is a majority and stag pays more (the watershed is
three quarters, so sixty goes to hare); proposes raising the stag-with-stag payoff (the weak
lever) rather than the lone-cooperator payoff; and proposes "mix everyone together more" (random
mixing is the enemy). The reading gives the watershed arithmetic and the three correlation
devices.

**Worked example (faded: the learner supplies the pacing decision).** *Decision: how to roll out
a new practice (blameless post-mortems) across a forty-person org where it is a stag hunt.* (1)
Classify: nobody gains by running a blame-free review alone while others still blame; everyone
gains if all do; a stag hunt (ledger rule 13). (2) Correlation lever one, location: start in two
stable teams of five to eight, not by assigning volunteers across the org; make the reviewed
teams' outcomes visible so that success-copying, not majority-copying, can operate (ledger rule
3). (3) Lever two, signals: a public opt-in pledge by the pilot teams, understood as a transient
handshake, not as a binding commitment. (4) Lever three, association and speed: let people choose
to join a piloting team before the org evaluates the practice. The learner writes the pacing
rule (form and protect the pilot cluster first; evaluate the practice only after the cluster's
interior is stable) and predicts what happens if the org instead runs a monthly "is this
working?" survey from week one. Tags: [E] that correlation expands the basin in models; [H] that
these teams and this pace are right; [V] that the pilot's slower spread is preferred to a mandate.

**Hinge questions.**

Q1. A CTO says: "Adopting the standard is obviously the rational choice, so teams that do not are
being irrational." Which correction applies?
- (a) They are being selfish, not irrational. *Diagnoses: rationality equals selfishness (ledger
  rule 16).*
- (b) Under uncertainty about the other team, the safe choice is defensible; the failure is
  structural (basin size), and so is the fix. **Correct** (`07` common misreadings; ledger
  rule 2).
- (c) They are irrational, and a payoff sweetener will fix it. *Diagnoses: "the efficient
  equilibrium is the rational one" plus "coordination failure is a payoff problem" (ledger C37).*
- (d) They lack information; publish the benefits. *Diagnoses: information deficit as the
  problem; the payoffs are already common knowledge in the scenario.*

Q2. A large org reorganises so that everyone rotates teams every quarter, expecting cooperation
norms to spread faster. What does `07` predict?
- (a) Faster spread, since more people meet the cooperators. *Diagnoses: "more mixing spreads
  good norms"; random mixing is the assumption under which cooperation is hardest.*
- (b) Slower or failed spread: rotation destroys the correlation that lets cooperators meet
  cooperators and re-evaluates strategies before association can help. **Correct** (`07` ch 6-7;
  postscript).
- (c) No effect; norms are about beliefs, not structure. *Diagnoses: expectations as the whole
  story; Skyrms shows basin size decides with no beliefs at all (ledger X5).*
- (d) Faster spread, provided the org is large enough. *Diagnoses: confusing collective-brain
  connectivity (information) with correlation (enforcement and complex contagion); ledger X15.*

Q3. A pilot cluster of cooperators sits inside a larger group. The larger group's habit is to do
"what most people here do". What happens to the cluster?
- (a) It spreads, since local interaction favours cooperation. *Diagnoses: local interaction as
  unconditionally helpful (ledger C39).*
- (b) It gets swamped, because majority-copying looks at what the neighbourhood does, not at
  who is thriving; only success-copying lets a cluster convert its boundary. **Correct** (`07`
  ch 3; ledger rule 3, 36).
- (c) It spreads if the cluster's members are the prestigious ones, since people copy the
  prestigious. *Diagnoses: substituting Henrich's whom-to-copy bias for Skyrms's learning rule;
  prestige decides whom people watch, but under majority-copying the boundary cells still act on
  what most of their neighbours do (`01` ch 8 vs `07` ch 3).*
- (d) It is protected by its density and stays as it is. *Diagnoses: partly right, wrong level;
  density protects an adopted behaviour (`10` ch 19), but under majority-copying the boundary
  cells see a hare-hunting majority and defect.*

Q4. Before a resource-allocation decision, a manager gets everyone to state publicly that they
will contribute their share. Under what condition does `07` say this is nearly worthless?
- (a) When the group is large. *Diagnoses: size as the condition; size matters in weak-link
  games (`06`) but the Skyrms condition is game shape.*
- (b) When defection dominates (a true PD): a mimic who pledges and defects invades, so the
  handshake needs sanctions or repetition behind it. **Correct** (`07` ch 5; ledger rule 12).
- (c) Always, because at equilibrium everyone sends the same message. *Diagnoses: assessing only
  the equilibrium; the information is transient and changes which equilibrium is reached.*
- (d) When the pledges are not binding. *Diagnoses: "communication works only through binding
  commitment" (`08` misreading); the pledges in every relevant model and experiment are
  non-binding.*

**Repair paths.** Wrong on Q1: `07` ch 1 (risk dominance) and its common misreadings. Q2: `07`
ch 6-7 (association, speed ratio) and the postscript. Q3: `07` ch 3 (learning rule) and ledger
X7. Q4: `07` ch 5 (cheap talk) and ledger X12.

**Brief deliverable (s7, "equilibrium selection plan").** Add: for the group's main stag-hunt
interaction, the current regime (near-random mixing and frequent re-evaluation, or stable
subgroups with visible success?); the learner's watershed estimate in words (is the group above
or below the fraction needed?); which correlation device (location, signal, partner choice) is
cheapest; the intended lone-cooperator cost reduction; the rollout pacing rule. Tag each.
Prediction: what a public pledge will do in this group, and how long the effect lasts without
sanctions if the interaction is really a PD.

**Deeper pointers.** `07` ch 2 (fairness contagion under local imitation, model-dependent per
D'Arms et al., ledger C65), ch 4 (meaning evolves in the simplest signalling game; dialects fork
on lattices, ledger C40); `04` ch 12 (ESS, hawk-dove, the bourgeois strategy); `06` ch 7 post-2003
additions (Weber; Brandts and Cooper).

### m7: Norms: expectations, measurement, change

**Draws on:** `08-grammar-of-society` (all chapters; evidence section; common misreadings);
`03` ch 9 (descriptive and injunctive norms, conformity); `10` ch 16 (information cascades);
ledger X8, X9, X12, X14, rules 10, 11, 12, 24, 37, 38.

**Learning objectives.** The learner can (a) classify any "norm" as descriptive, convention,
social or moral by the expectations that sustain it, and say which expectation to shift to change
it; (b) design a two-step expectation measurement (what you do; what most do; what most think you
should do; what happens if you do not) and read a pluralistic-ignorance gap from it; (c) explain
why relevant talk changes the game and how cascades make unpopular norms both fast to form and
fragile.

**Load-bearing ideas.**
1. *Hold in memory.* A social norm is a conditional preference keyed to two expectations: an
   empirical expectation that enough others conform and a normative expectation that enough
   others think one ought to, possibly backed by sanctions. A descriptive norm needs only the
   first; a convention is a descriptive norm that is also a coordination equilibrium; a moral
   norm needs neither. "What most people do" is a descriptive norm, not a social norm; a social
   norm can exist while widely violated. [E as a definition with validated measurement; ledger
   rule 11]
2. *Hold in memory.* Assume every norm is conditional until it survives a collapse of
   expectations; only then call it internalised. Diagnose by expectations, not behaviour or
   stated values; a values workshop targets the wrong thing when the norm is conditional. [H for
   the internalisation debate; E for the measurement; ledger rule 10]
3. Norms transform games without changing material payoffs: with a cooperation norm expected to
   apply and enough norm-sensitivity, a PD acquires a cooperative equilibrium and becomes a stag
   hunt (in the illustrative PD with payoffs 3 for mutual cooperation, 5 and 0 for defecting on a
   cooperator, 1 for mutual defection, sensitivity of at least two thirds suffices); when
   expectations lapse the game reverts. Norm-based utility is the course's working model, argued
   from fit rather than shown to beat inequity aversion, and still needs a substantive fairness
   concept to say which split people expect. [E for cue-dependence; H for the parametric model;
   ledger rule 38]
4. Unpopular norms live on pluralistic ignorance sustained by cascades; disapproval must become
   common knowledge; the levers are measuring and publishing the expectation gap and a credible
   trendsetter, with the caveat that social-norms marketing has mixed results and descriptive
   messages alone boomerang. [E for the diagnosis; H for the intervention in a given group;
   ledger rule 24, C44]
5. Norm activation is cue-driven (scripts), which is why templates, channel names and openers
   matter; this is not behavioural priming, and any specific cue-to-norm mapping is [H]. [ledger
   rule 37]

**Curiosity hook.** "Seven in ten members of a team privately think weekend messages are
inappropriate; eight in ten believe most colleagues think they are fine; three quarters send them.
Nobody is lying. What is the norm made of, and what single intervention would collapse it?"
(Pluralistic ignorance; publish the gap credibly and coordinate a visible first deviation; `08`
ch 5. Scenario numbers.)

**Attempt (cold, before content).** "A startup's engineers all write thorough pull-request
descriptions. A new lead joins and writes terse ones; within a month everyone does. Name what
kind of norm the thorough-description practice was, and explain the collapse. Then design the
measurement you would run before trying to restore it." Predictable errors: the learner calls it
"a value the team lost", proposes a values statement or a policy document, and designs a survey
about attitudes rather than expectations. The reading gives the taxonomy (this was a descriptive
norm sustained by empirical expectations only) and the two-step elicitation (`08` ch 1, 5;
Bicchieri and Xiao 2009, verified: empirical expectations of selfishness reduced giving even
under pro-giving normative messages).

**Worked example (faded: the learner writes the measurement items).** *Decision: whether to
address a "crunch is normal" culture with a leadership statement.* (1) Classify: is crunch a
descriptive norm (people match what they see), a social norm (people believe others expect it
and would disapprove of leaving on time), or a convention (nobody gains by leaving alone)?
Statements target only normative expectations, and only if the source is credible. (2) Measure
before acting: the learner drafts four items per the two-step method and one item on sanctions.
(3) Read the result: if private attitudes reject crunch but perceived normative expectations
support it, it is pluralistic ignorance; publish the gap and recruit a visible, credible
trendsetter with low sensitivity to the norm. If private attitudes support crunch, it is not
pluralistic ignorance and the intervention is a rule (m8), not a revelation. (4) Pair the
descriptive and injunctive channels (ledger rule 24) and never publish the share who crunch.
Tags: [E] for the diagnosis method; [H] for the trendsetter intervention (case studies, not
controlled tests); [V] that crunch should be reduced at all.

**Hinge questions.**

Q1. A community's rule says "cite sources". Most posts do not. Members, asked privately, say
others do not care. Which classification and lever?
- (a) It is a social norm being violated; punish violators. *Diagnoses: "a social norm is what the
  rules say" and sanctions as the only lever; the normative expectation is absent, so the norm
  does not exist in Bicchieri's sense.*
- (b) It is a dead rule: neither empirical nor normative expectations support it; the lever is to
  create both, starting with visible compliance by credible members and expressed expectations.
  **Correct** (`08` ch 1).
- (c) It is a moral norm that needs values work. *Diagnoses: norms as internalised values
  (ledger C43).*
- (d) It is a descriptive norm; publish that most posts lack sources so people realise. *Diagnoses:
  advertising the prevalence of misbehaviour (ledger rule 24).*

Q2. A team's "no blame in post-mortems" practice holds firm even after the manager who introduced
it leaves and a new manager visibly blames. What can you now conclude?
- (a) It was a convention. *Diagnoses: convention as any stable practice; a convention would flip
  with the visible majority since nobody gains by deviating only while others conform.*
- (b) It survived a collapse of expectations, so treat it as internalised or moral for these
  members. **Correct** (ledger rule 10, the agreed test).
- (c) It is proof that norms are always internalised. *Diagnoses: generalising from one survival
  to the Henrich/Gintis position; the debate is open (ledger X9).*
- (d) It will collapse within a month; wait. *Diagnoses: "all norms are conditional" as a law
  rather than a default assumption.*

Q3. Why does ten minutes of relevant discussion before a public-goods round raise cooperation,
according to `08`?
- (a) It lets people make binding commitments. *Diagnoses: commitment as binding (`08`
  misreading); the promises are unenforceable.*
- (b) It creates or makes salient the empirical and normative expectations a cooperation norm
  needs, turning the PD into a coordination game among norm-sensitive players. **Correct** (`08`
  ch 4).
- (c) It builds group identity, which is the whole effect. *Diagnoses: partly right, wrong level;
  identity accounts cannot explain why only relevant talk works.*
- (d) It does not; talk is empty at equilibrium. *Diagnoses: "talk is empty" (ledger rule 12);
  roughly doubled cooperation in Dawes 1977, background.*

Q4. Bicchieri's account of fair behaviour in experiments is best summarised as:
- (a) People have a taste for fairness of fixed size. *Diagnoses: fixed social preferences
  (ledger X8).*
- (b) Fair behaviour is norm compliance activated by cues of observation, entitlement and
  expectation; remove the cues and it evaporates; a substantive fairness concept is still needed to
  say which split is expected. **Correct** (`08` ch 3; ledger rule 38).
- (c) People are selfish and fairness is an illusion. *Diagnoses: over-reading "no taste for
  fairness needed" as "no fairness"; she allows moral norms and the behaviour is real.*
- (d) Fairness is primed by subtle cues like words and images. *Diagnoses: equating script
  activation with behavioural priming (ledger rule 37).*

**Repair paths.** Wrong on Q1 or Q2: `08` ch 1 (the definition and taxonomy) and ledger X9.
Q3: `08` ch 4 (covenants without swords). Q4: `08` ch 3 and evidence section ("fairness is still
needed").

**Brief deliverable (s8, "norm register").** Add: a table of the group's three most important
"norms", each classified by the expectations that sustain it, with the measurement the learner
will run (four items plus a sanction item), the expected pluralistic-ignorance gap, the current
descriptive and injunctive signals, and the cue set (templates, openers) that summons the script.
Tag each row. Prediction: which one norm will collapse if a visible member deviates, and which
will not.

**Deeper pointers.** `08` ch 2 (scripts and schemata, with the priming caveat), ch 6 (evolution
of a fairness norm as a possibility proof); the *Norms in the Wild* toolkit note in `08`
misreadings (trendsetters, reference networks); `03` ch 9 (Asch, 133 studies in 17 countries,
verified; minority influence); `10` ch 16 (the urn model; a wrong cascade about one time in five
with two-thirds-accurate signals, illustrative computation).

### m8: Institutions for the commons: design principles, sanctions, polycentricity

**Draws on:** `09-governing-the-commons` (all chapters; evidence section; common misreadings);
`04` ch 8 (credible sanctions), ch 10 (repetition), ch 11 (collective action); ledger X10, X11,
rules 13, 29, 30.

**Learning objectives.** The learner can (a) say why the tragedy of the commons is a tragedy of
open access and check whether members can communicate, observe each other and change their rules
before calling anything a free-rider problem; (b) run the eight principles (Cox's split version)
as a diagnostic checklist against a real group and name the missing ones; (c) design graduated
sanctions, by-product monitoring and a cheap dispute forum, and say which level of rules
(operational, collective-choice, constitutional) a stalled reform is failing at.

**Load-bearing ideas.**
1. *Hold in memory.* The PD, Hardin and Olson are valid for open access and wrong as laws:
   they assume no communication, no rule-making, no monitoring, no shared past or future. Where
   those exist, participants move themselves into a different game. Ask first whether the
   channels exist; the payoff matrix is the symptom. [E; ledger C49]
2. *Hold in memory.* Monitoring and commitment are one problem: compliance is contingent on
   believing others comply and violations are likely caught; monitoring that is a by-product of
   use is cheap; first sanctions are small and graduated because their job is to signal that the
   rule is alive, and severe escalation is held for repeat offenders. Real-world sanctioning is
   mostly cheap; design on the cheap version. [E from the cases; ledger rule 30, X4]
3. The eight principles (boundaries of users and resource; congruence with local conditions and
   proportionality of costs to benefits; collective-choice arrangements; monitoring of users and
   resource; graduated sanctions; conflict-resolution mechanisms; recognition of the right to
   organise; nested enterprises) are a diagnostic checklist supported by a review of 91 studies
   (Cox et al. 2010, verified) with publication-bias and structure-not-process caveats; never a
   recipe, never anti-state, never evidence of fairness; flag scope for digital or knowledge
   commons. [E as a checklist; ledger rule 29]
4. Institutions are supplied incrementally; the first cheap change that produces information
   and standing lowers the cost of the next; external authority is most useful as backstop and
   data supplier, least as rule-writer. Copy the norm package of a visibly successful peer, then
   craft with the people bound by the rules. [H; ledger X10]
5. Rules live at three levels; most proposed fixes are operational and most failures are at the
   collective-choice level (nobody affected can legitimately change the rule) or the
   constitutional level (the group has no recognised standing). Turnover raises discount rates
   and undermines every other principle. [E for the levels; H for the discount-rate claim in a
   given group]

**Curiosity hook.** "A village capped how many cows each household could send to the shared
alp in a rule dated 1517, and the rule is still in use. No state wrote it and nobody privatised
the pasture. What did the villagers have that the textbook herders did not?" (`09` ch 3, Törbel:
communication, rule-making, by-product monitoring, graduated fines, a forum; background date.)

**Attempt (cold, before content).** "An engineering org shares a CI cluster. Queues are long,
some teams submit huge jobs, and the platform team plans per-team quotas enforced by automatic
lockout. In ten lines, predict what happens in three months and propose an alternative."
Predictable errors: the learner accepts the quota as the obvious fix (an operational rule imposed
from outside with an unaccountable monitor and a nuclear first sanction), does not ask whether
usage is visible to teams, whether affected teams can change the rule, or where disputes go, and
does not recognise the Kirindi Oya pattern. The reading gives the checklist and the failure
cases (`09` ch 3, 5).

**Worked example (faded: the learner supplies the nesting step).** *Decision: a growing online
community whose moderation is run entirely by platform staff faces rising complaints about
inconsistent bans.* (1) Checklist: 3 missing (members cannot change rules), 4 missing (monitors
unaccountable to users), 5 missing (bans are not graduated), 6 missing (no cheap dispute forum),
7 ambiguous (has the platform recognised members' right to govern any domain?). Scope flag: a
community's attention and civility are not a subtractable resource in Ostrom's sense, so 1 and 2
need reinterpretation (ledger C48). (2) Cheapest incremental change that produces information and
standing: a public moderation log (by-product monitoring) and a recognised member forum with
authority over one class of decisions. (3) Sanctions ladder as in m3's worked example, applied by
rotating members. (4) The learner designs the nesting: sub-communities handle local disputes; a
higher layer handles cross-community conflict and shared infrastructure. Tags: [E] for the
principles as diagnosis; [H] for transfer to a digital commons; [V] for member governance over
staff efficiency.

**Hinge questions.**

Q1. A funder says: "Ostrom showed communities manage shared resources better than states or
markets, so we should just hand the resource to the community." What is wrong?
- (a) Nothing; that is the book's thesis. *Diagnoses: Ostrom as anti-state and pro-panacea
  (ledger C47).*
- (b) Self-governance is a third option that works under identifiable conditions; durable cases
  lean on courts and enabling law as backstops, and Ostrom warned against panaceas. **Correct**
  (`09` ch 4, evidence section).
- (c) Communities fail because the PD is a law; only privatisation works. *Diagnoses: the PD as
  a law of nature (ledger C49).*
- (d) It works if the community adopts all eight principles. *Diagnoses: principles as a recipe
  to install (ledger rule 29).*

Q2. A team's first response to a missed on-call handover is a formal HR warning. Six months
later nobody reports handover problems. What happened?
- (a) The warning worked; problems stopped. *Diagnoses: silence as compliance; rules-in-form vs
  rules-in-use.*
- (b) A nuclear first sanction drove violations and reports underground and eroded the
  information flow monitoring depends on. **Correct** (`09` ch 3, principle 5).
- (c) The team lacks a norm psychology and needs stronger penalties. *Diagnoses: deterrence
  needs big penalties; the field pattern is small first sanctions.*
- (d) The warning was not credible; make it a firing. *Diagnoses: partly right, wrong level;
  credibility matters (`04` ch 8) but is achieved by making the sanction cheap to apply, not
  bigger.*

Q3. A reform (a new rota rule) stalls for a year although everyone agrees it is better. Where
does `09` say to look first?
- (a) At the operational rule; rewrite it more clearly. *Diagnoses: most fixes are operational;
  most failures are a level up.*
- (b) At the collective-choice level: do the people bound by the rota have a legitimate,
  low-cost way to change it, and does anyone outside recognise their right to? **Correct** (`09`
  ch 2, 6).
- (c) At the individuals blocking it. *Diagnoses: dispositional diagnosis.*
- (d) At the discount rate: people do not care about the future. *Diagnoses: partly right, wrong
  level; discount rates affect willingness to invest in rule change, but "everyone agrees" says
  the block is standing, not horizon.*

Q4. Which claim about Ostrom's principles may be tagged [E]?
- (a) They cause durability. *Diagnoses: causal reading of cases selected on the dependent
  variable.*
- (b) They transfer directly to open-source projects and knowledge commons. *Diagnoses: scope
  over-extension (ledger C48).*
- (c) Where a study assessed a principle, its presence was mostly associated with success and its
  absence with failure, across 91 studies, with publication-bias and coding caveats. **Correct**
  (Cox et al. 2010, verified).
- (d) Durable commons are egalitarian. *Diagnoses: durability as fairness (`09` misreadings).*

**Repair paths.** Wrong on Q1: `09` ch 1 and the misreadings list. Q2: `09` ch 3, the reasoning
behind principles 4 and 5. Q3: `09` ch 2 (three levels of rules) and ch 6. Q4: `09` evidence
section (Cox, Arnold and Villamayor-Tomás).

**Brief deliverable (s9, "institutional design").** Add: the eight-principle checklist run
against the group, each marked present, absent or not applicable with a scope note; the sanctions
ladder; the by-product monitoring channel; the dispute forum; which rule level the v0 fix lives
at and who has standing to change it; the recognised external backstop. Tag each. Prediction: the
first cheap change that will produce information and standing, and what it will reveal in three
months.

**Deeper pointers.** `09` ch 4 (the California basins as a sequence of games), ch 5 (failure
cases paired with missing principles), ch 6 (situational variables and discount rates); `04` ch 14
(crowd-out of unmeasured effort); ledger open question on transfer to large or digital commons.

### m9: Networks: ties, homophily, cascades, small worlds

**Draws on:** `10-networks-crowds-markets` (ch 3, 4, 19, 20 in depth; ch 16, 17 recalled from m7
and m4; evidence section; common misreadings); `07` Parts I and III; ledger X7, X15, rules 3,
19, 33, 34, 35.

**Learning objectives.** The learner can (a) distinguish the three kinds of copying (informational
cascade, network effect, coordination on a graph) and name the fix for each; (b) compute the
cascade threshold from payoffs and apply the cluster-density theorem to decide where to seed a
norm and why a single liaison will not carry it; (c) tell closure from bridging, run the
homophily test, assume selection over influence, and say what makes a group navigable.

**Load-bearing ideas.**
1. *Hold in memory.* On a graph where each edge is a coordination game, a node switches when at
   least a fraction q = b/(a+b) of its neighbours have (a and b the payoffs to matching on the new
   and old behaviour); a cluster of density greater than 1 − q outside the seed set blocks a
   complete cascade, and conversely. Clusters block a norm entering from outside and protect one
   adopted inside; seed inside dense clusters, lower q, build wide bridges. [E as a theorem;
   Centola 2010 background; ledger rule 3, 19]
2. *Hold in memory.* Simple contagion (information, awareness) crosses one weak tie; complex
   contagion (costly behaviour) needs several adopting neighbours. Weak ties tend to be the
   bridges (structural claim robust); "useful information comes from weak ties" and "six degrees"
   are not to be quoted as facts. [E for the structural claims; ledger rule 33, 34]
3. Closure gives trust and enforcement; bridges give information. Cooperation needs both; the
   right mix is [H]. Connectivity for skill retention (m1) and closure for enforcement are
   different variables. [E for the trade-off; ledger X15]
4. Homophily has two sources, selection and influence, and only longitudinal data separate them;
   fewer than 2pq cross-boundary edges indicates homophily; assume selection until shown
   otherwise. [E; ledger rule 35]
5. Short paths exist in any large network; findability is separate and needs ties at every scale
   (Kleinberg 2000, theorem); rich-get-richer attention is the default consequence of copying and
   not evidence of quality. [E as theorems; ledger C50, C53]

**Curiosity hook.** "A documentation norm is adopted enthusiastically by one sub-team and by the
one person who liaises with the other four sub-teams. A year later it lives in one sub-team. The
liaison was diligent. Why did it not cross?" (Complex contagion: the liaison is one of many
neighbours for each node on the other side; `10` ch 19.)

**Attempt (cold, before content).** "Five sub-teams of eight rarely interact; each has one
liaison to the others. A new review norm pays 3 to each pair that both use it and 2 to each pair
that both keep the old way (illustrative payoffs). Where do you seed it, how many seeds, and
through whom?" Predictable errors: the learner seeds through the liaisons (weak bridges cannot
carry a complex contagion), spreads a few seeds evenly across all teams (each below its cluster's
threshold), and does not compute the threshold (two fifths of a node's neighbours) or notice that
each sub-team is a cluster of density well above three fifths and will therefore block entry
from outside. The reading gives the threshold, the theorem and the seeding rule (`10` ch 19).

**Worked example (rubric only: the learner reasons it through).** *Decision: a distributed
organisation wants to reduce silos.* Rubric: (1) Which face of connectedness is the problem,
structure (few cross-ties) or behaviour (people do not act on what crosses)? (2) Is the goal
information flow (simple contagion; a few weak bridges suffice; protect the people who hold
them) or norm adoption (complex contagion; needs wide bridges or moving whole sub-teams)? (3)
Homophily check: are cross-edges below 2pq for the trait that matters, and is the similarity
selection (fixed at recruiting) or influence? (4) Navigability: does each person have a contact at
every scale (team, department, org)? (5) Which of the three copying kinds is producing the
observed convergence, and what is the matching fix (private signals first; cross the tipping
point; lower q or seed inside)? Required tags: [E] for the theorems and the structural weak-tie
claim; [H] for the group's q and cluster densities; [V] for how much closure to give up for
bridging.

**Hinge questions.**

Q1. Twelve engineers vote by show of hands; the two most senior vote first, both yes; ten follow.
Which kind of copying, and which fix?
- (a) Network effect; the vote is above its tipping point. *Diagnoses: confusing the three kinds
  of copying (ledger rule 19); no payoff externality here.*
- (b) Informational cascade; collect private judgments before anyone announces and reverse the
  speaking order. **Correct** (`10` ch 16).
- (c) Coordination on a graph; lower the threshold. *Diagnoses: applying the ch 19 fix to an
  informational problem.*
- (d) Conformity as weakness; tell people to be independent. *Diagnoses: rational herding as
  irrationality; the third person's copy is correct Bayesian play.*

Q2. A norm has been adopted by a dense sub-team of ten. Management worries the sub-team's
insularity will "hold the norm back" and proposes breaking it up across the org.
- (a) Right: clusters slow spread. *Diagnoses: "clusters are bad" (ledger X7).*
- (b) Wrong: the cluster's density protects the adopted norm; breaking it up returns each member
  to a neighbourhood below threshold. Keep the cluster and build wide bridges from it.
  **Correct** (`10` ch 19; `07` ch 3).
- (c) Right, provided the members are influential. *Diagnoses: influencer model of spread
  (ledger C30).*
- (d) Wrong: norms spread by information, so a newsletter is enough. *Diagnoses: weak ties carry
  behaviour because they carry information (ledger C54).*

Q3. The people who thrive in a community are strikingly similar. A member concludes the
community "shapes people into that type". What is the correct default?
- (a) Accept it; influence is visible. *Diagnoses: influence assumed over selection (ledger
  C52).*
- (b) Assume selection (who joined and stayed) until longitudinal data show similarity rising
  after joining. **Correct** (`10` ch 4; Crandall 2008 as the design that can separate them).
- (c) Reject it; communities cannot influence people. *Diagnoses: over-correction; both are
  real where measured.*
- (d) Accept it if the community is large. *Diagnoses: size as evidence of mechanism; irrelevant.*

Q4. Which is the robust version of the weak-ties claim?
- (a) Most useful information and most jobs come through weak ties. *Diagnoses: the job-search
  claim as robust (ledger C51).*
- (b) Weak ties tend to be the local bridges between clusters, so novelty enters through them;
  they are fragile and worth protecting. **Correct** (Onnela 2007; `10` ch 3).
- (c) Weak ties are more valuable than strong ties. *Diagnoses: "weak ties beat strong ties";
  closure supplies trust and enforcement (`10` misreadings).*
- (d) Everyone is six steps from everyone, via weak ties. *Diagnoses: six degrees as fact (ledger
  C50).*

**Repair paths.** Wrong on Q1: `10` ch 16 and the misreading on three kinds of copying. Q2: `10`
ch 19 (cluster theorem, both directions) and `07` ch 3. Q3: `10` ch 4 (selection vs influence).
Q4: `10` ch 3 and evidence section.

**Brief deliverable (s10, "network map and seeding plan").** Add: a sketch of the group's
clusters and bridges (who holds them, how many parallel ties between sub-groups); the homophily
estimate for the trait that matters and whether selection or influence is assumed; for the target
norm, the estimated q and the cluster(s) that will block it; the seed set and where it sits;
which of the three copying kinds is currently producing the group's convergence and the matching
fix. Tag each. Prediction: which sub-group adopts first and which never adopts through the current
bridges.

**Deeper pointers.** `10` ch 5 (structural balance and two-faction splits), ch 12 (bargaining
power from outside options), ch 20 (navigable small worlds; the rank-based empirical check),
ch 21 (simple contagion contrast); `07` ch 6 (partner choice generates structure without payoff
differences).

### m10: The four accounts reconciled and Gintis assessed

**Draws on:** `11-bounds-of-reason` (ch 1, 3, 4, 7, 8, 10, 11, 12; evidence section; critical
assessment; common misreadings); ledger X5, X4, X16, rules 1, 4, 31, 32; `04` ch 4, `07` ch 1,
`08` ch 1 for the four accounts.

**Learning objectives.** The learner can (a) state the four layers of "how a group settles on a
way of behaving" (Nash/ESS as stability test; Skyrms and Camerer for which stable state is
reached absent intervention; Gintis for the public signal that aligns conjectures; Bicchieri for
what must be true inside agents and how to measure it) and refuse to present any one as "the"
theory; (b) run Gintis's two-part norm test (epistemic: can everyone say what the norm requires
of them and others; motivational: does anyone gain by deviating given others comply, and is
there a cheap sanction) and the BPC bookkeeping (beliefs, preferences, constraints); (c) assess
each of Gintis's eight claims against the rest of the list, carrying out the two that hold and
declining the unification.

**Load-bearing ideas.**
1. *Hold in memory.* Nash equilibrium is a social achievement, not a rational deduction:
   rationality plus common knowledge of rationality yields only rationalizability; Nash needs
   aligned conjectures that come from outside the players' heads (Aumann and Brandenburger 1995,
   theorem). Stop trying to reason a group into equilibrium; name the signal. [E; `11` claim 1
   holds up]
2. *Hold in memory.* A norm is a choreographer: a public signal that tells each person what to
   do and what others will do, such that following it is a best response when others follow it
   (correlated equilibrium). The model is weaker than Bicchieri on diagnosis, Ostrom on
   authorship and Skyrms on origins, and does not fit data better than Nash by any horse race.
   [E as a model; ledger rule 31, C58]
3. Four layers, not four rivals: stability test (04, 07), selection absent intervention (07, 06),
   the signal (11), the expectations inside agents (08). Which layer bites in a given group is [H].
   [ledger rule 1]
4. Strong reciprocity as an evolved trait is [H]; the lab willingness to punish is [E]; the
   design lesson is a cheap, legitimate, proportionate channel for sanctioning. BPC is bookkeeping,
   not an explanation of construal effects, and the falsifiability worry is real. [ledger rule 4,
   X16]
5. "Common priors are culture": persistent disagreement across sub-groups on shared data
   indicates different priors; align by shared definitions, training and narrative, not more
   dashboards. [E for the direction, supported by `01` and `02`; H for the intervention]

**Curiosity hook.** "A traffic light tells each driver something different and nobody would
gain by disobeying, given the others obey. A rule book tells everyone the same thing and is
ignored. What does the light have that the book lacks, and what is your group's light?" (A
correlating signal plus a reason to comply given others comply; `11` ch 2, 10.)

**Attempt (cold, before content).** "Two product squads look at identical weekly metrics and
reach opposite conclusions every week; a release cadence is half-assumed weekly and
half-assumed fortnightly and merges collide. Diagnose both in one paragraph each and say what
you would change." Predictable errors: the learner prescribes more data for the first (the
problem is priors, not information) and incentives for the second (the problem is the missing
epistemic half of a norm: no public signal). The reading gives ch 7 and ch 10.

**Worked example (rubric only).** *Decision: the learner's own v0 fix, re-run through the four
layers.* (1) Stability: is the proposed pattern an equilibrium at all (would anyone gain by
deviating alone)? (2) Selection: absent the fix, which stable state does the group's regime
(mixing, learning rule, size, talk) deliver, and does the fix change the regime or only the
payoffs? (3) Signal: what public cue tells each member which equilibrium is in play, and is it
visible across the whole network (`10`)? (4) Expectations: which empirical and normative
expectations must be live, and how will they be measured? Then the Gintis two-part test and the
BPC line for the group. Required tags: [E] for the formal relations; [H] for which layer bites;
[V] for any claim about which equilibrium ought to be chosen.

**Hinge questions.**

Q1. A contribution norm is posted on a visible board; everyone can state it; compliance is still
low. Which half has failed and which reading repairs it?
- (a) The epistemic half; make the board more visible. *Diagnoses: all norm failures as
  information failures.*
- (b) The motivational half: some members gain by deviating and no sanction bites; repair with
  Ostrom's graduated sanctions and Bicchieri's normative expectations. **Correct** (`11` ch 10;
  retrieval Q10).
- (c) Neither; people are irrational. *Diagnoses: "Gintis shows people are irrational" (`11`
  misreadings).*
- (d) The evolved norm psychology is absent in this group. *Diagnoses: strong reciprocity as a
  settled trait that should have carried compliance (ledger rule 4).*

Q2. Which statement about the four accounts is the course's position?
- (a) Bicchieri's is the correct theory of norms; the others are approximations. *Diagnoses: one
  account as "the" theory (ledger rule 1).*
- (b) They are layered: stability test, selection absent intervention, the aligning signal, the
  expectations inside agents; which layer bites in a group is a hypothesis. **Correct** (ledger
  X5).
- (c) Gintis unified them. *Diagnoses: "the unification" (ledger C55).*
- (d) Skyrms's dynamics make the others redundant. *Diagnoses: dynamics without beliefs as the
  whole story; Skyrms's agents have no expectations to measure (ledger C41).*

Q3. What is the durable contribution of `11` for the brief?
- (a) That correlated equilibrium fits data better than Nash. *Diagnoses: empirical superiority
  claim the book never tests (ledger C58).*
- (b) That the behavioural sciences now share one theory. *Diagnoses: programmatic unification
  read as achieved (ledger rule 31).*
- (c) The epistemic critique of Nash and the choreographer idea, which turn every Order-level
  book into one question: what is the signal, and why does each person comply given the others
  do? **Correct** (`11` net assessment).
- (d) That Binmore's review discredited the book. *Diagnoses: an attributed review that was not
  found (ledger C56).*

Q4. Ambiguous ownership of a shared codebase produces recurring fights. Which reading of `11`
ch 11 is right?
- (a) Assign the fairest owner and fights will fall most. *Diagnoses: fairness as the mechanism;
  the cue works by being salient, not fair.*
- (b) Assign a clear owner, even somewhat arbitrarily, because an ambiguous ownership cue leaves
  a hawk-dove game without a correlating signal; fairness matters for legitimacy and sanctioning,
  which Ostrom and Bicchieri supply. **Correct** (ledger rule 32).
- (c) Ownership fights are innate territoriality; only a manager's dominance stops them.
  *Diagnoses: endowment effect as evolved property psychology treated as [E] (ledger C57), plus
  dominance over prestige (`01`).*
- (d) Ownership is a rule system, so write a rule. *Diagnoses: partly right, wrong level; a rule
  nobody monitors is not a signal (`09` rules-in-use).*

**Repair paths.** Wrong on Q1: `11` ch 10 (two components) and retrieval Q10. Q2: ledger X5 and
`11` claim 2 assessment. Q3: `11` critical assessment, claims 1, 2, 8. Q4: `11` ch 11 and
claim 7.

**Brief deliverable (s11, "the signal and the BPC statement").** Add: the public signal for each
of the group's central coordination problems and whether it is visible across the network; the
two-part test result for the group's main norm; one BPC line (what members believe about each
other, what they value including status and fairness, what constrains them); which of the four
layers the v0 fix addressed and which it ignored. Tag each. Prediction: which layer, if addressed
alone, moves behaviour, and which does nothing without the others.

**Deeper pointers.** `11` ch 4-5 (rationalizability; backward induction's contradiction), ch 6
(mixing as population conjecture), ch 9 (refinements failed), ch 12 (five principles as a checklist
of layers a diagnosis has left out); ledger X16 and the open question on falsifiability.

### m11: Integration: tensions, decision rules, the diagnostic path

**Draws on:** all eleven files; ledger sections 1, 5 and 6; seeds 4a and 4b below (the dedicated
`unified-model.md` and `tensions.md` are authoritative once written).

**Learning objectives.** The learner can (a) walk the diagnostic path from a real failure to a
fix set (collective brain and models; situation and construal; game shape; curve shape and
threshold; type mix and amendment; regime and correlation; norm classification and
expectations; institutional checklist; network seeding; signal and layers); (b) state each major
tension as a conditional decision rule with the condition tagged [H]; (c) re-tag Brief v0 with a
changelog and identify the single most important missing decision.

**Load-bearing ideas.**
1. *Hold in memory.* Diagnose before prescribing, in order: is it arithmetic; is it the situation;
   what is the game shape; is behaviour contingent and where is the threshold; which amendment;
   what regime; what kind of norm; which principles are missing; where in the network; what is
   the signal. Most v0 fixes skip to a lever without a diagnosis. [V that this order is the
   course's; E for each step's source]
2. *Hold in memory.* The tensions are conditional, not contradictions: each resolves into an
   "if the group is like X, do A; if like Y, do B" rule whose condition is a hypothesis to test in
   the group. [ledger section 1]
3. Certainty drops as one climbs the model: formal results are theorems; lab mechanisms are [E]
   for direction; institutional and network prescriptions are [H] for any group; the choice of
   which equilibrium ought to hold is [V]. [ledger rule 27, 40]

**Curiosity hook.** "Five experts diagnose the same failing community: one says its learning
network is broken, one says the game is a PD, one says it is below critical mass, one says the
norm lacks normative expectations, one says the seed sat outside the cluster. All five are
right. In what order do you act?" (The diagnostic path; the answer depends on which layer bites,
which is the module's target.)

**Attempt (cold, before content).** "Take the five disagreements below and, for each, write the
condition under which each side is right: (i) sweeten the joint payoff vs cut the lone-cooperator
cost; (ii) mix people more vs keep stable clusters; (iii) explain vs model; (iv) publish the
descriptive norm vs never advertise prevalence; (v) install institutions vs let structure do the
work." Predictable errors: the learner picks a side for each rather than writing a condition,
and states the condition as a fact about groups in general rather than a hypothesis about theirs.

**Worked example (rubric only).** *Decision: the learner's group, walked through the ten-step
path in one page, ending in a ranked fix set with one prediction per fix and a tag per claim.*
Rubric: every step names its source; no step's fix is proposed before its diagnosis; at least one
step concludes "not the binding constraint here"; the fix set has no item that appears on the
failed-replication list; every [E] is a ledger [E].

**Hinge questions.**

Q1. A learner's brief tags "our team is a stag hunt" as [E]. Correct?
- (a) Yes; the stag hunt is a theorem. *Diagnoses: tagging the formal distinction's status onto
  the group's classification (ledger rule 13: E for the distinction, H for the classification).*
- (b) No; it is [H] until the defection question has been answered with the group's own
  payoffs, and even then remains a hypothesis. **Correct**.
- (c) No; it should be [V]. *Diagnoses: confusing an empirical hypothesis with a value
  commitment.*
- (d) Yes, if the team says so. *Diagnoses: self-report of payoffs as evidence; construal and
  naive realism (`03`).*

Q2. Which is a correctly stated tension rule?
- (a) "Always keep stable clusters." *Diagnoses: a side, not a condition.*
- (b) "Keep stable clusters while a norm is young if members copy success; if they copy the
  majority, clusters will not spread it and you need success-visibility first." **Correct**
  (ledger X7).
- (c) "Mixing spreads information and norms alike." *Diagnoses: simple and complex contagion
  collapsed (ledger rule 34).*
- (d) "Clusters help because Centola proved it." *Diagnoses: one background study as a
  theorem; the condition is missing.*

Q3. A brief's single most important missing decision is most often:
- (a) The incentive scheme. *Diagnoses: incentives as the default lever.*
- (b) Who has standing to change the rules, and what the public signal is. **Correct**: the
  collective-choice level (`09`) and the epistemic half of the norm (`11`) are the two decisions
  learners skip most, per the worked examples in m8 and m10.
- (c) The values statement. *Diagnoses: norms as values (ledger C43).*
- (d) The team-building event. *Diagnoses: proximity as contact (`03` ch 10).*

**Repair paths.** Wrong on Q1: `SPEC.md` tag definitions and ledger rule 13, 27. Q2: ledger X7
and `07` ch 3. Q3: `09` ch 2 and `11` ch 10.

**Brief deliverable (s12-s14 and the changelog).** Re-tag Brief v0 line by line against the
current version with a changelog of every tag that changed and why; fill the open-hypotheses
register (s12) with every [H] and its test; fill the value-commitments register (s13); write the
measurement plan and ninety-day predictions (s14). This is Brief v5, the capstone's input.

**Deeper pointers.** Ledger section 6 (open questions the sources cannot settle); each book file's
Connections section; `11` critical assessment as a model for how to assess one's own brief.

---
## 4. Cross-cutting artifacts (pointers and seeds)

The dedicated synthesis files are authoritative; this section seeds them and fixes the ids they
must keep.

### 4a. Unified model sketch (seeds `unified-model.md`)

A building, read bottom-up, with certainty falling as one climbs:

- **Foundation, Origins (m1):** cultural learners in a collective brain; copying rules
  (success, prestige, conformity, self-similarity, CREDs; copy-when-uncertain, discount stale);
  content-neutral norm psychology; fidelity threshold. Certainty: mechanisms [E], weights [H],
  deep-time story [H].
- **Band 2, Mechanisms (m2-m5):** situation and construal over disposition; the game shapes and
  the defection question; contingent behaviour, thresholds, tipping, sorting; the three
  amendments and the distribution of types. Certainty: theorems and replicated lab mechanisms
  [E]; any group's classification [H].
- **Band 3, Order (m6-m9):** regime and correlation (risk dominance vs payoff dominance); norms
  as conditional preferences with two expectations; institutions as the eight structural
  conditions with cheap graduated sanctions; networks as thresholds and clusters with three kinds
  of copying. Certainty: models and reviews [E]; prescriptions for a group [H]; which equilibrium
  ought to hold [V].
- **Roof, Synthesis (m10):** four layers of "how a group settles" (stability, selection, signal,
  expectations); Gintis's two durable ideas; the unification declined.
- **Arrows between bands:** Origins supplies the learning rule that decides whether structure
  helps (m1 to m6, m9); Mechanisms supplies the type mix that decides whether talk decays (m5 to
  m7); Order's expectations supply what Skyrms's dynamics leave out (m7 to m6); networks decide
  whether a signal is seen (m9 to m10).

### 4b. Tensions seed list (seeds `tensions.md`; that file's order is canonical)

Each becomes a conditional decision rule with the condition tagged [H]. Proposed ids follow the
ledger's proposal.

- t01 Evolved copying biases vs ecological copying strategies; copying vs teaching (X1, X13):
  spread adherence by models and expectations; transfer hidden-structure skill by teaching.
- t02 Strong reciprocity as evolved trait vs cheap graduated sanctioning (X4): design on the
  cheap version.
- t03 Four accounts of how a group settles (X5): layered, not rival.
- t04 Risk vs payoff dominance; clusters block vs help (X6, X7): regime and learning rule decide.
- t05 Stable social preferences vs cued norm compliance; internalised vs conditional (X8, X9):
  assume conditional until it survives a collapse of expectations.
- t06 Designed vs copied-and-evolved institutions (X10): copy a successful peer's package, then
  craft incrementally with those bound by it.
- t07 PD vs stag hunt; does cheap talk work (X11, X12): classify first; talk decays where
  defection dominates.
- t08 Cultural group selection and culture-drove-brains (X2, X3): [H], never load-bearing.
- t09 Connectivity vs closure (X15): connectivity for information and retention; closure for
  enforcement and complex contagion.
- t10 Descriptive-norm messaging (X14): always pair with injunctive; never advertise prevalence.
- t11 Anomalies as preferences vs unstable beliefs (X16): BPC as bookkeeping only.
- t12 Incentives vs norms (crowd-out; `03` ch 7, `04` ch 14, `11`): prefer the norm where the
  disposition exists; expect explicit incentives to displace it when large.
- t13 Change expectations vs change structure (`08` vs `10` and `07`): expectations where the
  group is one reference network; structure where clusters and bridges decide who sees the
  signal.

### 4c. Cooperation brief template skeleton (seeds `design-brief-template.md`)

```
# <Group> — Cooperation brief v<N>
s1  The group and its boundary: who is in, what is shared, subtractable or not   [E/H]
s2  Diagnosis: the games being played (matrix, defection question, shape, fix set)  [H]
s3  The collective brain: who learns from whom; models; single points of failure  [H]
s4  Situational audit and folk-psychology check (struck-through failed levers)     [E/H]
s5  Threshold and tipping map; minimum viable coalition; arithmetic constraints    [H]
s6  Population of types and fairness baseline; weak-link processes                  [H]
s7  Equilibrium selection plan: regime, correlation device, pacing, lone-cooperator cost [H]
s8  Norm register: taxonomy, expectation measurement, cues, trendsetters            [E for method, H for results]
s9  Institutional design: eight-principle checklist, sanctions ladder, monitoring, forum, standing, backstop [H/V]
s10 Network map and seeding plan: clusters, bridges, q, seed set, copying kind      [H]
s11 The signal and the BPC statement; the four layers addressed                     [H]
s12 Open hypotheses register (every [H] with its test and date)                      [H]
s13 Value commitments register                                                       [V]
s14 Measurement plan and ninety-day predictions                                      [H]
```

### 4d. Casebook seed list (seeds `casebook.md`; 24 one-liners, each with tension and slug)

- k01 The deployment expert leaves in three months; runbook unused. (t01; `01` ch 12, `02` ch 8)
- k02 "Quality first" announced; broken feature shipped to hit a date. (t01; `01` ch 4)
- k03 The best-practices wiki nobody updates. (t01; `02` ch 3)
- k04 Twelve-person team, two "coasters", output per head down. (t11; `03` ch 5, 12)
- k05 The rule-breaking banner that made rule-breaking worse. (t10; `03` ch 9)
- k06 Homogeneous hiring committee proposes implicit-bias training. (t11; `03` ch 10, 12)
- k07 Forty people saw the alarming post; nobody acted. (t11; `03` ch 14)
- k08 Volunteer event needs eight; call attendance falling. (t07; `04` ch 4, 11)
- k09 Code-of-conduct violation: ban or note? (t02; `04` ch 8, `09` ch 3)
- k10 Founder says years of repeat play guarantee cooperation. (t07; `04` ch 10)
- k11 Weekly cross-team demo dies from twelve to three. (t04; `05` ch 1, 3)
- k12 Architecture decision records stuck at a low share for a year. (t04; `05` ch 7)
- k13 Seniors cluster on one team without anyone deciding it. (t09; `05` ch 4, 5)
- k14 Unequal contributor rewards, complaints and exits every round. (t05; `06` ch 2)
- k15 Sixteen sign-offs and one late reviewer. (t04; `06` ch 7)
- k16 Quarterly team rotation to "spread the culture". (t04, t09; `07` ch 6-7)
- k17 Pledge round before a resource split in a group where skipping pays. (t07; `07` ch 5,
  `08` ch 4)
- k18 Weekend messages nobody likes and everybody sends. (t05; `08` ch 5)
- k19 CI cluster quotas with automatic lockout. (t06; `09` ch 3, 5)
- k20 Staff-only moderation and inconsistent bans. (t06; `09` ch 5)
- k21 Documentation norm that never crossed the liaison. (t09; `10` ch 19)
- k22 Show-of-hands vote after the two most senior say yes. (t13; `10` ch 16)
- k23 Two squads, same metrics, opposite conclusions weekly. (t03; `11` ch 7)
- k24 Ambiguous ownership of a shared codebase. (t03; `11` ch 11, `09`)

### 4e. Deck plan (seeds `flashcards.md`; ids c001..)

About fifteen atomic cards per module (roughly 165 plus 20 integration and evidence-strength
cards): per module, 4 definition cards (glossary terms in the ledger's wording), 3 mechanism
cards ("why does X happen"), 3 number-with-hedge cards (only ledger section 4 rows, status
included), 3 misconception cards (front: the folk claim; back: the correction and its ledger
row), 2 apply cards (a one-line scenario; back: shape or lever). Cards for module N enter the
deck the day after N completes; the first review is next day, then at 3, 7 and 14 days. The
integration cards cover the four layers, the tension rules and the tag definitions.

### 4f. Capstone outline (seeds `capstone.md`)

Three sittings over days 22-24. (1) Brief v6, 90 minutes: every section s1-s14 filled; every claim
tagged; no [E] that is not a ledger [E]; the diagnostic path visible. (2) Defence, 45 minutes:
the learner answers the `course.json` critique prompt against their own brief in writing, then
answers three casebook cases chosen to attack the brief's weakest tension. (3) First ninety days,
45 minutes: the first cheap change that produces information and standing; the measurement
plan; three predictions with dates; what would make the learner abandon the main hypothesis.
Scoring penalises mis-tags most heavily, then fixes proposed before diagnosis, then any reliance
on the failed-replication list.

---

## 5. Spaced schedule (21 days)

Retrieval days (R) never introduce content: deck reviews at 1, 3, 7 and 14 days, one to three
casebook cases, one free-recall task, and periodic re-tag checkpoints. Split modules put hook,
attempt and reading map on day one and worked example, hinges and deliverable on day two.

| Day | Session | Content | Min |
|-----|---------|---------|-----|
| 1 | m0 | Diagnostic d1-d16 with confidence (20) + cold challenge (40). Brief v0. Tag v0. | 60 |
| 2 | m1a | Hook (lost explorers), attempt (handover), reading map for `01`, `02`. | 50 |
| 3 | m1b | Worked example (flagging), hinges, brief diff s3. Deck: m1 cards introduced. | 50 |
| 4 | m2 | Full module (situations, replication rules). Deck: m2 cards. | 70 |
| 5 | R1 | Deck: m1 (day-1 and day-3 reviews), m2. Cases k01, k05. Free recall: redo the handover attempt from memory and compare with day 2. | 40 |
| 6 | m3a | Hook (two teams, no first mover), attempt (volunteer event), reading map for `04`. | 50 |
| 7 | m3b | Worked example (ban or note), hinges, brief diff s2. Deck: m3 cards. | 50 |
| 8 | R2 | Deck: m1 (day-7), m2, m3 interleaved. Cases k04, k08. Free recall: write the six classification questions and the five shapes with fix sets. | 45 |
| 9 | m4 | Full module (thresholds, tipping, sorting). Deck: m4 cards. | 70 |
| 10 | m5 | Full module (social preferences, coordination, learning). Deck: m5 cards. | 70 |
| 11 | R3 | Deck: m2 (day-7), m3, m4, m5. Cases k11, k14. Brief v2 checkpoint: re-tag s2-s6. | 45 |
| 12 | m6a | Hook, attempt (sixty stag hunters), reading map for `07`, re-read `06` ch 7. | 50 |
| 13 | m6b | Worked example (blameless post-mortems rollout), hinges, brief diff s7. Deck: m6 cards. | 50 |
| 14 | R4 | Deck: m1 (day-14), m3 (day-7), m4, m5, m6. Cases k15, k16. Free recall: draw the two-curve diagram and the stag-hunt watershed from memory. | 45 |
| 15 | m7 | Full module (norms). Deck: m7 cards. | 70 |
| 16 | m8 | Full module (institutions). Deck: m8 cards. | 70 |
| 17 | R5 | Deck: m4 (day-7), m5, m6, m7, m8. Cases k18, k19, k09. Free recall: the four-way norm taxonomy and the eight principles with Cox's splits. | 45 |
| 18 | m9 | Full module (networks). Deck: m9 cards. | 70 |
| 19 | m10 | Full module (four accounts, Gintis). Deck: m10 cards. | 70 |
| 20 | m11 | Integration: attempt (five disagreements), tensions, ten-step path, hinges, re-tag Brief v0 with changelog; Brief v5. Deck: integration cards. | 75 |
| 21 | R6 + prep | Deck: m6-m10 (day-7 and day-14 reviews), evidence-strength cards. Retake d1-d16; report accuracy and calibration delta; rewrite the baseline free response. Pick three capstone defence cases. | 55 |
| 22-24 | Capstone | Brief v6 (90), defence (45), first ninety days (45), three sittings. | 180 |

Scheduled total: 925 minutes of modules and 275 of retrieval, about 20 hours; with the capstone
about 23 hours. A learner who takes 40 minutes on every retrieval day and 2 hours on the
capstone lands near 17 hours. Cards for module N always enter the day after N completes; every
retrieval session pulls from at least three modules. Post-course: the deck goes to the learner's
own spaced-repetition system at one- to three-month spacing; the casebook cases not used during
the course (about ten) are answered one per week in 200 words against the brief.

---

## 6. Gaps: what the reading list omits that the goal needs

Seeds only; `gaps-primer.md` is written separately and is authoritative. Each area is labelled
and carries a one- to three-hour recommendation. None of these is in the sources.

1. **Measuring expectations in a real group — Critical.** `08` gives the definition and one
   validated two-step method with design-sensitivity caveats; it does not give a survey
   instrument, sampling advice or a way to map reference networks in a team or platform. About two
   hours: draft, pilot on five people, revise. This is not in the sources.
2. **Sanctioning in practice — Critical.** The list says sanctions should be cheap, graduated,
   participant-run and legitimate (`09`, `04`, `11`) and warns of antisocial punishment (`01`);
   it does not say how to run a restorative or graduated process in an organisation or online
   community, or how to prevent capture. About two hours. Not in the sources.
3. **Legitimacy, procedural justice and leadership — Critical.** Ostrom's cases and the
   Milgram design lesson (exits, peers, legitimacy of refusal) point at legitimacy; no source
   treats how a rule or sanction comes to be seen as legitimate, or the role of leaders beyond
   "communicate publicly" (`06`). About two hours. Not in the sources.
4. **Trust, reputation and identity systems — Critical for platforms, Important otherwise.**
   `04` ch 9 and `06` ch 8 give signalling and reputation in the abstract; nothing on designing
   reputation scores, identity verification, or their gaming. About two hours. Not in the sources.
5. **Mechanism design in practice — Important.** `04` ch 14-16 give the theory; nothing on
   implementing points, quotas or voting in a real organisation, or on the evidence for crowd-out
   at scale. About one to two hours. Not in the sources.
6. **Online governance, moderation and polarization — Important; Critical if the group is a
   community or platform.** `03` (SIDE model, polarization) and `09` (staff-run moderation as
   Kirindi Oya) gesture at it; no source treats scale, anonymity, recommendation systems or
   federated governance. About two hours. Not in the sources.
7. **Team-level practice: psychological safety and size — Important; Critical if the group is a
   team.** `03` gives a working-unit rule of thumb of 2-5 people tagged [H] and the wise-feedback
   pattern; the team-effectiveness literature is absent. About one hour. Not in the sources.
8. **Scaling and polycentric design beyond small commons — Important.** `09` ch 3 principle 8
   and `10` nesting are the only treatment; transfer to large, digital or knowledge commons is
   an open question in the ledger. About one to two hours. Not in the sources.

Useful but lower priority, also absent: the evolution-of-cooperation classics the list assumes
(kin selection, indirect reciprocity, Axelrod in the original), and the ethics of engineering
norms and consent (value-heavy).

---

## Reconciliation log

Every factual claim in the modules and hinge questions was checked against the relevant book
file's evidence section and the ledger's rules. Book files and the ledger won every disagreement.
Changes made to the first draft:

- **m5 idea 2 and d2.** Draft stated "half of offers below 20% are rejected" as a verified
  figure. Ledger row 4.2 marks it background and approximate. Now quoted as "about half,
  background", with the verified mean-offer row (about 40%, Oosterbeek 2004) carrying the weight.
- **m7 hook and d6.** Draft quoted Dawes 1977 as "30% to 70%". Ledger C46 and rule 12: quote as
  "roughly doubled" or "from about a third to about seven in ten, background". Rewritten in both
  places.
- **m6 hook and Q1.** Draft's hook said the efficient equilibrium is "the rational choice teams
  fail to make". `07` common misreadings and ledger rule 2 forbid "the efficient equilibrium is the
  rational one". Hook and Q1 rewritten around basin size and defensible safe choice.
- **m9 idea 1 and Q2.** Draft said dense clusters "block cascades" without the second direction.
  Ledger rule 3 and `10` misreadings require both: block from outside, protect inside. Added,
  and the Centola 2010 figure marked background.
- **m2 Q3.** Draft included "watching eyes on the honour box" as a cheap monitoring lever in the
  worked example. `03` evidence section and ledger C18: mostly failed replications. Moved to a
  distractor with diagnosis; identifiability retained as the lever.
- **m5 idea 2 and m10 idea 4.** Draft described strong reciprocity as "the evolved disposition
  behind costly punishment". Ledger X4 and rule 4 split the claim: lab willingness [E], evolved
  trait [H], real sanctioning cheap. Rewritten in m5, m8 and m10; d3 built from the correction.
- **m3 idea 3 and Q2.** Draft recommended tit-for-tat "with forgiveness". Ledger C26, rule 15:
  recommend the properties, never the rule. Rewritten; Q2 option (c) diagnoses the draft's error.
- **m3 Q2 option (d).** Draft treated "discount factor above one half" as a general threshold.
  `04` ch 10 shows it is the illustrative payoffs' threshold (rises with temptation). Now a
  distractor that diagnoses over-generalising the example.
- **m4 idea 4 and d4.** Draft summarised Schelling as "segregation arises from mild preferences".
  Ledger rule 17 prescribes exact wording (shows vs does not show; empirical 5-20% tipping; fragility
  disputed). Adopted verbatim in spirit; Q1 distractors (c) and (d) diagnose both over-readings.
- **m1 idea 4 and Q1.** Draft cited "Tasmania lost its technology when isolated" as the example
  of the collective brain. Ledger rule 6, C1: contested; say "connectivity of the learning
  network, lab-demonstrated, archaeologically contested". Rewritten; Q1 option (c) diagnoses the
  population-size reading.
- **m1 idea 5 and Q3.** Draft's worked example leaned on cultural group selection ("copy the
  winning group's norms because selection made them adaptive"). Ledger rule 5: [H], never sole
  basis. Rewritten as copy-and-modify with the CGS reading moved to a distractor.
- **m2 idea 2.** Draft cited Allcott's 2% as verified. Ledger row 4.20 marks it background.
  Now "about 2%, background".
- **m2 worked example and gaps 7.** Draft tagged "working units of 2-5" as [E]. Ledger row 4.26:
  a rule of thumb, tag [H]. Corrected in the gaps section; removed from the worked example.
- **m5 idea 1.** Draft quoted "two-thirds game guesses of 20-35" from `04`. Ledger prefers the
  verified Nagel figure (about 35-36) and τ about 1.5; the `04` range (background) dropped.
- **m8 hook.** Draft said the Törbel rule "has been enforced since 1517". `09` gives the 1517
  rule as background via Netting; the hook now says "dated 1517" and marks the date background.
- **m9 idea 2 and Q4.** Draft stated "most jobs come through weak ties (Granovetter)". Ledger
  C51, rule 33: quote the structural claim only. Rewritten; Q4 (a) diagnoses the draft's claim.
- **m9 idea 5.** Draft opened with "six degrees of separation". Ledger C50: "short paths exist;
  the number is unreliable". Rewritten; Q4 (d) diagnoses it.
- **m10 Q3 option (d).** Draft's distractor said "Binmore's review panned the book". `11`
  evidence section and ledger C56: no Binmore review found. The distractor now diagnoses the
  attribution itself.
- **m10 idea 2.** Draft said correlated equilibrium "fits the coordination data better than
  Nash". Ledger C58: conceptual argument, no horse race. Removed; Q3 (a) diagnoses it.
- **m7 idea 5.** Draft called norm activation "priming by cues". Ledger rule 37 and C12: do not
  equate with behavioural priming. Rewritten as scripts with the caveat; m7 Q4 (d) diagnoses it.
- **m2 Q2 option (c).** Draft's correct answer said "situations determine behaviour". Ledger
  C23 forbids the phrase; the option now says situations are underestimated with moderate effect
  sizes, and (c) diagnoses the strong claim.
- **m8 idea 3.** Draft listed the eight principles in Ostrom's 1990 wording. `09` evidence
  section says the Cox et al. 2010 split version is now standard; list rewritten with the splits.
- **Module order (architecture rationale).** The proposed spine put `10` ch 17 and 19 wholly in
  m9. `05` and `10` glossary say Schelling's tipping point and `10`'s z' are one object; the
  population-model half of ch 17 and the threshold notion of ch 19 moved to m4, the graph version
  stays in m9. Departure recorded.
- **Illustrative numbers.** Draft used invented payoffs in several attempts. Replaced with the
  ledger's illustrative rows (stag-hunt 4/0/3 with watershed three quarters; PD 3/5/0/1 with
  sensitivity two thirds; q = b/(a+b); 2pq) or the book files' own worked examples, and labelled
  "illustrative" wherever a number is not an evidence claim (m2 attempt's one-third drop, m4
  attempt's fifteen percent, m7 hook's shares are scenario numbers and say so).

Checked, no change needed:

- Herrmann et al. 2007 as the children-vs-chimpanzee social-learning result (`01` ch 2, robust).
- Morgan et al. 2015: N = 184, five conditions, teaching and language best (`02` ch 8, verified,
  one study); tagged [E] modest throughout.
- Rendell et al. 2010: 104 entries, a simulation, winner discounted stale information (`02` ch 3,
  verified); always paired with Rogers's paradox per rule 39.
- Hagger et al. 2016 ego-depletion figures; Ranehill 2015; Flore and Wicherts 2015; Burger 2009
  (`03` evidence section, verified).
- Bond and Smith 1996 (133 studies, 17 countries; verified).
- Van Huyck 1990 group-size collapse (verified) with round counts marked background.
- Camerer et al. 2016: 61% of 18, effects about two-thirds (verified).
- Engel 2011 dictator figures (verified) with the double-blind and take-option caveats.
- Henrich 2001 small-scale range 26-58% (verified) with causality unresolved (C59).
- Weber 2006 gradual growth (verified, single lab) tagged [E] with the "test in your setting"
  caveat (C60).
- Card, Mas and Rothstein 2008 tipping at 5-20% (verified).
- Cox, Arnold and Villamayor-Tomás 2010, 91 studies (verified), with publication-bias caveat.
- Bicchieri and Xiao 2009 direction (verified).
- The cluster-density theorem, q = b/(a+b), the 2pq test and Kleinberg's navigability exponent
  as theorems (`10`).
- Aumann and Brandenburger 1995 as the theorem behind `11` claim 1.
- Ellison 1993, Kandori-Mailath-Rob and Young as the best-response and noise qualifications to
  Skyrms (`07` evidence section).

Still open (the sources cannot settle these; the modules say so where they arise):

- Whether cultural group selection is a major engine or a redescription of within-group
  mechanisms (m1; ledger section 6).
- Whether norm-following is internalised or conditional-but-looks-internalised (m7; X9); the
  course uses the collapse-of-expectations test as an operational rule.
- Whether costly one-shot punishment is an evolved trait or repeated-play heuristics, and how
  much real sanctioning is costly (m5, m8, m10; X4).
- Whether payoff dominance is stable in the long run under noisy best response or only reachable
  transiently under imitation (m6; ledger section 6).
- Whether Ostrom's principles transfer to large or digital commons (m8; C48).
- Whether influence can be separated from selection for behaviours that matter to the learner's
  group without longitudinal data (m9; C52).
- Whether descriptive and normative expectations can be disentangled in the field (m7; ledger
  section 6).
- Whether the learning-science defaults behind principles 2 and 5 (worked-example fading,
  spacing intervals) hold for this content; they are not in the sources and are marked as such.

### QA fixes (cold-learner run)

Source: `synthesis/qa-cold-learner.md` (§4.1, §4.4, §7). All edits are in `app/data/`; nothing in `books/` or the ledger changed.

- All 48 hinges (m0-m11) → four options rewritten to the same register and within 25% of each other's length (each distractor now carries a mechanism/"because"/"since" clause; correct options tightened, never weakened); option order permuted with diagnoses attached; `answer` updated. Longest-is-correct fell from 47/49 to 3/48; correct index now 12/12/12/12 across 0-3 (per module: m0 [3,0,2,1], m1 [2,0,3,1], m2 [3,2,0,1], m3 [2,0,3,1,0], m4 [3,0,2,1], m5 [2,3,0,1], m6 [0,3,1,2], m7 [3,0,1,2], m8 [0,2,3,1], m9 [1,0,3,2], m10 [3,0,1,2], m11 [1,2,3]).
- m1 h1 → surface changed from "40 to 400, incident reviews" (verbatim from idea 4) to "25-person agency merges into a 200-person one; client-handover ritual decays"; diagnoses kept.
- m1 h3 option "written from scratch" → diagnosis rewritten as a fit/transfer belief ("their practices didn't suit us"), not "copying is lazy".
- m1 h4 → idea 4 body gains a paragraph on Morgan et al. 2015 (N = 184, five conditions; silent demonstration adds little, verbal teaching best) and the norm-adherence vs skill-transfer distinction, so the hinge is answerable from the body; two sentences trimmed elsewhere in the idea to stay at 597 words (≤600).
- m2 h2 option "accept the diagnosis" → diagnosis rewritten as "familiarity as a cure for the attribution error" (the error survives a visible constraint), not naive realism.
- m2 h3 → stem drops "for a mixed-culture team" (contradicted idea 4's Western-sampled boundary note); correct option now reads "...with the magnitude in this team tagged [H]"; its diagnosis states direction [E], magnitude and interdependent-self cultures [H].
- m3 h1 → stem no longer says "the honest answer is yes"; it gives the payoffs (skipped shift saves a night; covered → no loss; uncovered → manager pages everyone) and asks the learner to run the diagnostic question.
- m3 h2 option "guarantees nothing unless the horizon is finite" (a belief nobody holds) → replaced by "Repetition guarantees cooperation once the team has been together long enough for reputations to form"; diagnosis: reputation as automatic selection (needs observation and a willing responder).
- m3 h5 → scenario changed to two departments with separate incident templates and a quarter of rework for switching alone; no bonus mentioned, so the hook's "more money did nothing" no longer pre-answers option "raise the joint payoff".
- Diagnostic d1, d5, d7, d11, d12 → rewritten as scenario statements without absolute tells and re-keyed True (a learner holding the folk theory marks them False); explanations for d1, d7, d12 adjusted to the new wording.
- Diagnostic d4, d9 → rewritten as scenario statements ("mainly" and the design-rationale wording removed); keys unchanged (False).
- Diagnostic d10 → split: the interpretive clause ("trusted the institution, no graceful exit") removed; item is now "most went to the maximum even when a peer refused", keyed False; explanation adds the peer-refusal figure.
- Diagnostic d14 → "a commons satisfying each of the eight principles can be expected to hold", keyed False; explanation notes association in selected cases is not a guarantee.
- Diagnostic d15 → re-keyed to Rogers's paradox ("a population of pure copiers outperforms trial-and-error learners", False); folk_theory now "copying is a free lunch"; explanation keeps the tournament result and its caveats.
- Diagnostic d16 → "the scarce resource is a small number of members with wide influence", keyed False; folk_theory wording aligned.
- Diagnostic d8 → inverted to catch the popular job-search version ("an acquaintance is a better source of job leads than a close friend"), keyed False; explanation states the course position: most jobs via weak ties in aggregate (Gee et al. 2017), a single strong tie more valuable at the margin, moderately weak ties best (Rajkumar et al. 2022); the item does not claim most jobs come via strong ties.
- Diagnostic balance → 8 True / 8 False; mean statement length 153 (True) vs 132 (False) characters; no "not X but Y" course-voice items remain; validator reports no tells warning. d2, d3, d6, d13 unchanged.
- The diagnostic table in section 2 above was updated to match `diagnostic.json`; the hinge drafts in sections 3.x are marked as superseded by the app data.
- Not done (out of scope, left for a later pass): de-duplicating cases k02/k04/k09 from the m1-m3 hinges and worked examples (QA §7 item 20).
- `validate.py`: 0 errors, 0 warnings after the changes.
