# Course build spec (shared by all agents) — Games and Norms

Goal: the learner (software/product background, time-poor) must understand this entire reading
list well enough to **diagnose why a real group cooperates, coordinates or fails to — and design
the norms, incentives, network structure and institutions that fix it** — without reading the
books. The learner keeps an evolving "cooperation design brief" for a group of their choosing
(a team, a community, a platform, a commons). Two phases:

- **Catabolic** — break each source into parts → TOC → most salient knowledge per chapter/section.
- **Anabolic** — synthesize across sources into models, tensions, decisions, practice and a capstone.

Three levels organize everything (plus a critical synthesis):
1. **Origins** — why humans are cultural, social learners; where cooperation comes from
   (Henrich, Laland)
2. **Mechanisms** — the psychology of individuals in groups and the formal language of strategic
   interaction, and where real behavior departs from it (Gilovich et al., Dixit et al., Schelling, Camerer)
3. **Order** — how norms, institutions and networks turn interaction into stable collective
   patterns (Skyrms, Bicchieri, Ostrom, Easley & Kleinberg)
4. **Synthesis under critique** — Gintis's attempted unification and its problems

Every design claim is tagged: **[E]** supported by evidence · **[H]** hypothesis to test in the
learner's group · **[V]** value commitment.

## Per-book file template (`books/NN-slug.md`)

```
# <Title> — <Author(s)> (<edition/year>)
Level: Origins | Mechanisms | Order | Synthesis  ·  Priority: Core | Selections
Est. reading time saved: ~Nh  ·  Your time with this file: ~N min

## The book in one sentence
## The book in one paragraph
## Why it's in this curriculum (the question to read it with)

## Table of contents
(Parts → chapters, verified via web search where possible. State at top of section:
"TOC verified against <source>" or "TOC reconstructed — not verified". Never invent chapter titles
silently. For "selections" books, list the full TOC, then mark which chapters this file covers and why.)

## Chapter-by-chapter: the salient knowledge
### Part / Ch N — <title>
- Core claim(s) — 2-5 bullets, own words
- Key study / model / example (name researchers + year when known; for formal books, state the
  model setup and the result in plain words, with one small worked example where it helps)
- So-what for someone designing cooperation in a real group
(Group minor chapters; spend words where the ideas are load-bearing.)

## The 5-10 ideas you must carry out of this book
(numbered, each 1-3 sentences, ranked by importance)

## Mental models & vocabulary
(term — crisp definition — where it bites in practice)

## Evidence strength & limits
(what's robust, what's contested, what the author is arguing vs. showing; known critiques;
replication status of key experiments where relevant)

## Design implications for cooperation in real groups
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
- Use WebSearch (WebFetch may be blocked by the proxy — if so, rely on search snippets) to verify
  TOCs, editions, key studies. Say plainly when something is from your background knowledge vs.
  verified. Do not fabricate studies, numbers, or chapter titles.
- Where popular claims outrun the evidence (e.g. replication failures in social psychology,
  contested interpretations of experiments), say so explicitly.
- Dense, skimmable, high-signal. Target 3,500-6,000 words per book.
- Markdown only. No emojis.

## Source slugs (fixed — use exactly these)
- 01-secret-of-our-success — Henrich, The Secret of Our Success (2016) · Origins
- 02-darwins-unfinished-symphony — Laland, Darwin's Unfinished Symphony (2017) · Origins
- 03-social-psychology — Gilovich, Keltner, Chen & Nisbett, Social Psychology (latest ed., 5th/6th) · Mechanisms
- 04-games-of-strategy — Dixit, Skeath & McAdams (Reiley in older eds.), Games of Strategy (5th ed.) · Mechanisms
- 05-micromotives-and-macrobehavior — Schelling, Micromotives and Macrobehavior (1978/2006) · Mechanisms
- 06-behavioral-game-theory — Camerer, Behavioral Game Theory (2003), selections: ch 1 (intro), ch 2 (dictator/ultimatum/trust: social preferences), ch 7 (coordination), plus ch 6 (learning) briefly; full TOC listed · Mechanisms
- 07-stag-hunt — Skyrms, The Stag Hunt and the Evolution of Social Structure (2004) · Order
- 08-grammar-of-society — Bicchieri, The Grammar of Society (2006) · Order
- 09-governing-the-commons — Ostrom, Governing the Commons (1990) · Order
- 10-networks-crowds-markets — Easley & Kleinberg, Networks, Crowds, and Markets (2010), selections: ch 1, 3 (strong/weak ties), 4 (homophily), 6 (games), 16 (information cascades), 17 (network effects), 19 (cascading behavior in networks), 20 (small-world); full TOC listed · Order
- 11-bounds-of-reason — Gintis, The Bounds of Reason (2009; rev. 2014) · Synthesis

## ID schemes (fixed for every downstream file — do not renumber)
- modules: m0 (diagnostic + cold challenge), m1..mN in synthesis/learning-design.md
- tensions: t01..tNN in synthesis/tensions.md (that file's order is canonical)
- cases: k01..kNN in synthesis/casebook.md
- diagnostic items: d1..d16
- flashcards: c001..cNNN
- brief sections: s1..sNN in synthesis/design-brief-template.md
