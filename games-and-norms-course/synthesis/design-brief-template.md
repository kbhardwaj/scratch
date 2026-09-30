# Cooperation brief: template and guide

The cooperation brief is the one document you keep about a real group you choose: a team, a
community, a platform or a commons. It starts as a single cold page written before the course
(v0, module m0) and ends as the capstone's input (v6, 3,000–4,000 words). Every module's
deliverable is a diff against the current version, so by the end the brief carries the course's
whole diagnostic path: boundary, games, learning network, situational audit, threshold map, type
mix, equilibrium-selection plan, norm register, institutional checklist, network map, public
signal, and three registers (hypotheses, values, measurement).

Section ids s1–s14, titles and order are fixed by `synthesis/learning-design.md` section 4c and
must not be renumbered. For each section this guide gives the purpose and the tension it governs,
the default tag, three to five drafting prompts, and what a good entry looks like. The last part
is one fully worked brief for a hypothetical group, "Lanternfish", a 40-person open-source
library with a maintainer-burnout and drive-by-pull-request problem. It shows form and tagging
discipline, not a recommended design; its numbers are the hypothetical's own data, not evidence.

Where this guide and `synthesis/claims-ledger.md` section 5 disagree, the ledger wins. "Law N"
means the twelve laws of cooperation in `synthesis/unified-model.md` section 6; `primer §N` means
`synthesis/gaps-primer.md`.

---

## Rules that apply to the whole brief

1. **Tag every declarative sentence** in the mechanism sections (s2–s11): [E] supported by
   evidence, [H] hypothesis to test in your group, [V] value commitment. Untagged fails the rubric.
2. **[E] needs a source slug** (`01`…`11` with chapter, or `primer §N`) and, where the ledger marks
   the finding contested, the caveat in the same sentence. An [E] the ledger does not support is a
   mis-tag.
3. **Split compound claims.** "Graduated sanctions keep rules alive, so our first sanction is a
   private note" is a mechanism [E: `09` ch 3] plus a parameter for your group [H].
4. **Classification of your group is always [H].** The stag hunt and the dilemma are theorems;
   "our review process is a stag hunt" is a hypothesis until the defection question has been
   answered with the group's own payoffs, and stays one after (ledger rule 13).
5. **Values are not weaker than evidence.** Never upgrade [V] to [E] because a source agrees;
   never write fairness as evidence rather than commitment (law 12).
6. **Numbers.** Quote only ledger section-4 or primer-verified figures, with hedges; otherwise say
   small, moderate, roughly doubled. Your group's own data are quotable and labelled as yours.
7. **Never build on the failed-replication list** (ego depletion, priming, power posing, watching
   eyes, Stanford Prison, groupthink as syndrome, IAT training; ledger rule 20). Strike such
   levers through in s4 with the reason; the strike-through is the learning.
8. **Every [H] has an s12 row; every [V] an s13 row; every s12 row an s14 line.**
9. **Later sections cite earlier ones by id and laws by number.** "Because s2 classified this as a
   dilemma (law 1), s9 supplies sanctions and repetition, not assurance."
10. **The median case, not the showcase.** Describe an ordinary week.
11. **Length.** v0 one page; v2 two to three pages; v6 3,000–4,000 words including registers.

---

## Header and changelog format

```
# <Group> — Cooperation brief v<N>
Date: <yyyy-mm-dd> · Previous version: v<N-1> (<date>) · Author: <you>
Changelog:
- [s<n>] Reversed | Added | Re-tagged | Removed | Struck: <what>. Motivated by m<n> (<author,
  slug>). Tag <old>→<new>. New H-nn / V-nn / N-nn.
```

One line per change. "Motivated by" names the module and source that moved you, so the capstone
can tell what you learned from what. Re-tags are the most important lines: they are the record of
your calibration improving.

---

## Version plan

| Version | After | What changes |
|---------|-------|--------------|
| v0 | m0 cold challenge (40 min) | One page: what the group should cooperate on and where it fails; why; three changes; how you would know in three months. Then list the assumptions you could not defend to a sceptic, and tag every decision as best you can. Expect to do this badly. |
| v1 | m1–m2 | s3 (collective brain) and s4 (situational audit, struck levers) added. Most "the people are the problem" lines get a situational alternative. |
| v2 | m3–m5 + R3 | s2 (games), s5 (thresholds), s6 (types) added. **Full re-tag checkpoint** of s2–s6: every classification becomes [H]; every "an incentive fixes it" line is checked against the game shape. |
| v3 | m6–m7 | s7 (equilibrium selection) and s8 (norm register) added. At least one measured expectation must exist before v3 is saved. |
| v4 | m8–m9 | s9 (institutions) and s10 (network) added; s1 revised now that boundary and subtractability are understood. |
| v5 | m10–m11 | s11 added; s12–s14 filled; v0 re-tagged line by line with a changelog. Capstone input. |
| v6 | Capstone sitting 1 | Every section filled and tagged; no [E] that is not a ledger [E]; diagnostic path visible; s14 has three dated predictions and an abandonment condition for the main hypothesis. |

---

## The sections

### s1. The group and its boundary: who is in, what is shared, subtractable or not — default [E/H]

**Purpose and tension.** Name the group precisely enough that every later section has a referent:
who is a member, user, outsider; what is shared; whether one person's use reduces another's
(subtractable) or not. Durable commons have clear boundaries
[E: `09` ch 3; Cox et al. 2010]; open-source, platforms and knowledge commons are open by design
at the outer layer. The founding mistake is answering "open or closed" for the whole group rather
than layer by layer (`primer §6, §8`).

