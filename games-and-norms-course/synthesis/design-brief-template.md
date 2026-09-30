# Cooperation brief: template and guide

The cooperation brief is the one document you keep about a real group you choose: a team, a
community, a platform or a commons. It starts as a single cold page written before the course
(v0, module m0) and ends as the capstone's input (v6, 3,000–4,000 words). Every module's
deliverable is a diff against the current version, so by the end the brief carries the whole
diagnostic path of the course: the group's boundary, the games it plays, who learns from whom,
the situational audit, the threshold map, the type mix, the equilibrium-selection plan, the norm
register, the institutional checklist, the network map, the public signal, and three registers
(hypotheses, values, measurement).

Section ids s1–s14, their titles and their order are fixed by `synthesis/learning-design.md`
(section 4c) and must not be renumbered. For each section this guide gives: the purpose, the
tension it governs, the default tag, three to five drafting prompts, and what a good entry looks
like. The last part of the file is one fully worked brief for a hypothetical group, "Lanternfish",
a 40-person open-source library with a maintainer-burnout and drive-by-pull-request problem. The
example shows form and tagging discipline; it is not a recommended design for any real project,
and its numbers are the hypothetical's own data, not evidence.

Where this guide and `synthesis/claims-ledger.md` section 5 disagree, the ledger wins. Where it
cites "law N", it means the twelve laws of cooperation in `synthesis/unified-model.md` section 6.
Where it cites `gaps-primer §N`, it means `synthesis/gaps-primer.md`.

---

## Rules that apply to the whole brief

1. **Tag every declarative sentence** in the mechanism sections (s2–s11). An untagged sentence is
   a rubric failure, not a style choice. The tags are the course's: [E] supported by evidence;
   [H] hypothesis to test in your group; [V] value commitment.
2. **[E] needs a source slug** (`01`…`11`, a chapter where possible, or `gaps-primer §N`) and,
   where the ledger marks the finding contested, the caveat in the same sentence. An [E] that is
   not a ledger [E] is a mis-tag.
3. **Split compound claims.** "Graduated sanctions keep rules alive, so our first sanction will be
   a private note" is two sentences: the mechanism [E: `09` ch 3] and the parameter for your
   group [H].
4. **Classification of your group is always [H].** The stag hunt and the prisoner's dilemma are
   theorems; "our review process is a stag hunt" is a hypothesis until the defection question has
   been answered with the group's own payoffs, and remains one after (ledger rule 13).
5. **Values are not weaker than evidence.** Never upgrade [V] to [E] because a source agrees with
   you; never write "fairness" as evidence rather than commitment (law 12). A [V] is a choice of
   X over Y that someone reasonable could reject.
6. **Numbers.** Quote only numbers in the ledger's section 4 or in `gaps-primer` marked verified,
   with their hedges; otherwise say small, moderate, roughly doubled. Your own group's data are
   always quotable and always labelled as yours.
7. **Never build on the failed-replication list** (ego depletion, behavioural priming, power
   posing, watching eyes, the Stanford Prison Experiment, groupthink as a syndrome, IAT-based
   training; ledger rule 20). Strike such levers through in s4 with the reason; do not delete
   them, the strike-through is the learning.
8. **Every [H] appears in s12; every [V] in s13; every s12 row has a measure in s14.** A tag with
   no register row is an orphan and fails the self-check.
9. **Later sections cite earlier ones by id and cite the laws by number.** "Because s2 classified
   this as a PD (law 1), s9 must supply sanctions and repetition, not assurance."
10. **The median case, not the showcase.** Narrate the group as it is on an ordinary week, not on
    the day the launch went well.
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

One changelog line per change, never a paragraph. "Motivated by" names the module and the source
that moved you, so the capstone can tell what you learned from what. Re-tags are the most
important lines: they are the evidence that your calibration improved.

---

## Version plan

| Version | After | What changes |
|---------|-------|--------------|
| v0 | m0 (cold challenge, 40 min) | One page: what the group should cooperate on and where it fails; why you think it fails; three changes; how you would know in three months. Then two passes: list the assumptions you could not defend to a sceptic; tag every decision [E]/[H]/[V] as best you can. Expect to do this badly. |
| v1 | m1–m2 | s3 (collective brain, models, single points of failure) and s4 (situational audit, struck-through failed levers) added. Most v0 "the people are the problem" lines get a situational alternative. |
| v2 | m3–m5 + retrieval R3 | s2 (games), s5 (thresholds), s6 (types and fairness) added. **Full re-tag checkpoint** of s2–s6: every classification becomes [H]; every "incentive fixes it" line is checked against the game shape. |
| v3 | m6–m7 | s7 (equilibrium selection) and s8 (norm register with the four-question measurement) added. First measured expectation must exist before v3 is saved. |
| v4 | m8–m9 | s9 (institutions, sanctions ladder, legitimacy) and s10 (network map, seeding) added. s1 revised now that boundary and subtractability are understood (s9 principle 1). |
| v5 | m10–m11 | s11 (signal, BPC, four layers) added; s12–s14 registers filled; v0 re-tagged line by line with a changelog. Capstone input. |
| v6 | Capstone sitting 1 | Every section filled; every claim tagged; no [E] that is not a ledger [E]; diagnostic path visible; the first ninety days (s14) has three dated predictions and an abandonment condition for the main hypothesis. |

---

## The sections

### s1. The group and its boundary: who is in, what is shared, subtractable or not — default [E/H]

