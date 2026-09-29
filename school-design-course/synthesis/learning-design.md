# Learning design for the anabolic phase

Status: designed against the SPEC curriculum and slugs; the per-book files in `books/` were not yet
written when this was drafted, so every "draws on" reference is to the slug, not to a section
number. When the book files land, the hinge questions and worked examples below should be checked
against them and adjusted where a book file contradicts a claim made here.

Learner profile assumed throughout: software/product background, comfortable with systems
thinking, product specs, and iteration loops; time-poor; wants *usable* understanding, not
coverage. Total learner time budget: 15-18 hours over three weeks, versus roughly 150-180 hours to
read the thirteen books and the papers.

---

## 1. Design principles (each tied to the book that justifies it)

1. **Attempt before instruction, but only where the learner has enough prior knowledge to generate
   plausible wrong answers.** (`04-productive-failure`, Kapur.) Every module opens with a design
   problem the learner tries cold. The point is not to succeed; it is to activate prior knowledge,
   surface the learner's intuitive theory of schooling, and make the subsequent explanation land
   on something. Where the learner has no relevant priors (e.g. the mechanics of early reading),
   we skip the attempt and go straight to a worked example. Kapur's own boundary condition,
   applied.

2. **Worked examples first, faded problems second, novel problems last.** (`00-foundational-papers`
   Sweller; `01-how-learning-happens`, worked-example and expertise-reversal effects.) Each module
   shows a fully worked design decision before asking the learner to make one. As the learner
   accumulates schemas across modules, the scaffolding fades: Module 1 gives a complete worked
   example; Module 9 gives only a case and a rubric.

3. **Manage intrinsic load by splitting; kill extraneous load by ruthless cutting.**
   (`00-foundational-papers` Sweller; `01-how-learning-happens`.) Each module carries one or two
   load-bearing ideas, never five. Everything else in the book file is marked "reference, not
   memory". No module exceeds ~100 minutes, and no single sitting exceeds 60.

4. **Confront the intuitive theory, do not just supply the correct one.** (`02-scienceblind`
   Shtulman; `00-foundational-papers` Posner et al. 1982, Chi, Vosniadou; `13-learning-scientific-
   concepts` Amin.) The learner arrives with a folk theory of learning (learning styles,
   discovery-is-natural, motivation-precedes-effort, knowledge-is-obsolete-because-Google). Each
   module names the relevant folk theory, creates dissatisfaction with it (Posner's first
   condition), then offers an intelligible, plausible, fruitful replacement. Hinge-question
   distractors are built from these folk theories so that a wrong answer tells us which one is
   still active.

5. **Retrieve, space, interleave.** (`01-how-learning-happens`, Roediger & Karpicke, Cepeda et al.,
   Rohrer; `12-why-we-remember` Ranganath on error-driven and reconsolidation-based memory.)
   Every third day is a retrieval day, not a new-content day. Retrieval questions mix modules
   (interleaving) and include "spot the misconception" prompts, because Ranganath's point is that
   memory improves most when retrieval is effortful and slightly wrong, then corrected.

6. **Formative assessment with hinge questions, and decisions made on the evidence.**
   (`07-embedding-formative-assessment` Wiliam & Leahy; `10-creating-the-schools-our-children-need`.)
   The hinge questions are not a quiz; they gate what the learner does next. A wrong answer sends
   the learner to a specific 5-minute repair, not to "re-read the module".

7. **Mentor-mindset tone: high standards, high support, and respect for the learner's status.**
   (`05-10-to-25` Yeager.) The course speaks to the learner as a capable adult building something
   serious. Feedback is "wise feedback": here is the high bar, here is why I think you can meet
   it, here is the specific thing to fix. No condescension, no cheerleading.

8. **The learner's own design brief improves through disciplined cycles, not one big reveal.**
   (`11-improvement-in-action` Bryk; `08-extraordinary-learning-for-all` Samouha et al.)
   The school-design brief is versioned. Each module ends with a small change to it, a stated
   prediction, and a note on what evidence would show the change was wrong. The capstone is v5 of
   the brief, with the changelog.

9. **Curiosity is a state to be engineered, not a trait to be waited for.** (`03-intellectual-
   lives-of-children` Engel; `00-foundational-papers` Gruber, Gelman & Ranganath 2014.) Modules
   open with a genuine question whose answer the learner cannot yet guess, because information gap
   plus prior knowledge is what drives the dopaminergic curiosity state that improves encoding.

10. **Every institutional claim carries an [E]/[H]/[V] tag.** (`10-creating-the-schools-our-
    children-need`, `09-in-search-of-deeper-learning`.) The learner will be tempted to launder
    values as evidence. The course models the distinction on every design decision and the
    capstone rubric penalizes untagged or mis-tagged claims.

11. **Deeper learning is found at the periphery, so the design targets the core.** (`09-in-search-
    of-deeper-learning` Mehta & Fine.) The course refuses to let the learner design "the cool
    elective" as the school. Every deliverable asks: what happens in the median 9th-grade math
    period on a Tuesday in February?

---

## 2. Course architecture

### Three levels, one spine

The SPEC's three levels (Minds, Design, Institutions) are the spine. The order runs bottom-up
because each level constrains the one above it: you cannot evaluate an instructional design
without a model of memory, and you cannot evaluate an institutional structure without a model of
instruction. But the *opening* is top-down: the learner attempts an institutional design before
any content, so that everything after is heard as an answer to a question they already asked.

### Module list

| # | Module | Level | Time | Draws on |
|---|--------|-------|------|----------|
| 0 | Diagnostic and opening design challenge | All | 60 min | none (deliberately) |
| 1 | How memory and attention actually work | Minds | 90 min | 00 (Sweller), 01, 12 |
| 2 | Why learners are not blank slates: intuitive theories and conceptual change | Minds | 90 min | 02, 13, 00 (Posner, Chi, Vosniadou) |
| 3 | Curiosity, motivation, and the adolescent mind | Minds | 90 min | 03, 05, 00 (Gruber) |
| 4 | Instruction: explicit teaching, productive failure, and when each wins | Design | 100 min | 01, 04, 00 (Kirschner, Sweller & Clark) |
| 5 | Knowledge, curriculum, and the reading problem | Design | 90 min | 06, 10, 01 |
| 6 | Formative assessment as the engine of the classroom | Design | 90 min | 07, 10 |
| 7 | The grammar of school and where deeper learning lives | Institutions | 90 min | 09, 08 |
| 8 | What actually moves outcomes: teachers, policy, and the evidence | Institutions | 90 min | 10, 01, 11 |
| 9 | Running the school as an improvement system | Institutions | 100 min | 11, 08, 07 |
| 10 | Integration: tensions, decision rules, and the unified model | All | 90 min | all |
| C | Capstone: the brief, the defense, the first 90 days | All | 180 min | all |
| R | Retrieval sessions (6 x 30 min) | All | 180 min | deck |

Total: roughly 17.5 hours. The learner can shave to ~14 by trimming retrieval sessions to 20 min
and the capstone to 2 hours, but not by skipping modules; the interleaving depends on all of them.

### Rationale for the order

- **Module 0 first, cold.** Kapur: the design attempt generates the learner's own theory of
  schooling, which the rest of the course will confront. Also gives us a baseline artifact to
  compare the capstone against; the delta is the proof of learning.
- **Minds before Design.** Sweller's cognitive load theory is the tool with which the learner
  evaluates every instructional claim afterward. Without it, Module 4's debate is just opinion.
- **Conceptual change (M2) before Curiosity (M3).** Shtulman and Engel both describe what children
  bring; putting the "wrong prior knowledge" module before the "wanting to know" module lets M3
  explain *why* information gaps matter (Gruber: curiosity needs prior knowledge to create a gap).
- **Motivation (M3) before Instruction (M4).** Yeager's mentor mindset is the frame for how any
  instructional approach is delivered; the learner should hear the explicit-vs-inquiry debate
  already knowing that tone and status matter independently of method.
- **Knowledge/curriculum (M5) after Instruction (M4).** Wexler's argument only makes sense once the
  learner has the long-term-memory-is-the-point idea from M1 and the guided-instruction evidence
  from M4.
- **Formative assessment (M6) closes Design.** It is the mechanism that makes everything before it
  adaptive, and it bridges into Institutions because Wiliam's argument in book 10 is that teacher
  learning communities around formative assessment are the highest-leverage institutional move.
- **Mehta & Fine (M7) opens Institutions** because it is the honest picture of what schools are
  really like; Bryk (M9) closes it because improvement science is how you change that picture.
- **Integration (M10) is its own module,** not a wrap-up paragraph, because the tensions are where
  the actual design skill lives.

### Pre-course diagnostic (Module 0, part A, 20 min)

Twelve items, taken before any content, answers stored and revisited at the end. Purpose:
surface the learner's intuitive theories, calibrate their confidence, and give us a baseline. The
learner also rates confidence (1-5) on each answer; the confidence-accuracy gap is fed back at the
end of the course.

Items (a selection; the full set lives in the deck):

1. "Students learn better when taught in their preferred learning style." Agree/disagree, and
   how confident are you? (Diagnoses the learning-styles myth; `01`.)
2. "A 14-year-old who does not care about school mainly lacks motivation, which must be built
   before you can teach them." (Diagnoses motivation-precedes-competence; `05`, `01`.)
3. "Because facts are searchable, schools should focus on skills like critical thinking rather
   than knowledge." (Diagnoses the knowledge-is-obsolete theory; `06`, `10`, `01`.)
4. "Letting students struggle with a problem before explaining it is usually a waste of
   instructional time." (Diagnoses the naive explicit-instruction position; `04`.)
5. "Letting students discover principles for themselves produces deeper learning than
   explaining." (Diagnoses the naive discovery position; `00`, `01`.)
6. "A school with great teachers and a rigorous curriculum will produce deep learning in most
   classrooms." (Diagnoses underestimation of the grammar of school; `09`.)
7. "The most reliable way to raise a school's results is to hire better teachers." (Diagnoses
   the selection-over-development theory; `10`.)
8. "If a child believes the earth is round, they have no misconception about the earth's shape."
   (Diagnoses the belief-vs-mental-model confusion; `02`, `00` Vosniadou.)
