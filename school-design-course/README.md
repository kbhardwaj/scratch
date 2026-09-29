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

- `learning-design.md` is the course design, co-planned with a Fable agent. It sets out
  modules, a productive-failure opener, hinge questions and a 3-week spaced schedule.
- `unified-model.md` shows how minds → design → institutions connect in one model.
- `tensions.md` covers the live debates, each with a conditional decision rule.
- `design-brief-template.md` is your evolving school-design brief, with every decision labeled E/H/V.
- `casebook.md` holds founder dilemmas to practice judgment on.
- `capstone.md` defines the final performance that proves mastery, with a rubric.
- `flashcards.json` is the spaced-retrieval deck.

**Phase 3 (experience).** `app/index.html` is the interactive course. It includes the
modules, retrieval quizzes, flashcards with spacing, the casebook and the design brief builder.

## How to use it (short version)

1. Take the diagnostic and attempt the opening design challenge *before* reading anything.
   Failing at it is the point.
2. Work through one module a day (45–60 min). Do the hinge questions honestly.
3. Do the flashcard review daily (5–10 min). The spacing is where the learning comes from.
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
