# Games and Norms — a course on cooperation, from cultural evolution to institutions

Built with the `curriculum-designer` skill (`.claude/skills/curriculum-designer/`) from an 11-book
reading list. Goal: **diagnose why a real group (team, community, platform, commons) cooperates or
fails to, and design the norms, incentives, network structure and institutions that fix it** —
without reading the books. The learner keeps an evolving *cooperation brief* for a group they choose.

Interactive course (private artifact): https://claude.ai/artifact/Qm3p8dsMnGCW67QXA3pv6x

## The reading list, in four levels
| Level | Sources |
|---|---|
| Origins | Henrich *The Secret of Our Success*; Laland *Darwin's Unfinished Symphony* |
| Mechanisms | Gilovich et al. *Social Psychology*; Dixit et al. *Games of Strategy*; Schelling *Micromotives and Macrobehavior*; Camerer *Behavioral Game Theory* (selections) |
| Order | Skyrms *The Stag Hunt*; Bicchieri *The Grammar of Society*; Ostrom *Governing the Commons*; Easley & Kleinberg *Networks, Crowds, and Markets* (selections) |
| Synthesis | Gintis *The Bounds of Reason* (read as an attempted synthesis to assess critically) |

## Files
- `SPEC.md` — the run spec: goal, levels, per-book template, rules, fixed slugs and ID schemes.
- `course.json` — app manifest (titles, level names, artifact name, mentor voice, prompts).
- `books/01…11-*.md` — one breakdown per source (~64k words): TOC with verification status, chapter-by-chapter salient knowledge, carry-out ideas, vocabulary, evidence strength and limits, E/H/V-tagged design implications, connections, 10 retrieval questions, common misreadings.
- `synthesis/claims-ledger.md` — reconciliation across sources: 16 contradictions, 65 corrections where popular claims outrun evidence, 42-term glossary, 48 numbers with verified/background status, 40 binding rules for everything downstream.
- `synthesis/learning-design.md` — the course design: 11 principles, m0–m11, 44 hinge questions with a diagnosed misconception per distractor, 16-item diagnostic, 21-day schedule, reconciliation log.
- `synthesis/unified-model.md` — 32 ideas in four bands, 14-step causal chain, 12 laws of cooperation, the diagnosis loop.
- `synthesis/tensions.md` — 14 tensions t01–t14 with IF/THEN rules and switch signals.
- `synthesis/casebook.md` — 24 cooperation dilemmas k01–k24 with model answers keyed to modules and tensions.
- `synthesis/capstone.md` — three deliverables, 10-criterion rubric (pass 32/40, none below 2; world-class 36/40 with 4s on criteria 1, 2, 3, 7), repair map.
- `synthesis/design-brief-template.md` — the cooperation brief, sections s1–s14, registers, version plan, and a worked example ("Lanternfish", a 40-person open-source project).
- `synthesis/gaps-primer.md` — 10 things the reading list omits that the goal needs (measuring expectations, sanction design, legitimacy, reputation systems, mechanism design, online governance, psychological safety, scaling, the Axelrod/Nowak classics, ethics of nudging norms).
- `synthesis/qa-fact-check.md`, `synthesis/qa-cold-learner.md` — QA reports (see below).
- `app/data/*.json` — the app's content; `app/games-and-norms.html` — the built page. Rebuild with `python3 ../.claude/skills/curriculum-designer/app/build.py .` after `scripts/validate.py` passes.

## The modules (~20 hours over 21 days; ~23 with the capstone)
| # | Module | Level | Min |
|---|---|---|---|
| m0 | Start here: cold diagnosis, the map, the tagging discipline | Start | 60 |
| m1 | Cultural learners and the collective brain | Origins | 100 |
| m2 | The psychology of individuals in groups, with the replication rules | Mechanisms | 70 |
| m3 | The formal toolkit: draw the game before arguing about it | Mechanisms | 100 |
| m4 | Micro to macro: thresholds, tipping, sorting | Mechanisms | 70 |
| m5 | What people actually do: social preferences, coordination experiments, learning | Mechanisms | 70 |
| m6 | How populations settle: risk dominance, correlation, signals | Order | 100 |
| m7 | Norms: expectations, measurement, change | Order | 70 |
| m8 | Institutions for the commons: design principles, sanctions, polycentricity | Order | 70 |
| m9 | Networks: ties, homophily, cascades, small worlds | Order | 70 |
| m10 | The four accounts reconciled and Gintis assessed | Synthesis | 70 |
| m11 | Integration: tensions, decision rules, the diagnostic path | Integration | 75 |

## How to use it
1. Open the app. Take the **Diagnostic** (true/false + confidence) and do **m0's cold challenge** before reading anything; getting it wrong is the method.
2. One module a day (the two 100-minute modules split over two days). Every module: hook → attempt before content → ideas → worked example → hinge questions → update your brief.
3. Review the card deck daily (cards unlock as modules complete; 184 cards).
4. Every third day is a retrieval day: cards, 1–3 cases, one free recall.
5. Day 21: retake the diagnostic. Days 22–24: capstone (brief v6, defence, first 90 days).
6. Ask the mentor (Claude) for feedback on attempts, cases and the brief; it asks your permission and uses your own Claude usage.

## Honesty notes
- Full web pages could not be fetched (proxy); TOCs and studies were verified from search snippets. Each book file states its status. Least certain: Gilovich 6th-edition chapters 2–8 (reconstructed from the 5th), Dixit 5th-edition chapters 16–17 titles, the Gintis 2014 revised-edition TOC, and the Binmore/Sugden reviews of Gintis (not found; the file uses their general positions).
- Where popular claims outrun the evidence, the course says so: strong reciprocity as an evolved trait is [H]; ego depletion, behavioural priming, power posing, watching eyes, the Stanford Prison Experiment, groupthink-as-syndrome and IAT training are on the do-not-build-on list; Schelling's checkerboard shows that mild preferences can produce extreme sorting, not that preferences cause real segregation; dense clusters both block outside cascades and protect inside adoption.
- The goal and the "cooperation brief" artifact were chosen by the course builder, not the reading list; change `course.json` and the brief template if you want a different end capability.