**Prompts.**
1. Who says "I am part of this", and whom does the core say is part of it? Where do they differ?
2. Which resources are used up by use (review time, moderator time, a channel's signal) and which
   are not (docs, code, the group's reputation)?
3. What is churn per quarter, and newcomers per experienced member?
4. Which boundary is open that a later section will want to close, and vice versa?

**What good looks like.** Three layers with rules; a resource table; the scarce resource named in
one sentence; the open/closed answer per layer, [H] where it is a design choice.

### s2. Diagnosis: the games being played — default [H]

**Purpose and tension.** Draw the two or three central interactions before proposing anything
(law 1): players, options, payoffs as members construe them, order, information. Then the one
test: does a member gain by defecting when everyone else cooperates? Yes is a dilemma (fix set:
payoffs, repetition, detection, sanctions); no is a stag hunt (assurance, correlation, pledges)
[E: `04` ch 4, 10; `07` ch 1; ledger rule 13]. Governs assurance and talk versus enforcement
(t07). The founding mistake is a stag-hunt fix for a dilemma, or sanctions for a stag hunt where
they signal distrust and raise the lone cooperator's cost. Check one existing sanction for
credibility and separation [E: `04` ch 8, 9], and ask whether a "defector" is a one-shot player
rather than a type.

**Prompts.**
1. What does the cooperator get when all others defect, and the defector when all others cooperate?
2. Is the interaction repeated with the same people, and how fast is defection detected?
3. Which existing threat would its enforcer actually carry out?
4. If you reclassified the main interaction, which v0 fix would you withdraw?

**What good looks like.** A matrix or two-curve sketch per interaction; the defection question
answered in one sentence; shape tagged [H]; the fix set listed; one v0 fix marked "withdrawn:
wrong shape".

### s3. The collective brain: who learns from whom; models; single points of failure — default [H]

**Purpose and tension.** Map the actual learning network, never the org chart. Humans copy
prestigious and successful models more than they follow explanations [E: `01` ch 3–5, 8]; norm
adherence spreads by modelling, whereas skills with hidden structure need explicit teaching
[E: `02` ch 8; Morgan et al. 2015, one study, N = 184; ledger rule 8]. Governs copying versus
teaching (t01). The founding mistake is "just document it" for a norm, or "just model it" for a
skill.

**Guidance.** Name single points of failure; the prestigious members and whether they model the
target; one place where a leader's costly actions contradict the stated norm (credibility-enhancing
displays cut both ways [E: `01` ch 8]).

**Prompts.**
1. When someone new needs to learn how things are done, whom do they watch and whom do they ask?
2. Which critical process lives in one head?
3. Which prestigious member visibly does the opposite of the stated norm?
4. Which target behaviours are norms (model them) and which are skills (teach them)?

**What good looks like.** A learning-network sketch; a single-point-of-failure list; a prestige
list with a "models the target?" column; one behaviour predicted to change if a prestigious member
adopts it and one that will not change however well explained.

### s4. Situational audit and folk-psychology check — default [E/H]

**Purpose and tension.** For every v0 failure, write the situational alternative to the
dispositional story: workload, ambiguity, visibility, ownership, deliberation design [E: `03`
ch 1, 5, 12; attribution error; loafing under low identifiability]. Governs dispositions versus
structure (t14). The founding mistake is "the people are the problem", closely followed by a
lever from the failed-replication list.

**Guidance.** Record current descriptive and injunctive signals per target behaviour and whether
they agree; never advertise low adoption [E: `03` ch 9; Schultz et al. 2007; ledger rule 24;
law 5]. Strike through every v0 lever on ledger rule 20's list.

**Prompts.**
1. For each "they don't care" line, what would the same behaviour look like from someone who
   cared but faced this workload, ambiguity and visibility?
2. What tells a member what most people here do, and what is approved? Do the two agree?
3. Which v0 lever rests on a failed finding?
4. Where is effort unidentifiable, and what one change would make it identifiable?

**What good looks like.** A two-column table per failure; a signal audit with an "agree?"
column; struck levers with reasons; one structural change with a predicted effect size in words.

### s5. Threshold and tipping map; minimum viable coalition; arithmetic constraints — default [H]

**Purpose and tension.** Decide whether the target behaviour is contingent and where the group
sits relative to the crossing. Mild individual contingency produces stable low and high states
with an unstable tipping point between [E: `05` ch 3, 7; `10` ch 17]; the scarce resource is
low-threshold actors, never "influencers" (ledger rule 18). Governs t04 in population form. The
founding mistake is ignoring arithmetic: mentors per mentee, reviewers per review.

**Guidance.** Sketch the two curves and mark the current state. Estimate the minimum viable
coalition k as [H]. State one accounting identity v0 ignored [E: `05` ch 2]. Separate conventions
(self-enforcing) from norms that need a rule.

**Prompts.**
1. If a third of the group did it, would you? If two-thirds? Whose threshold is lower than yours?
2. Units of work per week divided by people willing and able: does the plan add up?
3. What is the smallest coalition that could run a pilot where the game is the same as at scale?
4. Which norms survive if nobody is watching (conventions) and which collapse (need a rule)?

**What good looks like.** A two-curve sketch with the group's position; k with reasoning; an
identity; the convention/rule split; what happens if the coalition falls one short.

### s6. Population of types and fairness baseline; weak-link processes — default [H]

**Purpose and tension.** State the type mix in words, what conditional cooperators can see of
others' contributions, and the group's own fairness reference point. Lab populations are roughly a
third self-interested and about half conditional cooperators (Camerer's summary, background;
direction only); fairness is cue- and expectation-dependent, not a fixed taste (ledger rule 9).
Governs t05 and t11. The founding mistake is explaining by selfishness what is strategic
uncertainty among conditional cooperators.

**Guidance.** Find any weak-link process and its size: pairs reach the top, groups of 14–16
collapsed within about ten rounds [E: `06` ch 7; Van Huyck et al. 1990]. Pick the amendment that
explains the v0 failure: social preferences, limited reasoning, or learning and history.

**Prompts.**
1. Of the under-contributors, how many would contribute if they could see others doing so?
2. What allocation do members compare, and against whom?
3. Which process aggregates by the minimum, and how many people are in it?
4. What would members read as a broken promise, and has one occurred?

**What good looks like.** Type mix with the visibility gap; the reference point and comparison
group; weak-link sizes; the amendment defended; a prediction for when contributions become visible.

### s7. Equilibrium selection plan: regime, correlation device, pacing, lone-cooperator cost — default [H]

**Purpose and tension.** For the main stag hunt, plan how to reach the payoff-dominant state.
Risk dominance wins under random mixing, best-response updating, large groups and no
communication; payoff dominance is reachable through correlation: small stable groups,
success-visible imitation, public pledges, gradual growth from a core, a lower cost of being the
lone cooperator [E: `07` ch 1, 3; `06` ch 7; Weber 2006, one lab lineage; ledger rule 2].
Sweetening the joint payoff is the weakest lever (law 3). The founding mistake is a big-bang
rollout to a mixed audience with a bonus attached.

**Guidance.** State the regime (random mixing and frequent re-evaluation, or stable subgroups with
visible success). Choose the cheapest correlation device: location, signal, or partner choice.
Local interaction helps only under success-copying (rules 3, 36). Cheap talk roughly doubles lab
cooperation and decays without sanctions or repetition where defection dominates (rule 12; law 6).

**Prompts.**
1. Who interacts with whom, how often does it change, and is success visible when it happens?
2. What is the cheapest way to make cooperators meet cooperators more than chance?
3. What does the lone cooperator lose today, and what change halves it?
4. From which core, at what rate per period, does the rollout grow?

**What good looks like.** Regime named; watershed in words; device chosen and costed;
lone-cooperator loss and its reduction; a pacing rate; a dated prediction of pledge decay.

### s8. Norm register: taxonomy, expectation measurement, cues, trendsetters — default [E for method, H for results]

**Purpose and tension.** Classify each "norm" by the expectations that sustain it: descriptive
norm, convention, social norm (conditional on empirical and normative expectations, can exist
while widely violated), moral norm [E: `08` ch 1; ledger rule 11]. Assume every norm conditional
until it survives a collapse of expectations (rule 10). Governs broadcasting the majority versus
building normative expectations (t10). The founding mistake is a values campaign aimed at
pluralistic ignorance, or a "most people do it" message where nobody does (`primer §1`).

**Guidance.** Run the four-question battery per behaviour in the reference network, not the org
chart: what do you do; what do most of them do; what do they think you should do; what happens to
a deviator; plus a sanction item [E: `primer §1`; *Norms in the Wild*]. Empirical expectations tend
to dominate normative ones [E: Bicchieri & Xiao 2009, lab]. Measure the
perceived-versus-actual gap [E: Tankard & Paluck 2016]. Record cues (templates, openers, bots) as
[H] for any specific cue-to-norm mapping (rule 37). Name trendsetters by nomination [E: Paluck et
al. 2016, school scale; H in an organisation].

**Register format (N-nn rows).**

| Id | Behaviour | Kind | Empirical expectation | Normative expectation | Sanction expectation | Perceived–actual gap | Descriptive signal | Injunctive signal | Cues | Trendsetters | Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Prompts.**
1. For each norm: what do members do, think others do, think others expect, and expect to happen
   to a deviator? Where does the pattern show pluralistic ignorance?
2. Whose opinion would a member actually notice? That is the reference network.
3. What template, label or bot message activates the norm at the moment of action?
4. Which norm collapses if one visible member deviates?

**What good looks like.** Three rows minimum, each classified; one expectation measured before
v3; gap direction stated; cues listed; the collapse prediction.

### s9. Institutional design: eight-principle checklist, sanctions ladder, monitoring, forum, standing, backstop — default [H/V]

**Purpose and tension.** Run Ostrom's principles as a diagnostic checklist, not a recipe:
boundaries, congruence, collective choice, monitoring, graduated sanctions, conflict resolution,
recognition, nesting [E: `09` ch 3; Cox et al. 2010, 91 studies, publication-bias and
structure-not-process caveats; rule 29]. Flag scope for digital commons. Governs designed versus
self-governed rules (t06) and incentives versus norm-based motivation (t12). The founding mistake
is a rule announced by the wrong person with a first sanction so severe nobody applies it.

**Guidance.** First sanctions are small and graduated; monitoring is a by-product of use [E: `09`
ch 3; rule 30; law 9]. Write the ladder with a trigger per rung (private note, public note,
temporary loss of a privilege, removal) [E: pyramid, `primer §2`; H your rungs]. Anti-social
punishment is real: measure or pilot before opening peer sanctions [E: Herrmann et al. 2008].
Fines can turn a norm into a price [E: Gneezy & Rustichini 2000; H here]. Elected sanctioners beat
appointed ones with identical powers [E: Baldassarri & Grossman 2011; `primer §3`]; rules members
made are followed more [E: principle 3]. State each rule's legitimacy source and the four
procedural-justice components (voice, neutrality, respect, trustworthy motives). Name the rule
level of each fix and who has standing to change it [E: `09` ch 2], and the external backstop.

**Prompts.**
1. For each principle: present, absent, or not applicable, with a scope note?
2. Who can sanction whom, at what cost to themselves, with what appeal?
3. What is the first, smallest sanction, and how many climbed each rung last quarter?
4. Who decided the rules, and can members show where their input changed them?
5. Which v0 fix was an operational rule, and who has standing to change it?

**What good looks like.** Eight rows with scope notes; a ladder with triggers; the by-product
monitoring channel; forum and appeal; legitimacy source per rule; backstop; the first cheap change
that produces information and standing.

### s10. Network map and seeding plan: clusters, bridges, q, seed set, copying kind — default [H]

**Purpose and tension.** Sketch clusters and bridges, estimate the adoption threshold q, place
the seed. A node adopts when at least q = b/(a+b) of its neighbours have; a cluster of density
above 1 − q blocks a cascade from outside and protects one adopted inside [E: `10` ch 19,
theorem; rule 3]. Information crosses one weak tie; costly behaviour needs several adopting
neighbours and wide bridges [E: `10` ch 19; rule 34]. Governs closure versus bridges (t09). The
founding mistake is announcing a costly norm across weak ties and expecting adoption. Name the
copying kind and its fix (cascade: collect private signals first; network effect: cross the
tipping point; coordination on a graph: lower q or seed inside clusters; rule 19); quote only the
structural weak-tie claim (rule 33); assume selection over influence (rule 35); seed inside
clusters and grow slowly (law 8).

**Prompts.**
1. Which sub-groups talk mostly to themselves, who holds the ties between them, and how many?
2. How many adopting neighbours does a typical member need before adopting?
3. Which cluster blocks the norm, and which protects it once adopted?
4. Is convergence a cascade, a network effect, or coordination on a graph?

**What good looks like.** A map with bridge holders; q with reasoning; the blocking cluster; the
seed inside a cluster; the copying kind and fix; which sub-group never adopts through current
bridges.

### s11. The signal and the BPC statement; the four layers addressed — default [H]

**Purpose and tension.** Name the public signal per coordination problem and check its
visibility. Nash equilibrium is a social achievement: aligned conjectures come from a public
signal, a choreographer [E: `11` ch 7; Aumann & Brandenburger 1995; rule 31]. Run the two-part
norm test on the main norm: epistemic (can everyone say what it requires of them and others) and
motivational (does anyone gain by deviating, and is there a cheap sanction). Write one BPC line
(beliefs about each other, preferences including status and fairness, constraints). Then say
which of the four layers v0 addressed: stability test, selection absent intervention, the signal,
the expectations inside agents (rule 1). Governs t03. The founding mistake is a vague value in
place of a specific signal (law 11).

**Prompts.**
1. What one public thing tells everyone what to do and what others will do? Who cannot see it?
2. Can a newcomer state the norm's requirement in one sentence?
3. Who gains by deviating while others comply, and what cheap sanction meets them?
4. Which layer did v0 touch, and which layer alone would move behaviour here?

**What good looks like.** A signal per problem with visibility; pass/fail on each half of the
test; a one-line BPC; a four-layer audit of v0; a prediction per layer.

### s12. Open hypotheses register — default [H]

**Purpose.** Every [H] in s1–s11 gets a row. This is the brief's experimental design; without it,
hypotheses are opinions with a label. "Why H not E" names the missing step (a lab result not
observed here; a classification not checked against the group's payoffs; a parameter the sources
leave open). "Decision rule" says what result keeps, revises or abandons the row.

| Id | Hypothesis | Section | Why H not E | Test | Prediction | Practical measure | Balancing measure | Decision rule | Review date | Status |
|---|---|---|---|---|---|---|---|---|---|---|

**Prompts.** What would I see in ninety days if true, and if false? What cheap observation moves
this toward E for this group, or kills it? What harm would the intervention cause if the row is
wrong, and how would I see it?

**What good looks like.** Every column filled; no row without a balancing measure; no duplicate
hypotheses; statuses updated each version.

### s13. Value commitments register — default [V]

**Purpose.** Every [V] gets a row of the form "We choose X over Y". A value with no reasonable
dissenter is a platitude; one with no cost is a description. Apply `primer §10`: is the
intervention reflective or automatic, disclosed or not; who consented; who bears the cost when it
misfires; what is the exit.

| Id | Commitment ("We choose X over Y") | Section | Who reasonably disagrees, best argument | Cost | Evidence that informs it | Conflicts with | Owner and review |
|---|---|---|---|---|---|---|---|

**Prompts.** What are we optimising for and knowingly giving up? Who would object, and what is the
strongest version of their objection? Which interventions sit in the automatic-and-undisclosed
quadrant? Who can change this rule, and who can leave at what cost?

**What good looks like.** Four to eight rows with a named dissenter and a cost each; no row that
restates evidence; conflicts column non-empty for at least two rows.

### s14. Measurement plan and ninety-day predictions — default [H]

**Purpose.** Convert the registers into three measures per intervention: the **practical measure**
(the behaviour or expectation expected to move, from logs or the battery), the **predicted value**
(direction and size in words, or a number from your own baseline, with a date), and the
**balancing measure** (what would show harm: newcomer rejection, reviewer churn, anti-social
sanctioning, the boomerang, load shifting onto the already loaded). Surveys measure beliefs and
logs measure behaviour; report both, the mismatch is diagnostic (`primer §1`). Re-measure and
revise: both moved, scale gradually; behaviour only, the change rides on observation and will
decay; expectations only, the game is unstable at layer one, return to s2 (`unified-model` §4).

| Intervention (id) | Practical measure | Baseline (own data, date) | Predicted at day 90 | Balancing measure | Harm threshold | Abandon if | Owner | Cadence |
|---|---|---|---|---|---|---|---|---|

**Prompts.** What is the first cheap change that produces both information and standing? For each
intervention, what number do I expect on day 90, and what number makes me stop? What could go up
that I would not want, and am I logging it? Which measure can the intervention satisfy without the
behaviour changing?

**What good looks like.** Three dated predictions; a balancing measure per intervention; an
abandonment condition for the main hypothesis; the re-measurement date.

---

## Self-check before saving a new version

1. **Traceability.** Does every fix in s7–s11 cite the s2 classification and a law by number, and
   does diagnosis precede fix in every section?
2. **Tags.** Any untagged sentence in s2–s11? Any [E] without a slug? Any [E] the ledger marks [H]
   (your group's classification; cultural group selection; evolved strong reciprocity; the
   population-size collective brain; any single social-preference model)?
3. **Caveats.** Does every contested finding carry its caveat in the same sentence?
4. **Registers.** Every [H] in s12 with a balancing measure; every [V] in s13 with a dissenter;
   every s12 row in s14?
5. **Median case.** An ordinary week, own data labelled as own?
6. **Changelog.** Every change names module and source; every re-tag shows old and new?
7. **Failed levers.** Anything on ledger rule 20's list still load-bearing?
8. **The missing decision.** Who has standing to change the rules, and what is the public signal?
   These are the two decisions learners skip most.

---

## Worked example: Lanternfish — Cooperation brief v6

*Context (all parameters invented).* Lanternfish is a seven-year-old open-source data-validation
library in Python, a dependency of a moderate number of commercial products. About 40 people
contributed in the last twelve months: three maintainers with merge rights (Priya, founder and
lead; Tomasz; Wen, who went "emeritus" four months ago citing exhaustion); twelve regulars with
three or more merged changes who answer issues; about 25 occasional or first-time contributors.
About 30 pull requests arrive a month, half from first-timers, and about a third of those are
abandoned after the first review round. Priya does about 60% of reviews and merges. Median time
to first maintainer response is around three weeks. There is a code of conduct enforced by Priya
alone, a `CONTRIBUTING.md` nobody reads, and a Discord where regulars talk. The v0 fixes were:
rewrite `CONTRIBUTING.md`; ask for review volunteers on Discord; add a "good first issue" label.
Numbers below are Lanternfish's own logs and surveys unless a slug is given.

```
# Lanternfish — Cooperation brief v6
Date: 2026-09-30 · Previous version: v5 (2026-09-24) · Author: T. (regular contributor)
Changelog:
- [s2] Re-tagged: "review load is a tragedy of the commons" [E]→[H]. Motivated by m11
  (ledger rule 13).
- [s4] Struck: "burnout is depleted willpower". Motivated by m2 (`03` evidence; ledger C11).
- [s9] Reversed: review bounty removed; reputational credit substituted. Motivated by m8 and
  primer §2 (Gneezy & Rustichini). Tag [E]→[H]. New H-06, V-04.
- [s9] Added: elected stewards replace lead-appointed helpers. Motivated by primer §3
  (Baldassarri & Grossman). New V-05.
- [s14] Added: first-PR 90-day return rate as balancing measure. Motivated by primer §6
  (Halfaker et al. 2013).
```

### s1. The group and its boundary

Three layers. Core: three maintainers, boundary "invited by existing maintainers" [E: fact].
Regulars: twelve people, boundary informal; eleven of twelve named a different list when asked
who counts [E: own survey]. Periphery: anyone with a GitHub account [E: fact]. Users: unknown; a
moderate share of issues come from company email domains [H: inferred, not verified].

Resources. Code and docs are non-subtractable [E: public good by construction]. Maintainer review
attention is subtractable and is the scarce resource: about 30 PRs a month at roughly 45 minutes
is about 22 hours against about 25 hours of total maintainer time [E: own logs; the 45-minute
unit is a self-report, H]. Triage time is subtractable and unowned: 80% of open issues have no
assignee [E: own data]. Reputation for reliability is depletable by a bad release [H].

Size. Contributors flat at about 40 for two years; PR volume up about a third year on year after a
popular framework made Lanternfish a default [E: own data]. Roughly fifteen newcomers a month
against three maintainers, a ratio no onboarding absorbs by teaching [H; `primer §8` treats
onboarding capacity as a constraint].

Open versus closed. The periphery stays open [V: V-02]. The regular layer gets a boundary because
a layer with no boundary cannot carry obligations [E: `09` ch 3, digital-commons scope caveat] and
the rota in s7 needs a defined membership [H: H-02].

### s2. Diagnosis: the games being played

**A: opening PRs against maintainer attention.** A first-time contributor pays nothing to open a
PR; the review cost falls on maintainers [E: own logs; `04` ch 11 on unpriced external costs].
Defection question: does a contributor gain by opening a low-effort PR when everyone else opens
careful ones? Yes: the queue is served roughly in order and review is free to them [H: H-01].
Shape: an open-access dilemma on a subtractable resource, Ostrom's open-access case [H: H-01;
`09` ch 1; rule 13]. Fix set: boundaries on what enters the queue, an entry price in effort (not
money), detection, graduated sanctions; assurance alone will not do [E: `04` ch 10; `09` ch 3;
H that the shape is right]. Most "defectors" are one-shot players with no shadow of the future,
not a type, so the folk theorem gives nothing here [E: `04` ch 10; rule 15]; the lever is entry
structure, not reputation [H: H-01].

