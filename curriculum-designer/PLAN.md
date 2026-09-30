# Curriculum Designer — plan for a general skill

Goal: a skill (`/curriculum-designer`) that takes a subject or a reading list and produces
what the school-design run produced: per-source breakdowns (catabolic), a synthesis layer
(anabolic), and an interactive course app with spaced repetition, diagnostics, hinge
questions and mentor feedback — for any domain.

## 1. Inputs

```
/curriculum-designer "<subject>" [--sources <file|inline list>] [--goal "<capability>"]
                     [--depth light|standard|deep] [--no-app] [--claim-tags EHV|ECO]
```

| Input | Required | Notes |
|---|---|---|
| subject | yes | e.g. "behavioral finance" |
| sources | no | titles of books/papers. Strongly improves results. If absent, phase 0 discovers them. |
| goal | no | the capability the learner wants at the end ("run a systematic fund", "build a school"). Drives the capstone and the working artifact. If absent, the planner proposes one and confirms. |
| depth | no | light ≈ 3k words/source, 6 modules; standard ≈ 7k/source, 10–12 modules (what we did); deep adds primary-paper deep dives and a second casebook. |
| claim-tags | no | EHV (evidence/hypothesis/value) for design-oriented goals; ECO (established/contested/open) for knowledge-oriented goals. |

## 2. Pipeline (each phase = one or more background agents; orchestrator commits after each)

**Phase 0 — Intake and discovery** (1 agent, Fable; only when sources are missing or thin)
- Build a candidate reading list of 8–14 sources: canonical text(s), 3–5 seminal papers, one recent synthesis, at least one critic/contrarian (needed later for tensions), one adjacent-field source.
- Search-verify each exists (title, author, year, edition). WebFetch may be blocked; label verification status.
- One AskUserQuestion: confirm list + goal. This is the only interactive step.

**Phase 1 — Structure** (1 agent, Fable)
- Propose the level structure. Default pattern generalizes the Minds/Design/Institutions ladder: *foundations (mechanisms) → practice (methods/design) → systems (institutions/markets/organizations)*. Assign every source to a level.
- Write the run's `SPEC.md` from `references/spec-template.md`: source slugs 00–NN, the fixed ID scheme for every later object (`mNN`, `tNN`, `kNN`, `dNN`, `cNNN`), rules (own words, no quotes >12 words, never fabricate, verify TOCs).
- Lesson baked in: IDs are fixed here, up front. Last time the casebook agent used a different tension order than tensions.json and needed a remap.

**Phase 2 — Catabolic breakdowns** (one agent per source, all in parallel; default model)
- Template = the one that worked: TOC → chapter-by-chapter salient knowledge → keep-list (5–10 ideas) → evidence strength and limits → decisions tagged E/H/V (or E/C/O) → links to other sources → 10 retrieval questions → verification status.
- Book files are authoritative for everything downstream.

**Phase 3 — Reconciliation** (1 agent, Fable) — new step, promoted from an ad-hoc fix last time
- Read all breakdowns. Produce `synthesis/claims-ledger.md`: contradictions between sources, corrections where later evidence overturned a claim, shared glossary, and effect-size table. Every later agent gets this file.

**Phase 4 — Anabolic synthesis** (Fable for learning-design; then 5 agents in parallel)
1. `learning-design.md` — modules with: cold challenge before content (productive failure), hinge questions with a diagnosed misconception per distractor, retrieval schedule, 21-day plan, gaps section.
2. `unified-model.md` — nodes by band, causal chain, laws, certainty table.
3. `tensions.md` — debates with poles, evidence, IF/THEN rule, switch signal, common mistake. (Needs the critic source from phase 0.)
4. `casebook.md` — 20–24 dilemmas keyed to modules and tensions.
5. `capstone.md` — deliverables + rubric tied to the goal.
6. `gaps-primer.md` — what the reading list omits that the goal needs.
7. `working-artifact-template.md` — the generalization of the design brief (for a fund: investment policy; for a language: a study plan; for medicine: a clinical protocol).
- Each agent must append a reconciliation log if it departs from the book files.

**Phase 5 — Data** (2–3 agents in parallel) → `app/data/*.json` per `references/data-spec.md`
- modules, diagnostic (16 items with confidence rating), flashcards (~15/module, atomic), cases, tensions, brief sections, model.
- `scripts/validate.py` checks schema, ID cross-references, distractor diagnoses present, card counts, no dangling module refs. Fails the run if not clean.

**Phase 6 — App** (orchestrator)
- `app/template.html` generalized: all domain strings come from `course.json` (title, subtitle, artifact name, band names, case noun, icon). `build.py` reads the manifest.
- `scripts/smoke.js`: Playwright with `executablePath: /opt/pw-browsers/chromium`; every view renders, hinge diagnosis, card grading, artifact entry, case reveal, model panel, 390px no overflow.
- Publish artifact with `db`, `user`, `sample` capabilities; private by default.

**Phase 7 — QA** (2 agents in parallel)
- Fact spot-check: sample 30 claims across files, search-verify, report.
- Cold learner: an agent takes the diagnostic and M0 challenge without the content, then reads M1–M3 and retakes — sanity check that questions discriminate and the sequence teaches.

## 3. Skill layout

```
.claude/skills/curriculum-designer/
  SKILL.md                     orchestration procedure, phase gates, commit-after-each-agent rule
  references/
    spec-template.md           run SPEC (rules, ID scheme, slugs)
    source-breakdown.md        per-source template + agent prompt
    reconciliation.md          claims-ledger template
    learning-design.md         module template + hinge-question rules
    unified-model.md / tensions.md / casebook.md / capstone.md / gaps.md / artifact.md
    data-spec.md               JSON contracts
    discovery.md               how to build a reading list from a bare subject
    lessons.md                 what went wrong last time and the rule that prevents it
  app/
    template.html              generalized, manifest-driven
    build.py
  scripts/
    validate.py
    smoke.js
```

## 4. Lessons from run 1 → rules in the skill
- Fix all ID schemes in SPEC before any synthesis agent starts.
- Book files > learning-design; every synthesis agent logs departures.
- Commit and push after every agent hand-back (stop hook, and no lost work).
- Assume WebFetch may be blocked: verify via search snippets, label status per file, name the least-certain items in the README.
- Cold challenge first, hinge distractors each diagnose a misconception, cards unlock on module completion, diagnostic captures confidence.
- Playwright: use system Chromium path; don't `playwright install`.
- Corrections matter: instruct breakdown agents to flag where popular claims outrun the evidence (curiosity/memory, PF on procedures).

## 5. Scale and cost
- Standard depth, 12 sources: ~22 agents, 3–5 hours wall-clock, ~150k words of markdown, one ~600 KB HTML page. Run 1 was this size.
- Light depth: ~10 agents, about a third of that.

## 6. Validation of the skill itself
- Eval run on a second domain with sources given: **behavioral finance** (Kahneman, Thaler, Shiller, Barberis & Thaler survey, Lo, a critic such as Gigerenzer).
- Eval run with subject only: e.g. "Roman Republic politics" — tests discovery.
- Success = validate.py clean, smoke test clean, QA fact-check ≥ 90% confirmed, cold-learner agent shows a gain between the two diagnostics.

## 7. Build order (if approved)
1. Extract templates and prompts from run 1 into `references/` (mostly copy + generalize).  
2. Generalize template.html + build.py behind `course.json`; rebuild the school course from it as a regression check.  
3. Write validate.py and smoke.js.  
4. Write SKILL.md with the phase procedure.  
5. Run the behavioral-finance eval end to end; fix what breaks.  
6. Run the subject-only eval.
