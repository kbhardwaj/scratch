# Capstone: the brief, the defense, the first 90 days

The capstone is the course's final assessment (`synthesis/learning-design.md` section 4f). It asks
one question: could you open a school on this design, defend it under pressure, and run its first
term as a learning system? It has three deliverables, one challenge-selection procedure, and one
10-criterion rubric. The rubric's top level means "a thoughtful head of school would sign this."

| | Deliverable | Length | Time | Main criteria |
|---|-------------|--------|------|---------------|
| 1 | Design Brief v5 | 3,000-4,000 words | 90 min (revising v4) | 1-8, 10 |
| 2 | The defense: six challenges | 6 x 200-300 words, or a 20-minute recorded talk | 45 min | 9 (and 8) |
| 3 | The first 90 days | One page (about 500 words, plus a driver diagram) | 45 min | 7 (and 5) |

Schedule: days 22-24 of the course plan, one deliverable per sitting. Do the brief first, the
defense second (it attacks the brief), and the 90-day plan last (it operationalizes the brief).

Prerequisites: Brief v4 with both registers started; the day-21 retake of the diagnostic; at least
eight casebook cases answered during the course.

---

## Deliverable 1: Design Brief v5

Use the template and guide in `synthesis/design-brief-template.md`: 11 sections, versioned, with
the changelog from v0. Before submitting, check the brief against this minimum contents list. A
brief missing an item can still pass, but the matching rubric criterion is capped at 2.

- **s1:** Three to five checkable graduate outcomes; a statement of which design layers are open to
  community codesign.
- **s2:** Three Tuesdays at three ages, each with one lesson minute by minute and inline tags.
- **s3:** Five learner-model commitments (L1-L5) with source slugs, and a list of rejected folk
  theories.
- **s4:** A sequence sketch for at least two subjects across grades; one conceptual progression
  across three or more grades naming the intuitive theory it must outcompete; literacy minutes;
  deliberate exclusions.
- **s5:** The default lesson with mechanisms; at least one exception with its conditions and a
  switch signal; a homework policy.
- **s6:** The hinge-question standard plus two sample hinge questions with misconception-keyed
  distractors and decision rules; the grading policy; a definition of mastery; family reporting.
- **s7:** Hiring process; a three-year development plan; the TLC compact including where the time
  comes from.
- **s8:** Timetable sketch; grouping policy; the periphery; what is kept conventional and why.
- **s9:** The year-one aim; a driver diagram; the separation rule between improvement and
  accountability data.
- **s10:** At least eight hypotheses, each with a prediction and a decision rule.
- **s11:** At least six value commitments, each with a named dissenter and a cost.
- **Changelog:** At least eight substantive reversals of v0 positions, each attributed to a module
  and an author.

---

## Deliverable 2: The defense

You answer six challenges. At least two must attack your own value commitments (register s11).
Answer in writing (200-300 words each) or as a recorded 20-minute talk (about three minutes per
challenge). Every answer follows the same five moves:

1. **Name the tension** (id and name, t01-t14, from `synthesis/tensions.md`). If two are in
   play, say which dominates and why.
2. **Apply the decision rule** to this case *and your brief*: what your school does, citing the
   section of the brief that already covers it, or saying that it doesn't.
3. **State the switch signal**: the specific observation or number, in this case, that would make
   you reverse your decision.
4. **Say what you don't know**: the weakest evidence behind your answer, tagged.
5. **Say what changes in the brief**, or why nothing does. At least one of the six answers must
   change the brief. Add that change to the v5 changelog as "v5.1".

For the two value challenges, move 2 changes. First steelman the dissenter: state their best
argument better than they would. Then name the cost of your commitment. Then hold it or revise it,
with reasons. Citing evidence as if it settled a value question scores as a mis-tag.

### Challenge-selection procedure

The procedure has two aims. The learner must not be able to pick only cases they are comfortable
with, and the challenges must cover both the classroom and the institution.