**B: regulars reviewing.** If four or more review regularly, each review is cheap (shared context,
fast turnaround, visible credit); if one reviews alone, that person becomes the next Priya [E:
Wen's exit; H that others see it so]. Defection question: does a regular gain by not reviewing
when all others review? No: they lose standing and the queue they depend on slows; but the lone
reviewer loses badly [H: H-02]. Shape: a stag hunt with a high lone-cooperator cost [H: H-02;
`07` ch 1]. Fix set: assurance, correlation, lower lone-cooperator cost, pacing (s7); sanctions
would signal distrust [E: `07` ch 3; rule 2]. Reclassifying B from my v0 dilemma ("people won't
review because it's unrewarded") withdraws the v0 fix "reward reviewers" [H: H-02].

**C: Priya merging her own PRs unreviewed.** A single-player deviation, a credibility problem for
s3 and s11 [H].

**Existing sanction.** Closing a PR, applied inconsistently: 40% of closes carry no comment [E: own
logs]. Credible but unpredictable, so it separates nobody: careful and careless contributors face
the same expected outcome [E: `04` ch 8 on separation; own data].

### s3. The collective brain

Newcomers learn conventions from recently merged PRs, not `CONTRIBUTING.md`: seven of eight recent
contributors said so [E: own survey; H that it generalises]. Regulars learn from Priya's review
comments, the de facto style guide [E: same survey]. So the models are whatever merged last
month, including Priya's unreviewed merges [E: own logs].

Single point of failure: the release process (signing, changelog, deprecation policy) lives in
Priya's head; Wen knew it and left [E: fact]. It is a skill with hidden structure, so it needs a
runbook practised by someone else, not modelling [E: `02` ch 8; Morgan et al. 2015, one study;
rule 8]. Review conventions are a norm and spread through what gets merged; the v0 fix "rewrite
CONTRIBUTING.md" hit the wrong channel for the norm and the right one for the skill [H: H-03].

Prestige. Priya is the model; her most-copied behaviour is merging without review, against the
stated two-approval rule: roughly a quarter of her merges have zero approvals [E: own logs].
Costly actions outweigh statements [E: `01` ch 8; H for size here]. Tomasz waits for review and
nobody notices [H]. Nobody is licensed to try a different workflow; the last proposal got "that's
not how we do it" [E: fact]; pure copying stagnates [E: `02` ch 3, simulation], so the pilot is
also the licence to experiment [V: V-06].

Prediction. If Priya visibly waits for review for a month, regulars' approval rate on each
other's PRs rises within three months [H: H-04]. The runbook is not learned until someone
performs a release with it [H: H-03].

### s4. Situational audit and folk-psychology check

| v0 story | Situational alternative |
|---|---|
| "Drive-by contributors are lazy and don't read the guide." | The guide is not at the point of action; the PR template is empty; newcomers cannot see the queue or the expected turnaround [E: fact; `03` ch 1 attribution; H that fixing it changes behaviour, H-05]. |
| "Regulars don't care about the project." | Reviewing is unidentifiable: no reviewer credit exists; the lone reviewer inherits the queue [E: `03` ch 12, loafing under low identifiability; own data]. |
| "Priya can't say no." | Priya is the only merger on the default branch, the only CoC enforcer and the only releaser: three unowned jobs in one person [E: fact; `primer §7` on load]. |

Signals. Descriptive signal for "respond promptly": the queue itself, 90 open PRs, some a year
old, which advertises that nobody responds [E: fact; law 5 violation]. Injunctive: the
`CONTRIBUTING.md` line "we aim to respond within a week" [E: fact]. They disagree and the
descriptive one wins [E: `primer §1`; Bicchieri & Xiao 2009, lab]. The pinned Discord message
"we're drowning in PRs, please help" advertises low adoption of reviewing, the boomerang case
[E: rule 24].

Struck v0 levers.
- ~~Burnout is depleted willpower; schedule reviews in the morning.~~ Ego depletion failed a
  23-lab registered replication, d = 0.04 [E: `03` evidence; ledger C11].
- ~~A "you are being watched" review-count widget.~~ Watching-eyes is on the failed list [E: rule
  20]; a public count also advertises the low rate.
- ~~Implicit-bias training for reviewers who close newcomer PRs.~~ IAT training is on the failed
  list [E: rule 20]; the close rate is a process problem (s9).

Predicted structural change: identifiable review credit moves the share of non-lead reviews by a
moderate amount [H: H-06].

### s5. Threshold and tipping map

Target: a regular reviewing two PRs a week. Nine of twelve regulars said they would "if I knew
others were" [E: own survey], so the behaviour is contingent. The payoff to reviewing rises with
the number of other reviewers and is negative alone; the curves cross at about four reviewers,
below which the state decays to Priya-only [H: H-02, crossing estimated from the survey]. Current
state: below the crossing [E: own logs]. Low-threshold members: Tomasz and two regulars who
already review occasionally [E: own logs]. Minimum viable coalition k = 4, Priya excluded so the
pilot tests the regulars' equilibrium and not her stamina [H: H-02].

Arithmetic v0 ignored: 30 PRs at 45 minutes is about 22 hours a month; four reviewers at two a
week cover about 32 PRs, barely sufficient with no slack for abandoned PRs [E: own arithmetic;
H for the unit]. "Ask for volunteers" had no number and so no way to know when it had succeeded.

Convention versus rule. Commit-message format is self-enforcing: CI rejects deviations and nobody
gains by deviating [E: fact; `08` ch 1 convention]. "Two approvals before merge" needs a rule
because the lead gains speed by deviating [E: own logs; H-04]. Regulars have clustered on Discord
and newcomers on GitHub without anyone deciding; assume selection, not influence [E: rule 35].

### s6. Population of types and fairness baseline

Regulars are mostly conditional cooperators with one or two who review regardless; nine of twelve
conditional matches the lab direction, quoted as direction only [E: `06` ch 2, background; H for
the mix, H-02]. First-timers are not "selfish": they are one-shot players and A explains them
without a preference story [H: H-01; rule 9 against fixed-taste stories]. Visibility gap: a
regular cannot see that anyone else reviewed this week [E: fact].

Fairness reference point. Maintainers compare their unpaid load against commercial users who file
issues and never contribute; the felt violation is a broken implicit promise, the strong
negative-reciprocity case [E: rule 28; H that this is their reference point, H-07]. The lab's
ultimatum figure is irrelevant to this allocation and not quoted as ours [E: rule 25 scope].

Weak link. Release readiness is a minimum-effort game across about eight module owners; one
unresponsive owner blocks a release [E: fact]. Groups of 14–16 collapsed in the lab while pairs
reached the top [E: `06` ch 7]; eight is the uncertain middle, so ownership goes in pairs, not
committees [H: H-08].

Amendment. The main v0 failure is strategic uncertainty among conditional cooperators, not
selfishness; the history amendment also applies, since Wen's exit locked in "reviewing is how you
burn out" as the visible lesson [H: H-02; `06` ch 6 path dependence as the mechanism]. Prediction:
when weekly review counts become visible to regulars, regular-authored reviews rise by a moderate
amount within six weeks [H: H-06].

### s7. Equilibrium selection plan

Regime now: near-random mixing (any regular may pick any PR, nobody does, no success is visible)
and weekly re-evaluation [E: fact; `07` ch 3 on why this selects the risk-dominant state].
Watershed: well below the fraction of reviewers needed for reviewing to be the safe choice [H:
H-02].

Correlation device: signal plus location, a labelled queue with a named rota of four regulars in
pairs, each pair owning two weekdays [H: H-02]. Pairs form by mutual nomination, since partner
choice generates structure cheaply [E: `07` ch 6, model; H here]. Money is the weakest lever and
rejected [E: law 3; V: V-04].

Lone-cooperator cost. Today the lone reviewer inherits an unbounded queue. Each rota member
commits to two PRs per shift, not to the queue; the rest is explicitly nobody's job [H: H-02;
V: V-01].

Pacing. Tomasz plus three low-threshold regulars for six weeks with a visible weekly one-line
history; add two regulars a month only after the pilot's numbers hold [E: Weber 2006, gradual
growth with visible history, one lab lineage; H for the rate, H-02].

