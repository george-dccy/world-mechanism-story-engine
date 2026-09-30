---
name: wm-mechanism-explorer
description: Use when a user wants to understand why a phenomenon happens, uncover a system's underlying mechanism, deepen a content idea before writing, stress-test a world rule, or turn a promising creative seed into a mechanism map. Do not use as a shortcut to directly produce scripts, titles, storyboards, or videos.
---

# World Mechanism Explorer

## Core contract

Help the creator **understand before expressing**.

The skill does not optimize for fast content generation. It turns a question, observation, historical detail, current phenomenon, knowledge point, or creative seed into a clearer model of how a system works, what is known, what is uncertain, and which counterfactuals reveal the mechanism.

A successful run should leave the creator with at least one of these:
- a sharper question;
- a mechanism they did not see before;
- a causal distinction that changes their view;
- a productive uncertainty worth researching;
- a counterfactual that exposes the mechanism.

If none happens, the run is not successful even if the output looks complete.

## Two valid entry routes

### Question-first
Use when the input is a real-world question or observation.

```text
Question → Question Ladder → Mechanism Candidates → Evidence Gaps → Mechanism Map → Counterfactuals
```

### Spark-first
Use when the input is already a vivid premise, strange rule, relationship, or story seed.

```text
Creative Seed → What behavior does this rule change? → What real mechanism might it expose? → Mechanism Map → Counterfactual stress test
```

Do not force a creative seed to pretend it began as research. Do not let a vivid seed bypass mechanism exploration entirely.

## Scope gate

Before exploring, infer the user's intended scope:

- **Explore only**: deepen the question and stop at mechanism / uncertainty.
- **Explore for creation**: deepen the mechanism and optionally propose creative hypotheses, but do not write a final script.
- **Evaluate an existing premise**: test whether the rule can generate sustained consequences and whether it maps to a real mechanism.
- **Research-backed exploration**: separate facts from interpretations and identify or retrieve evidence.

If the user already supplied the scope, do not re-ask. If the request is broad, default to **Explore for creation** while keeping the output pre-script.

## Workflow

### 1. Preserve the creator's starting point

Record, in plain language:
- what they noticed;
- what feels strange or interesting;
- their current intuition;
- why they care, if known.

Do not replace their question with a more fashionable content angle.

### 2. Build a short Question Ladder

Read `references/question-ladder.md`.

Move through only the layers that add understanding:
- phenomenon;
- causality;
- incentives;
- system;
- time;
- information;
- human behavior;
- author perspective.

Do not mechanically answer every question. Select the 5–10 highest-value questions for this case.

### 3. Generate competing mechanism candidates

Produce 2–4 plausible mechanism models when uncertainty exists.

For each candidate:
- what it explains;
- what it fails to explain;
- what evidence would distinguish it from alternatives.

Never collapse correlation, incentive, and causation into one claim.

### 4. Separate evidence states

Use these labels consistently:

- **F — Fact**: directly verifiable.
- **I — Interpretation**: a reasoned explanation based on facts.
- **H — Hypothesis**: plausible but unverified.
- **R — Fictional Rule**: intentionally invented for creative work.

If a factual claim matters to the mechanism and is not established, mark it as a research gap. Do not fill the gap with confident prose.

### 5. Build the Mechanism Map

Read `references/mechanism-map-template.md`.

Include only relevant dimensions:
- actors;
- goals / incentives;
- constraints;
- flows of information, money, resources, risk, or attention;
- feedback loops;
- thresholds;
- time scales;
- path dependence;
- information asymmetry;
- institutional or physical substrate.

Finish with a **one-sentence model** that is accurate rather than clever.

### 6. Stress-test with counterfactuals

Read `references/counterfactual-protocol.md`.

Use at least three structurally different transformations where useful:
- Remove;
- Expose;
- Amplify;
- Delay / Accelerate;
- Localize;
- Invert.

Trace first-, second-, and third-order consequences. A good counterfactual reveals the mechanism; a weak one merely creates spectacle.

### 7. Return authorship to the human

Always include a short **Creator Gate**:

- What surprised you?
- Which explanation feels correct but uninteresting?
- Which uncertainty do you personally want to pursue?
- What would you refuse to simplify?
- What question would you actually want to discuss with your child, friend, or reader?

Do not answer these on the creator's behalf unless they explicitly ask for candidate answers.

### 8. Stop before production

If the user asked only for mechanism exploration, stop.

If the user wants to continue toward creation, output 2–4 **creative hypotheses** at most. Each must state:
- what real mechanism it exposes;
- what rule or perspective changes;
- what new behavior it would generate.

Do not silently advance to screenplay, storyboard, renderer, or video prompts.

## Output contract

Read `references/output-contract.md`.

Default sections:
1. Starting Point
2. Core Question
3. Question Ladder
4. Mechanism Candidates
5. Mechanism Map
6. Evidence Ledger
7. Counterfactuals
8. Creator Gate
9. Optional Creative Hypotheses
10. Status: `candidate`, `needs-research`, or `ready-for-editorial-gate`

## Failure modes

Reject these defaults:

- **Title-first thinking**: turning the question into "The real reason..." before understanding it.
- **Three-truth compression**: forcing complex systems into three neat causes.
- **Moral-first analysis**: deciding who is good or bad before modeling incentives.
- **Mechanism = theme**: "loneliness", "capitalism", "human nature", or "technology" are not mechanisms by themselves.
- **Single-cause confidence**: choosing one explanation because it makes the cleanest story.
- **Counterfactual spectacle**: making the world stranger without revealing anything.
- **Research dumping**: collecting facts that do not change the model.
- **Creator erasure**: letting the model decide what the creator should care about.

## Completion test

Before finishing, check:

- Did the core question become more precise?
- Is the one-sentence mechanism actually causal or structural?
- Are F / I / H / R clearly separated?
- Is there at least one viable alternative explanation or boundary condition?
- Did the counterfactual reveal behavior beyond a one-shot twist?
- Is there a real human decision still left for the creator?
- Have you stopped before production unless explicitly asked to continue?