**Step 1: Build your attack map (10 minutes, before any draw).**
List your s11 value commitments as V-01 to V-n. Next to each, write one casebook case (k01-k24)
whose scenario puts pressure on it, and the dissenter named in your register. Some pairings are
natural: a commitment to comment-only feedback pairs with k03 or k22, a protected periphery with
k23 or k05, a common curriculum with k02, "understanding, not belief" with k21. If no case
pressures a commitment, write a one-line scenario in which that commitment's dissenter holds power,
such as a board vote, an authorizer review, or a funder's condition.

**Step 2: Draw four casebook challenges.**
Generate four distinct random numbers from 1 to 24, with a die or with
`python3 -c "import random; print(random.sample(range(1, 25), 4))"`. Each number is a case, k01 to
k24. Then check the set against three constraints, and redraw the latest number until all three
hold:
- At least two of the four cases were **not** answered by you during the course.
- The four cases include **at least one classroom tension** (t01, t02, t03, t08, t09, t10, t11, t12)
  and **at least one institutional tension** (t04, t05, t06, t07, t13, t14), using each case's
  primary tension (the `tension` field in `app/data/cases.json`).
- No two cases share the same primary tension.

**Step 3: Draw two value attacks.**
Number the rows of your attack map and draw two distinct rows at random. For each, write the
challenge in the dissenter's voice, 80-150 words, set in *your* school, using the paired case as
raw material. If a co-planner is available (a colleague, mentor, or Claude in a separate session),
the co-planner writes both value attacks instead of you. They see your brief but not your defense
drafts, and they may choose the two commitments they judge most vulnerable rather than drawing.

**Step 4: Transplant.**
Rewrite each casebook challenge so it happens at your school. Keep the numbers and people, but make
the grades, programs and policies those in your brief. The defense is scored against your brief,
not against the casebook's model answer. The model answers are available afterwards for
comparison.

**Step 5: Seal.**
Write the six challenges at the top of the defense document before answering any of them. No swaps.
Timebox to 45 minutes of writing (or one 20-minute recording after 25 minutes of notes).

**Worked example of a draw.** The random numbers are 7, 12, 3 and 20.
- k07 (t13) and k12 (t06) are both institutional, and k03 (t12) is classroom.
- k20 (primary t13) duplicates k07's primary tension, so redraw it. The redraw is 17: k17 (t11,
  classroom).
- The learner had answered k07 and k03 during the course but not k12 or k17, so the "unseen"
  constraint holds.
- The attack map has seven rows. The draws are row 2 (V-02, "no grades on formative work," paired
  with k22) and row 6 (V-06, "Friday studio protected in test season," paired with k23 and k05).
- A co-planner writes V-06's attack as a board member's motion to suspend the studio for the six
  weeks before state testing.

### What the defense is not

It is not a place to be right about everything. An answer that says "my brief doesn't address this,
here is what I would add, and here is what would show me wrong" can earn a 4. An answer that recites
the casebook model answer about a school that isn't yours cannot.

---

## Deliverable 3: The first 90 days

One page, plus a driver diagram, which may be a sketch or an indented list. It must contain:

1. **Year-one aim.** One sentence covering what, how much, by when, and for whom, with the subgroup
   gap you intend to close. Tagged [V] for the choice of aim and [H] for the size of the target.
2. **Driver diagram.** The aim, three or four primary drivers, secondary drivers, and change ideas.
   Give one measure at each level. Mark which change ideas implement settled evidence [E] and which
   are local bets [H].
3. **The first three PDSA cycles.** For each: the change, who runs it and where (start with one
   classroom or one team), the written prediction with a number, the practical measure and how fast
   it gets back to teachers, the balancing measure, the start and end dates, and the rule for
   adopt / adapt / abandon. At least one cycle tests an [H] from your s10 register.