9. "Testing students is mainly for measuring; learning happens during teaching." (Diagnoses
   testing-as-measurement-only; `01`, `12`.)
10. "When an intervention works in a pilot, the next step is to scale it." (Diagnoses scaling-
    before-understanding-variation; `11`.)
11. "Giving students a grade plus a comment helps them more than a comment alone." (Diagnoses
    the grade-plus-comment myth; `07`.)
12. Free response: "In three sentences, what makes a school world-class?" (Baseline for the
    capstone comparison.)

### Opening productive-failure design challenge (Module 0, part B, 40 min)

Prompt, given verbatim to the learner:

> You have been given a building, a budget for 30 staff, and permission to enroll 400 students
> aged 5-18 next August. In 40 minutes, write a one-page design: what a Tuesday in February looks
> like for a 7-year-old, a 12-year-old, and a 16-year-old; how you will know in year two whether
> it is working; and the three decisions you are least sure about. Do not research. Use what you
> already believe.

The learner is told explicitly, in Kapur's spirit, that the point is to generate, not to be
right, and that this page will be graded only against their own later work. This document becomes
Brief v0. Every module's deliverable is a diff against it.

Two instructions to the learner after they finish, before Module 1: (a) list the assumptions they
made about how children learn that they could not defend to a skeptic; (b) mark each decision on
their page as [E], [H], or [V] as best they can. They will do this badly. That is the point; M10
revisits it.

---

## 3. Module specifications

Every module follows the same shape, in this order, so the structure itself becomes a schema and
stops costing working memory by Module 3:

1. Curiosity hook (a question the learner cannot yet answer; 2 min).
2. Attempt (the productive-failure or case prompt; 10-15 min).
3. Load-bearing ideas (1-2 ideas, explained; 15-20 min of reading the relevant sections of the
   book files, with a reading map that says which sections to skip).
4. Worked example (a design decision fully reasoned, 10 min).
5. Hinge questions (3, with repair paths; 10 min).
6. Brief deliverable (a diff to the design brief; 15-20 min).

### Module 1: How memory and attention actually work

**Draws on:** `00-foundational-papers` (Sweller, CLT), `01-how-learning-happens` (Sweller,
Paas, Roediger & Karpicke, Bjork's desirable difficulties, Chase & Simon expertise studies,
Willingham on attention), `12-why-we-remember` (Ranganath on encoding, error-driven learning,
reconsolidation, and the reconstructive nature of memory).

**Learning objectives.** The learner can (a) explain why working memory limits are the binding
constraint on instructional design and state the three load types; (b) explain why long-term
memory, organized as schemas, is what expertise *is*; (c) predict which of two lesson designs will
produce more durable learning and say why using retrieval, spacing, and load arguments.

**Load-bearing ideas.**
1. Working memory is tiny and fragile; long-term memory is vast and is the site of expertise.
   Instruction is the business of moving knowledge from the first to the second while not
   overflowing the first. Everything Sweller says follows from this.
2. Memory is strengthened by effortful retrieval and by being slightly wrong then corrected
   (Ranganath's error-driven learning; Bjork's desirable difficulties). Fluency during learning is
   a poor predictor of retention.

**Curiosity hook.** "A student reads a chapter four times and feels confident. Another reads it
once and takes a hard quiz they mostly fail. Who remembers more in a week, and by how much?"
(Roediger & Karpicke 2006: the tested group retains substantially more at a week; the reread group
predicts the opposite.)

**Attempt (productive failure).** Before reading: "You have 50 minutes to teach 25 twelve-year-
olds to compute the area of a trapezoid. Design the lesson minute by minute." The learner will
almost certainly front-load explanation, give one example, and assign practice. They will not
plan retrieval of prior knowledge, will not fade worked examples, and will not spread practice
over days. These absences are what the reading then explains.

**Worked example (fully reasoned design decision).** *Decision: how should homework work in the
school?* Reasoning shown step by step: (1) The purpose of homework is retention, so the mechanism
must be retrieval, not rereading. (2) Spacing effect implies homework should mostly cover material
from one to three weeks ago, not today. (3) Interleaving implies mixed problem sets, which feel
harder and produce worse in-session performance but better retention (Rohrer). (4) Cognitive load
implies the tasks must be ones the student can attempt without the teacher present, so novel
problem types are excluded. (5) Ranganath implies immediate corrective feedback after the attempt
is more valuable than the attempt alone, so homework must be self-checkable. Resulting policy:
"Homework is a 20-minute, self-checking, mixed retrieval set drawn from the last three weeks; new
material never appears in homework." Tagged [E] for the mechanisms, [H] for the 20-minute figure
and the three-week window.

**Hinge questions.**

Q1. A teacher explains a new concept while showing a slide with a diagram and a paragraph of text
that she reads aloud. Which change most reduces extraneous load?
- (a) Remove the diagram so students focus on the words. *Diagnoses: belief that fewer modalities
  is always better; misses the modality effect.*
- (b) Remove the on-screen text and keep the diagram while she narrates. **Correct**: the redundancy
  effect; reading text while hearing it read is pure extraneous load.
- (c) Give students the slide to read silently first, then explain. *Diagnoses: belief that
  pre-exposure reduces load; it splits attention across time and does not remove redundancy.*
- (d) Add a second worked example to the slide. *Diagnoses: conflating more examples with lower
  load; adds intrinsic and extraneous load simultaneously.*

Q2. Two Year 9 classes learn the same 12 topics over a term. Class A studies each topic in a block
of 3 lessons. Class B cycles through them so each topic returns every few weeks. On the end-of-term
test, which is most likely?
- (a) Class A scores higher because uninterrupted focus builds deeper understanding. *Diagnoses:
  blocking-is-better, the fluency illusion.*
- (b) Class B scores higher despite feeling like they learned less during the term. **Correct**:
  spacing and interleaving effects.
- (c) They score the same because total practice time is equal. *Diagnoses: time-on-task is the
  only variable; ignores the distribution of practice.*
- (d) Class B scores higher only on the topics they saw most recently. *Diagnoses: recency-only
  model of memory.*

Q3. A student says "I understand it when you explain it, but I can't do it on the test." What is
the most likely mechanism?
- (a) Test anxiety. *Diagnoses: affective explanation reached for first; possible but not the
  default mechanism.*
- (b) She has a learning style mismatch with the test format. *Diagnoses: the learning-styles myth.*
- (c) Following an explanation loads working memory much less than generating a solution; she has
  not yet built the schema that lets her generate. **Correct**.
- (d) She has not memorized enough facts. *Diagnoses: knowledge-as-facts rather than as organized
  schemas; partly right, wrong level.*

Repair paths: wrong on Q1 sends the learner to the `01` entries on Mayer and the redundancy
effect; Q2 to Cepeda/Rohrer entries; Q3 to the worked-example and expertise entries.

**Brief deliverable.** Rewrite the "Tuesday in February" for the 12-year-old in Brief v0 so that
it contains explicit retrieval at lesson start, at least one faded worked example sequence, and a
spacing policy. Add a one-line statement of the school's position on cognitive load, tagged.

### Module 2: Why learners are not blank slates: intuitive theories and conceptual change

**Draws on:** `02-scienceblind` (Shtulman's intuitive theories of matter, energy, life, cosmos,
etc.; the claim that they are never fully replaced, only suppressed), `13-learning-scientific-
concepts` (Amin on concepts, representations, and the role of language and embodied experience in
conceptual change), `00-foundational-papers` (Posner, Strike, Hewson & Gertzog 1982's four
conditions; Chi's ontological categories and why some misconceptions are robust; Vosniadou's
synthetic mental models of the earth).

**Learning objectives.** (a) Explain why misconceptions are not gaps but theories, and why telling
does not fix them; (b) apply Posner's four conditions to design an intervention; (c) distinguish
Chi-style ontological miscategorization (heat as substance) from Vosniadou-style synthetic models
(the flattened round earth) and say which needs what kind of teaching.

**Load-bearing ideas.**
1. Children (and adults) reason from coherent intuitive theories that make good predictions in
   daily life and bad predictions in science; new knowledge is assimilated into these theories,
   producing synthetic hybrids, unless the theory itself is confronted.
2. Conceptual change is slow, effortful, and reversible under load; even experts revert to
   intuitive answers under time pressure (Shtulman's reaction-time studies). Curriculum must
   therefore revisit core concepts across years, not "cover" them once.

**Curiosity hook.** "Ask a physics PhD whether a bowling ball or a tennis ball falls faster, but
make them answer in under a second. Are they slower to say 'same'?" (They are; the intuitive
theory is suppressed, not deleted.)

**Attempt (productive failure).** "A 9-year-old insists that a heavy sweater 'makes heat'. Design
a 15-minute intervention that changes their mind, and predict what they will say a month later."
Most learners will design a demonstration (thermometer in a sweater). The reading then shows why
a single demonstration is usually assimilated ("the sweater's heat takes a while to come out").

**Worked example.** *Decision: how does the science curriculum handle the twenty or so intuitive
theories Shtulman catalogs?* Reasoning: (1) Identify the intuitive theory the child brings
(diagnostic pre-question, cheap). (2) Create dissatisfaction: a prediction the child makes
confidently that fails visibly and repeatedly, not once (Posner condition 1). (3) Offer the
scientific model at the level of intelligibility appropriate to age (condition 2), in multiple
representations, since Amin's argument is that concepts live across language, diagram, and
gesture. (4) Make it plausible by connecting to something the child already accepts (condition 3).
(5) Make it fruitful: the new model must let the child predict something they care about
(condition 4). (6) Schedule the same concept for return in 2 later years, since the theory
resurfaces. Resulting policy: a "core concepts spiral" of ~15 concepts, each with a documented
intuitive theory, a diagnostic question, a canonical anomaly, and a three-year revisit schedule.
Tagged [E] for the mechanism, [H] for the count and schedule.

**Hinge questions.**

Q1. A student correctly answers "the earth is round" on a test. Which follow-up best reveals
whether they hold a scientific model?
- (a) Ask them to explain why the earth is round. *Diagnoses: belief that verbal explanation
  reveals the model; students reproduce taught phrases.*