**Purpose.** Name the group precisely enough that every later section has a referent. Say who is
a member, who is a user, who is an outsider; what the shared thing is; and whether one person's
use of it reduces another's (subtractable, a commons) or not (a public good, knowledge). The
tension governed: open versus closed layers. Ostrom's principle 1 says durable commons have clear
boundaries [E: `09` ch 3; Cox et al. 2010 review]; open-source, platforms and knowledge commons
are open by design at the outer layer. The mistake is to answer "open or closed" for the whole
group instead of layer by layer (the primer's scope caveat, `gaps-primer §6, §8`).

**Guidance.** Draw at least three concentric layers (core, regulars, periphery) and state the
boundary rule for each. Then list every shared resource and mark it subtractable or not; for most
teams and projects the truly subtractable resource is someone's attention. Give the size now and
the size in twelve months (`gaps-primer §8`). Write the group's actual, not stated, purpose.

**Prompts.**
1. Who would say "I am part of this", and who would the core say is part of it? Where do the two
   answers differ?
2. Which shared resources are used up by use (review time, moderator time, budget, a channel's
   signal-to-noise) and which are not (documentation, code, reputation of the group)?
3. What is the membership churn per quarter, and how many newcomers arrive per experienced member?
4. What is the group's purpose as revealed by what it actually spends its scarce resource on?
5. Which boundary is currently open that a later section will want to close, and vice versa?

**What good looks like.** Three layers with a rule each; a resource table with a subtractability
column; the group's size trajectory; the scarce resource named in one sentence; the layer-by-layer
answer to open versus closed tagged [H] where it is a design choice and [E] where it is a fact.

### s2. Diagnosis: the games being played — default [H]

**Purpose.** Draw the two or three central interactions before proposing anything (law 1). For
each: players, options, payoffs as the members see them, order, information; then the one agreed
test: does a member gain by defecting when everyone else cooperates? Yes is a dilemma (fix set:
payoffs, repetition, detection, sanctions); no is a stag hunt (fix set: assurance, correlation,
pledges) [E: `04` ch 4, 10; `07` ch 1; ledger rule 13]. The tension governed: assurance and talk
versus enforcement and commitment (t07). The founding mistake is prescribing a stag-hunt fix
(a pledge, a workshop) for a dilemma, or a dilemma fix (sanctions) for a stag hunt, where it
signals distrust and raises the cost of being the lone cooperator.

**Guidance.** Payoffs are the members' construals, not yours [E: `03` ch 1; construal]. For a
large population add Schelling's binary-choice diagram (s5 does the shape). Note that Nash is a
stability test, not a prediction; with several equilibria it predicts nothing [E: `04` ch 4;
ledger rule 14]. Check one sanction or signal already in use for credibility (would the enforcer
apply it at the moment of enforcement?) and separation (does its cost differ by type?) [E: `04`
ch 8, 9].

**Prompts.**
1. For each central interaction, what does the cooperator get when everyone else defects, and
   what does the defector get when everyone else cooperates?
2. Is the interaction repeated with the same people, and how fast is defection detected?
3. Which existing rule or threat would its enforcer actually carry out, and which is a bluff?
4. If you reclassified the main interaction from PD to stag hunt or the reverse, which of your v0
   fixes would you withdraw?
5. Is any "defector" actually a one-shot player with no shadow of the future, rather than a
   type?

**What good looks like.** A drawn matrix or two-curve sketch per interaction; the defection
question answered in one sentence each; the shape tagged [H]; the fix set that shape allows,
listed; at least one v0 fix marked "withdrawn: wrong shape".

### s3. The collective brain: who learns from whom; models; single points of failure — default [H]

**Purpose.** Map the group's actual learning network, which is never the org chart. Humans are
cultural learners who copy prestigious and successful models more than they follow explanations
[E: `01` ch 3–5, 8]; norm adherence spreads through models, prestige and expectations, whereas
skills with hidden structure need explicit teaching [E: `02` ch 8; Morgan et al. 2015, one
study, N = 184; ledger rule 8]. The tension governed: copying versus teaching (t01). The founding
mistake is "just document it" for a norm, or "just model it" for a skill.

**Guidance.** Name the single points of failure for critical skills; the visibly successful and
prestigious members and whether they model the target behaviour; and one place where a leader's
costly actions contradict the stated norm (credibility-enhancing displays cut both ways [E: `01`
ch 8]). Do not state the population-size collective-brain effect as [E]; say connectivity of the
learning network, lab-demonstrated and archaeologically contested (ledger rule 6). Populations of
pure copiers stagnate: say who is paid to innovate [E: `02` ch 3, simulation; ledger rule 39].

**Prompts.**
1. When someone new needs to learn how things are done here, whom do they watch, and whom do
   they ask?
2. Which critical process lives in one head, and what happens in three months if that head leaves?
3. Which prestigious member visibly does the opposite of the stated norm, and what do others copy?
4. Which of your target behaviours is a norm (spread by modelling) and which a skill with hidden
   structure (needs teaching)?
5. Who is allowed to try something different, and is that tolerated or punished?

**What good looks like.** A learning-network sketch distinct from the org chart; a single-point-
of-failure list; a prestige list with a "models the target?" column; the copy-versus-teach split
per target behaviour; one prediction: a behaviour that changes within three months if one
prestigious member adopts it, and one that will not change however well it is explained.

### s4. Situational audit and folk-psychology check — default [E/H]

**Purpose.** For every failure named in v0, write the situational alternative to the dispositional
story: workload, ambiguity, visibility, ownership, deliberation design [E: `03` ch 1, 5, 12; the
fundamental attribution error; social loafing under low identifiability]. The tension governed:
individual dispositions versus structure (t14). The founding mistake is "the people are the
problem", followed closely by a lever from the failed-replication list.

**Guidance.** Record the current descriptive and injunctive signals for each target behaviour and
whether they agree; never advertise low adoption [E: `03` ch 9; Schultz et al. 2007 boomerang;
ledger rule 24; law 5]. Strike through every v0 lever on ledger rule 20's list with the reason.
Stereotype threat may be quoted only as small after correction (ledger rule 21); Milgram's lesson
is exits, peers and legitimacy of refusal (ledger rule 22); bystander effects hold only in
ambiguous, low-risk settings (ledger rule 23). Working-unit size of 2–5 to limit loafing is a rule
of thumb, tag [H] (ledger section 4).

**Prompts.**
1. For each "they don't care" line in v0, what would the same behaviour look like from someone
   who cared but faced this workload, this ambiguity, this visibility?
2. What does a member see and hear that tells them what most people here do (descriptive) and
   what is approved (injunctive)? Do the two signals point the same way?
3. Which v0 lever rests on a finding from the failed-replication list?
4. Where is effort unidentifiable, and what one change would make it identifiable?
5. Which decisions are made after the two most senior have spoken, and what would a speaking
   order change?

**What good looks like.** A two-column table (dispositional story, situational alternative) per
failure; a signal audit with an "agree?" column; struck-through levers with reasons; one
structural change predicted to move the metric by a size given in words (small, moderate).

### s5. Threshold and tipping map; minimum viable coalition; arithmetic constraints — default [H]

**Purpose.** Decide whether the target behaviour is contingent (people do it when enough others
do) and, if so, where the group sits relative to the crossing. Schelling's binary-choice curves
show how mild individual contingency produces stable low and high states with an unstable tipping
point between them [E: `05` ch 3, 7; `10` ch 17]; the tipping point is a property of the threshold
distribution, and the scarce resource is low-threshold actors, never "influencers" (ledger rule
18). The tension governed: risk dominance versus payoff dominance in population form (t04). The
founding mistake is ignoring arithmetic: mentors per mentee, reviewers per review, hours per week.

**Guidance.** Sketch the two curves for the key behaviour; mark the current state as below or
above the crossing; estimate the minimum viable coalition k for a pilot as a hypothesis. Name one
accounting identity the v0 plan ignored [E: `05` ch 2]. Distinguish a norm that is self-enforcing
(a convention: nobody gains by deviating alone) from one that needs a rule. Sorting can arise from
mild preferences plus interdependence, and homogeneity is weak evidence of intolerance; the
model does not show preferences are the real cause (ledger rule 17).

**Prompts.**
1. If a third of the group did the target behaviour, would you do it? If two-thirds? Where is your
   own threshold, and whose is lower?
2. What is the arithmetic? Units of work per week divided by people willing and able to do it.
3. Which sub-group's current state is above the crossing (self-sustaining) and which below?
4. What is the smallest coalition that could run a pilot where the game is the same as at scale?
5. Which of your norms would survive if everyone stopped watching (convention) and which would
   collapse (needs a rule)?

**What good looks like.** A two-curve sketch with the group's position; a k estimate tagged [H]
with the reasoning; one arithmetic constraint stated as an identity; the convention-versus-rule
split; a prediction of what happens if the coalition falls one member short.

### s6. Population of types and fairness baseline; weak-link processes — default [H]

**Purpose.** State the group's likely mix of types in words, what conditional cooperators can
currently see of others' contributions, and the group's own fairness reference point for the
allocations that matter. Lab populations are roughly a third self-interested, about half
conditional cooperators, with a small altruist tail (Camerer's summary, background; ledger
section 4) [E as a direction, not a field estimate]; fairness and generosity are cue- and
expectation-dependent with a distribution of sensitivities, not a fixed taste (ledger rule 9).
The tension governed: stable social preferences versus cued norm compliance (t05), and
mis-specified preferences versus unstable beliefs (t11). The founding mistake is explaining a
failure by selfishness when it is strategic uncertainty among conditional cooperators.

**Guidance.** Identify any weak-link process, where the worst performer sets the outcome, and its
group size: pairs reach the best equilibrium, groups of 14–16 collapsed within about ten rounds in
the baseline game [E: `06` ch 7; Van Huyck et al. 1990]. Say which of the three amendments to
self-interest best explains the main v0 failure: social preferences, limited reasoning, or
learning and history. Positive reciprocity to gifts is weak and decays; negative reciprocity to
cuts and broken promises is strong (ledger rule 28). Quote ultimatum and dictator figures only as
the ledger gives them, with the double-blind caveat (rules 25, 26).

**Prompts.**
1. Of the members who currently under-contribute, how many would contribute if they could see
   others doing so? What do they see now?
2. What allocation do members compare (credit, pay, review load, visibility), and against whom?
3. Which process in the group aggregates by the minimum, and how many people are in it?
4. Which amendment explains the failure: people want something other than payoff, people reason
   one step, or early rounds locked in a bad pattern?
5. What would members read as a broken promise, and has one occurred?

**What good looks like.** A type-mix estimate in words with the visibility gap; the fairness
reference point named with the comparison group; weak-link processes with sizes; the amendment
chosen and defended; a prediction of what happens to contributions when others' contributions
become visible.

### s7. Equilibrium selection plan: regime, correlation device, pacing, lone-cooperator cost — default [H]

**Purpose.** For the group's main stag-hunt interaction, plan how to reach the payoff-dominant
state. Risk dominance wins under random mixing, best-response updating, large groups and no
communication; payoff dominance is reachable through correlation: small stable groups,
success-visible imitation, public pledges, gradual growth from a core, a lower cost of being the
lone cooperator [E: `07` ch 1, 3; `06` ch 7; Weber 2006, single lab lineage; ledger rule 2].
Sweetening the joint payoff is the weakest lever (law 3). The tension governed: t04. The founding
mistake is a big-bang rollout to a randomly mixed audience with a bonus attached.

**Guidance.** State the current regime (near-random mixing with frequent re-evaluation, or stable
subgroups with visible success). Give a watershed estimate in words. Choose the cheapest
correlation device: location (stable units), signal (a public rule or rota), or partner choice.
Local interaction helps only under success-copying; under conformist copying, clusters converge
on the majority whatever it is (ledger rule 3, 36). Write the pacing rule: grow from a core that
already coordinates, with visible history. Cheap talk roughly doubles lab cooperation and decays
without sanctions or repetition where defection dominates (ledger rule 12; law 6).

**Prompts.**
1. Who interacts with whom, and how often does that change? Is success visible when it happens?
2. What is the cheapest way to make cooperators meet cooperators more than chance?
3. What does the lone cooperator lose today, and what single change halves that loss?
4. What is the rollout order, from which core, at what rate per period?
5. What will a public pledge do here, and how long will it last if the interaction is really a PD?

**What good looks like.** Regime named; watershed in words; correlation device chosen and costed;
lone-cooperator loss and its reduction stated concretely; a pacing rule with a rate; a dated
prediction for the pledge's decay.

### s8. Norm register: taxonomy, expectation measurement, cues, trendsetters — default [E for method, H for results]

**Purpose.** Classify each important "norm" by the expectations that sustain it and measure them.
Bicchieri's four-way taxonomy: descriptive norm (I do it because others do), convention (nobody
gains by deviating alone), social norm (conditional on empirical and normative expectations,
can exist while widely violated), moral norm (unconditional) [E: `08` ch 1; ledger rule 11].
Assume every norm is conditional until it survives a collapse of expectations (ledger rule 10).
The tension governed: broadcasting the majority versus building normative expectations (t10).
The founding mistake is a values campaign aimed at a pluralistic-ignorance problem, or a "most
people do it" message in a group where nobody does (`gaps-primer §1`).