4. **TLC launch.** Dates of the first three meetings; how groups are formed; who facilitates and
   how facilitators are prepared; the first meeting's agenda; where the time comes from (the stop
   list).
5. **Three things the founder will personally observe every week.** For each: where and when you
   will look; what "good" looks like in one sentence; and what you will do if you don't see it for
   two weeks running. These should be observations of mechanisms, such as whether every student
   responds to the hinge question, or whether the consolidation phase gets its full time. They
   should not be observations of compliance, such as "objectives on the board."
6. **Days 30, 60 and 90.** One line each: what must be true by then, and what you will do if it
   isn't.

---

## Rubric

Each criterion is scored from 1 to 4. **Pass:** 32 out of 40, with no criterion below 2.
**World-class** for this course: 36 out of 40 with a 4 on criteria 1, 2, 7 and 8. Those four
separate a school built on how learning works from a school built on how schools usually look.

The general meaning of each level:
- **4** A thoughtful head of school would sign this.
- **3** Sound, with gaps a colleague would catch in one read.
- **2** The right words without the working parts.
- **1** Absent, wrong, or contradicted elsewhere in the submission.

### 1. The model of the learner is correct and load-bearing

*Where to look:* s3, then trace forward into s4-s6.

- **4:** Five (plus or minus one) commitments, each accurate to the evidence, with a source slug and
  a caveat wherever the finding is contested (for example curiosity spillover, mindset messages).
  Every instruction and assessment decision in s4-s6 cites the commitment it rests on. Intuitive
  theories are treated as outcompeted over time, not erased by one lesson. Motivation claims split
  [E] mechanism from [H] school-scale effect. Rejected folk theories are listed, and their use in
  hiring or procurement is stated.
- **3:** Commitments accurate and sourced. Most decisions trace to them, but one commitment is
  decorative (nothing depends on it), or one contested claim lacks its caveat.
- **2:** Commitments are generic ("children learn by doing," "every child is different") or loosely
  sourced. Traceability is occasional. Or a contested finding is stated as settled.
- **1:** Learning styles, motivation-before-competence, or knowledge-is-obsolete appears untagged or
  endorsed anywhere in the brief (this caps the criterion at 1). Or there is no learner model.

### 2. Instructional defaults and exceptions are conditional, not ideological

*Where to look:* s5, s2, the three Tuesdays, and the defense answers on t01.

- **4:** The default lesson is explicit, with its phases and each phase's mechanism. Every exception
  names its conditions (for productive failure, all four), who approves it, and a switch signal
  that returns the unit to the default. Unguided discovery is excluded for novices, with the
  reason. The three Tuesdays show scaffolding fading from the youngest to the oldest child
  (expertise reversal made visible). Homework is retrieval of taught material with a target
  success rate.
- **3:** The default is explicit and exceptions have conditions, but a switch signal is missing, or
  fading is asserted in s5 without being visible in the Tuesdays.
- **2:** A "balanced" or "blended" approach with no conditions, or exceptions granted by teacher
  preference. Or explicit-only with no account of goals or expertise.
