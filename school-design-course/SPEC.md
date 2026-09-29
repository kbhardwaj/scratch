# Course build spec (shared by all agents)

Goal: the learner (software/product background, time-poor) must understand an entire reading
curriculum well enough to design and build a world-class K-12 institution from scratch — without
reading the books. Two phases:

- **Catabolic** — break each source into parts → TOC → most salient knowledge per chapter/section.
- **Anabolic** — synthesize across sources into models, tensions, decisions, practice and a capstone.

Three levels organize everything:
1. **Minds** — how minds learn
2. **Design** — how learning experiences should be designed (instruction, motivation, assessment)
3. **Institutions** — how institutions make good learning happen consistently

Every institutional claim is tagged: **[E]** supported by evidence · **[H]** hypothesis to test · **[V]** value commitment.

## Per-book file template (`books/NN-slug.md`)

```
# <Title> — <Author(s)> (<edition/year>)
Level: Minds | Design | Institutions  ·  Priority: Core-5 | Core | Extension
Est. reading time saved: ~Nh  ·  Your time with this file: ~N min

## The book in one sentence
## The book in one paragraph
## Why it's in this curriculum (the question to read it with)

## Table of contents
(Parts → chapters, verified via web search where possible. State at top of section:
"TOC verified against <source>" or "TOC reconstructed — not verified". Never invent chapter titles
silently.)

## Chapter-by-chapter: the salient knowledge
### Part / Ch N — <title>
- Core claim(s) — 2-5 bullets, own words
- Key study / evidence / example (name researchers + year when known)
- So-what for a school designer
(Group minor chapters; spend words where the ideas are load-bearing.)

## The 5-10 ideas you must carry out of this book
(numbered, each 1-3 sentences, ranked by importance)

## Mental models & vocabulary
(term — crisp definition — where it bites in practice)

## Evidence strength & limits
(what's robust, what's contested, what the author is arguing vs. showing; known critiques)

## Institutional design implications
(bulleted decisions, each tagged [E]/[H]/[V])

## Connections
(agrees with / tensions with other curriculum books — use the slugs below)

## Retrieval practice
10 questions, mixed: recall, explain-why, apply-to-a-scenario, spot-the-misconception.
Put answers in a <details> block after each question.

## Common misreadings of this book
```

## Rules
- Write in your own words. No quotations longer than ~12 words; no reproducing passages.
  Chapter titles are fine.
- Use WebSearch/WebFetch to verify TOCs, editions, key studies. Say plainly when something is
  from your background knowledge vs. verified. Do not fabricate studies, numbers, or chapter titles.
- Dense, skimmable, high-signal. Target 3,000-6,000 words per book (more for How Learning Happens,
  which is a collection of ~30+ study summaries — cover every study it discusses).
- Markdown only. No emojis.

## Source slugs
- 00-foundational-papers — the learner's own papers (Sweller CLT; Kirschner, Sweller & Clark 2006;
  Gruber, Gelman & Ranganath 2014 curiosity; Chi; Posner et al. 1982; Vosniadou)
- 01-how-learning-happens — Kirschner & Hendrick, 2nd ed. 2024
- 02-scienceblind — Shtulman 2017
- 03-intellectual-lives-of-children — Engel 2021
- 04-productive-failure — Kapur 2024
- 05-10-to-25 — Yeager 2024
- 06-beyond-the-science-of-reading — Wexler 2025
- 07-embedding-formative-assessment — Wiliam & Leahy (2015 / 2024 printing)
- 08-extraordinary-learning-for-all — Samouha, Wetzler, Henry Wood 2024/25
- 09-in-search-of-deeper-learning — Mehta & Fine 2019
- 10-creating-the-schools-our-children-need — Wiliam 2018
- 11-improvement-in-action — Bryk 2020
- 12-why-we-remember — Ranganath 2024 (extension)
- 13-learning-scientific-concepts — Amin 2025/26 (extension)