**Guidance.** Run the four-question battery per behaviour in the reference network, not the org
chart: what do you do; what do most of them do; what do most of them think you should do; what
happens to someone who does not; plus one sanction item [E: `gaps-primer §1`; Bicchieri, *Norms in
the Wild*]. Empirical expectations tend to dominate normative ones when they conflict [E: Bicchieri
& Xiao 2009, lab]. Use vignettes for sensitive behaviours and a Krupka–Weber coordination question
where confession is unlikely [E as method; H that the unpaid version keeps its properties]. Measure
the perceived-versus-actual gap, not just the level [E: Tankard & Paluck 2016]. Record the cue set
(templates, openers, bots) that summons the script, tagged [H] for any specific cue-to-norm
mapping (ledger rule 37). Name trendsetters by nomination, not seniority [E: Paluck et al. 2016,
school scale; H in an organisation].

**Register format (N-nn rows).**

| Id | Behaviour | Kind (descriptive / convention / social / moral) | Empirical expectation (measured) | Normative expectation (measured) | Sanction expectation | Perceived–actual gap | Current descriptive signal | Current injunctive signal | Cues | Trendsetters | Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Prompts.**
1. For each norm: what do most members do, what do they think others do, what do they think others
   expect, and what happens to a deviator? Where does the pattern show pluralistic ignorance?
2. Whose opinion would a member actually notice on this? That is the reference network.
3. What template, opener, label or bot message activates the norm at the moment of action?
4. Which norm collapses if one visible member deviates, and which does not?
5. Who do members nominate as the person whose behaviour they notice?

**What good looks like.** Three rows minimum; each classified; at least one expectation measured
before v3 is saved; the gap direction stated; cues listed; a prediction of which norm collapses on
a visible deviation.

### s9. Institutional design: eight-principle checklist, sanctions ladder, monitoring, forum, standing, backstop — default [H/V]

**Purpose.** Run Ostrom's eight principles as a diagnostic checklist, not a recipe: boundaries,
congruence of rules with local conditions, collective-choice arrangements, monitoring, graduated
sanctions, conflict-resolution mechanisms, recognition of the right to organise, nested enterprises
[E: `09` ch 3; Cox et al. 2010, 91 studies, with publication-bias and structure-not-process
caveats; ledger rule 29]. Flag scope when applying to a digital or knowledge commons. The
tension governed: designed rules versus self-governed rules (t06), and explicit incentives versus
norm-based motivation (t12). The founding mistake is a rule announced by the wrong person, with a
first sanction so severe nobody applies it.

**Guidance.** First sanctions are small and graduated; monitoring is a by-product of use [E: `09`
ch 3; ledger rule 30; law 9]. Write the ladder with the trigger for each rung (private note, public
note, temporary loss of a privilege, removal) [E for the pyramid: `gaps-primer §2`; H for your
ladder]. Anti-social punishment is real and predictable: measure or pilot before opening a peer
sanction channel [E: Herrmann et al. 2008]. Fines can turn a norm into a price [E: Gneezy &
Rustichini 2000; H whether it happens here]. Legitimacy: elected sanctioners outperform appointed
ones with identical powers [E: Baldassarri & Grossman 2011; `gaps-primer §3`]; rules members made
are followed more [E: `09` principle 3]. State the legitimacy source of every rule and the four
procedural-justice components (voice, neutrality, respect, trustworthy motives). Name which rule
level the fix lives at (operational, collective-choice, constitutional) and who has standing to
change it [E: `09` ch 2]. Name the recognised external backstop. Any reputation signal: say what
it predicts, how it can be gamed, and what identity re-entry costs (`gaps-primer §4`).

**Prompts.**
1. For each principle: present, absent, or not applicable here, with a scope note?
2. Who can sanction whom, at what cost to themselves, and what stops a sanction being used to
   settle a score? What is the appeal?
3. What is the first, smallest sanction, and how many people climbed each rung last quarter?
4. Who decided the current rules, and can members show where their input changed them?
5. Which fix in v0 was an operational rule, and who has standing to change it?

**What good looks like.** The checklist with eight rows and scope notes; a ladder with triggers;
the by-product monitoring channel named; the dispute forum and appeal path; the legitimacy source
per rule; the backstop; the first cheap change that produces both information and standing, with
what it will reveal in three months.

### s10. Network map and seeding plan: clusters, bridges, q, seed set, copying kind — default [H]

**Purpose.** Sketch clusters and bridges, estimate the adoption threshold q for the target
behaviour, and place the seed set. A node adopts when at least a fraction q = b/(a+b) of its
neighbours have; a cluster of density above 1 − q blocks a cascade entering from outside and
protects one adopted inside [E: `10` ch 19, theorem; ledger rule 3]. Information crosses one weak
tie (simple contagion); costly behaviour needs several adopting neighbours and wide bridges
(complex contagion) [E: `10` ch 19; ledger rule 34]. The tension governed: closure and homophily
versus bridges and diversity (t09). The founding mistake is announcing a costly norm across weak
ties and expecting adoption.

**Guidance.** Quote the structural weak-tie claim (bridges tend to be weak), not "useful
information comes from weak ties" (ledger rule 33). Assume selection over influence for any
observed similarity unless longitudinal data say otherwise (ledger rule 35). Name which copying
kind currently produces convergence and its fix: informational cascade (collect private signals
first), network effect (cross the tipping point), coordination on a graph (lower q or seed inside
clusters) (ledger rule 19). Seed inside clusters and grow slowly (law 8).

**Prompts.**
1. Which sub-groups talk mostly to themselves, and who holds the ties between them? How many
   parallel ties?
2. How many adopting neighbours would a typical member need before adopting the target behaviour?
3. Which cluster will block the norm, and which will protect it once adopted?
4. Is the current convergence a cascade, a network effect, or coordination on a graph?
5. Where do you seed, and which sub-group adopts first?

**What good looks like.** A drawn map with clusters, bridges and their holders; q estimated with
the reasoning; the blocking cluster named; the seed set placed inside a cluster; the copying kind
identified and its fix chosen; a prediction of which sub-group never adopts through current
bridges.

### s11. The signal and the BPC statement; the four layers addressed — default [H]

**Purpose.** Name the public signal for each central coordination problem and check it is visible
across the network. Nash equilibrium is a social achievement, not a rational deduction: aligned
conjectures come from a public signal, a choreographer [E: `11` ch 7; Aumann & Brandenburger
1995, theorem; ledger rule 31]. Run the two-part norm test on the main norm: epistemic (can
everyone say what it requires of them and others) and motivational (does anyone gain by
deviating given others comply, and is there a cheap sanction). Write one BPC line: what members
believe about each other, what they value including status and fairness, what constrains them.
Then say which of the four layers the v0 fix addressed and which it ignored: stability test,
selection absent intervention, the public signal, the expectations inside agents (ledger rule 1).
The tension governed: rational equilibrium versus norm-choreographed order (t03). The founding
mistake is a vague value in place of a specific signal (law 11).