Cheap talk. A pledge round on Discord ("I'll take Tuesdays") should roughly double short-run
participation and then decay unless repetition and visible credit sustain it; in A (a dilemma) a
pledge would do nothing durable [E: rule 12; law 6; H for duration, H-02].

### s8. Norm register

Reference network: eleven regulars and two maintainers answered the four-question battery with one
vignette (a reviewer approving an unread PR from a senior author) [E: method, `primer §1`; `08`
ch 1]. The normative item used Krupka–Weber framing without payment [H: H-09].

| Id | Behaviour | Kind | Empirical expectation | Normative expectation | Sanction expectation | Gap | Descriptive signal | Injunctive signal | Cues | Trendsetters | Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| N-01 | Two approvals before merge | Social norm, violated by the lead | 4 of 13 believe most merges have two; actual about 55% [E: logs] | 12 of 13 think others expect it | "Nothing happens" (13 of 13) | Perceived below actual; the lead's deviations are what people see | Priya's merges | CONTRIBUTING.md | Branch protection; template checkbox | Priya (11 of 13 nominations) | [H: H-04] |
| N-02 | First response within seven days | Aspiration; no descriptive norm (median about three weeks) | 0 of 13 | 10 of 13 | None | Perception matches reality: a dead rule, not pluralistic ignorance | The 90-PR queue | CONTRIBUTING.md | "needs first response" label; rota bot | Tomasz | [H: H-05; not to be advertised until the rota makes it true, law 5] |
| N-03 | Issue before PR | Convention among regulars, unknown to newcomers | Regulars 9 of 11; newcomers no data | 5 of 13 | None | A boundary problem, not an expectation problem | Merged PRs with linked issues | None | PR template first line | none | [H: H-05; cue mapping is H, rule 37] |