- (b) Ask where people live on the earth and where the sky is, and have them draw it. **Correct**:
  Vosniadou's method surfaces the synthetic "hollow sphere" or "flattened disc" models.
- (c) Ask a harder question about gravity. *Diagnoses: assumes progression by difficulty rather
  than by model coherence.*
- (d) Accept the answer; the misconception is fixed. *Diagnoses: belief-equals-model confusion.*

Q2. Which misconception is hardest to change by demonstration alone, per Chi?
- (a) Heavier objects fall faster. *Diagnoses: assumes all physics misconceptions are alike; this
  one is within-category and demonstration helps.*
- (b) Heat is a substance that flows. **Correct**: an ontological miscategorization (process
  treated as substance); demonstrations get assimilated into the substance theory.
- (c) Plants get their mass from the soil. *Diagnoses: choosing by unfamiliarity; this is a
  factual attribution error, not ontological.*
- (d) The seasons are caused by distance from the sun. *Diagnoses: choosing by frequency; robust,
  but within-category.*

Q3. A school teaches evolution in Year 8 and finds most students hold the scientific view on the
end-of-unit test. Two years later most have reverted to teleological explanations. The best
institutional response is:
- (a) Teach it later, when students are more mature. *Diagnoses: maturational theory of
  conceptual change.*
- (b) Teach it more intensively in Year 8. *Diagnoses: dosage theory; coverage-once-but-harder.*
- (c) Build the concept into Years 8, 9, and 11 with explicit confrontation of the teleological
  theory each time. **Correct**: suppression, not replacement, implies spiraling.
- (d) Accept it; the test showed they learned it. *Diagnoses: performance-equals-learning.*

**Brief deliverable.** Add a "core concepts spiral" section to the brief: list five intuitive
theories the school will explicitly confront, at what ages, and what anomaly will be used for
each. Tag. Also: identify one intuitive theory *about schooling* in Brief v0 that Module 1 or 2
has already disturbed, and write two sentences on what replaced it.

### Module 3: Curiosity, motivation, and the adolescent mind

**Draws on:** `03-intellectual-lives-of-children` (Engel on curiosity's decline across school
years, inquiry, invention, and ideas as intellectual activity; how classrooms suppress questions),
`05-10-to-25` (Yeager: the mentor mindset vs. enforcer and protector mindsets; status and respect
as the adolescent's central concern; wise feedback; the "transparency statement"; stress-is-
enhancing reappraisal), `00-foundational-papers` (Gruber, Gelman & Ranganath 2014: curiosity
states enhance hippocampal-dependent memory for both target and incidental information via
dopaminergic midbrain activity).

**Learning objectives.** (a) Explain the neural and behavioral case that curiosity is a state that
improves encoding, and what triggers it; (b) diagnose an adult's interaction with a teenager as
enforcer, protector, or mentor and rewrite it; (c) design a classroom norm set that raises question-
asking rather than suppressing it.

**Load-bearing ideas.**
1. Curiosity is an information-gap state; it requires prior knowledge to notice the gap, and while
   it is active memory improves for everything nearby. Schools suppress it mostly by accident,
   through pacing and by treating questions as interruptions (Engel's observation counts of
   questions per hour).
2. Adolescents are exquisitely sensitive to status and respect. The mentor mindset (high standards
   plus high support, delivered with transparency about the adult's intent) outperforms both the
   enforcer (standards without support) and the protector (support without standards), and the
   mechanism is that it preserves the teenager's status while asking more of them.

**Curiosity hook.** "Engel observed classrooms and counted the questions children asked per
hour. Give a number for kindergarten and for fifth grade." (The drop is steep; the exact counts
will be in the `03` file.)

**Attempt (case prompt).** "A 15-year-old has stopped doing work in your school's math class. Her
teacher's current message is: 'I'm not going to keep chasing you. It's your choice.' Rewrite the
teacher's next conversation with her, then explain what you changed and why." Most learners will
soften the message (protector) or add consequences (enforcer). The reading then gives the third
option.

