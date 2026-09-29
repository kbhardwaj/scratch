# School Design Course

A self-study course for learning, in about 15 hours instead of about 150, everything in a 13-book
curriculum on learning science, instructional design and school building. The goal is to finish
able to design and found a world-class K–12 institution.

## The plan

**Three levels** organize everything:

| Level | Question | Sources |
|---|---|---|
| 1. Minds | How do minds learn? | Foundational papers, *How Learning Happens*, *Scienceblind*, *Intellectual Lives of Children*, (*Why We Remember*, *Learning Scientific Concepts*) |
| 2. Design | How should learning experiences be designed? | *Productive Failure*, *10 to 25*, *Beyond the Science of Reading*, *Embedding Formative Assessment* |
| 3. Institutions | How do institutions make good learning happen consistently? | *Extraordinary Learning for All*, *In Search of Deeper Learning*, *Creating the Schools Our Children Need*, *Improvement in Action* |

**Phase 1 (catabolic): break it down.** `books/` holds one file per source. Each file has a
verified (or clearly marked) table of contents, the salient knowledge chapter by chapter, the
5–10 ideas you must keep, a list of evidence strengths and limits, institutional implications
tagged **[E]** evidence / **[H]** hypothesis / **[V]** value, connections to the other books,
and 10 retrieval questions.

**Phase 2 (anabolic): build it back up.** `synthesis/` holds:

- `learning-design.md` is the course design, co-planned with a Fable agent. It sets out 11 modules,
  a productive-failure opener, hinge questions, a 3-week spaced schedule, and a log of where it was
  reconciled against the book files.
- `unified-model.md` shows how minds → design → institution connect: 30 ideas, the causal chain, and
  the 12 laws of the school. **Reread this before any big decision.**
- `tensions.md` covers 14 live debates, each with a conditional IF/THEN rule, a switch signal, and a
  common mistake.
- `design-brief-template.md` is your evolving school-design brief: 11 sections, E/H/V labeling,
  a worked example (a hypothetical 400-student K–8), and registers for hypotheses and values.
- `casebook.md` holds 24 founder dilemmas with model answers.
- `capstone.md` defines the final performance that proves mastery: the brief, a defense against
  six challenges, and a first-90-days plan, scored on a 10-criterion rubric.
- `founder-gaps-primer.md` covers what the reading list leaves out for an actual founder: finance,
  governance, special education, early reading and numeracy, math, hiring, assessment, behavior,
  AI tutoring, families, and leadership.

**Phase 3 (experience).** The `app/` folder holds the interactive course, called *Founding School*:
modules with attempt-first prompts and hinge questions, a 212-card spaced-repetition deck, the
casebook, the tensions, the unified model, a diagnostic you take at the start and the end, and a
design brief builder. Mentor feedback from Claude is available on your attempts, cases and brief.
Rebuild it with `python3 app/build.py`, which inlines `app/data/*.json` into
`app/founding-school.html`.

## How to use it (short version)

1. Take the diagnostic and attempt the opening design challenge *before* reading anything.
   Failing at it is the point.
2. Work through one module a day (45–60 min). Do the hinge questions honestly.
3. Do the flashcard review daily (5–10 min). The spacing is where the learning comes from.
   Cards unlock as you complete modules.
4. After each module, add decisions to your design brief, each labeled E/H/V.
5. Finish with the capstone.

Open the `books/` files only when a module sends you there or you want depth.

## Honesty notes

- Summaries are written in our own words from publisher material, reviews, the research
  literature and background knowledge. They are not the books. Each file says whether its table of
  contents was verified.
- "Your papers" in the original curriculum were not supplied, so `books/00-foundational-papers.md`
  reconstructs the likely set (Sweller, Kirschner/Sweller/Clark, Gruber et al., Posner et al., Chi,
  Vosniadou). Correct it if yours differ.
- The links between the books and decisions about an institution are synthesis. They are not
  claims that any book validates a complete school model.