Reading. N-01 is the classic pluralistic-ignorance case: regulars hold the norm and believe others
hold it, but see the lead violate it and infer it is dead [E: `08` ch 5 mechanism; H here, H-04].
N-02 is a rule with no empirical support; a "we respond in seven days" campaign would advertise a
falsehood [E: law 5; rule 24]. Prediction: N-01 collapses further if Priya self-merges a large PR
during the pilot; N-03 survives any single deviation because it is a convention with CI-like cues
[H: H-04, H-05].

### s9. Institutional design

Scope: a knowledge commons with an open outer layer; principles applied to review attention, not
to the code [E: rule 29 scope flag].

| Principle | Status | Note |
|---|---|---|
| 1 Boundaries | Absent for regulars | "Regular" = three merged changes in twelve months plus opt-in to the roster [H: H-02]. Periphery open [V: V-02]. |
| 2 Congruence | Absent | A 2,000-line PR and a typo fix enter the same queue [E: fact]. Size label; large PRs need an issue and design note first [H: H-05]. |
| 3 Collective choice | Absent | Priya decides alone. Rota rules set and changed by rota members in a monthly thread [E: `09` principle 3; Fiesler et al. 2018, `primer §3`; V: V-05]. |
| 4 Monitoring | Present, by-product | CI, the PR dashboard and the weekly summary monitor without a monitor [E: `09` ch 3; law 9]. |
| 5 Graduated sanctions | Absent | Close-or-nothing today. Ladder below [H: H-06]. |
| 6 Conflict resolution | Absent | Elected steward pair with a public appeal thread; explanations on every close [E: Jhaver et al. 2019, observational, `primer §2`; H here]. |
| 7 Recognition | Partial | The hosting foundation recognises maintainers but has never been asked to recognise a rota [E: fact]. Ask for written recognition of the rota's authority over the queue [H: H-10]. |
| 8 Nesting | Not applicable at 40 | Revisit above about 25 regulars [H; `primer §8`, Dunbar's number contested]. |

Ladder for A [E: graduated sanctions, `09` ch 3; pyramid, `primer §2`; H for the rungs, H-06].
(1) Automatic: a PR without a linked issue or completed template gets a bot comment explaining
what is missing and a "needs info" label; nothing is closed [E: Matias 2019 on rules at the
point of action, `primer §6`; H here]. (2) After fourteen days of silence: "stale" label and a
second explained comment. (3) After thirty days: closed with explanation and an explicit "reopen
any time". (4) Repeated bad-faith PRs: temporary block by the stewards with an appeal thread
[V: V-03]. No rung is monetary: a bounty or fine would say the norm is purchasable [E: Gneezy &
Rustichini 2000, `primer §2`; H that crowding-out would occur here, H-06; V: V-04].

Sanctions for B: none. A stag hunt needs assurance, not punishment; a missed shift is handled by
the pair [E: rule 2; H here]. No peer down-vote or "unhelpful reviewer" flag, because anti-social
punishment is real and predictable [E: Herrmann et al. 2008, cross-societal; H for our position].

Legitimacy. Stewards are elected by regulars for six months, not appointed, because election
raised cooperation beyond appointment with identical powers [E: Baldassarri & Grossman 2011; H for
transfer, H-06; V: V-05]. Procedural justice: voice (monthly thread), neutrality (the bot applies
rung 1 to everyone including maintainers), respect (a tone standard for close messages),
trustworthy motives (Priya's PRs go through the same queue) [E: `primer §3` for the components;
H for their weight here].

Rule levels and standing. The v0 fix "rewrite CONTRIBUTING.md" was an operational rule nobody had
standing to enforce. Rota rules are operational; who may change them (rota members plus one
maintainer) is the collective-choice rule; the constitutional backstop is the foundation's
code-of-conduct committee [E: `09` ch 2 on rule levels; fact for the committee].

Reputation. The contributor graph rewards volume and predicts nothing about review quality
[E: `primer §4` on aggregate scores; own data]. Add one narrow signal, reviews completed per
release listed in release notes, and no score [H: H-06]. Identity re-entry is cheap on GitHub, so
the ladder is per-PR, not per-person, until rung 4 [E: `primer §4` on whitewashing; H design].

First cheap change producing information and standing: the rung-1 bot plus elected stewards. In
three months it reveals how many first-time PRs lack information versus effort, and it creates a
role that can legitimately close [H: H-06].

### s10. Network map and seeding plan

Clusters: the maintainer–regular cluster on Discord (dense, about 15); the issue-answering cluster
on GitHub Discussions (about 8, overlapping regulars by 3); the periphery, unconnected [E: own map].
Bridge: Sam alone is active in all three; the tie is structurally weak, as bridges tend to be
[E: `10` ch 3; rule 33; fact for Sam]. The Discord cluster is mostly European time zones; assume
selection, not influence [E: rule 35].

Threshold. Reviewing two PRs a week is costly, so a complex contagion: a regular needs to see at
least two close ties doing it; q around one-third [H: H-02; `10` ch 19 mechanism]. The Discord
cluster is dense enough to block the norm from outside and protect it once adopted inside
[E: cluster-blocking theorem, `10` ch 19]. Seed inside it: all four pilot members are Discord
regulars [H: H-02; law 8]. The issue-answering cluster will not adopt through Sam's single tie;
one pilot member comes from the overlap [H: H-11].

Copying kind. "Nobody reviews" is conformist transmission, which is why clusters have not
helped; the fix is success visibility (the weekly summary naming who reviewed and what merged
faster) so success-copying takes over [E: rules 3, 36; H here, H-06]. Not an informational
cascade: nobody has private information that reviewing is bad [H]. Prediction: Discord regulars
adopt first; the issue-answering cluster does not adopt within ninety days unless the second
bridge is in the pilot [H: H-11].

### s11. The signal and the BPC statement

Signals. For B, the rota page: who reviews when, visible to all regulars [H: H-02]. Today "please
help" is not a choreographer: it tells nobody what to do or what others will do [E: `11` ch 7;
law 11]. For A, the PR template and bot comment at the moment of action [E: Matias 2019; H here,
H-05]. The periphery cannot see the rota; acceptable, they are not players in B [H].