**Prompts.**
1. What is the one public thing everyone can see that tells them what to do and what others will
   do? Who cannot see it?
2. Can a newcomer state what the norm requires of them and of others in one sentence?
3. Who gains by deviating while others comply, and what cheap sanction meets them?
4. Which layer did your v0 fix touch, and which did it skip?
5. Which layer, addressed alone, would move behaviour here, and which does nothing without the
   others?

**What good looks like.** A signal per coordination problem with its visibility; the two-part test
result written as pass/fail with the failing half named; a one-line BPC statement; a four-layer
audit of v0; a prediction per layer.

### s12. Open hypotheses register — default [H]

**Purpose.** Every [H] in s1–s11 gets a row. The register is the brief's experimental design;
without it, hypotheses are opinions with a label.

**Format.**

| Id | Hypothesis | Section | Why H not E | Test | Prediction | Practical measure | Balancing measure | Decision rule | Review date | Status |
|---|---|---|---|---|---|---|---|---|---|---|

"Why H not E" must name the missing step (a lab result not yet observed here; a classification
not yet checked against the group's payoffs; a parameter the sources leave open). "Decision rule"
states what result keeps, revises or abandons the hypothesis.

**Prompts.**
1. What would I see in ninety days if this is true, and what if false?
2. What cheap observation moves this from H toward E for this group, or kills it?
3. What harm would the same intervention cause if the hypothesis is wrong, and how would I see it?

**What good looks like.** Every column filled; no row without a balancing measure; no two rows
that are the same hypothesis in different words; statuses updated each version.

### s13. Value commitments register — default [V]

**Purpose.** Every [V] gets a row of the form "We choose X over Y". A value with no reasonable
dissenter is a platitude; a value with no cost is a description. The primer's ethics section
supplies the tests: is the intervention reflective or automatic, disclosed or not; who consented;
who bears the cost when it misfires; what is the exit (`gaps-primer §10`).

**Format.**

| Id | Commitment ("We choose X over Y") | Section | Who reasonably disagrees, and their best argument | Cost | Evidence that informs it (does not settle it) | Conflicts with | Owner and review |
|---|---|---|---|---|---|---|---|

**Prompts.**
1. What are we optimising for, and what are we knowingly giving up?
2. Who in the group would object, and what is the strongest version of their objection?
3. Which interventions in the brief sit in the automatic-and-undisclosed quadrant, and do we
   accept that?
4. Who can change this rule, and who can leave at what cost?

**What good looks like.** Four to eight rows; each with a named dissenter and a cost; no row that
restates evidence; the conflicts column non-empty for at least two rows.

### s14. Measurement plan and ninety-day predictions — default [H]

**Purpose.** Convert the registers into a plan with three kinds of measure for every hypothesis
and intervention: the **practical measure** (the behaviour or expectation you expect to move, from
logs or the four-question battery), the **predicted value** (a direction and a size in words, or a
number from your own baseline, with a date), and the **balancing measure** (what would show harm:
newcomer rejection, reviewer churn, anti-social sanctioning, the boomerang, load shifting onto the
already loaded). Surveys measure beliefs; logs measure behaviour; report both, because the
mismatch is diagnostic (`gaps-primer §1`, point 9). Re-measure and revise: behaviour and
expectations both moved, scale gradually; behaviour moved without expectations, the change rides
on observation and will decay; expectations moved without behaviour, the game is unstable at layer
one, return to s2 (`unified-model` section 4, station 5).

**Format.**

| Intervention or hypothesis (id) | Practical measure | Baseline (own data, date) | Predicted at day 90 | Balancing measure | Harm threshold | Abandon if | Owner | Cadence |
|---|---|---|---|---|---|---|---|---|

**Prompts.**
1. What is the first cheap change that produces both information and standing?
2. For each intervention, what is the number I expect on day 90, and what number makes me stop?
3. What could go up that I would not want, and am I logging it?
4. Which measure could be gamed by the intervention itself (a score that rewards volume)?
5. When do I re-run the expectation battery?

**What good looks like.** Three dated predictions; a balancing measure per intervention; an
abandonment condition for the main hypothesis; the re-measurement date; no measure that the
intervention can satisfy without the behaviour changing.

---

## Self-check before saving a new version

1. **Traceability.** Does every fix in s7–s11 cite the s2 classification and a law by number, and
   is the diagnosis written before the fix in every section?
2. **Tags.** Is any declarative sentence in s2–s11 untagged? Is any [E] missing a slug? Is any
   [E] a claim the ledger marks [H] (classification of your group; cultural group selection;
   evolved strong reciprocity; the population-size collective brain; any single social-preference
   model)?
3. **Caveats.** Does every contested finding carry its caveat in the same sentence (Ostrom's
   review; cheap-talk decay; local interaction only under success-copying; lab numbers as
   directions)?
4. **Registers.** Does every [H] have an s12 row with a balancing measure, every [V] an s13 row
   with a dissenter, every s12 row an s14 line?
5. **Median case.** Is the group described on an ordinary week, with its own data labelled as
   its own?
6. **Changelog.** Does every change name the module and source that motivated it, and does every
   re-tag show old and new?
7. **Failed levers.** Is anything on ledger rule 20's list still load-bearing rather than struck
   through?
8. **The missing decision.** Have you written who has standing to change the rules and what the
   public signal is? These are the two decisions learners skip most.

---

## Worked example: Lanternfish — Cooperation brief v6

*Context (the hypothetical's parameters, all invented).* Lanternfish is an open-source data-
validation library in Python, seven years old, used as a dependency by a moderate number of
commercial products. About 40 people have contributed in the last twelve months: three
maintainers with merge rights (Priya, the founder and lead; Tomasz; and Wen, who stepped back to
"emeritus" four months ago citing exhaustion); twelve regulars who have landed three or more
changes and answer issues; and about 25 occasional or first-time contributors. The project
receives about 30 pull requests a month, roughly half from first-time contributors; about a third
of those are abandoned after the first review round. Priya performs about 60% of all reviews and
merges. The median time to a first maintainer response is around three weeks. There is a code of
conduct enforced by Priya alone, a `CONTRIBUTING.md` nobody reads, and a Discord where the
regulars talk. The v0 fixes were: rewrite `CONTRIBUTING.md`; ask for review volunteers on
Discord; add a "good first issue" label. Numbers below are Lanternfish's own logs and surveys
unless a slug is given.

```
# Lanternfish — Cooperation brief v6
Date: 2026-09-30 · Previous version: v5 (2026-09-24) · Author: T. (regular contributor)
Changelog:
- [s2] Re-tagged: "review load is a tragedy of the commons" [E]→[H]; classification is a
  hypothesis about our payoffs. Motivated by m11 (ledger rule 13).
- [s4] Struck: "maintainer burnout is depleted willpower". Motivated by m2 (`03` evidence;
  ledger C11). Tag [E]→struck.
- [s9] Reversed: bounty for reviews removed; reputational credit substituted. Motivated by m8
  and gaps-primer §2 (Gneezy & Rustichini). Tag [E]→[H]. New H-07, V-04.
- [s9] Added: elected triage stewards replace Priya-appointed helpers. Motivated by gaps-primer
  §3 (Baldassarri & Grossman). New V-05, H-06.
- [s14] Added: first-PR 90-day return rate as balancing measure. Motivated by gaps-primer §6
  (Halfaker et al. 2013).
- [s12] Added: abandonment condition for H-01.
```

### s1. The group and its boundary

Three layers. Core: three maintainers with merge rights, boundary rule "invited by existing
maintainers" [E: fact of the repo]. Regulars: twelve people with three or more merged changes and
Discord membership; the boundary is informal and nobody can say who is in [E: own survey, eleven
of twelve regulars named a different list]. Periphery: anyone with a GitHub account can open a
pull request [E: fact]. Users: unknown number; a moderate share of issues come from employees of
companies that depend on the library [H: inferred from email domains, not verified].

Resources. The codebase and documentation are non-subtractable [E: public good by construction].
Maintainer review attention is subtractable and is the scarce resource: about 30 PRs a month at
roughly 45 minutes each is about 22 hours of review, against about 25 hours of total maintainer
time available, before any other work [E: own logs; the estimate of 45 minutes is a maintainer
self-report, H]. Issue triage time is subtractable and currently unowned [E: no assignee on 80%
of open issues, own data]. The project's reputation for reliability is non-subtractable but
depletable by a bad release [H].

Size trajectory: contributors flat at about 40 for two years; PR volume up about a third year on
year because a popular framework added Lanternfish as a default [E: own data]. Newcomers arrive
at roughly fifteen per month against three maintainers, a ratio no onboarding can absorb by
teaching [H: `gaps-primer §8` point 5 treats onboarding capacity as a constraint; the ratio is
ours].

Open versus closed, by layer. The periphery stays open: we choose an open PR door over a gated
one [V: V-02]. The regular layer gets a boundary because Ostrom's principle 1 predicts that a
layer with no boundary cannot carry obligations [E: `09` ch 3, with the digital-commons scope
caveat] and because the review rota in s7 needs a defined membership [H: H-02].

### s2. Diagnosis: the games being played

**Interaction A: opening pull requests against maintainer attention.** Players: contributors
(mostly one-shot) and maintainers. A first-time contributor pays nothing to open a PR and gains
a chance of a merge and a credit; the review cost falls entirely on maintainers [E: own logs;
`04` ch 11 on unpriced external costs]. Defection question: does a contributor gain by opening a
low-effort PR when everyone else opens careful ones? Yes: the queue is served roughly in order
and the review is free to them [H: H-01, classification]. Shape: an open-access dilemma on a
subtractable resource, Ostrom's open-access case, not a stag hunt [H: H-01; `09` ch 1; ledger
rule 13]. Fix set this shape allows: boundaries on what enters the queue, a price in effort
(not money) to enter, detection, graduated sanctions; assurance alone will not do it [E: fix set
follows from the shape, `04` ch 10, `09` ch 3; H that the shape is right]. Important amendment:
most "defectors" are one-shot players with no shadow of the future, not a type; the folk theorem
gives nothing here because there is no repetition [E: `04` ch 10; ledger rule 15]. So the lever
is entry structure, not reputation.

**Interaction B: regulars reviewing each other's and newcomers' PRs.** Players: the twelve
regulars. If four or more review regularly, each review is cheap (shared context, fast turnaround,
visible credit); if one reviews alone, that person becomes the next Priya [E: own experience of
Wen's exit; H that others see it this way]. Defection question: does a regular gain by not
reviewing when all others review? No: they lose standing and the queue they depend on slows; the
lone reviewer, however, loses badly [H: H-02]. Shape: a stag hunt with a high cost of being the
lone cooperator [H: H-02; `07` ch 1]. Fix set: assurance, correlation, a lower lone-cooperator
cost, pacing (s7); sanctions here would signal distrust [E: `07` ch 3; ledger rule 2]. Reclassifying
B from a dilemma (my v0 assumption, "people won't review because it's unrewarded") to a stag hunt
withdraws the v0 fix "reward reviewers" [H: H-02; the withdrawal is what the reclassification
implies].

**Interaction C: Priya merging her own PRs without review.** A single-player deviation from the
stated norm; not a game so much as a credibility problem, handled in s3 and s11 [H].

**Existing sanction checked.** The only sanction is closing a PR, applied inconsistently and
without explanation [E: own logs, 40% of closes have no comment]. Credibility: Priya does apply
it, but at unpredictable times, so it separates nobody: careful and careless contributors face the
same expected outcome [E: `04` ch 8 on separation; own data for the inconsistency].

### s3. The collective brain

Learning network. Newcomers learn conventions by reading recently merged PRs, not
`CONTRIBUTING.md` [E: own survey of eight recent contributors, seven cited merged PRs; H that
this generalises]. Regulars learn from Priya's review comments, which are the de facto style
guide [E: same survey]. So the models are whatever got merged last month, which includes Priya's
unreviewed merges [E: own logs].

Single points of failure. The release process (signing, changelog, the deprecation policy) lives
only in Priya's head; Wen knew it and left [E: fact]. This is a skill with hidden structure, so it
needs explicit teaching and a written runbook practised by someone else, not modelling [E: `02`
ch 8; Morgan et al. 2015, one study; ledger rule 8]. Review conventions, by contrast, are a norm
and spread through what people see merged; the v0 fix "rewrite CONTRIBUTING.md" targeted the
wrong channel for the norm and the right channel for the skill [H: H-03; ledger rule 8].

Prestige and credibility. Priya is the prestigious model; her most-copied behaviour is merging
without review, which contradicts the stated "two approvals" rule [E: own logs, roughly a quarter
of her merges have zero approvals]. Costly actions outweigh statements [E: `01` ch 8, CREDs; H
for the size of the effect here]. Tomasz is visibly successful and does wait for review; nobody
notices because his merges look like everyone else's [H].

Innovation budget. Nobody is licensed to try a different review workflow; the last person who
proposed one was told "that's not how we do it" on Discord [E: fact]. Pure copying stagnates
[E: `02` ch 3, simulation; ledger rule 39], so the rota pilot in s7 is also the licence to
experiment [V: V-06].

Prediction. If Priya visibly waits for review on her own PRs for a month, regulars' approval
rate on each other's PRs rises within three months [H: H-04]. The release runbook will not be
learned however well it is written until someone performs a release with it [H: H-03].

### s4. Situational audit and folk-psychology check

| v0 story (dispositional) | Situational alternative |
|---|---|
| "Drive-by contributors are lazy and don't read the guide." | The guide is not at the point of action; the PR template is empty; a newcomer cannot see the queue or the expected turnaround [E: fact; `03` ch 1 on attribution; H that fixing the situation changes the behaviour, H-05]. |
| "Regulars won't help because they don't care about the project." | Reviewing is unidentifiable: no reviewer credit appears anywhere; the lone reviewer inherits the queue [E: `03` ch 12, loafing under low identifiability; own data on credits]. |
| "Priya is burned out because she can't say no." | Priya is the only person with merge rights on the default branch, the only CoC enforcer and the only releaser: three unowned jobs collapsed into one person [E: fact; `gaps-primer §7` on stable membership and load]. |

Signal audit. Descriptive signal for "respond to PRs promptly": the queue itself, 90 PRs open,
some a year old, which advertises that nobody responds [E: fact; law 5 violation]. Injunctive
signal: `CONTRIBUTING.md` says maintainers "aim to respond within a week" [E: fact]. The signals
disagree; the descriptive one wins by default [E: `gaps-primer §1`, Bicchieri & Xiao 2009, lab].
The pinned Discord message "we're drowning in PRs, please help" advertises low adoption of
reviewing and is the boomerang case [E: ledger rule 24; own text].

Struck-through v0 levers.
- ~~Maintainer burnout is depleted willpower; schedule reviews in the morning.~~ Ego depletion
  failed a 23-lab registered replication, d = 0.04 [E: `03` evidence; ledger C11, rule 20].
- ~~Add a "you are being watched" review-count widget to nudge reviewers.~~ Watching-eyes effects
  are on the failed list [E: ledger rule 20]; a public count also advertises the low rate.
- ~~Implicit-bias training for reviewers who close newcomer PRs.~~ IAT-based training is on the
  failed list [E: ledger rule 20]; the close rate is a process problem (s9).

Structural change predicted. Making review effort identifiable (a monthly "reviewed by" credit in
the release notes) moves the share of non-Priya reviews by a moderate amount [H: H-06].

### s5. Threshold and tipping map

Target behaviour: a regular reviewing at least two PRs a week. Contingency: in the survey, nine of
twelve regulars said they would review "if I knew others were" [E: own survey]. Two-curve sketch:
the payoff to reviewing rises with the number of other reviewers (shared queue, fast merges,
reciprocated reviews) and is negative alone; the curves cross at about four reviewers, below
which the state decays to Priya-only [H: H-02, the crossing is estimated from the survey]. Current
state: below the crossing (one reviewer plus sporadic help) [E: own logs]. Low-threshold members:
Tomasz and two regulars who already review occasionally [E: own logs]. Minimum viable coalition
k = 4 for a rota pilot, with Priya not counted so the pilot is a test of the regulars' equilibrium
and not of her stamina [H: H-02].

Arithmetic constraint ignored in v0. Thirty PRs a month at 45 minutes is about 22 hours; four
reviewers at two PRs a week each cover about 32 PRs a month, so the rota is barely sufficient
and has no slack for abandoned PRs [E: own arithmetic; H that 45 minutes is the right unit]. v0's
"ask for volunteers" had no such number and therefore no way to know when it had succeeded.

Convention versus rule. Commit-message format is self-enforcing: nobody gains by deviating and CI
rejects deviations (a convention, `08` ch 1) [E: fact]. "Two approvals before merge" needs a rule
because the lead gains speed by deviating [E: own logs; H that a branch-protection rule is
accepted, H-04]. Sorting note: regulars have clustered on Discord and newcomers on GitHub without
anyone deciding it; assume selection, not influence, absent longitudinal data [E: ledger rule 35].

### s6. Population of types and fairness baseline

Type mix (in words). Among regulars, mostly conditional cooperators with one or two who review
regardless; the survey pattern (nine of twelve conditional) matches the lab direction of a
conditional-cooperator majority, quoted as direction only [E: `06` ch 2, ledger section 4 type
distribution as background; H for the mix here, H-02]. Among first-time contributors, "selfish" is
the wrong word: they are one-shot players, and their behaviour is fully explained by the game in
s2-A without any preference story [H: H-01; ledger rule 9 against fixed-taste stories].
Visibility gap: a regular cannot currently see that anyone else reviewed this week [E: fact].

Fairness reference point. Maintainers compare their unpaid load against the commercial users
who file issues from company addresses and never contribute; the felt violation is a broken
implicit promise, which is the strong negative-reciprocity case, not a missing gift [E: ledger
rule 28, Gneezy & List 2006 on weak positive reciprocity; H that this is the maintainers' actual
reference point, H-08]. The lab's 40% ultimatum reference is irrelevant to this allocation and is
not quoted as ours [E: ledger rule 25 on scope].

Weak-link process. Release readiness is a minimum-effort game across about eight people who own
modules; one unresponsive owner blocks the release [E: fact]. Groups of 14–16 collapsed in the
baseline lab game while pairs reached the top [E: `06` ch 7; Van Huyck et al. 1990]; eight is in
the uncertain middle, so the rule is to keep module ownership pairs, not committees [H: H-09].

Amendment chosen. The main v0 failure (no one reviews) is strategic uncertainty among conditional
cooperators, not selfishness and not limited reasoning; the history amendment also applies, since
Wen's exit locked in "reviewing is how you burn out" as the visible lesson [H: H-02; `06` ch 6 on
path-dependent learning as [E] for the mechanism].

Prediction. When weekly review counts by person become visible to regulars (not to the public),
regular-authored reviews rise by a moderate amount within six weeks [H: H-06].

### s7. Equilibrium selection plan

Regime now: near-random mixing (any regular may pick any PR, nobody does, no success is visible)
and frequent re-evaluation (each week each regular decides afresh) [E: fact; `07` ch 3 on why this
regime selects the risk-dominant state]. Watershed in words: we are well below the fraction of
reviewers needed for reviewing to be the safe choice [H: H-02].

Correlation device. The cheapest is a signal plus location: a labelled review queue with a named
rota, four regulars in pairs, each pair owning two weekdays [H: H-02]. Partner choice is second:
allow pairs to form by mutual nomination rather than assignment, since partner choice generates
structure at low cost [E: `07` ch 6, model; H here]. Money is the weakest lever and is rejected
(s9, V-04) [E: law 3].

Lone-cooperator cost. Today the lone reviewer inherits an unbounded queue. Reduction: each rota
member commits to two PRs per shift, not to the queue; anything beyond that is explicitly nobody's
job [H: H-02; V: V-01 sustainability over throughput]. This halves the felt loss for the first
mover by making the commitment bounded [H].

Pacing. Grow from a core that already coordinates: the pilot is Tomasz plus three low-threshold
regulars for six weeks with a visible history (a weekly one-line summary of reviews done);
add two regulars per month only after the pilot's own numbers hold [E: Weber 2006, gradual growth
with visible history, single lab lineage, `06` ch 7; H for the rate here, H-02].