- **1:** Discovery, projects or playlists are the default for novices. Or the evidence is
  misrepresented in either direction (for example, "research shows students learn best when they
  discover for themselves").

### 3. The curriculum is knowledge-rich, sequenced, and honest about values

*Where to look:* s4, s11.

- **4:** A real sequence for at least two subjects across grades, with dependencies named (what each
  unit builds on). At least one conceptual progression across three or more grades names the
  intuitive theory it must outcompete and the prerequisite concepts. A phonics track and literacy
  minutes are specified. Deliberate exclusions are stated with reasons. Content choices are tagged
  [V] and appear in the value register with a real dissenter and a cost.
- **3:** A sequence exists but dependencies are thin, or the progression names no intuitive theory.
  Values are logged but the dissenters are generic.
- **2:** "Knowledge-rich" is asserted and topics are listed, without sequence or dependencies. Or
  content choices are presented as if the science dictated them.
- **1:** A skills-first or content-agnostic curriculum (for example, strategy-of-the-week), or no
  curriculum section.

### 4. Assessment is genuinely formative

*Where to look:* s6, s7 (TLC accountability), and the two sample hinge questions.

- **4:** A hinge-question standard with every element: every student responds, under a minute,
  distractors keyed to named misconceptions, a decision rule written in advance, and banking. Two
  sample hinge questions meet it. Formative work is comment-only and requires student action
  (Butler; Kluger & DeNisi). Mastery of core concepts requires transfer and delayed success.
  Families get reporting specific enough to prevent a revolt. TLCs contain a peer accountability
  mechanism (action plans and a report-back round). Formative and practical data never enter
  evaluation.
- **3:** All of the above are present, but the sample hinge questions are weak (for example, a
  distractor not tied to a misconception), or family reporting is vague.
- **2:** "Formative assessment" is named but formative work is graded, or there is no hinge
  standard, or TLCs have no accountability mechanism.
- **1:** Assessment means tests and grades, or formative data feeds evaluation.

### 5. Adults are developed, not merely selected

*Where to look:* s7, the 90-day plan (TLC launch), and the defense answers on t06.

- **4:** Hiring directly observes a work sample, the response to feedback, and subject knowledge.
  These criteria are tagged [H] and entered in the register. There is a three-year development plan
  for new teachers. The TLC compact specifies group size, cadence, agenda, peer observation with
  cover, facilitator preparation, and the source of time (a stop list). TLCs are kept separate from
  evaluation. The mentor mindset is applied to adults (high bar, high support) and specified for
  adult-student talk. A switch signal for the TLC design is stated (t06: within-school variation
  not narrowing after two full years).
- **3:** Coherent with Wiliam, but the source of time, facilitator preparation, or switch signal is
  missing.
- **2:** TLCs are mentioned without a compact, or hiring is the main quality lever.
- **1:** Selection, deselection or incentives (for example, merit pay) are the strategy, or
  professional learning consists of one-off training days.

### 6. The core is designed for depth, not just the periphery

*Where to look:* s2, s4, s8, and the defense answers on t07 and t13.

- **4:** Every core course has at least one apprenticeship feature per term: an authentic product
  for a real audience, critique against practitioner standards, or older students coaching younger
  ones. The periphery is compulsory, protected in the timetable, and designed with coaching and
  exhibition, not just open time. Each structural departure from convention names the instructional
  need behind it. Conventional elements are kept on purpose. The three Tuesdays describe median
  lessons, not showcases.
- **3:** Most core courses have a depth feature, and the periphery is protected, but one structural
  departure has no instructional rationale.
- **2:** Depth lives only in an elective or project block, or structural novelty (schedule, calendar,
  platform) appears with no instructional need behind it.
- **1:** No design for depth anywhere, or the whole school is restructured around a model without
  an instructional rationale.

### 7. The improvement system is real

*Where to look:* s9, the 90-day plan, s10.

- **4:** One precise year-one aim with subgroups. A driver diagram with a measure at every level.
  Three PDSA cycles, each with a numeric written prediction, a practical measure returned within
  days, a balancing measure, an owner, dates, and an adopt/adapt/abandon rule. At least one cycle
  tests an s10 hypothesis. The cadence is specified. A written rule keeps improvement data out of
  evaluation and splits what the board sees. A switch signal covers what happens if practical and
  accountability measures diverge.
- **3:** All the parts exist, but predictions are not numeric, balancing measures are missing, or
  cycles are too large to finish in 90 days.
- **2:** An aim and "PDSA" appear, but the cycles are initiatives or plans rather than tests, or
  the measures are annual tests.
- **1:** No improvement system, or improvement measures are used to rank or evaluate staff.

### 8. Tagging discipline

*Where to look:* every sentence of s3-s9; s10 and s11.

- **4:** Every declarative sentence in s3-s9 is tagged. Compound claims are split ([E] mechanism,
  [H] parameter). Every [E] has a slug. Contested findings are caveated: formative effect sizes
  from 1998, growth-mindset messages, wise feedback at scale, curiosity spillover, PF effect sizes,
  knowledge-curriculum effects on general tests. No value is laundered as evidence. The s10
  register has eight or more entries, each with a prediction and a decision rule. The s11 register
  has six or more, each with a real dissenter and a cost.
- **3:** Up to three untagged sentences or one mis-tag. The registers are complete but a few
  entries are thin.
- **2:** Frequent untagged sentences or several mis-tags (for example, a mindset poster campaign
  tagged [E]). The registers are sketchy.
- **1:** Tags are missing or decorative, or values are presented as evidence throughout.

### 9. Defense quality

*Where to look:* Deliverable 2.

- **4:** All six answers make the five moves. The rule is applied to this case and to the learner's
  own brief. The switch signal is specific to the case (a number or an observation, not "if it
  doesn't work"). Uncertainty is stated and tagged. The value attacks are answered by steelmanning
  the dissenter, naming the cost, and then holding or revising with reasons. At least one answer
  changes the brief.
- **3:** Five or six answers are complete, but the value attacks are defended without a genuine
  steelman, or one switch signal is generic.
- **2:** Tensions are named but rules are applied generically. Switch signals are missing in two or
  more answers. Or value attacks are answered with evidence as if evidence settled them.
- **1:** Answers are opinions, tensions are not named, or the answers recite casebook model answers
  about a school that isn't the learner's.

### 10. Delta from v0

*Where to look:* the changelog, v0, and the diagnostic retake.

- **4:** At least eight substantive reversals of v0 positions, each attributed to a module and an
  author, with the tag change shown. The v0 free response ("what makes a school world-class") is
  revisited in a paragraph. The diagnostic retake is compared with the day-1 answers, including a
  note on confidence calibration (where the learner was confidently wrong). At least one v0
  position is explicitly kept, with the reason.
- **3:** At least eight reversals with attributions, but some are cosmetic (wording or formatting),
  or the diagnostic comparison is missing.
- **2:** Four to seven reversals, or reversals without attribution.
- **1:** Fewer than four reversals, or no changelog.

### Scoring procedure

1. **Self-score immediately** after finishing all three deliverables, citing the evidence (section
   and sentence) for each score.
2. **Re-score cold after 48 hours** without looking at the first scores. Where the two differ by
   two or more points, re-read the "where to look" sections and settle on a score with a one-line
   reason.
3. **If a co-planner is available,** they score independently from the same rubric. Discuss any
   criterion where you differ by more than one point, and take the lower score unless the evidence
   is quoted.
4. **Repair map** for any criterion scored at 2 or below:

| Criterion | Revisit |
|-----------|---------|
| 1 | M1, M2, M3; `01-how-learning-happens` 5-10 ideas; `02-scienceblind` evidence limits |
| 2 | M4; `04-productive-failure` conditional rules; `00-foundational-papers` implications |
| 3 | M5; `06-beyond-the-science-of-reading` implications; `13-learning-scientific-concepts` |
| 4 | M6; `07-embedding-formative-assessment` ideas 4-6 |
| 5 | M8; `10-creating-the-schools-our-children-need` ideas 2-4; `05-10-to-25` staff implications |
| 6 | M7; `09-in-search-of-deeper-learning` ideas 2, 3, 6 |
| 7 | M9; `11-improvement-in-action` ideas 4-6 and evidence limits |
| 8 | M10; every book's "Evidence strength & limits" |
| 9 | Casebook: redo three cases from different tensions, timed |
| 10 | M10 re-tagging exercise |

After repair, revise and re-score only the affected criteria. The capstone may be resubmitted once.

---

## Worked exemplar: what a 4 looks like

The excerpts below are from a hypothetical learner's v5 for **Harbor Lane**, a 720-student K-12
school. They show criteria 2, 7 and 9. Tagging discipline (criterion 8) is visible throughout. The
annotations say why each excerpt earns a 4 and what would drop it to a 3.

### Criterion 2: excerpt from s5, Instruction

> **Default lesson (all grades, all core subjects).** (1) Retrieval starter, 5-8 minutes, mixing
> the previous day, week and month (L3) [E, `01-how-learning-happens`; H for the durations]. (2)
> Learning intention stated separately from the task [H]. (3) Explanation with worked examples;
> slides carry diagrams, not duplicate text (L1) [E, `00-foundational-papers`: the redundancy effect
> is robust in the lab and moderate in classrooms]. (4) All-student check via whiteboards or a hinge
> question; below 80% correct, re-teach from the most common distractor (L2) [E for eliciting from
> all students; H for the 80% threshold]. (5) Guided practice aiming for about 80% success, then
> (6) independent practice, then (7) an exit ticket that plans tomorrow's lesson [E for components;
> H that a shared model beats teacher-by-teacher variation].
>
> **Exception A: productive failure.** Grades 6-10 math and science, at most five designated
> concepts a year (variability, rate, density, natural selection, proportionality). Approved by the
> department lead only when all four hold: the goal is conceptual; the pre-assessment shows relevant
> prior knowledge; the task admits three or more solution methods; and a scripted consolidation
> comparing student methods with the canonical one is scheduled in the *next* period, so the bell
> cannot eat it [E for the conditions, `04-productive-failure`; H for the five-concept cap].
> Procedural goals are never taught this way, because the meta-analysis shows no procedural benefit
> (g about -0.03) [E]. *Switch signal:* a unit reverts to the default if observed consolidation
> runs under 20 minutes in two lessons, or if its delayed transfer quiz falls below the previous
> year's explicit-instruction baseline.
>
> **Fading across ages.** K-2: every new skill is modeled, then practised with support. Grades 6-8:
> about one lesson in six opens with a short attempt before instruction. Grades 11-12: seminar and
> independent investigation become the default only in courses where a diagnostic shows students
> have the schemas to use them (expertise reversal) [E for the principle, `01`; H for the
> proportions].
>
> **Excluded:** unguided discovery for novices in any core course [E, `00`]; "learning style"
> differentiation [E that it has no benefit].

*Why this is a 4.* Every phase names its mechanism and the learner-model commitment it serves. The
exception has all four conditions, a named approver, a structural protection against the known
failure mode (consolidation in the next period), and a switch signal with numbers. Fading is
concrete by age band. Tags are split within sentences, and the one moderately supported effect is
caveated. *What would make it a 3:* the same default and exception with the switch signal reduced to
"revert if it isn't working," or fading asserted without the age-band detail.

### Criterion 7: excerpt from the 90-day plan

> **Aim.** By 15 December, 75% of grade-9 students pass all core courses at the first grading
> period, up from a projected 58% (the feeder schools' rate). The gap for students entering below
> grade level falls from 25 to 12 points [V for the aim; H for the size; E that grade-9 course
> performance predicts graduation, Chicago on-track research via `11-improvement-in-action`].
>
> **PDSA 1 (weeks 2-5, owner: grade-9 math team, two sections).** *Change:* a daily 5-minute
> cumulative retrieval starter, with missed items re-queued the next week. *Prediction:* accuracy on
> the Friday cumulative quiz rises from its week-1 baseline to at least 70% by week 5 in both
> sections. *Practical measure:* Friday quiz accuracy, sent to the teachers Monday morning.
> *Balancing measure:* teacher prep time (target under 15 minutes a week) and minutes lost from new
> content. *Rule:* adopt across grade-9 math if both sections meet the prediction; adapt if only
> one does, studying the difference first; abandon if neither moves 10 points.
>
> **PDSA 2 (weeks 3-8, advisors for 40 students).** Tests H-03 from the register: a weekly
> 10-minute advisor check-in on missing work, using the early-warning list. *Prediction:* the share
> of these students with any missing assignment falls from about 35% to under 20%. *Balancing
> measure:* advisor time and the student item "my advisor respects me."
>
> **Separation.** Section-level quiz and missing-work data stay inside the team huddle. The board
> sees grade-wide pass rates monthly. No improvement measure appears in any appraisal document
> [V; E that high-stakes use corrupts indicators, `11`].

*Why this is a 4.* The aim is precise, has subgroups, and names its evidence. The cycles are
small, dated, owned, predicted with numbers, and paired with balancing measures. One cycle tests a
register hypothesis. The adopt/adapt/abandon rule includes studying variation between sections. The
separation rule is written into the plan. *What would make it a 3:* "we will run PDSA cycles on
retrieval starters and measure quiz results," with no numeric prediction or balancing measure.

### Criterion 9: one defense answer to a value attack

> **Challenge (co-planner, attacking V-06, "Friday studio protected even in test season").** "I
> chair the board. Forty-one percent of grade 8 is below proficiency in math. For six weeks before
> the state test, the studio's 90 minutes a week should become math intervention. Protecting a
> maker space while children fail math is a luxury our families can't afford."
>
> **Answer.** The tension is t07, core versus periphery, with t05 (accountability versus
> improvement measurement) behind it: the state test is an accountability measure, and the
> pressure is to manage to it. The chair's
> best argument is stronger than "test scores matter." It is that the students furthest behind pay
> the highest price for our value choice, and that is an equity argument I share [V].
>
> The t07 rule is to design the core first and, under budget pressure, to protect the periphery
> as infrastructure, never building a two-tier school. So I
> would not suspend the studio for everyone. I would put intervention time where the need is. The
> 41% below proficiency get small-group math tutoring in the second half of the advisory block,
> four days a week, for six weeks. Tutoring for students behind has strong support [E,
> `01-how-learning-happens`], and its dose can be targeted in a way a whole-grade suspension can't.
>
> The cost of my position is real. Those students lose advisory time, and if the tutoring
> underdelivers, we will have protected the studio at their expense. What I don't know: whether
> six weeks of targeted tutoring moves state-test proficiency measurably. Short-run effects on
> distal tests are often small [H].
>
> *Switch signal:* if tutored students' practical measure (weekly skills checks) hasn't risen by at
> least 15 points by week 3, I will bring the board a proposal to use studio time for those students
> only, not the grade. *Brief change:* I am adding "test-season tutoring in the advisory block" to
> s8, and entering H-11 (six weeks of targeted tutoring raises the tutored group's checks by 15
> points) in the register.

*Why this is a 4.* It names both tensions and which dominates. It steelmans the chair on equity
grounds rather than dismissing "test pressure." It applies the rule to the learner's own structure
(the advisory block, s8). It names the cost to the students it most wants to protect. It tags its
uncertainty, gives a switch signal with a number and a date, and changes the brief and the register.
*What would make it a 3:* the same decision defended by citing Mehta & Fine's periphery finding as
if it settled the question, with no named cost and no switch signal.

---

## Appendix: scoring sheet

| # | Criterion | Self (day 0) | Self (day 2) | Co-planner | Final | Evidence (section and sentence) |
|---|-----------|--------------|--------------|------------|-------|----------------------------------|
| 1 | Model of the learner | | | | | |
| 2 | Instructional defaults and exceptions | | | | | |
| 3 | Curriculum | | | | | |
| 4 | Assessment | | | | | |
| 5 | Adults | | | | | |
| 6 | Depth in the core | | | | | |
| 7 | Improvement system | | | | | |
| 8 | Tagging discipline | | | | | |
| 9 | Defense | | | | | |
| 10 | Delta from v0 | | | | | |
| | **Total** (pass 32, no criterion below 2; world-class 36 with 4s on 1, 2, 7, 8) | | | | | |