Two-part test on N-01. Epistemic: fails; newcomers cannot say what an approval requires and
regulars disagree on whether self-approval counts [E: survey]. Motivational: fails; the lead gains
speed by deviating and no cheap sanction exists [E: logs]. Fix: a one-paragraph review checklist
(epistemic) and branch protection applying to maintainers (motivational, a rule not a sanction)
[H: H-04].

BPC. Beliefs: others will not review, and reviewing leads to burnout; preferences: the project's
reputation and standing among regulars over speed; constraints: bounded free time, no merge rights,
an unfilterable queue [H: H-02; BPC is bookkeeping, not explanation, ledger X16].

Four-layer audit of v0. The fixes touched layer three only, and weakly (a document as signal).
Layer one (is reviewing an equilibrium of the game as structured?) was never asked; layer two
(where the group drifts under random mixing) ignored; layer four (what regulars expect of each
other) unmeasured [E: rule 1 for the layers; H for the audit]. Prediction: layer two alone (the
rota) moves the pilot; layer three alone (a better document) does nothing; layer four alone
(publishing that twelve of thirteen expect two approvals) moves N-01 only if the lead's compliance
is visible at the same time [H: H-02, H-04].

### s12. Open hypotheses register

| Id | Hypothesis | Section | Why H not E | Test | Prediction | Practical measure | Balancing measure | Decision rule | Review date | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| H-01 | A is an open-access dilemma; entry structure, not reputation, is the lever | s2, s6 | Classification of our payoffs; one-shot status inferred | Rung-1 bot for 60 days | Abandonment falls from about a third to well under a fifth | Share of PRs abandoned after first round | First-PR 90-day return rate; good-faith closes at rung 3 | Keep if abandonment falls and return rate holds; abandon ladder if good-faith closes exceed one in ten | 2026-12-01 | Open |
| H-02 | B is a stag hunt; a bounded rota of four inside the Discord cluster reaches the high state | s2, s5, s7, s10, s11 | Payoffs self-reported; k from survey; Weber 2006 is one lab lineage | Six-week pilot with visible weekly history | Regular-authored reviews from about 15% to over 40%; Priya under 40% | Reviews by author per week | Rota-member self-reported load; rota churn | Keep if both hold six weeks; revise k if fewer than 3 shifts filled; abandon if any member's load rises | 2026-11-15 | Open |
| H-03 | The release process is a hidden-structure skill: runbook plus a supervised release transfers it; a runbook alone does not | s3 | Morgan et al. 2015 is one study | Tomasz releases with runbook, Priya observing; then alone | Second solo release succeeds | Non-lead releases | Defects per release | Keep if two solo releases ship; else rewrite and repeat | 2026-12-15 | Open |
| H-04 | Visible lead compliance with N-01 restores regulars' expectation and approval rate | s3, s8, s11 | CRED size unknown here; one expectation measurement | Branch protection on maintainers; re-run battery at day 60 | Belief from 4 of 13 to a majority | N-01 battery; share of two-approval merges | Median merge time (not above 10 days) | Keep if belief and behaviour move; behaviour only means decay, add checklist emphasis | 2026-12-01 | Open |
| H-05 | Rules at the point of action (template, bot) raise newcomer compliance with N-03 | s4, s8, s9, s11 | Matias 2019 is one platform; cue mapping is H | Template on all new PRs | Linked-issue share rises moderately | Newcomer PRs with linked issue | First-PR volume; friction complaints | Keep if compliance rises and volume falls under 10% | 2026-12-01 | Open |
| H-06 | Identifiable credit, elected stewards and a non-monetary ladder raise regular reviewing and lower abandonment without crowding out or gaming | s4, s6, s9, s10 | Field results from farmers and day care; loafing is direction only | Credit line in two releases; election; ladder on | Named reviewers per release up; rung 4 near zero | Reviews per release by non-lead; rung transitions | Trivial-approval rate; disputed closes overturned on appeal | Keep unless trivial approvals exceed one in five or most rung-3 closes are good-faith | 2027-01-15 | Open |
| H-07 | Maintainers' reference point is commercial users' non-contribution; a visible "sponsor or contribute" ask reduces felt violation | s6 | Inferred from two interviews | Maintainer interview at day 90 | Felt-fairness item improves | One-item fairness question | Issue quality from company users | Low stakes; keep or drop | 2026-12-30 | Open |
| H-08 | Module ownership in pairs keeps the release weak-link game small enough | s6 | Eight is between the lab's pairs and 14–16 | Pair the eight owners | Blockers per release fall | Release blockers | Owner load | Keep if blockers fall over two releases | 2027-01-15 | Open |
| H-09 | Unpaid Krupka–Weber framing recovers normative expectations here | s8 | Primer marks the unpaid version H | Compare with the direct item | Framed answers less socially desirable | Item difference | None | Method note | 2026-11-01 | Open |
| H-10 | Written foundation recognition makes rota rules stick | s9 | Principle 7 is a cross-case regularity | Ask; watch for overrides | No overrides in 90 days | Overrides | Foundation friction | Keep if none | 2026-12-30 | Open |
| H-11 | The issue-answering cluster adopts only with a second bridge in the pilot | s10 | Cluster blocking is a theorem; our q is an estimate | One pilot member from the overlap | Adoption there by day 90 | Reviews by that cluster | Sam's load | Keep or add a third bridge | 2026-12-30 | Open |