Cheap talk. A public pledge round on Discord ("I'll take Tuesdays") should roughly double
short-run participation as in the lab and then decay unless the rota's repetition and visible
credit sustain it; in interaction A (a dilemma) a pledge would do nothing durable [E: ledger rule
12; law 6; H for duration here, H-02].

### s8. Norm register

Reference network: eleven regulars and two maintainers answered; the four-question battery was
run as a short form with one vignette (a reviewer approving an unread PR from a senior author)
[E: method, `gaps-primer §1`; `08` ch 1]. Krupka–Weber framing was used for the normative item
("what would most Lanternfish regulars say is appropriate?") without payment [H: that the unpaid
version keeps its properties, H-10].

| Id | Behaviour | Kind | Empirical expectation | Normative expectation | Sanction expectation | Gap | Descriptive signal | Injunctive signal | Cues | Trendsetters | Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| N-01 | Two approvals before merge | Social norm, widely violated by the lead | "Most merges have two approvals": 4 of 13 believe it; actual: about 55% [E: logs] | 12 of 13 think others expect it | "Nothing happens" (13 of 13) | Perceived below actual for regulars; the lead's deviations are what people see | Priya's merges | CONTRIBUTING.md | Branch-protection rule, PR template checkbox | Priya (by nomination, 11 of 13) | [H: H-04 that making the lead's compliance visible restores the expectation] |
| N-02 | First response to a PR within seven days | Aspiration only: no descriptive norm exists (actual median about three weeks) | 0 of 13 believe others do it | 10 of 13 think it should be done | None | Perception matches reality; not pluralistic ignorance, a dead rule | The 90-PR queue | CONTRIBUTING.md line | Queue label "needs first response", rota bot | Tomasz | [H: H-05; must not be advertised as a norm until the rota makes it true, law 5] |
| N-03 | Open an issue before a PR | Convention among regulars, unknown to newcomers | Regulars: 9 of 11 believe others do it; newcomers: no data | Weak (5 of 13) | None | Regular–newcomer split: a boundary problem, not an expectation problem | Merged PRs with linked issues | None | PR template first line | none nominated | [H: H-05 that a template cue moves newcomer compliance; cue-to-norm mapping is H, ledger rule 37] |

Pluralistic-ignorance reading. N-01 is the classic case: regulars privately hold the norm and
believe others hold it but see the lead violate it, so they infer the norm is dead [E: `08` ch 5
mechanism; H for the diagnosis here, H-04]. N-02 is not pluralistic ignorance; it is a rule with
no empirical support, and a campaign saying "we respond in seven days" would be advertising a
falsehood [E: law 5; ledger rule 24].

Prediction. N-01 collapses further if Priya self-merges a large PR during the pilot; N-03 does
not collapse on any single deviation because it is a convention with CI-like cues [H: H-04,
H-05].

### s9. Institutional design

Eight-principle checklist, scope: a knowledge commons with an open outer layer; principles
applied to the review-attention commons, not to the code [E: ledger rule 29 scope flag].

| Principle | Status | Note |
|---|---|---|
| 1 Boundaries | Absent for the regular layer; present for core | Define "regular" as three merged changes in twelve months plus opt-in to the rota roster [H: H-02]. Periphery stays open [V: V-02]. |
| 2 Congruence | Absent | No rule matches PR size to reviewer time; a 2,000-line PR and a typo fix enter the same queue [E: fact]. Add a size label and a "large PRs need an issue and a design note first" rule [H: H-05]. |
| 3 Collective choice | Absent | Priya decides alone. Rota rules to be set and changed by rota members in a monthly thread [E: `09` principle 3; Fiesler et al. 2018 on self-made rules, `gaps-primer §3`; V: V-05]. |
| 4 Monitoring | Present as by-product | CI, the PR dashboard and the weekly summary monitor without a monitor [E: `09` ch 3; law 9]. |
| 5 Graduated sanctions | Absent | Currently close-or-nothing. Ladder below [H: H-07]. |
| 6 Conflict resolution | Absent | Add a named steward pair for disputes with a public appeal thread; explanations attached to every close [E: Jhaver et al. 2019, observational, `gaps-primer §2`; H here]. |
| 7 Recognition | Partial | Priya's employer allows her a day a week; the foundation hosting the project recognises maintainers but has never been asked to recognise a rota [E: fact]. Ask for written recognition of the rota's authority over the queue [H: H-11]. |
| 8 Nesting | Not applicable at 40 | Revisit if regulars exceed about 25 [H: threshold is ours, `gaps-primer §8` on Dunbar's number as contested]. |

Sanctions ladder for interaction A (contributors) [E for graduated sanctions: `09` ch 3; the
pyramid, `gaps-primer §2`; H for the rungs: H-07].
1. Automatic: a PR without a linked issue or completed template gets a bot comment explaining
   what is missing and a "needs info" label; nothing is closed [E: Matias 2019 on rules at the
   point of action, `gaps-primer §6`; H for effect here].
2. After fourteen days of silence: a "stale" label and a second explained comment.
3. After thirty days: closed with an explanation and an explicit "reopen any time" line.
4. Repeated bad-faith PRs (spam, generated slop): temporary block by the steward pair, with an
   appeal thread [V: V-03 explained sanctions over quiet closes].
No rung is monetary: a bounty or a fine would tell contributors the norm is purchasable [E:
Gneezy & Rustichini 2000, `gaps-primer §2`; H that crowding-out would occur here, H-07; V: V-04].

Sanctions for interaction B (regulars): none. A stag hunt needs assurance, not punishment; a
missed shift is handled by the pair, not the project [E: ledger rule 2; H that this holds here].
Anti-social punishment risk is why there is no peer down-vote or "unhelpful reviewer" flag
[E: Herrmann et al. 2008, cross-societal; H for our position on that distribution].

Legitimacy. The two steward roles are elected by the regulars for six months, not appointed by
Priya, because election raised cooperation beyond appointment with identical powers [E:
Baldassarri & Grossman 2011; H for transfer to a project, H-06; V: V-05]. Procedural justice:
voice (monthly rules thread), neutrality (the ladder is public and the bot applies rung 1 to
everyone including maintainers), respect (a tone standard for close messages), trustworthy motives
(Priya's own PRs go through the same queue) [E: `gaps-primer §3` for the four components; H for
their weight here].

Rule levels and standing. The v0 fix "rewrite CONTRIBUTING.md" was an operational rule that
nobody had standing to enforce. The rota rules are operational; who may change them is the
collective-choice rule (rota members plus one maintainer); the constitutional backstop is the
foundation's code-of-conduct committee, which is the recognised external forum for interpersonal
disputes [E: `09` ch 2 on rule levels; fact for the committee].

Reputation. The only reputation signal is the contributor graph, which rewards volume and
predicts nothing about review quality [E: `gaps-primer §4` on aggregate scores losing predictive
power; own data]. We add one narrow signal (reviews completed per release, listed in release
notes) and no score [H: H-06]. Identity re-entry is cheap on GitHub, so nothing in the ladder
depends on reputation memory for newcomers; the ladder is per-PR, not per-person, until rung 4
[E: `gaps-primer §4` on whitewashing; H for the design].

First cheap change producing information and standing: the bot at rung 1 plus the elected
stewards. It reveals within three months how many first-time PRs are missing information versus
missing effort, and it creates a role that can legitimately close [H: H-07].

### s10. Network map and seeding plan

Clusters. Three: the maintainer–regular cluster on Discord (dense, about 15 people); the
issue-answering cluster on GitHub Discussions (about 8, overlapping the regulars by 3); and the
periphery, unconnected to each other [E: own map from Discord and GitHub activity]. Bridges: one
regular, Sam, is the only person active in all three; the tie is weak in the structural sense and
is the sole bridge, as the theory predicts bridges tend to be [E: `10` ch 3; ledger rule 33; fact
for Sam].

Homophily. The Discord cluster is mostly people in European time zones; assume selection (they
joined because they were already awake together), not influence [E: ledger rule 35].

Threshold q for "review two PRs a week". It is costly behaviour, so it is a complex contagion:
a regular needs to see at least two of their close ties doing it before adopting; we estimate
q around one-third [H: H-02; `10` ch 19 for the mechanism]. The Discord cluster is dense enough
to block the norm arriving from outside and to protect it once adopted inside [E: cluster-blocking
theorem, `10` ch 19]. Seed inside that cluster: the four-person pilot are all Discord regulars
[H: H-02; law 8]. The issue-answering cluster will not adopt through Sam's single tie; it needs a
second bridge, so one pilot member comes from the overlap of the two clusters [H: H-12].

Copying kind. Convergence on "nobody reviews" is conformist transmission (copy the majority),
which is why clusters have not helped; the fix is success visibility, the weekly summary naming
who reviewed and what merged faster because of it, so that copying the successful takes over
[E: ledger rule 3, 36; H here, H-06]. It is not an informational cascade: nobody has private
information about reviewing being bad [H].

Prediction. The Discord regulars adopt first; the issue-answering cluster does not adopt through
current bridges within ninety days unless the second bridge is in the pilot [H: H-12].

### s11. The signal and the BPC statement

Public signals. For interaction B the signal is the rota page: who reviews when, visible to all
regulars, updated weekly [H: H-02]. Today there is no signal: "please help" is not a
choreographer, because it tells nobody what to do or what others will do [E: `11` ch 7 on the
norm as correlating device; law 11]. For interaction A the signal is the PR template plus the bot
comment at the moment of action [E: Matias 2019, `gaps-primer §6`; H here, H-05]. Visibility gap:
the periphery cannot see the rota; that is acceptable because they are not players in B [H].

Two-part test on N-01 (two approvals before merge). Epistemic: fails today; newcomers cannot say
what an approval requires, and regulars disagree on whether a maintainer's self-approval counts
[E: survey]. Motivational: fails; the lead gains speed by deviating and no cheap sanction exists
[E: logs]. Fix: a one-paragraph review checklist (epistemic) and branch protection that applies to
maintainers (motivational, a rule rather than a sanction) [H: H-04].

BPC line. Beliefs: regulars believe others will not review and that reviewing leads to burnout;
preferences: they value the project's reputation and their own standing among regulars more than
speed; constraints: bounded free time, no merge rights, a queue they cannot filter [H: H-02; the
BPC frame is bookkeeping, not explanation, ledger X16].

Four-layer audit of v0. The v0 fixes touched layer three only (a document as a signal, and a
weak one). Layer one (is reviewing an equilibrium of the game as structured?) was never asked;
layer two (where does the group drift with random mixing?) was ignored; layer four (what do
regulars expect of each other?) was unmeasured [E: ledger rule 1 for the layers; H for the
audit]. Prediction: layer two alone (the rota as correlation device) moves behaviour for the
pilot; layer three alone (a better document) does nothing; layer four alone (publishing that
twelve of thirteen expect two approvals) moves N-01 only if the lead's compliance is visible at
the same time [H: H-02, H-04].

### s12. Open hypotheses register

| Id | Hypothesis | Section | Why H not E | Test | Prediction | Practical measure | Balancing measure | Decision rule | Review date | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| H-01 | Interaction A is an open-access dilemma; entry structure, not reputation, is the lever | s2, s6 | Classification of our payoffs; one-shot players unverified | Bot at rung 1 for 60 days; count PRs that complete the template vs abandon | Abandonment falls from about a third to well under a fifth; complete-template PRs get a first response inside 7 days | Share of PRs abandoned after first review round | First-PR contributors' 90-day return rate; share of good-faith PRs closed at rung 3 | Keep if abandonment falls and return rate holds; abandon H-01 (and the ladder) if good-faith closes exceed one in ten | 2026-12-01 | Open |
| H-02 | Interaction B is a stag hunt; a bounded rota of four inside the Discord cluster reaches the high state | s2, s5, s7, s10 | Payoffs self-reported; k estimated from survey; Weber 2006 is one lab lineage | Six-week pilot with visible weekly history | Regular-authored reviews rise from about 15% to over 40% of reviews; Priya's share below 40% | Reviews by author per week (logs) | Reviewer self-reported load (monthly one-item survey); rota churn | Keep if both measures hold for 6 weeks; revise k if fewer than 3 shifts filled; abandon if any rota member reports load above their prior | 2026-11-15 | Open |
| H-03 | Release process is a hidden-structure skill: runbook plus a supervised release transfers it; a runbook alone does not | s3 | Morgan et al. 2015 is one study of stone tools | Tomasz performs release with runbook and Priya observing; then alone | Second solo release succeeds without Priya | Releases performed by non-lead | Release defects per release | Keep if two solo releases ship; else rewrite runbook and repeat | 2026-12-15 | Open |
| H-04 | Visible lead compliance with N-01 restores regulars' expectation and approval rate | s3, s8, s11 | CRED effect size unknown here; expectation measured once | Branch protection applied to maintainers; re-run N-01 battery at day 60 | Belief "most merges have two approvals" from 4 of 13 to majority | N-01 battery; share of merges with two approvals | Median merge time (should not exceed 10 days) | Keep if belief and behaviour both move; if behaviour only, expect decay and add review checklist emphasis | 2026-12-01 | Open |
| H-05 | Rules at the point of action (template, bot) raise newcomer compliance with N-03 | s4, s8, s9, s11 | Matias 2019 is one platform; cue-to-norm mapping is H | Template on for all new PRs | Linked-issue share of newcomer PRs rises by a moderate amount | Share of newcomer PRs with linked issue | First-time commenter drop-off; complaints about friction | Keep if compliance rises without a fall in first-PR volume beyond 10% | 2026-12-01 | Open |
| H-06 | Identifiable review credit (release-notes listing) and elected stewards raise regular reviewing without a score | s4, s6, s9, s10 | Baldassarri & Grossman is a field lab with farmers; loafing literature is direction only | Credit line in next two releases; steward election | Named reviewers per release rises; no gaming (volume of trivial approvals) | Reviews per release by non-lead | Trivial-approval rate (approvals under 2 minutes after open) | Keep unless trivial approvals exceed one in five | 2027-01-15 | Open |
| H-07 | A non-monetary graduated ladder lowers abandonment without crowding out; a bounty would crowd out | s9 | Crowding-out shown in day care, not here; ladder rungs are ours | Ladder on; no bounty; compare with prior quarter | Rung-4 use near zero; rung-1 comments answered in over half of cases | Rung transitions per month | Anti-social use: stewards' closes disputed and upheld on appeal | Keep if appeals uphold most closes; revise rungs if rung-3 closes are mostly good-faith | 2026-12-15 | Open |
| H-08 | Maintainers' fairness reference point is commercial users' non-contribution, and a visible "sponsor or contribute" ask reduces felt violation | s6 | Reference point inferred from interviews with two people | Maintainer interview at day 90 | Felt-fairness item improves | One-item fairness question, maintainers | Any decline in issue quality from company users | Keep or drop; low stakes | 2026-12-30 | Open |
| H-09 | Module ownership in pairs keeps the release weak-link game small enough to sustain high effort | s6 | Eight is between the lab's pairs and its 14–16 | Pair up the eight owners; count release blockers | Blockers per release fall | Release blockers | Owner load | Keep if blockers fall over two releases | 2027-01-15 | Open |
| H-10 | The unpaid Krupka–Weber framing recovers normative expectations here | s8 | Primer marks the unpaid version H | Compare with the direct question in the same survey | Framed answers less socially desirable than direct | Difference between the two items | None | Method note only | 2026-11-01 | Open |
| H-11 | Written recognition of the rota by the foundation makes its rules stick | s9 | Ostrom's principle 7 is a regularity across cases | Ask; observe whether Priya overrides rota decisions | No overrides in 90 days | Overrides | Foundation friction | Keep if no overrides | 2026-12-30 | Open |
| H-12 | The issue-answering cluster adopts only if a second bridge is in the pilot | s10 | Cluster-blocking is a theorem; our q is an estimate | One pilot member from the overlap | Adoption in that cluster by day 90 | Reviews by that cluster's members | Sam's load | Keep or add a third bridge | 2026-12-30 | Open |

### s13. Value commitments register

| Id | Commitment | Section | Who reasonably disagrees, best argument | Cost | Evidence that informs it | Conflicts with | Owner and review |
|---|---|---|---|---|---|---|---|
| V-01 | We choose maintainer sustainability over PR throughput | s7, s14 | Users depending on fast fixes: "a slower project is a worse dependency, and forks will follow" | Slower merges; some contributors leave | Wen's exit; stable membership as precondition (`gaps-primer §7`) | V-02 (an open door raises load) | Maintainers; review at v7 |
| V-02 | We keep the PR door open to anyone over gating first-time contributors behind an application | s1, s9 | Tomasz: "gating would cut spam and slop by more than it costs" | Bot and steward effort; some slop | Halfaker et al. 2013 on newcomer rejection killing retention (`gaps-primer §6`) | V-01 | Stewards; six months |
| V-03 | Every sanction is explained in public over quiet closes | s9 | A steward: "public explanations invite arguments and humiliate newcomers" | Steward time; some public friction | Jhaver et al. 2019, observational | none | Stewards |
| V-04 | No money for reviews or fixes; recognition instead | s7, s9 | A commercial user: "we would pay for review; refusing money is ideology" | Forgone funds; slower for paying users | Gneezy & Rustichini 2000 (informs, does not settle; crowding-in also occurs) | V-01 (money could buy maintainer time) | Maintainers; revisit if a foundation grant appears |
| V-05 | Stewards and rota rules are elected and member-made over founder-appointed | s9 | Priya: "elections are theatre at 12 people; I know who is reliable" | Time; risk of an unreliable steward | Baldassarri & Grossman 2011; Ostrom principle 3 | none | Regulars; six-month term |
| V-06 | Regulars may experiment with workflow over "that's not how we do it" | s3 | A regular: "experiments cost the rest of us stability" | Some churn in process | Innovation budget (`02` ch 3, simulation) | V-01 | Rota; monthly thread |
| V-07 | Members are told what is being measured and why; no undisclosed nudges | s8, s14 | Nobody strongly; a steward notes disclosure may change survey answers | Possible loss of measurement purity | Transparent nudges retain effect for defaults (`gaps-primer §10`, H for norm messages) | none | Author; each version |

### s14. Measurement plan and ninety-day predictions

Baseline date 2026-09-30, from Lanternfish's own logs and the s8 survey. Re-run the s8 battery
on 2026-12-01. All figures are ours.

| Intervention / hypothesis | Practical measure | Baseline | Predicted at day 90 | Balancing measure | Harm threshold | Abandon if | Owner | Cadence |
|---|---|---|---|---|---|---|---|---|
| Rota pilot (H-02) | Share of reviews by non-lead | about 40% overall, about 15% by regulars | Regulars over 40%; Priya under 40% | Rota-member self-reported load; rota churn | Any member reports load above prior; more than one drop-out | Fewer than 3 of 4 shifts filled in weeks 3–6 | Tomasz | Weekly |
| Bot and ladder (H-01, H-07) | First-response median; abandonment share | about 3 weeks; about a third | Under 7 days for complete PRs; abandonment well under a fifth | First-PR contributors' 90-day return rate; good-faith closes at rung 3 | Return rate falls by more than a fifth; good-faith closes over one in ten | Both harms observed | Stewards | Fortnightly |
| Branch protection and lead compliance (H-04) | Share of merges with two approvals; N-01 belief | about 55%; 4 of 13 | Over 90%; majority belief | Median merge time | Over 10 days | Merge time doubles with no belief change | Priya | Monthly |
| Release credit and elected stewards (H-06) | Named reviewers per release | 2 | 6 or more | Trivial-approval rate | Over one in five | Trivial approvals dominate | Stewards | Per release |
| Runbook and supervised release (H-03) | Non-lead releases | 0 | 2 | Defects per release | Above prior average | Two failed solo releases | Tomasz | Per release |
| Template cue (H-05) | Newcomer PRs with linked issue | about 20% | Moderate rise | First-PR volume | Falls more than 10% | Volume falls with no compliance gain | Stewards | Monthly |

Three dated predictions. (1) By 2026-12-01, regular-authored reviews exceed 40% of all reviews
and Priya's share is below 40% [H: H-02]. (2) By 2026-12-01, the belief that most merges get two
approvals is held by a majority of regulars, and actual two-approval merges exceed 90% [H: H-04].
(3) By 2026-12-30, first-response median for template-complete PRs is under seven days while the
first-PR return rate has not fallen by more than a fifth [H: H-01, H-05].

Abandonment condition for the main hypothesis. If by week six the rota fills fewer than three
shifts in four, or any rota member reports higher load than before, H-02 is wrong about either
the shape (B is a dilemma after all, and needs repetition and a sanction) or the coalition size;
return to s2 and re-draw B with the pilot's own payoffs [H: H-02; `unified-model` station 5].

What decays if expectations do not move. If reviews rise but the N-01 battery does not move, the
change rides on the weekly summary being read and will decay when it lapses; the response is to
keep the summary and add the checklist, not to add a reward [E: `unified-model` section 4, station
5; law 6].

---

## Reconciliation notes

- The template's "model-of-the-foundation commitments L1–L5" section does not exist in this
  course's canonical skeleton (learning-design 4c has s3 as the collective brain); the template's
  role of "commitments cited by number in later sections" is filled by the twelve laws
  (`unified-model.md` section 6) and the ledger's binding rules, which this guide cites by number.
- The version plan runs v0–v6 per learning-design (v5 after m11; v6 at the capstone), not v0–v5
  as in the generic template.
- Every number in the example is either the hypothetical's own data (labelled) or a ledger
  section-4 or primer-verified figure with its hedge; no lab figure is used as a field estimate
  (ledger rules 27, 40).
- The primer's sections 1–4 add to the brief: the four-question battery and reference network
  (s8), the sanctions ladder and anti-social punishment check (s9), legitimacy source and
  procedural-justice components (s9), reputation scope and identity re-entry (s9), and the
  practical/predicted/balancing triple (s14).
