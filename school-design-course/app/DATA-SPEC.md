# App data contract

The interactive course (`app/index.html`) inlines these JSON files at build time. All text is plain
strings; light markdown (**bold**, *italic*, `- ` bullets, line breaks) is allowed and will be rendered.
Tags: "E" evidence · "H" hypothesis · "V" value.

## app/data/modules.json
```json
{ "modules": [ {
  "id": "m1", "num": 1, "title": "...", "level": "Minds|Design|Institutions|Integration|Start",
  "minutes": 60, "sources": ["01-how-learning-happens", "..."],
  "hook": "a short opening question or puzzle",
  "attempt": { "prompt": "productive-failure / case prompt the learner tries BEFORE the content", "minutes": 10 },
  "objectives": ["..."],
  "ideas": [ { "title": "load-bearing idea", "body": "300-600 words of the distilled teaching, markdown", "tag": "E" } ],
  "worked_example": { "title": "...", "steps": ["step with reasoning", "..."] },
  "hinge": [ { "q": "...", "options": ["A","B","C","D"], "answer": 1,
               "diagnoses": ["misconception revealed by choosing A", "correct - why", "...", "..."] } ],
  "brief_prompt": "what to add/change in the school-design brief after this module",
  "deeper": ["books/NN-slug.md#section to open for depth"]
} ] }
```
Modules: m0 (diagnostic + cold design challenge), m1..m10, as in synthesis/learning-design.md.

## app/data/diagnostic.json
```json
{ "items": [ { "id": "d1", "statement": "...", "correct": true|false, "folk_theory": "...", "explanation": "...", "module": "m2" } ] }
```
Learner answers true/false + confidence 1-5.

## app/data/flashcards.json
```json
{ "cards": [ { "id": "c001", "module": "m1", "type": "recall|explain|apply|discriminate",
               "front": "...", "back": "...", "source": "01-how-learning-happens" } ] }
```

## app/data/cases.json
```json
{ "cases": [ { "id": "k01", "title": "...", "scenario": "...", "tension": "t03",
               "question": "What do you do?", "considerations": ["..."], "model_answer": "...",
               "sources": ["..."] } ] }
```

## app/data/tensions.json
```json
{ "tensions": [ { "id": "t01", "name": "X vs Y", "pole_a": "...", "pole_b": "...",
                  "rule": "conditional decision rule: IF ... THEN ...", "switch_signal": "...",
                  "evidence": "...", "sources": ["..."] } ] }
```

## app/data/brief.json
The design-brief template: `{ "sections": [ { "id": "s1", "title": "...", "guidance": "...", "default_tag": "V", "prompts": ["..."] } ] }`

## app/data/model.json
Unified model for the diagram: `{ "bands": [ { "id":"minds","title":"...","nodes":[{"id":"...","label":"...","summary":"...","tag":"E","links":["node ids"]}] } ], "loop": "improvement loop description" }`