### s13. Value commitments register

| Id | Commitment | Section | Who reasonably disagrees, best argument | Cost | Evidence that informs it | Conflicts with | Owner and review |
|---|---|---|---|---|---|---|---|
| V-01 | Maintainer sustainability over PR throughput | s7, s14 | Dependent users: "a slower project is a worse dependency; forks will follow" | Slower merges; some contributors leave | Wen's exit; stable membership as precondition (`primer §7`) | V-02 | Maintainers; v7 |
| V-02 | An open PR door over gating first-timers behind an application | s1, s9 | Tomasz: "gating cuts spam by more than it costs" | Bot and steward effort; some slop | Halfaker et al. 2013 on newcomer rejection (`primer §6`) | V-01 | Stewards; six months |
| V-03 | Every sanction explained in public over quiet closes | s9 | A steward: "public explanations invite arguments and humiliate newcomers" | Steward time; friction | Jhaver et al. 2019, observational | none | Stewards |
| V-04 | Recognition, not money, for reviews | s7, s9 | A commercial user: "we would pay for review; refusing is ideology" | Forgone funds; slower for payers | Gneezy & Rustichini 2000 informs, does not settle; crowding-in also occurs | V-01 | Maintainers; revisit on any grant |
| V-05 | Elected stewards and member-made rota rules over founder appointment | s9 | Priya: "elections are theatre at 12 people; I know who is reliable" | Time; an unreliable steward | Baldassarri & Grossman 2011; Ostrom principle 3 | none | Regulars; six-month term |
| V-06 | Regulars may experiment with workflow over "that's not how we do it" | s3 | A regular: "experiments cost the rest of us stability" | Process churn | Innovation budget (`02` ch 3, simulation) | V-01 | Rota; monthly |
| V-07 | Members are told what is measured and why; no undisclosed nudges | s8, s14 | A steward: disclosure may change survey answers | Some measurement purity | Disclosed nudges retain effect for defaults (`primer §10`; H for norm messages) | none | Author; each version |