**Worked example.** *Decision: how does the school give feedback on written work?* Reasoning: (1)
Yeager's wise-feedback studies: a note stating high standards plus explicit belief the student can
reach them roughly doubled revision rates among students who most distrusted school. (2) The
mechanism is status: the feedback removes the threat that criticism means "you don't belong". (3)
So the feedback policy has three fixed parts: the standard, the specific gap, the statement of
belief and the next step. (4) It is paired with a norm that first drafts are expected to be
revised, so revision is not stigmatized. (5) Grades are withheld until after the revision cycle
(connects to Wiliam in M6). Resulting policy tagged [E] for wise feedback effects (with the note
that replication is mixed in some contexts, per `05`'s evidence-limits section), [H] for the
grade-withholding, [V] for revision-as-norm.

**Hinge questions.**

Q1. Per Gruber et al., when does curiosity most improve memory for an unrelated face shown between
trivia questions?
- (a) When the face is shown after the answer is revealed. *Diagnoses: reward-after model;
  actually the state during anticipation matters.*
- (b) When the face is shown while the person is waiting for the answer to a question they were
  curious about. **Correct**.
- (c) Only for the trivia answer itself, not incidental material. *Diagnoses: narrow-encoding
  model; the incidental effect is the striking finding.*
- (d) When the question was easy. *Diagnoses: fluency-equals-engagement; easy questions generate
  no gap.*

Q2. A teacher tells a student, "I'm giving you these comments because I have very high
standards and I know you can meet them." Which is the most accurate account of why this helps?
- (a) It raises the student's self-esteem. *Diagnoses: self-esteem theory of motivation.*
- (b) It makes the criticism feel less harsh. *Diagnoses: protector theory; softening is not the
  mechanism.*
- (c) It resolves the ambiguity about whether the criticism signals bias or low expectations,
  protecting the student's status. **Correct**.
- (d) It works only for high-achieving students. *Diagnoses: reverses the finding; effects were
  largest for students with low trust.*

Q3. A middle school wants to raise curiosity. Which is most likely to work per Engel?
- (a) A weekly "wonder hour" with open exploration. *Diagnoses: curiosity as a scheduled special
  event rather than a classroom norm.*
- (b) Teachers explicitly respond to student questions during lessons, even at the cost of pacing,
  and model their own uncertainty. **Correct**.
- (c) More hands-on science kits. *Diagnoses: materials-produce-curiosity.*
- (d) Rewarding students for asking questions. *Diagnoses: extrinsic-reward theory; risks
  undermining.*

**Brief deliverable.** Add a "how adults talk to students" section: three sentences the school
expects from every adult in the three canonical moments (criticism, refusal to do work, failure),
each showing the mentor mindset. Add a question-asking norm and how it will be measured. Tag.

### Module 4: Instruction: explicit teaching, productive failure, and when each wins

**Draws on:** `00-foundational-papers` (Kirschner, Sweller & Clark 2006 on why minimal guidance
fails), `01-how-learning-happens` (Rosenshine's principles, direct instruction evidence, the
expertise reversal effect, Project Follow Through), `04-productive-failure` (Kapur: problem-
solving before instruction with well-designed problems and later consolidation beats instruction-
then-problem-solving for conceptual understanding and transfer, with the boundary conditions
that matter).

**Learning objectives.** (a) State the Kirschner-Sweller-Clark argument and its evidence; (b) state
Kapur's argument and where it does *not* contradict KSC; (c) given a lesson goal and learner
profile, choose a sequence and defend it with the expertise-reversal effect.

**Load-bearing ideas.**
1. For novices, unguided discovery is worse than explicit, fully guided instruction; this is one
   of the most replicated findings in the field. Guidance fades as expertise grows (expertise
   reversal).
2. Productive failure is *not* unguided discovery: it is a designed generation phase (a problem
   with multiple plausible approaches, drawing on prior knowledge, in small groups) followed by
   explicit consolidation that contrasts student solutions with the canonical one. Its gains are on
   conceptual understanding and transfer, less on procedural fluency, and it depends on the
   consolidation being done well. Framed correctly, Kapur and Kirschner disagree on emphasis and
   on how much prior knowledge counts as "enough", not on the core mechanism.

**Curiosity hook.** "In Kapur's studies, the students who struggled first did *worse* during
the lesson and *better* on the test. What test, and why the reversal?"

**Attempt (productive failure, deliberately).** "Design a Year 7 lesson introducing standard
deviation. Then design it the opposite way. Predict which one wins on (i) a procedural post-test,
(ii) a conceptual post-test, (iii) a transfer test a month later, and say why." The learner will
predict explicit-first wins everything or PF wins everything; the reading shows it splits.

**Worked example.** *Decision: what is the school's default lesson structure, and when is it
overridden?* Reasoning: (1) Default is explicit: retrieval starter, small-step explanation with
worked examples, guided practice with high success rate, independent practice, because most
students are novices most of the time (Rosenshine). (2) Override to a PF sequence when the goal is
a *conceptual* idea, the students have relevant prior knowledge, the problem admits multiple
plausible approaches, and the teacher has a scripted consolidation. (3) The override is a named
lesson type ("generate-then-consolidate") with its own planning template, not a teacher's
improvisation. (4) The school explicitly forbids "discovery" as a lesson type without the
consolidation phase. Resulting policy tagged [E] for both mechanisms, [H] for the proportion of
lessons (say 15-25%) run as PF, [V] for the commitment to teach conceptual understanding rather
than only procedures.

**Hinge questions.**

Q1. Kirschner, Sweller & Clark's central argument is that minimally guided instruction fails
because:
- (a) Students lack motivation without a teacher directing them. *Diagnoses: motivational
  misreading.*
- (b) Searching a problem space consumes working memory that could be used to build schemas.
  **Correct**.
- (c) Students are not intelligent enough to discover principles. *Diagnoses: ability-deficit
  misreading; it is a load argument, not an ability argument.*
- (d) Discovery is fine for science but not for math. *Diagnoses: domain-specific misreading.*

Q2. Which condition is *not* required for productive failure to work, per Kapur?
- (a) Students have prior knowledge relevant to the problem. *Diagnoses: none; this is required.*
- (b) The problem admits multiple representations or solution methods. *This is required.*
- (c) Students solve the problem correctly before instruction. **Correct**: they almost never
  do; generating varied wrong solutions is the mechanism.
- (d) A consolidation phase compares student methods to the canonical one. *This is required.*

Q3. A teacher of experienced Year 12 chemists gives them a fully worked example for every problem
type. Test performance falls. Best explanation:
- (a) Worked examples only work in math. *Diagnoses: domain misreading.*
- (b) Expertise reversal: for learners with schemas, studying worked examples becomes redundant
  load and problem-solving practice is better. **Correct**.
- (c) Year 12 students are unmotivated by examples. *Diagnoses: motivational explanation.*
- (d) The examples were badly designed. *Diagnoses: implementation-quality explanation; possible
  but not what the evidence points to.*

**Brief deliverable.** Write the school's "default lesson and its named exceptions" as a half-
page, with the conditions for each exception stated as a checklist a teacher could apply. Tag.

### Module 5: Knowledge, curriculum, and the reading problem

**Draws on:** `06-beyond-the-science-of-reading` (Wexler: decoding is necessary, comprehension
depends on background knowledge and vocabulary; comprehension "skills and strategies" instruction
has small, quickly saturating effects; content-rich curriculum from early years; writing as a
lever), `10-creating-the-schools-our-children-need` (Wiliam on what a curriculum is for and why
curriculum choice matters more than most reforms), `01-how-learning-happens` (Recht & Leslie's
baseball study; Hirsch; knowledge and reading comprehension).

**Learning objectives.** (a) Explain why "reading comprehension" is not a transferable skill and
what that implies for the elementary day; (b) distinguish decoding instruction (settled, phonics)
from comprehension instruction (knowledge-dependent); (c) evaluate a curriculum by its knowledge
sequencing, not its skill labels.

**Load-bearing ideas.**
1. Comprehension is mostly a function of what you already know about the topic (Recht & Leslie's
   weak readers who knew baseball outperforming strong readers who did not). Teaching "finding the
   main idea" as a content-free skill yields a small, one-time gain. The elementary day must
   therefore be dense with sequenced content in history, science, geography, and the arts, from
   kindergarten.
2. Curriculum, understood as a coherent, cumulative sequence of what students will know, is one of
   the highest-leverage and lowest-cost decisions a school makes, and one of the most neglected
   (Wiliam).

**Curiosity hook.** "Take weak readers who know baseball and strong readers who don't. Give them
a passage about a baseball inning. Who comprehends it better?"

**Attempt (case prompt).** "Your elementary school's reading scores are low. Your literacy lead
proposes doubling the daily reading block and buying a comprehension-strategies program. Write
the two-paragraph memo you send back." Most learners with a product background will approve the
proposal on the grounds that more practice on the metric should move the metric.

**Worked example.** *Decision: what does the K-5 day look like?* Reasoning: (1) Decoding is
taught systematically and explicitly; this is settled and takes 30-45 min daily in K-2 [E]. (2)
The remainder of literacy time is content: read-alouds and texts about a sequenced set of topics
across science, history, and geography, with vocabulary taught in context, because comprehension
is knowledge [E]. (3) Comprehension strategies are taught briefly, once, not as a multi-year
strand [E]. (4) Writing is embedded in every content unit, as sentence-level work first (Wexler's
argument from The Writing Revolution), because writing about content consolidates both [E-ish,
labeled H for the specific method]. (5) The topic sequence is fixed school-wide so that Year 3
teachers can assume what Year 2 taught [H for the specific sequence, V for the choice of what
knowledge matters]. Policy: "Reading is 40% decoding and 60% knowledge in K-2, then knowledge-
dominant."

**Hinge questions.**

Q1. A Year 4 student decodes fluently but comprehends poorly. Most likely lever:
- (a) More comprehension-strategy lessons. *Diagnoses: skills theory of comprehension.*
- (b) More silent reading time with self-chosen books. *Diagnoses: volume theory; volume without
  knowledge building has weak effects.*
- (c) Building background knowledge and vocabulary on the topics of the texts. **Correct**.
- (d) Phonics review. *Diagnoses: misdiagnosis; decoding is not the bottleneck here.*

Q2. Wiliam argues that curriculum choice is high-leverage mainly because:
- (a) A good curriculum is cheaper than good teachers. *Diagnoses: cost-only reading.*
- (b) It determines what is actually taught regardless of teacher quality, and coherence across
  years compounds. **Correct**.
- (c) Curriculum standards are legally required. *Diagnoses: compliance reading.*
- (d) Students prefer structured content. *Diagnoses: preference reading.*

Q3. Which claim is best tagged [V] rather than [E]?
- (a) Systematic phonics improves decoding. *Diagnoses: over-tagging settled evidence as values.*
- (b) Background knowledge improves comprehension. *Same.*
- (c) Every child should learn the history of their own country before others'. **Correct**: a
  value choice about which knowledge.
- (d) Writing about content improves retention of it. *Diagnoses: over-tagging; this is at least
  [H]-to-[E].*

**Brief deliverable.** Add a K-5 knowledge sequence sketch (six topics per year across science
and social studies is enough) and the literacy time allocation. Add one paragraph on how the
school will decide what knowledge counts, explicitly marked [V].

### Module 6: Formative assessment as the engine of the classroom

**Draws on:** `07-embedding-formative-assessment` (Wiliam & Leahy's five strategies: clarifying
and sharing intentions and success criteria; eliciting evidence; feedback that moves learning
forward; activating students as instructional resources for each other; activating students as
owners of their learning; the techniques: hinge questions, no hands up, mini-whiteboards, comment-
only marking, exit passes; and Teacher Learning Communities as the implementation vehicle),
`10-creating-the-schools-our-children-need` (Wiliam's argument that formative assessment is the
best-evidenced classroom lever and TLCs the best way to spread it).

**Learning objectives.** (a) Explain what makes assessment formative (the decision it informs, not
the instrument); (b) write a hinge question whose distractors diagnose; (c) design a teacher
learning community that changes practice rather than shares ideas.

**Load-bearing ideas.**
1. Assessment is formative only if the evidence changes what happens next, in the lesson, for that
   student. The five strategies are the toolkit; the hinge question is the smallest unit: one
   question, mid-lesson, answered by all, that tells the teacher in under a minute whether to move
   on or reteach, and to whom.
2. Changing teaching practice requires sustained, structured, peer-accountable practice over
   months (TLCs), not workshops; and grades attached to comments cancel the comments (Butler
   1988).

**Curiosity hook.** "Butler gave students comments only, grades only, or grades plus comments.
Which group learned least, and why does it matter for your gradebook policy?"

**Attempt (productive failure).** "Write a single multiple-choice question for the end of a Year 8
lesson on photosynthesis that tells the teacher whether to move on. Then explain what each wrong
answer tells her." The learner will write a recall question; the reading shows why the
distractors must each map to a known misconception (and the learner has just done this format
for five modules, so the mechanism is felt).

**Worked example.** *Decision: what is the school's grading and feedback policy?* Reasoning: (1)
Grades on formative work suppress the effect of comments [E]. (2) Therefore formative work
receives comments only, and a small number of summative points per term receive grades [E for the
mechanism, H for the frequency]. (3) Every lesson has at least one all-student response check
(whiteboards or hinge question) [E]. (4) Teachers meet in TLCs monthly for 75 minutes, with a
fixed protocol: each teacher reports on one technique they tried and commits to one for next
month; peer observation is the accountability mechanism [E for TLC design, H for the cadence].
(5) Success criteria are shared, but co-constructed with students where possible [E]. Policy
tagged.

**Hinge questions.**

Q1. Which is a formative use of a test?
- (a) A quiz returned with scores so students know where they stand. *Diagnoses: information-
  to-student equals formative.*
- (b) A quiz whose results the teacher uses to regroup students for the next two lessons.
  **Correct**.
- (c) A quiz that is low-stakes. *Diagnoses: stakes define formativeness.*
- (d) A quiz written by the teacher rather than an external body. *Diagnoses: authorship defines
  formativeness.*

Q2. A hinge question is well designed if:
- (a) About half the class gets it right. *Diagnoses: difficulty-calibration theory.*
- (b) Each wrong answer corresponds to a specific misconception and the teacher can act in the
  same lesson. **Correct**.
- (c) It requires an extended written answer. *Diagnoses: rigor-equals-length; makes real-time
  reading impossible.*
- (d) It is asked at the end of the lesson. *Diagnoses: timing error; a hinge is mid-lesson so the
  lesson can change.*

Q3. A school runs a two-day formative assessment workshop with a famous speaker. Nine months later
practice is unchanged. Wiliam's most likely explanation:
- (a) Teachers are resistant to change. *Diagnoses: attribution to disposition.*
- (b) The techniques do not work in this context. *Diagnoses: evidence-doesn't-transfer.*
- (c) Practice changes only through sustained, small, accountable steps with peer support;
  workshops transmit knowledge but not habit. **Correct**.
- (d) The school needed a follow-up workshop. *Diagnoses: more-of-the-same.*

**Brief deliverable.** Add the assessment and feedback policy and the TLC design to the brief.
Write two hinge questions for a lesson in the school's core curriculum, with distractor
rationales, as an appendix demonstrating the standard.

### Module 7: The grammar of school and where deeper learning lives

**Draws on:** `09-in-search-of-deeper-learning` (Mehta & Fine: six years of observation in 30
American high schools; deeper learning as the intersection of mastery, identity, and creativity;
it appears at the periphery (electives, extracurriculars, clubs) far more than in the core; whole-
school models like no-excuses, project-based, and IB each succeed on some dimensions and fail on
others; the "grammar of schooling" and the need for teachers who have themselves experienced
deeper learning in a discipline), `08-extraordinary-learning-for-all` (Samouha, Wetzler & Henry
Wood: the Transcend approach, community-based design, the "leaps" from industrial-era to learner-
centered design, and codesign with communities).

**Learning objectives.** (a) Describe what Mehta & Fine actually saw, including the finding that
the periphery outperforms the core and why; (b) explain the three whole-school models' tradeoffs;
(c) apply the mastery/identity/creativity lens to a proposed design.

**Load-bearing ideas.**
1. Deeper learning happens where students have mastery, identity, and creativity at once, and
   this is rare in core classes because the grammar of school (age-grading, 50-minute periods,
   coverage, teacher isolation, Carnegie units) crowds it out. The periphery works because it has
   apprenticeship structure: authentic purpose, real audience, iteration, and a teacher who is a
   practitioner.
2. Whole-school models trade off: no-excuses models deliver mastery on measured outcomes and often
   struggle with identity and creativity; project-based models deliver identity and creativity and
   can under-deliver rigor in the disciplines; the best classrooms are pockets driven by
   individual teachers who love their discipline, and are fragile.

**Curiosity hook.** "Mehta and Fine went looking for deep learning in America's best high
schools. Where did they find most of it?"

**Attempt (case prompt).** "You have a choice between two 9th-grade schedules: eight 45-minute
periods, or four 90-minute blocks including a daily 90-minute interdisciplinary studio. Choose
and defend your choice in 200 words. Then predict what will go wrong." Learners will choose the
studio schedule; the reading complicates this (the studio becomes the periphery; the core stays
shallow).

**Worked example.** *Decision: how does the school bring apprenticeship structure into the core,
not just the periphery?* Reasoning: (1) Identify the features that make the periphery work:
purpose, audience, iteration, practitioner-teacher [E, observational]. (2) Do not add a studio
and leave the core alone; that reproduces the finding. (3) Instead, redesign the core disciplinary
course so each unit ends in a product with a real audience, drafts are expected (connects to M3
feedback norm), and the teacher's own disciplinary practice is visible [H]. (4) Hire and develop
teachers who have done the discipline, not only taught it [H, connects to M8]. (5) Keep the
schedule mostly conventional to avoid burning change capacity on structure; Mehta & Fine's point
is that structure is not the bottleneck [H]. (6) Protect the periphery anyway; it is where
identity lives [V]. Policy: "Every core course, every term, one authentic product."

**Hinge questions.**

Q1. Per Mehta & Fine, the main reason electives and clubs often show deeper learning than core
classes is:
- (a) Students choose them, so they are more motivated. *Diagnoses: choice-only theory; part of
  it, but the structural features matter more.*
- (b) They have apprenticeship-like structure: authentic purpose, audience, iteration, and a
  practitioner teacher. **Correct**.
- (c) They are not tested. *Diagnoses: testing-kills-learning theory.*
- (d) They have smaller classes. *Diagnoses: resource explanation.*

Q2. A founder plans a project-based school with no traditional courses. Mehta & Fine's evidence
suggests the most likely failure mode is:
- (a) Students will be bored. *Diagnoses: engagement-is-the-risk.*
- (b) Disciplinary mastery will be uneven and some projects will lack rigor. **Correct**.
- (c) Teachers will refuse to teach that way. *Diagnoses: adoption-is-the-risk.*
- (d) Parents will withdraw students. *Diagnoses: market-is-the-risk.*

Q3. "Deeper learning" in Mehta & Fine's sense requires:
- (a) Student choice of topic. *Diagnoses: choice-equals-depth.*
- (b) Mastery, identity, and creativity together. **Correct**.
- (c) Interdisciplinary content. *Diagnoses: integration-equals-depth.*
- (d) Technology-rich environments. *Diagnoses: tools-equal-depth.*

**Brief deliverable.** Rewrite the 16-year-old's Tuesday in Brief v0 so that the core courses show
at least one apprenticeship feature, and note what you deliberately kept conventional and why.
Add a paragraph on how the community will be involved in design (from `08`), tagged [V] and [H].

### Module 8: What actually moves outcomes: teachers, policy, and the evidence

**Draws on:** `10-creating-the-schools-our-children-need` (Wiliam's review of popular reforms:
class size, technology, charter schools, school choice, curriculum, firing bad teachers, hiring
better ones; his conclusion that teacher quality is the biggest in-school factor and that
improving existing teachers via formative assessment and TLCs beats every alternative on cost and
effect), `01-how-learning-happens` (the meta-analytic and effect-size literacy needed to read
this), `11-improvement-in-action` (Bryk on why interventions vary by context).

**Learning objectives.** (a) Rank the common reforms by evidence and cost and explain the ranking;
(b) read an effect size and know its three main traps (age, test design, and time span); (c)
state the case for developing teachers over selecting them.

**Load-bearing ideas.**
1. Teacher quality varies enormously and matters more than any other in-school factor; but you
   cannot hire your way to a great faculty (the signal at hiring is weak and the supply is
   limited), so the institutional lever is developing the teachers you have, primarily in
   classroom formative assessment, primarily through TLCs. Cost per unit of learning gain is the
   metric that makes this obvious.
2. Most popular reforms (smaller classes, more technology, school choice, structural change) have
   small effects, high costs, or both. Effect sizes must be read with care: they shrink with
   student age, inflate with test proximity to the intervention, and are not comparable across
   studies without adjustment.

**Curiosity hook.** "Wiliam estimates the effect of being in a top-quartile versus bottom-
quartile teacher's class for a year. How many months of extra learning is it?"

**Attempt (case prompt).** "You have $600k of annual discretionary budget. Options: reduce class
sizes from 26 to 22; hire an instructional coach per department; buy 1:1 devices and adaptive
software; raise salaries 8% to attract stronger applicants. Allocate and justify." Product
people love adaptive software and salary; the reading gives them the cost-effectiveness lens.

**Worked example.** *Decision: hiring versus development strategy.* Reasoning: (1) Hiring signals
(credentials, interview performance, even demo lessons) predict later effectiveness weakly [E].
(2) The variation among teachers already in the building is large [E]. (3) Formative assessment
practice change via TLCs has among the best effect-per-dollar of any known intervention [E, with
Wiliam's own caveats on effect-size comparability]. (4) Therefore hire for coachability and
disciplinary knowledge, invest heavily in the first three years of development, and make TLC
participation a condition of employment [H for the specific criteria, V for the compact]. (5)
Retain by making the school a place teachers get visibly better; the mentor mindset applies to
adults too [H]. Policy: "We select for learnability and build for effectiveness."

**Hinge questions.**

Q1. Wiliam's argument against relying on firing weak teachers and hiring stronger ones is mainly:
- (a) It is unkind. *Diagnoses: values reading of an evidence argument.*
- (b) The predictive validity of hiring signals is low and the supply of proven-effective
  teachers is small, so it barely moves the average. **Correct**.
- (c) Unions prevent it. *Diagnoses: political-constraint reading.*
- (d) All teachers are roughly equal. *Diagnoses: reverses the premise; variation is the whole
  point.*

Q2. Two interventions report effect sizes of 0.4. One was measured on 7-year-olds with a
researcher-designed test one week later; the other on 15-year-olds with a standardized test a year
later. Which is more impressive?
- (a) The first, because 0.4 is large for young children. *Diagnoses: reverses the age effect;
  effect sizes are naturally larger in young children.*
- (b) The second. **Correct**: older students, standardized test, delayed measure all deflate
  effect sizes.
- (c) Neither; 0.4 is 0.4. *Diagnoses: effect sizes as universal currency.*
- (d) The first, because a shorter delay means a cleaner measurement. *Diagnoses: proximity
  equals validity.*

Q3. The best-evidenced use of $1 of school improvement money, per Wiliam, is:
- (a) Reducing class size. *Diagnoses: intuitive-and-popular.*
- (b) Technology. *Diagnoses: modernity theory.*
- (c) Sustained, structured teacher development in formative assessment. **Correct**.
- (d) Performance pay. *Diagnoses: incentive theory; the evidence is weak.*

**Brief deliverable.** Add a staffing and development section: hiring criteria, first-three-year
development plan, TLC compact, and a table allocating the discretionary budget with the
cost-per-gain reasoning shown. Tag.

### Module 9: Running the school as an improvement system

**Draws on:** `11-improvement-in-action` (Bryk: the six improvement principles; see the system
that produces the outcomes; variation in performance is the problem to solve; PDSA cycles; driver
diagrams; practical measurement distinct from accountability and research measurement; networked
improvement communities; the cases in the book), `08-extraordinary-learning-for-all` (codesign,
prototyping, community learning), `07-embedding-formative-assessment` (TLCs as an improvement
structure at the classroom level).

**Learning objectives.** (a) Draw a driver diagram for a school outcome; (b) design a PDSA cycle
with a practical measure and a prediction; (c) explain the difference between measurement for
accountability, research, and improvement, and what each does to behavior.

**Load-bearing ideas.**
1. Outcomes are produced by systems; a school that wants to improve must make its system
   visible (process maps, driver diagrams), study variation (who is it working for, who not,
   under what conditions), and change through small, rapid, predicted, measured cycles that
   scale only after they work reliably across contexts.
2. Practical measures are frequent, cheap, embedded in the work, and sensitive to change; they
   are not the accountability measures. Using accountability measures to drive improvement
   produces gaming and despair; using research measures produces paralysis.

**Curiosity hook.** "Bryk's teams often find that a promising intervention works for 60% of
students and hurts 20%. What is the first question improvement science asks about that?"

**Attempt (productive failure).** "Your school's Year 7 math attainment is flat. Draw the
system that produces it, name three drivers you could change, and write the first two-week test
of one of them with a prediction and a measure." Learners will write an intervention rather than
a system, choose an annual test as the measure, and forget the prediction.

**Worked example.** *Decision: what is the school's improvement operating system?* Reasoning: (1)
One primary aim per year, stated as a measurable outcome for a specific population [E-method, V-
aim]. (2) A driver diagram maintained by a small improvement team; every initiative must attach to
a driver or be declined [H]. (3) PDSA cycles of two to four weeks, each with a written prediction
before it runs, a practical measure collected in the work, and a study meeting; three cycles per
term per team [E-method, H-cadence]. (4) Practical measures live in a lightweight dashboard
separate from the gradebook and never feed teacher evaluation [V, and E for the reason]. (5) TLCs
(M6) are the classroom-level instance of this same loop [H]. (6) Community codesign sessions
(`08`) feed the driver diagram, not the aim [V]. Policy: "Every change is a test with a
prediction."

**Hinge questions.**

Q1. Bryk's "see the system" principle means:
- (a) Use data dashboards. *Diagnoses: tools-equals-seeing.*
- (b) Map the actual processes and conditions that produce the outcome, including the ones
  nobody designed. **Correct**.
- (c) Hold everyone accountable for the outcome. *Diagnoses: accountability-equals-system.*
- (d) Adopt a whole-school program. *Diagnoses: program-equals-system.*

Q2. A PDSA cycle without a written prediction is deficient because:
- (a) Nobody will remember what was planned. *Diagnoses: documentation reading.*
- (b) Without a prediction the result cannot surprise you, so the theory of the system is never
  tested or revised. **Correct**.
- (c) Predictions are required for research ethics. *Diagnoses: compliance reading.*
- (d) Predictions motivate the team. *Diagnoses: motivational reading.*

Q3. Which is a practical measure, in Bryk's sense, for "students revise their writing"?
- (a) End-of-year state writing score. *Diagnoses: accountability measure used for improvement.*
- (b) A validated writing self-efficacy scale administered each term. *Diagnoses: research
  measure; too slow and not embedded.*
- (c) Weekly count of drafts submitted per student, pulled from the existing platform.
  **Correct**.
- (d) Teacher's overall impression at the end of the unit. *Diagnoses: too vague to detect
  change.*

**Brief deliverable.** Add the improvement operating system to the brief, including a driver
diagram for the school's year-one aim and one fully specified PDSA cycle. Convert three [H] items
from earlier modules into PDSA cycles with predictions and measures.

### Module 10: Integration: tensions, decision rules, and the unified model

**Draws on:** all files, with the "Connections" and "Evidence strength & limits" sections of each
being the primary reading.

**Learning objectives.** (a) Reproduce the unified model from memory and explain each arrow; (b)
for each major tension, state the conditional decision rule and the evidence behind each branch;
(c) re-tag Brief v0 correctly and explain the errors in the original tagging.

**Load-bearing ideas.**
1. The debates in this curriculum are mostly resolved by conditions, not by winners: the question
   is never "explicit or inquiry" but "for whom, for what goal, at what point in expertise, with
   what consolidation".
2. Institutions make good learning happen consistently by making the right instructional
   defaults easy, making variation visible, and developing adults through the same learning
   mechanisms that apply to children.

**Attempt.** Before reading the tensions list in section 4b: "Write down the five biggest
disagreements among the authors you have met, and for each say who you side with and under what
conditions you would switch." Compare to section 4b.

**Worked example.** The unified model (4a), walked through with one worked path: a policy decision
at the institution level ("comment-only marking") traced down through the design level
(formative feedback that moves learning) to the minds level (retrieval plus corrective feedback,
status protection) and back up through the improvement loop (practical measure: revision rate).

**Hinge questions.**

Q1. "Productive failure contradicts Kirschner, Sweller & Clark." Best assessment:
- (a) True; you must pick a side. *Diagnoses: winner-take-all reading.*
- (b) False; they agree entirely. *Diagnoses: false harmony; they disagree on prior-knowledge
  thresholds and on emphasis.*
- (c) Mostly false; PF includes explicit consolidation and targets learners with relevant prior
  knowledge, so it satisfies KSC's core mechanism while disagreeing on how much guidance novices
  need up front. **Correct**.
- (d) True for math, false for science. *Diagnoses: domain reading.*

Q2. Which is the correct chain from institution to mind for the policy "all teachers use hinge
questions"?
- (a) Institution mandates; teachers comply; students learn more. *Diagnoses: mandate theory.*
- (b) TLCs build the habit; the hinge question makes student thinking visible; the teacher's next
  move is adapted; students receive instruction matched to their current schema, reducing load and
  correcting misconceptions in time. **Correct**.
- (c) Hinge questions test students; testing improves memory. *Diagnoses: retrieval-only reading;
  true but misses the adaptive mechanism.*
- (d) Students see teachers care; motivation rises. *Diagnoses: affective-only reading.*

Q3. A claim in your brief reads "small classes improve learning." Correct tag and reason:
- (a) [E]; it is obvious. *Diagnoses: obviousness as evidence.*
- (b) [E] with caveat: effects are real but small and expensive relative to alternatives.
  **Correct**.
- (c) [V]; class size is a values choice. *Diagnoses: over-tagging.*
- (d) [H]; no one has studied it. *Diagnoses: ignorance of the literature.*

**Brief deliverable.** Re-tag every claim in Brief v0. Write a one-page changelog: for each
[E]/[H]/[V] error in v0, the module that fixed it.

### Capstone: the brief, the defense, the first 90 days

See section 4f.

---

## 4. Cross-cutting synthesis artifacts

### 4a. Unified model: learning → design → institution (diagram spec)

Three horizontal bands, bottom to top, connected by upward arrows labeled "constrains" and
downward arrows labeled "enables". A fourth element, a loop on the right-hand edge, labeled
"improvement", connects the top band back to the bottom.

**Band 1, Minds (bottom).** Four boxes in a row:
- Working memory: small, fragile; the bottleneck. (Sweller)
- Long-term memory: schemas; the site of expertise; strengthened by effortful retrieval, spacing,
  error-correction. (Sweller, Ranganath, Roediger, Bjork)
- Prior knowledge: intuitive theories; assimilates new input; changed only by confrontation and
  revisiting. (Shtulman, Posner, Chi, Vosniadou, Amin)
- Motivational state: curiosity (information gap) and status/respect (adolescence); modulates
  encoding and effort. (Gruber, Engel, Yeager)

Arrows within the band: prior knowledge → working memory ("determines what counts as a chunk");
motivational state → long-term memory ("modulates encoding"); working memory ↔ long-term memory
("schema construction / retrieval").

**Band 2, Design (middle).** Four boxes, each sitting above the mind box it primarily serves:
- Instruction: explicit by default, guided generation when conditions hold, fading with expertise.
  (Kirschner, Rosenshine, Kapur)
- Curriculum: coherent, cumulative knowledge; concept spirals; content-rich literacy. (Wexler,
  Wiliam, Shtulman)
- Assessment: formative; hinge questions; comment-only feedback; success criteria. (Wiliam & Leahy)
- Relationship: mentor mindset; wise feedback; question-welcoming norms. (Yeager, Engel)

Upward arrows from Band 1 to Band 2 are labeled with the constraint: "load limits pacing and
guidance", "schemas determine readiness", "theories determine what must be confronted", "status
determines how feedback lands".

**Band 3, Institution (top).** Four boxes:
- Adult learning: TLCs; hiring for learnability; development over selection. (Wiliam 2018, Wiliam
  & Leahy)
- Structure: schedule, grouping, and the grammar of school; apprenticeship features in the core.
  (Mehta & Fine)
- Community and purpose: codesign; what knowledge counts; identity. (Samouha et al., Mehta & Fine)
- Improvement system: aim, driver diagram, PDSA, practical measures. (Bryk)

Downward arrows from Band 3 to Band 2 are labeled "makes the default easy" (adult learning →
instruction and assessment), "gives it time and audience" (structure → instruction), "decides
what is worth knowing" (community → curriculum).

**The loop.** From "Improvement system" in Band 3, an arrow descends the right edge past Band 2
to Band 1 with the label "practical measures of what is happening in minds (retrieval, revision,
misconception rates)", and returns up the left edge labeled "predictions tested, defaults
revised". This loop is the point of the diagram: the institution is the thing that learns.

**Rendering notes.** Each box carries its [E]/[H]/[V] weight as a small badge: Band 1 boxes are
mostly [E]; Band 2 is [E] for mechanisms and [H] for parameters; Band 3 is [H] and [V] heavy.
The badge distribution itself teaches something: certainty declines as you go up.

### 4b. Major tensions with conditional decision rules

Each is written as: the tension, who argues what, the decision rule, what would make you switch.

1. **Explicit instruction vs. productive failure.** (Kirschner/Sweller vs. Kapur.) Rule: default
   explicit. Use generate-then-consolidate when all four hold: conceptual (not procedural) goal;
   learners have relevant prior knowledge; the problem admits multiple plausible approaches; a
   scripted consolidation contrasts student methods with the canonical one. Never use unguided
   discovery. Switch signal: if PF lessons show weak consolidation on observation, or procedural
   fluency drops on practical measures, revert to explicit for that unit.

2. **Knowledge vs. curiosity/inquiry.** (Wexler/Hirsch vs. Engel.) This is a false tension once
   you accept Gruber: curiosity requires knowledge to notice a gap. Rule: knowledge-rich
   curriculum is the substrate; curiosity is protected by classroom norms (questions answered,
   uncertainty modeled, pacing that allows detours) rather than by content-free exploration time.
   Switch signal: if question rates per hour fall over the years in your own classrooms, the norms
   are failing; fix the norms, not the curriculum.

3. **Standardization vs. community design.** (Wiliam/Wexler's coherence argument vs. Samouha et
   al.'s codesign.) Rule: standardize the mechanisms (retrieval, feedback, TLCs, the default
   lesson) and the knowledge sequence within a discipline; codesign the purpose, the culture,
   the periphery, and which knowledge is prioritized where the evidence is silent [V]. Switch
   signal: if community codesign starts proposing to change mechanisms (e.g. "drop phonics"), that
   is a governance failure; the compact should say which layer is open.

4. **Accountability vs. improvement.** (External accountability regimes vs. Bryk.) Rule: keep the
   two measurement systems physically and culturally separate; improvement measures are never
   used in evaluation; accountability measures are reported, not managed to. Switch signal: if
   practical measures start improving while accountability measures do not over two years, the
   drivers are wrong; if the reverse, someone is gaming.

5. **Mastery vs. identity and creativity.** (No-excuses models vs. project-based models; Mehta &
   Fine.) Rule: mastery first in the core, with one authentic product per course per term;
   identity and creativity concentrated in a protected periphery that every student must
   participate in. Switch signal: if the periphery becomes the only place students say they learn,
   the core has failed; if core scores rise and student voice collapses, the periphery is being
   starved.

6. **Selecting teachers vs. developing them.** (Folk "hire the best" vs. Wiliam.) Rule: develop.
   Hire for disciplinary depth and coachability; make the first three years a structured
   development program. Switch signal: if after three years of TLCs the within-school variation in
   teacher effectiveness has not narrowed, the TLC design is broken (usually: no accountability
   for trying techniques, or turnover).

7. **Testing as measurement vs. testing as learning.** (Folk view vs. Roediger, Ranganath.) Rule:
   most testing is for learning: frequent, low-stakes, comment-only, spaced. A small number of
   summative points exist for reporting. Switch signal: if students or parents treat every check as
   a judgment, the communication has failed; rename and reframe.

8. **Confront misconceptions vs. avoid them.** (Some direct-instruction proponents argue against
   showing wrong answers; Shtulman/Chi/Kapur argue for confrontation.) Rule: confront, but only
   after the correct model has been made intelligible, and always with immediate correction; never
   leave a wrong model as the last thing seen. Switch signal: if hinge-question distractor rates for
   a misconception rise after a confrontation lesson, the confrontation is being remembered as the
   content; restructure.

9. **Structural reform vs. instructional reform.** (Schedule/school-model enthusiasts vs. Wiliam
   and Mehta & Fine.) Rule: spend change capacity on instruction, assessment, and adult learning
   first; keep structure conventional unless a specific instructional need requires it (e.g. 90-
   minute blocks for the studio). Switch signal: if instructional changes are blocked by structure
   (no common planning time for TLCs), change structure, minimally.

10. **Adolescent autonomy vs. adult direction.** (Protector and enforcer mindsets vs. Yeager's
    mentor mindset.) Rule: high standards, high support, transparency about intent, and choice
    within structure. Switch signal: if compliance rises while effort quality falls, you have
    drifted to enforcer; if effort quality falls while satisfaction rises, protector.

### 4c. School-design brief template

The learner's brief uses this template from Module 1 onward, versioned. Every declarative
sentence in sections 3-9 carries a tag. Untagged sentences fail the capstone rubric.

```
# <School name> — Design Brief v<N>
Changelog since v<N-1>: (bullet per change, with the module that motivated it)

## 1. Purpose and community                         [mostly V]
Who the school serves; what "world-class" means here; how the community is involved in design.

## 2. The three Tuesdays                             [narrative; tagged inline]
A February Tuesday for a 7-, 12-, and 16-year-old, minute by minute for one lesson each.

## 3. Model of the learner                            [mostly E]
The five commitments about memory, prior knowledge, and motivation the school designs around.

## 4. Curriculum                                      [E for mechanisms, V for content choices]
Knowledge sequence sketch; concept spirals; literacy allocation; what is deliberately excluded.

## 5. Instruction                                     [E defaults, H parameters]
Default lesson; named exceptions with conditions; homework and practice policy.

## 6. Assessment and feedback                         [E mechanisms, H cadence]
Formative toolkit; grading policy; hinge-question standard; reporting to families.

## 7. Adults                                          [E for TLCs, H for hiring criteria]
Hiring; first-three-years development; TLC compact; how adults talk to students.

## 8. Structure                                       [H]
Schedule; grouping; the periphery; what is kept conventional and why.

## 9. Improvement system                              [E method, V aim]
Year-one aim; driver diagram; PDSA cadence; practical measures; separation from accountability.

## 10. Open hypotheses register                       [H]
Every [H] in sections 3-9, with the PDSA cycle or evidence that would resolve it.

## 11. Value commitments register                     [V]
Every [V], with one sentence on who might reasonably disagree and why.
```

### 4d. Scenario casebook (founder dilemmas)

Each case is 100-200 words in the deck, ends with "What do you do, and which two authors are
arguing in your head?", and has a model answer that names the tension from 4b. The eighteen
cases:

1. **The phonics parent.** A vocal parent group demands a "balanced literacy" approach with
   leveled readers and less phonics, citing a neighboring school's results. (Wexler; tension 3.)
2. **The star teacher who hates TLCs.** Your highest-performing teacher refuses to attend
   TLCs, saying she has nothing to learn from peers. (Wiliam; tension 6; Yeager for the
   conversation.)
3. **The board wants test scores by year two.** The board sets a target on the state test for
   year two, and wants monthly progress reports against it. (Bryk; tension 4.)
4. **The project-based pitch.** A well-funded partner offers to make the school a project-based
   flagship with their curriculum and coaching. (Mehta & Fine; tension 5.)
5. **The kid who "just doesn't care".** A 14-year-old has stopped working, and his advisor
   proposes a behavior contract with consequences. (Yeager; tension 10.)
6. **The homework revolt.** Families complain that homework is "review of old stuff" and not
   what was taught today; some want more, some none. (Sweller/Roediger; tension 7.)
7. **The gradebook.** Teachers ask for grades on all work so students "take it seriously".
   (Wiliam & Leahy; tension 7.)
8. **The struggling PF lesson.** Observations show generate-then-consolidate lessons ending with
   ten minutes of rushed, muddled consolidation. (Kapur; tension 1.)
9. **The adaptive software vendor.** A vendor offers AI tutoring for math with impressive pilot
   data from a different context. (Wiliam on effect sizes; Bryk on variation; tension 9.)
10. **The schedule war.** Teachers want 90-minute blocks for depth; the math department wants
    daily 50-minute lessons for spacing. (Mehta & Fine vs. Cepeda; tension 9.)
11. **The evolution unit.** A community subgroup objects to how evolution is taught; another
    objects to teaching it at all. (Shtulman; tension 3; the [V] register.)
12. **The 60/20 result.** A PDSA on a reading intervention shows 60% of students improving,
    20% getting worse. The team wants to scale it. (Bryk.)
13. **The curiosity audit.** A staff member counts questions per hour and finds fifth graders
    asking almost none. Some teachers say it is because the curriculum is too packed. (Engel vs.
    Wexler; tension 2.)
14. **The new hire with the great demo lesson.** A candidate gives a brilliant demo lesson but
    bristles at feedback. (Wiliam on hiring signals; tension 6.)
15. **The misconception that got stronger.** After a "confront the misconception" unit, hinge
    data show more students selecting the misconception distractor. (Chi, Kapur; tension 8.)
16. **The discovery-learning elective.** A beloved elective is pure unguided exploration and
    students love it. Should it be brought into line with the default lesson? (KSC vs. Mehta &
    Fine on the periphery; tensions 1 and 5.)
17. **The dashboard that became a stick.** The principal starts using PDSA practical measures in
    teacher evaluations. (Bryk; tension 4.)
18. **The knowledge-sequence fight.** Two history teachers want to teach different periods in
    Year 5; each has a good argument. (Wiliam on coherence; tension 3; the [V] register.)

### 4e. Spaced-repetition deck plan

Format: plain-text Q/A cards suitable for Anki or a Markdown flashcard tool; ~180 cards total,
built incrementally. Each module contributes 12-18 cards in four types:

- **Recall (4-5 per module).** "Name the three types of cognitive load." "State Posner's four
  conditions." "What are Wiliam & Leahy's five strategies?"
- **Explain-why (3-4 per module).** "Why does grading formative work suppress the effect of
  comments?" "Why does curiosity require prior knowledge?"
- **Apply (3-4 per module).** Short scenarios: "A teacher reads slide text aloud; name the effect
  and the fix." Cases from 4d appear here in compressed form.
- **Spot-the-misconception (2-3 per module).** A plausible wrong claim to correct: "'Productive
  failure means letting students discover the method.' What is wrong with this?"

Plus 20 integration cards from Module 10 (tensions and decision rules: "State the rule for
explicit vs. PF and the switch signal") and 12 "evidence strength" cards ("How strong is the
evidence for wise feedback, and what is the main limit?").

Scheduling: the retrieval sessions in section 5 use the deck; cards are introduced the day after
their module, reviewed at intervals of 1, 3, 7, and 14 days within the course, then handed to the
learner's own SRS. Cards are tagged by module and by tension so that retrieval sessions can be
deliberately interleaved (each session pulls from at least three modules). Cards the learner gets
wrong twice are flagged for a 5-minute re-read of the specific book-file section, not the module.

### 4f. Capstone

**Deliverable 1: Design Brief v5** (the template in 4c, fully tagged, with changelog from v0 and
the open-hypotheses and value-commitment registers). Target 3,000-4,000 words.

**Deliverable 2: The defense.** A written response (or recorded 20-minute talk) to six challenges
drawn from the casebook, chosen by rolling dice or by the co-planner, at least two of which attack
the learner's own [V] commitments. The learner must name the tension, apply the rule, and state
the switch signal.

**Deliverable 3: The first 90 days.** A one-page plan: the year-one aim, the driver diagram, the
first three PDSA cycles with predictions and practical measures, the TLC launch, and the three
things the founder will personally observe in classrooms every week.

**Rubric** (each criterion scored 1-4; 4 is "a thoughtful head of school would sign this"):

1. *Model of the learner is correct and load-bearing.* The five commitments are accurate to the
   evidence, and every instruction/assessment decision can be traced to one of them. (Fails if
   learning styles, motivation-precedes-competence, or knowledge-is-obsolete appear untagged.)
2. *Instructional defaults and exceptions are conditional, not ideological.* The default lesson is
   explicit; exceptions have stated conditions; unguided discovery is excluded; the expertise-
   reversal effect is visible in how scaffolding changes across ages.
3. *Curriculum is knowledge-rich, sequenced, and honest about values.* A real sequence sketch
   exists; the [V] register names who might disagree.
4. *Assessment is genuinely formative.* Hinge questions meet the standard; grading policy reflects
   Butler; TLCs have an accountability mechanism.
5. *Adults are developed, not merely selected.* Hiring criteria, development plan, and compact are
   coherent with Wiliam; the mentor mindset is applied to adults.
6. *The core is designed for depth, not just the periphery.* Every core course has an
   apprenticeship feature; the periphery is protected; structure is changed only where instruction
   requires it.
7. *The improvement system is real.* A driver diagram, PDSA cycles with written predictions,
   practical measures separated from accountability.
8. *Tagging discipline.* Every claim tagged; no [E] on a contested finding without a caveat; no
   [V] laundered as [E]; the open-hypotheses register is non-empty and specific.
9. *Defense quality.* Each challenge answered by naming the tension, applying the rule, stating
   the switch signal, and acknowledging what the learner does not know.
10. *Delta from v0.* The changelog shows at least eight substantive reversals of v0 positions,
    each attributed to a module and an author.

Pass is 32/40 with no criterion below 2. "World-class" for the purpose of this course means
36/40 with 4s on criteria 1, 2, 7, and 8: those are the four that distinguish a school built on
how learning works from a school built on how schools usually look.

---

## 5. Spaced schedule: three weeks, 45-60 minutes a day

Retrieval days (R) use the deck and one casebook case; they never introduce new content. Modules
are split across two days where they exceed 60 minutes, with the attempt and reading on day one
and the worked example, hinge questions, and deliverable on day two, because a night's sleep
between generation and consolidation is itself a spacing interval.

| Day | Session | Content | Min |
|-----|---------|---------|-----|
| 1 | M0 | Diagnostic (20) + opening design challenge (40). Brief v0. | 60 |
| 2 | M1a | Hook, attempt (trapezoid lesson), reading map for 00/01/12. | 50 |
| 3 | M1b | Worked example (homework policy), hinge Qs, brief diff. Deck: M1 cards introduced. | 50 |
| 4 | M2a | Hook, attempt (sweater heat), reading map for 02/13/00. | 50 |
| 5 | R1 | Deck: M1 cards (day-1 and day-3 reviews). Case 6 (homework revolt). Re-attempt the trapezoid lesson from memory; compare with day-2 version. | 40 |
| 6 | M2b | Worked example (concept spiral), hinge Qs, brief diff. Deck: M2 cards. | 50 |
| 7 | M3 | Full module: hook, case (the 15-year-old), reading map for 03/05/00, worked example (feedback), hinge Qs, brief diff. Deck: M3 cards. | 60 |
| 8 | R2 | Deck: M1 (day-7), M2, M3 cards interleaved. Case 5 (the kid who doesn't care). Free recall: write the unified model's bottom band from memory. | 40 |
| 9 | M4a | Hook, attempt (standard deviation two ways), reading map for 00/01/04. | 55 |
| 10 | M4b | Worked example (default lesson and exceptions), hinge Qs, brief diff. Deck: M4 cards. | 50 |
| 11 | M5 | Full module (reading problem). Deck: M5 cards. | 60 |
| 12 | R3 | Deck: M1-M5 interleaved, M1 day-14 review. Cases 8 (struggling PF lesson) and 1 (phonics parent). Brief v2 checkpoint: re-tag everything so far. | 45 |
| 13 | M6 | Full module (formative assessment). Deck: M6 cards. | 60 |
| 14 | M7 | Full module (grammar of school). Deck: M7 cards. | 60 |
| 15 | R4 | Deck: M2-M7 interleaved. Cases 7 (gradebook) and 4 (project-based pitch). Write two hinge questions cold for a lesson you have not planned. | 45 |
| 16 | M8 | Full module (what moves outcomes). Deck: M8 cards. | 60 |
| 17 | M9a | Hook, attempt (Year 7 math system), reading map for 11/08. | 50 |
| 18 | M9b | Worked example (improvement OS), hinge Qs, brief diff. Deck: M9 cards. | 50 |
| 19 | R5 | Deck: all modules, weighted to M4-M9. Cases 12 (60/20 result), 17 (dashboard as stick), 9 (adaptive software vendor). Draw the full unified model from memory; compare to 4a. | 50 |
| 20 | M10 | Integration: attempt (five disagreements), tensions reading, worked path through the model, hinge Qs, re-tag Brief v0 with changelog. | 60 |
| 21 | R6 + Capstone prep | Deck: integration and evidence-strength cards. Retake the day-1 diagnostic; compare answers and confidence. Draft Brief v5 outline and pick capstone defense cases. | 50 |
| 22-24 | Capstone | Brief v5 (90 min), defense (45 min), first 90 days (45 min), spread over three sittings. | 180 |

Total scheduled: 21 content/retrieval days at about 52 minutes average, plus 3 capstone
sittings. Roughly 21.5 hours including capstone; a learner who takes the 45-minute floor on
retrieval days and trims the capstone lands near 17.

Post-course: the deck is handed to the learner's own SRS with cards spaced at 1-3 months. The
casebook cases not used during the course (about eight) are scheduled one per week for two
months, each answered in 200 words against the brief.

---

## 6. What the curriculum is missing for someone actually founding a school

The curriculum is excellent on minds and design and honest about institutions, but it is a
learning-science curriculum, not a school-founding curriculum. The gaps below are labeled
by how much they matter and by how confident the recommendation is. None of them should be
added as full books; each is a compact addition of one to three hours, and most belong in a
"Founder's supplement" module inserted between M9 and M10 or taken after the capstone.

**Critical gaps (the school will fail without them, and the curriculum says nothing).**

1. *School finance and the operating model.* Per-pupil revenue, staffing ratios as the dominant
   cost, facilities, the enrollment ramp, and the runway math. Recommendation: a two-hour session
   building a five-year model in a spreadsheet, using public per-pupil figures for the intended
   jurisdiction. Sources: jurisdiction-specific charter or independent-school authorizer guidance;
   a finance primer from a charter support organization. Honest label: this is management
   knowledge, not learning science; nothing in the thirteen books helps.

2. *Governance and law.* Legal form (charter, independent, public), board composition and role,
   the authorizer or regulator relationship, admissions law, child safeguarding obligations,
   employment law, data privacy for minors, accessibility obligations. Recommendation: one hour
   with a jurisdiction-specific checklist and a conversation with a lawyer who has opened a school;
   no substitute. Label: entirely jurisdictional; the course cannot supply it, only flag it.

3. *Special education and inclusion.* The curriculum is nearly silent on students with
   disabilities, on legal entitlements (IEPs or equivalents), on multi-tiered systems of support,
   and on how explicit instruction and formative assessment interact with intensive intervention.
   This is not a peripheral gap; 10-20% of any enrolled population will be affected. Recommendation:
   a compact module on tiered support, the legal minimum in the jurisdiction, and the evidence base
   for explicit, intensive, small-group intervention (which is consistent with M4 and M5, so it
   integrates well). Label: partly [E] (intervention evidence is strong), partly legal.

4. *Early literacy and numeracy specifics.* Wexler covers the comprehension argument and endorses
   systematic phonics, but the curriculum does not teach what a systematic phonics scope and
   sequence looks like, how to screen for dyslexia risk, or anything about early numeracy (number
   sense, subitizing, the evidence on explicit early math instruction). Recommendation: ninety
   minutes on a phonics scope and sequence and a screening protocol; sixty minutes on early number
   sense with the key studies. Label: [E] heavy; this is among the best-evidenced territory in
   education and should be treated as settled.

**Important gaps (the school will be mediocre without them).**

5. *Mathematics curriculum and instruction.* Beyond productive failure examples, the curriculum
   does not address math curriculum design: sequencing, the role of fluency and procedural
   automaticity, the evidence on mastery-based progression, worked-example-heavy math programs,
   and the persistent debates about problem-based approaches. Recommendation: two hours,
   including a comparison of two or three well-regarded math curricula against the M1/M4
   mechanisms. Label: the mechanisms are [E]; specific curriculum choices are [H].

6. *Hiring, teacher labor markets, and retention.* Wiliam tells you not to rely on hiring; he
   does not tell you how to hire, what the market looks like in your region, how to structure
   compensation, or how to retain. Recommendation: one hour on the local supply picture and the
   evidence on retention (working conditions, especially leadership and collegial support,
   dominate salary at the margin). Label: [E] for retention drivers, jurisdictional for market.

7. *Measurement literacy beyond effect sizes.* The curriculum teaches effect-size reading (M8)
   and practical measurement (M9), but not how to choose or build assessments: reliability,
   validity, standard-setting, the difference between norm- and criterion-referenced tests, and
   how to report to families without lying. Recommendation: ninety minutes on assessment design
   basics; a short treatment of how to build a school's own interim assessments so that they
   serve learning rather than reporting. Label: [E] for the psychometrics; [V] for reporting
   choices.

8. *Behavior, culture, and routines.* Yeager and Mehta & Fine cover relationships and culture at
   the level of mindset and models; nothing in the curriculum covers the operational layer:
   classroom routines, behavior systems, the evidence on restorative versus consequence-based
   approaches, and how routines reduce extraneous load (a direct M1 connection). Recommendation:
   one hour, framed explicitly as cognitive-load reduction and status protection so it integrates
   with M1 and M3. Label: [E] for routines reducing load; [H]/[V] for behavior philosophy.

**Emerging gaps (label: mostly hypothesis; the evidence is thin and moving).**

9. *AI tutoring and adaptive systems.* The curriculum predates or ignores large-language-model
   tutoring. The learner, from a product background, will be drawn to it. Recommendation: a one-
   hour session that applies M1 (worked examples, load, retrieval), M4 (guidance for novices), and
   M8 (effect-size skepticism, pilot-to-scale) to the vendor claims; and a standing rule that any
   AI tool is a PDSA cycle with a practical measure, never a platform decision. Label: [H]
   throughout; the honest position is that the evidence for durable learning gains at scale is
   not yet in, and that the most plausible wins are in teacher-side workload (feedback drafting,
   hinge-question generation, practice-set generation) rather than replacing instruction.

10. *Family engagement, physical environment, and the founder's own leadership.* Each gets thirty
    minutes at most. Family engagement: [H]. Facilities: [H]; acoustics and air quality have the
    clearest effects, open-plan has weak-to-negative evidence (consistent with M1). Founder
    leadership: [V]; apply Yeager's mentor mindset to the board and staff relationship and Bryk's
    "see the system" to the founder's own calendar.

The gaps above are supplements, not replacements. The thirteen books answer the question almost
no founder asks well: what happens in the mind of the child in the median lesson, and what the
institution must do so that it happens well and consistently.

---

## Notes for the co-planning agents

- The hinge questions assert specific findings (Butler 1988; Roediger & Karpicke 2006; Recht &
  Leslie 1988; Gruber et al. 2014; Vosniadou; Kapur's boundary conditions; Wiliam's effect-size
  traps). When the book files land, check each against the file's "Evidence strength & limits"
  section and soften any hinge where replication is contested (wise feedback is the likeliest).
- Reading maps should be built from each book file's "5-10 ideas" and "Mental models" sections
  first; the target is that the learner reads 25-35% of each file during the course.
- Modules 3 and 7 depend most on specifics from `03`, `05`, `08`, and `09` (Engel's question
  counts, Yeager's studies, Transcend's leaps, Mehta & Fine's cases); revise once those land.