### s14. Measurement plan and ninety-day predictions

Baseline 2026-09-30 from Lanternfish's own logs and the s8 survey; battery re-run 2026-12-01.

| Intervention | Practical measure | Baseline | Predicted day 90 | Balancing measure | Harm threshold | Abandon if | Owner | Cadence |
|---|---|---|---|---|---|---|---|---|
| Rota pilot (H-02) | Share of reviews by non-lead | about 40% overall, about 15% by regulars | Regulars over 40%; Priya under 40% | Rota self-reported load; churn | Any member above prior load; more than one drop-out | Fewer than 3 of 4 shifts filled in weeks 3–6 | Tomasz | Weekly |
| Bot and ladder (H-01, H-06) | First-response median; abandonment | about 3 weeks; about a third | Under 7 days for complete PRs; well under a fifth | First-PR 90-day return rate; good-faith rung-3 closes | Return rate down more than a fifth; good-faith closes over one in ten | Both harms observed | Stewards | Fortnightly |
| Branch protection (H-04) | Two-approval merges; N-01 belief | about 55%; 4 of 13 | Over 90%; majority | Median merge time | Over 10 days | Merge time doubles with no belief change | Priya | Monthly |
| Release credit and stewards (H-06) | Named reviewers per release | 2 | 6 or more | Trivial-approval rate | Over one in five | Trivial approvals dominate | Stewards | Per release |
| Runbook (H-03) | Non-lead releases | 0 | 2 | Defects per release | Above prior average | Two failed solo releases | Tomasz | Per release |
| Template cue (H-05) | Newcomer PRs with linked issue | about 20% | Moderate rise | First-PR volume | Falls over 10% | Volume falls with no compliance gain | Stewards | Monthly |

Three dated predictions. (1) By 2026-12-01, regular-authored reviews exceed 40% of all reviews and
Priya's share is below 40% [H: H-02]. (2) By 2026-12-01, a majority of regulars believe most
merges get two approvals, and actual two-approval merges exceed 90% [H: H-04]. (3) By 2026-12-30,
first-response median for template-complete PRs is under seven days and the first-PR return rate
has not fallen by more than a fifth [H: H-01, H-05].

Abandonment condition for the main hypothesis. If by week six the rota fills fewer than three
shifts in four, or any member reports higher load than before, H-02 is wrong about the shape (B is
a dilemma needing repetition and a sanction) or the coalition size; return to s2 and re-draw B with
the pilot's own payoffs [H: H-02; `unified-model` §4 station 5]. If reviews rise but the N-01
battery does not move, the change rides on the weekly summary being read and will decay when it
lapses; keep the summary and add the checklist, not a reward [E: `unified-model` §4; law 6].

---

## Reconciliation notes

- The generic template's "L1–L5 foundation commitments" section is absent from this course's
  canonical skeleton (s3 is the collective brain); its role of numbered commitments cited by later
  sections is filled by the twelve laws (`unified-model.md` §6) and the ledger's binding rules.
- The version plan runs v0–v6 per learning-design (v5 after m11, v6 at the capstone).
- Every number in the example is the hypothetical's own labelled data or a ledger section-4 or
  primer-verified figure with its hedge; no lab figure is used as a field estimate (rules 27, 40).
- Primer sections 1–4 add to the brief: the four-question battery and reference network (s8);
  the sanctions ladder, anti-social punishment check, legitimacy source, procedural-justice
  components, reputation scope and identity re-entry (s9); the practical/predicted/balancing
  triple (s14).
