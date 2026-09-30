# Behavioral Game Theory: Experiments in Strategic Interaction — Colin F. Camerer (Princeton / Russell Sage, 2003)
Level: Mechanisms  ·  Priority: Selections
Est. reading time saved: ~18h (550 pages, dense)  ·  Your time with this file: ~35 min

## The book in one sentence
Game theory is right about the *structure* of strategic situations but wrong about the *players*, and twenty years of lab experiments show exactly how: people care about fairness and reciprocity, reason only a step or two ahead, and learn their way toward equilibrium rather than computing it.

## The book in one paragraph
Camerer's book is the first systematic survey of the experimental literature testing game theory against real people. It keeps the formal apparatus (games, payoffs, equilibrium as benchmark) while replacing the selfish, unboundedly rational player with three empirically grounded amendments: **social preferences** (fairness and reciprocity), **limited strategic thinking** (a finite number of steps of iterated reasoning), and **learning** (behavior moves over repeated play by simple adaptive rules). Each chapter takes a class of games, reports what dozens of experiments find, and asks which amended model fits. It is a *catalogue with a thesis*: behavioral game theory should generalize standard theory, collapsing to it when the amendments are switched off. For this course it supplies the evidence base Dixit et al.'s formal models lack, and the micro-foundations (fairness, punishment, strategic uncertainty, focal points) on which Ostrom, Bicchieri and Skyrms build.

## Why it's in this curriculum (the question to read it with)
Read it asking: **"When my group departs from the game-theoretic prediction, is it because of preferences (they care about fairness), cognition (they can't or won't reason that far), or history (they haven't learned yet)?"** Those three diagnoses call for three different fixes: change the payoffs and the fairness frame; simplify and make the desired move salient; or engineer early experience. Camerer gives you the evidence to tell them apart.

## Table of contents
TOC verified against publisher and bookseller listings (Princeton University Press page, Labyrinth Books, Eyrolles, Ingram Academic). Chapter numbering below follows the book's sequence; section-level headings within chapters are from my background knowledge and are not verified.

1. Introduction
2. Dictator, Ultimatum, and Trust Games
3. Mixed-Strategy Equilibrium
4. Bargaining
5. Dominance-Solvable Games
6. Learning
7. Coordination
8. Signaling and Reputation
9. Conclusion: What Do We Know, and Where Do We Go?

Appendices: a brief primer on game theory and on experimental design (background knowledge; unverified).

**Coverage in this file.** In depth: ch 1 (what BGT is and how to read the rest), ch 2 (social preferences — the foundation for every "why do people cooperate at all" question in the course), ch 7 (coordination — the direct experimental complement to Schelling and Skyrms). Briefly: ch 5 (limited strategic thinking) and ch 6 (learning), because they supply the other two amendments and the vocabulary (level-k, EWA) that later literature uses. One paragraph each for ch 3, 4, 8, 9, which are important for game theorists but less load-bearing for designing group cooperation.

## Chapter-by-chapter: the salient knowledge

### Ch 1 — Introduction (what behavioral game theory is)
- **Core claims**
  - Standard game theory is a theory of how idealized players *should* behave given mutual rationality; it is a poor description of how people *do* behave in first encounters, though often a decent description of where experienced players end up.
  - BGT keeps the mathematical structure of games and adds psychological realism in three places: preferences (social utility), thinking (bounded iterated reasoning) and dynamics (learning). The aim is a *generalization* of game theory with parameters that, at extreme values, recover the standard model.
  - Experiments are the right tool because payoffs, information and move order are controlled, so a deviation can be attributed to the player. Conventions: real stakes, no deception, anonymity, re-matched repeated play to study learning.
  - Equilibrium remains the right *benchmark* — you need the prediction to see the deviation. Key distinction: "one-shot" behavior (what people bring to a new situation) versus "converged" behavior (what learning produces).
- **So-what**: When you model your group with a payoff matrix (as Dixit et al. teach), treat the equilibrium as a hypothesis about *experienced* behavior and expect first-round behavior to be governed by fairness norms and shallow reasoning. The design question becomes "which of the three amendments dominates here?"

### Ch 2 — Dictator, Ultimatum, and Trust Games (social preferences)
This is the chapter to know cold. The three games isolate three things: pure altruism/norm-following (dictator), willingness to punish unfairness at a cost (ultimatum), and trust plus reciprocity (trust game).

**The games and the standard prediction**
- *Ultimatum*: proposer splits a pie; responder accepts (split stands) or rejects (both get zero). Subgame-perfect prediction: proposer offers the smallest positive amount, responder accepts anything.
- *Dictator*: same but the recipient cannot reject. Prediction: give zero.
- *Trust (investment) game* (Berg, Dickhaut & McCabe 1995): investor sends any part of an endowment; the experimenter triples it; the trustee returns whatever they like. Prediction by backward induction: trustee returns nothing, so investor sends nothing.

**What people actually do (numbers, with uncertainty flags)**
- Ultimatum: modal offers are 40–50% of the pie; mean offers around 40% (Oosterbeek, Sloof & van de Kuilen 2004 meta-analysis of 37 papers — verified via search snippet). Offers below about 20% are rejected roughly half the time in Western student samples (Camerer's summary; "half" is approximate and varies with stakes, framing and culture). Offers of 50% are almost never rejected. Raising stakes to weeks of wages (Cameron 1999, Indonesia; Slonim & Roth 1998, Slovakia) lowers rejection rates somewhat but proposers still offer about 40%.
- Dictator: average giving around 20–30%, with a large mass at zero and a secondary mass at 50%. Engel's 2011 meta-analysis (post-book; verified via snippet) reports mean giving of about 28%, with roughly 64% giving something. Giving is very sensitive to design: double-blind anonymity (Hoffman, McCabe, Shachat & Smith 1994) cuts it substantially; "earning" the endowment cuts it; adding a *take* option changes the distribution (List 2007, post-book). Camerer's reading: dictator giving is real but fragile — norm compliance under observation more than a stable taste for others' welfare.
- Trust game: in Berg et al.'s original, 30 of 32 investors sent something, averaging about $5.16 of $10 (verified via snippet); trustees returned on average roughly what was sent, so trusting did not pay but did not lose much (return figure from background knowledge; not verified). Later studies broadly replicate: investors send around half, trustees return around a third of the tripled amount, with wide dispersion. A "social history" treatment showing past behavior raised trust — reputation matters.
- Gift exchange (Fehr, Kirchsteiger & Riedl 1993 and successors): in a lab labor market, "firms" pay above market-clearing wages and "workers" respond with higher costly effort; the wage–effort correlation is robust in the lab.

**Why the ultimatum result is not just noise or confusion**
- Responders reject in one-shot anonymous play with no reputational reason; rejection rates are stable across many replications and countries.
- Comparison treatments isolate the mechanism: when the proposer's offer is generated by a computer or a random device, low offers are rejected far less often (Blount 1995) — people punish *intentions*, not just outcomes. When the proposer has a menu of only unequal splits, responders accept the unequal offer more (Falk, Fehr & Fischbacher 2003) — again intentions.
- Proposers are partly strategic: dictator giving is far below ultimatum offers, so much ultimatum "generosity" is fear of rejection. Offers are roughly the expected-payoff-maximizing response to the empirical rejection function.

**Models of social preferences Camerer compares**
- *Inequity aversion* (Fehr & Schmidt 1999): utility = own payoff minus α × (disadvantageous inequality) minus β × (advantageous inequality), with α ≥ β. A responder with high α rejects low offers; a proposer with moderate β offers something. It is tractable and fits ultimatum and public-goods data with a plausible distribution of α, β across people. Bolton & Ockenfels's ERC (2000) is a close relative that uses the person's *share* of the total.
- *Reciprocity / intention-based* models (Rabin 1993; Dufwenberg & Kirchsteiger; Falk & Fischbacher): utility depends on beliefs about whether the other is being kind or unkind. These fit the Blount / Falk-Fehr-Fischbacher intention results that pure inequity aversion cannot.
- *Charness & Rabin (2002)*: concern for the worst-off player and for total surplus (quasi-maximin) plus a reciprocity term; fits their large battery of allocation games better than inequity aversion, because people care about efficiency more than equality per se.
- Camerer's verdict: no single model wins; inequity aversion is the workhorse for its simplicity; reciprocity is needed to explain intention effects; distributions of types matter more than a representative agent.

**Cross-cultural results (Henrich et al. 2001; Henrich et al. 2004 volume)**
- Fifteen small-scale societies on five continents (foragers, horticulturalists, pastoralists, farmers), ultimatum game with local stakes of about a day's wages. Mean offers ranged from about 26% (Machiguenga, Peru) to about 58% (Lamalera whale-hunters, Indonesia); verified via snippet. Student samples cluster at 40–45%, so the student result is roughly in the middle of the human range, not an outlier — but nor is it universal.
- Two variables explained most of the between-group variance: **market integration** (more exposure to markets → more equal offers) and **payoffs to cooperation** in daily life (societies that depend on collective production like whale hunts offer more). Individual-level variables (age, sex, wealth) explained little.
- Some societies (Au and Gnau, Papua New Guinea) showed *hyper-fair* offers above 50% that were sometimes rejected — interpreted as gift-giving norms in which accepting a large gift creates an unwelcome obligation.
- Camerer's reading: the *game* is the same but players import their society's norms about what the situation "is"; fairness preferences are culturally evolved, not a fixed constant. This is the bridge to Henrich and to Bicchieri's norms-as-scripts.

**So-what for designers**
- Assume a *distribution* of types: roughly a third purely self-interested, a large middle of conditional cooperators / reciprocators, a small fraction of unconditional altruists. Design for the middle: make reciprocity possible and visible.
- People will pay to punish unfair *intentions*. Any allocation mechanism that is perceived as intentionally unfair will be resisted at a cost to the resistor and to you; the same outcome from a rule seen as impersonal or random is tolerated far more.
- Observation and anonymity change generosity a lot; the dictator literature says "who is watching" is a design lever of the same order as the payoffs themselves.
- Culture sets the baseline of what "fair" means; do not import lab-student norms into a group whose members were socialized under different exchange norms.

### Ch 3 — Mixed-Strategy Equilibrium (one paragraph)
Matching-pennies-type games where the only equilibrium is randomization. Aggregate choice frequencies are often close to the mixed-equilibrium prediction, especially with experience and in field data (tennis serves, soccer penalties: Walker & Wooders 2001; Palacios-Huerta 2003), but individuals alternate too much and chase opponents' recent moves. Mixed equilibrium is a decent *population-level* description produced by heterogeneous, imperfectly randomizing people; do not expect any individual to play it.

### Ch 4 — Bargaining (one paragraph)
Alternating-offer games with shrinking pies test backward induction directly. First offers sit between the equal split and the subgame-perfect prediction, and Mouselab studies of information lookup (Johnson, Camerer, Sen & Rymon 2002) show people barely look at later-round payoffs, though they can be taught to. Unstructured bargaining shows deadline effects, self-serving bias about what is fair (Babcock & Loewenstein), and costly disagreement even when a surplus exists. Fairness and limited look-ahead, not just discounting, drive outcomes.

### Ch 5 — Dominance-Solvable Games (limited iterated reasoning; brief)
- **Setup**: games solvable by iteratively deleting dominated strategies. The flagship is the *p-beauty contest* (Nagel 1995): everyone picks a number in [0, 100]; the winner is closest to p × (the average), with p typically 2/3. Iterated dominance shrinks the choice set toward 0, the unique equilibrium.
- **Result**: first-round average choices are around 35–36 (verified via snippet for Nagel 1995), with spikes near 33 and 22 — consistent with one or two steps of reasoning from a naive starting point of 50, not with equilibrium. Choices fall toward 0 over repetitions. Similar patterns appear in "travelers' dilemma", centipede-style and other dominance-solvable games: people do one to three steps.
- **Models**: *level-k* (Stahl & Wilson 1995; Nagel; Costa-Gomes, Crawford & Broseta 2001): level-0 chooses naively (uniformly or salient), level-1 best-responds to level-0, level-2 to level-1, etc. *Cognitive hierarchy* (Camerer, Ho & Chong 2004, developed while the book was written): level-k players best-respond to a Poisson-distributed mixture of all lower levels, with one parameter τ (mean number of thinking steps); τ ≈ 1.5 fits a large set of games (verified via snippet). CH also explains why equilibrium is a good approximation in some games (where one or two steps already land near equilibrium) and terrible in others.
- **So-what**: Assume most people in your group reason one or two steps about others. Rules that only work if everyone anticipates everyone else's anticipation (deep iterated reasoning) will not work on first contact. Make the intended action a level-1 best response to a naive belief about others, and if necessary make level-0 salient.

### Ch 6 — Learning (brief)
- **Question**: given that first-round play is not in equilibrium, how does it move? Camerer surveys three families of adaptive rules and estimates them on many datasets.
  - *Reinforcement learning* (Roth & Erev 1995; Erev & Roth 1998): strategies that paid off get chosen more; players need not know others' payoffs or even the game. Fits well in low-information settings and where feedback is sparse.
  - *Belief learning* (fictitious play, Cournot best-response, weighted fictitious play): players form beliefs about opponents' strategies from history and best-respond. Requires knowing the payoff matrix; fits better when payoffs are known.
  - *Experience-weighted attraction (EWA)* (Camerer & Ho 1999): a hybrid in which each strategy has an "attraction" updated by realized payoff *and* by forgone payoff (weighted by a parameter δ); δ = 0 gives reinforcement, δ = 1 with certain other parameters gives belief learning. EWA usually fits and predicts better out of sample than either parent, and later "functional EWA" (Ho, Camerer & Chong 2007) reduces the free parameters. Camerer also discusses *sophisticated* learning and *teaching* (Camerer, Ho & Chong 2002): some players know others learn and act to steer them, which matters in repeated games with fixed partners.
- **Regularities**: convergence is faster with rich feedback and strict equilibria; learning often drifts toward equilibrium and stalls; the drift's direction depends on early rounds.
- **So-what**: You can shape what a group learns by controlling *feedback* (what people see about what others did and what they would have earned) and *early rounds*. A group's steady state is path-dependent, so seed the first few interactions.

### Ch 7 — Coordination
Coordination games have multiple equilibria; theory says little about which is chosen. Camerer reviews the experimental literature on equilibrium selection, which is where behavioral game theory meets Schelling and Skyrms.

**Game classes and findings**
- *Pure matching / focal points*: Mehta, Starmer & Sugden (1994) formalized Schelling's focal-point idea: given a coordination task ("name a year", "pick a number"), people coordinate far above chance by using labels and cultural salience. Pure Nash reasoning cannot explain this; a theory of "team reasoning" or shared salience is needed. Coordination on labels is fragile when salience is ambiguous.
- *Stag hunt (assurance) games*: two equilibria, one payoff-dominant (both hunt stag) and one risk-dominant (both hunt hare). Cooper, DeJong, Forsythe & Ross (1990, 1992) found that play usually converges to the risk-dominant, inefficient equilibrium unless communication is allowed; *one-way* cheap talk helps, *two-way* cheap talk helps more, and pre-play talk almost always raises stag-hunting. Strategic uncertainty — fear that the other will play safe — beats payoff dominance. Rydval & Ortmann and others (post-book) showed that the payoff to the safe action is a strong predictor of outcomes.
- *Weak-link (minimum-effort) games*: Van Huyck, Battalio & Beil (1990). Each of n players chooses an effort 1–7; group payoff depends on the *minimum* effort, and each unit of one's own effort is costly. Every common effort level is an equilibrium, Pareto-ranked with 7 best. Findings: groups of 14–16 collapsed to effort 1 within about ten rounds; first-round efforts were spread with many choosing high, but one low chooser drags the minimum down and everyone races to the bottom. Fixed pairs converged to 7. (Group-size result verified via snippet; exact round counts from background knowledge.) The pattern is robust and has been replicated many times: large groups never coordinate efficiently in the baseline game.
- *Median-effort games* (Van Huyck, Battalio & Beil 1991): payoff depends on the median rather than the minimum; groups converge quickly to whatever the first-round median was — strong history dependence with no drift to the worst outcome. The rule for aggregating individual contributions matters enormously.
- *Bonuses and cheap interventions*: raising the bonus for the minimum, lowering effort cost, and communication all raise efficiency; a leader's suggestion or a shared history of success can select a good equilibrium.
- *Market-entry games*: n players decide whether to enter a market of capacity c. Even without communication, aggregate entry tracks capacity closely from the first round (Kahneman called it "magic"), though individuals do not play mixed equilibria; heterogeneity and level-k thinking produce the aggregate fit.

**Camerer's synthesis**
- Equilibrium selection is driven by (a) *salience and labels* (focal points), (b) *strategic uncertainty* and the payoff to the safe action (risk dominance), (c) *history* (early rounds lock in), (d) *group size* (larger groups are more fragile in weak-link games because one defector spoils the minimum), and (e) *communication*, which works partly by changing beliefs and partly by creating social commitment.
- The efficient equilibrium is not self-enforcing in the sense of being reachable; it needs a selection device.

**Post-2003 additions worth knowing**
- Weber (2006, verified via snippet): large groups that *start* small and grow gradually, with entrants shown the group's history, can reach and sustain high effort — the first demonstration of efficient large-group tacit coordination. Groups that start large fail.
- Brandts & Cooper (2006, 2007): in a "corporate turnaround" weak-link game, raising the bonus for coordination rescues stuck groups, and a manager's communication (especially messages asking for high effort and emphasizing mutual benefit) works as well as or better than money; simple exhortation from a leader is cheap and effective.
- Chaudhuri, Schotter & Sopher (2009): advice between generations of players helps only when common knowledge (publicly read aloud), not when private. Blume & Ortmann (2007): cheap talk in weak-link games raises efficiency substantially; Cachon & Camerer (1996): having to *pay* to play (a forward-induction cue) selects the efficient equilibrium.

**So-what for designers**
- Weak-link structures (anything where the worst performer determines the outcome: security, release pipelines, joint deadlines) are fragile at scale. Either shrink the group whose minimum matters, change the aggregation rule (median, average, "best of"), or grow the group from a coordinated core.
- Make the intended equilibrium focal: name it, put a leader's suggestion on it, and give a history of success. Cheap talk is far from cheap in its effects.
- Reduce the cost of failed cooperation (the payoff to the safe action is the enemy): insurance, lowered downside for early high effort, or bonuses conditional on the minimum.
- Early rounds decide everything. Over-invest in the first few cycles of a new team or community.

### Ch 8 — Signaling and Reputation (one paragraph)
Games with private information: signaling games, and reputation formation in finitely repeated trust and chain-store games (Camerer & Weigelt 1988), where a small fraction of committed cooperative types induces rational players to mimic them until near the end. Reputation-building happens roughly as sequential-equilibrium models predict once players are experienced, but with a "homemade prior" — players act as if more honest types exist than the experimenter induced, itself a social-preference effect. Equilibrium refinements predict poorly on first play and better after learning.

### Ch 9 — Conclusion: What Do We Know, and Where Do We Go? (one paragraph)
Camerer summarizes the three amendments and argues for parametric behavioral models (inequity aversion, cognitive hierarchy, EWA) as the path to a cumulative science. Open questions that became the next fifteen years' agenda: field validity, neural mechanisms, communication, and the interaction between learning and social preferences. He is candid that BGT is descriptive rather than normative.

## The 5-10 ideas you must carry out of this book
1. **Three amendments, not a rejection.** Real play differs from equilibrium because of social preferences, limited iterated thinking, and learning. Diagnose which one is operating before you intervene.
2. **People pay to punish unfair intentions.** Ultimatum rejections (about half of offers below 20% in Western samples) are robust across decades and countries and are driven by inferred intentions, not outcomes alone.
3. **Generosity is real but conditional.** Dictator giving (~20–30% on average, a third give nothing) collapses under anonymity and rises under observation; reciprocity, not altruism, is the main engine of cooperation.
4. **Fairness norms are cultural.** Across 15 small-scale societies mean ultimatum offers ran from ~26% to ~58%, tracking market integration and the payoffs to cooperation in daily life. Students are mid-range, not the human default.
5. **Most people think one or two steps ahead.** The beauty contest and cognitive hierarchy (τ ≈ 1.5) say deep iterated reasoning is rare on first contact; equilibrium is reached only when the game makes it easy or through learning.
6. **Weak-link coordination fails at scale.** With 14–16 players, minimum-effort games collapse to the worst equilibrium; pairs reach the best. The aggregation rule and group size are design variables.
7. **Selection devices beat payoff dominance.** Strategic uncertainty (fear of others playing safe) wins over efficiency unless communication, leadership, focal labels, forward induction or gradual growth make the good equilibrium believable.
8. **History locks in.** Learning models (EWA and kin) and median-effort experiments show early rounds determine the steady state; the first few interactions of a group are disproportionately valuable.
9. **Aggregates can look rational when individuals are not.** Mixed-strategy and market-entry results fit at the population level thanks to heterogeneity; don't infer individual sophistication from aggregate fit.
10. **No single social-preference model wins.** Inequity aversion is the workhorse; reciprocity is needed for intention effects; Charness–Rabin's efficiency/maximin concerns fit allocation data better. Model people as a distribution of types.

## Mental models & vocabulary
- **Social preferences** — utility that depends on others' payoffs or on the fairness of the process — bites whenever you assume "they'll take any positive offer".
- **Inequity aversion (Fehr–Schmidt α, β)** — disutility from being behind (α) or ahead (β) — predicts rejection of low offers and voluntary contribution when others contribute.
- **Reciprocity (positive/negative)** — rewarding kindness and punishing unkindness at a cost — the mechanism behind gift exchange and ultimatum rejections; intention-sensitive.
- **Conditional cooperator** — contributes if others do — the plurality type; needs visibility of others' behavior to function.
- **Level-k / cognitive hierarchy (τ)** — players reason a finite number of steps about others — explains beauty-contest choices and why "obvious" equilibria are missed on first play.
- **EWA (experience-weighted attraction)** — learning rule blending reinforcement and belief learning via a forgone-payoff weight δ — tells you that richer feedback (showing forgone payoffs) accelerates learning.
- **Payoff dominance vs. risk dominance** — the efficient equilibrium vs. the one that is safest against uncertainty about others — risk dominance usually wins without communication.
- **Strategic uncertainty** — not knowing what others will do even when the game is common knowledge — the root of coordination failure; lowered by talk, history and commitment.
- **Weak-link (minimum-effort) game** — outcome set by the worst contributor — the model for any "one broken link" process; fragile in large groups.
- **Focal point** — an equilibrium selected because it is salient — cheap to create with labels and leadership, fragile when salience is contested.
- **Homemade prior** — players act as if more cooperative types exist than were induced — social preferences leaking into reputation games.

## Evidence strength & limits
- **Robust**: ultimatum offers around 40% and rejection of low offers; dictator giving well above zero but sensitive to anonymity; trust-game sending and partial return; beauty-contest first-round averages around 35; weak-link collapse in large groups; risk-dominant selection in stag hunts without communication; efficacy of cheap talk in coordination. These have been replicated across dozens of labs and decades. Camerer et al. (2016, *Science*) replicated 18 lab experiments in economics from top journals with 61% showing a significant same-direction effect and replicated effects averaging about two-thirds of the originals (verified via snippet) — better than social psychology's rate, but a reminder that effect sizes in the original literature are inflated.
- **Contested / fragile**:
  - *Dictator giving as evidence of altruism.* List (2007) and Bardsley (2008) showed that adding a "take" option or changing the action set shifts giving dramatically; giving reflects the experimenter-created norm of the situation more than a stable preference. Camerer already treats it cautiously; later work strengthened the caution.
  - *Gift exchange in the field.* Gneezy & List (2006, verified via snippet): higher-than-promised wages raised output in library data entry and door-to-door fundraising for the first few hours only, after which effort fell back; the "gift" cost the employer more than it earned. Later field work (Kube, Maréchal & Puppe 2012) found non-monetary gifts and *wage cuts* have larger and more persistent effects than wage raises — negative reciprocity is stronger than positive. Esteves-Sorenson & Macera and Hennig-Schmidt et al. found weak or null gift effects in some field settings. Lab gift exchange is robust; its field magnitude and persistence are modest and context-dependent.
  - *Which social-preference model.* Fehr–Schmidt remains widely used for tractability, but its estimated parameters are unstable across games; Charness–Rabin's efficiency concerns fit allocation games better; intention-based models are needed for the Blount-type results; Bruhin, Fehr & Schunk (2019) estimate that roughly 40% of subjects are "strongly altruistic" behind or "behindness-averse" types while a large minority are close to selfish, again pointing to type heterogeneity as the real finding. Camerer's "no winner" verdict has held up.
  - *Cross-cultural conclusions.* Henrich et al. (2001) had small samples per society and used varied procedures; the 2010 *Science* follow-up (Henrich, Ensminger et al.) with dictator, ultimatum and third-party punishment games in 15 societies found that market integration and world-religion membership predict fairer offers, and community size predicts more punishment (verified via snippet). Causality (do markets make people fair, or do fair people build markets?) is unresolved; critics also note that game framing may not be equivalent across cultures.
  - *Learning models.* EWA's out-of-sample predictive advantage over simpler rules is modest in many datasets, and Wilcox (2006) showed that pooled estimation with heterogeneous subjects biases toward reinforcement-like fits. The qualitative points (feedback matters, history matters) are robust; the specific parametric claims are not the load-bearing ones.
  - *Stakes.* High-stakes ultimatum studies (Andersen et al. 2011 in India, up to months of income) show rejection rates fall substantially as stakes rise; costly punishment is real but bounded.
- **What Camerer is arguing vs. showing**: he *shows* the regularities; he *argues* that parametric behavioral models are the right response and that they generalize standard theory. Critics (e.g., Binmore; Smith) argue that many "anomalies" are artifacts of one-shot play with unfamiliar games, and that with experience and market discipline standard theory does fine. Camerer's own learning chapter half-concedes this for converged play.
- **The population**: nearly all pre-2003 evidence is from undergraduates in the US, Europe, Israel and Japan; Henrich's "WEIRD" critique (2010) applies.

## Design implications for cooperation in real groups
- Model your group as ~30% self-interested, ~50% conditional cooperators, a small tail of altruists; let conditional cooperators see others cooperating. [E]
- Make allocations that must be unequal look procedurally impartial (rule- or lottery-based), because people punish intended unfairness far more than unlucky outcomes. [E]
- Expect costly retaliation against offers or terms perceived as below ~20–30% of "fair share"; it will not disappear at higher stakes, only shrink. [E]
- Use observation and identifiability to sustain generosity; anonymity roughly halves it. [E]
- For any weak-link process, cap the group whose minimum matters at a handful of people, or change the aggregation rule to median/average. [E]
- Grow coordinated groups from a small core with a visible history of success rather than launching at full size. [E] (Weber 2006; single-lab lineage — test in your setting.) [H]
- Have a leader publicly name the target equilibrium and ask for it; public, common-knowledge communication is more effective than private messaging. [E]
- Lower the payoff to the safe, non-cooperative action (reduce the downside of being the only one who tried) rather than only raising the reward for success. [E]
- Show people what they *would have* earned under alternative choices (forgone payoffs) to speed learning toward the cooperative equilibrium. [H] (EWA implies it; direct field tests are scarce.)
- Do not rely on members reasoning more than two steps about others; make the desired action a best response to a naive belief. [E]
- Calibrate the fairness baseline to the group's cultural norms of exchange; do not import student-lab norms. [E]
- Treat pay raises as a weak and decaying reciprocity lever; treat pay cuts, broken promises and non-monetary gestures as strong ones. [E]
- Value the fairness of process as a good in itself, not only as an instrument for compliance. [V]

## Connections
- **04-games-of-strategy** — supplies the games Camerer tests; read Camerer as the empirical annex. Tension: Dixit et al. present equilibrium as prediction; Camerer shows it is a benchmark for experienced play only.
- **05-micromotives-and-macrobehavior** — Schelling's focal points and critical-mass dynamics get lab confirmation in ch 7; market-entry results are Schelling-style aggregate order from heterogeneity.
- **07-stag-hunt** — Skyrms's evolutionary selection of risk-dominant equilibria matches Cooper et al.; Camerer adds the human selection devices (talk, history, leadership) Skyrms models via networks and signals.
- **08-grammar-of-society** — Bicchieri's norms-conditional-on-expectations is the natural reading of dictator/ultimatum sensitivity to framing and observation.
- **09-governing-the-commons** — Ostrom's monitoring and graduated sanctions rest on the costly punishment documented here; type heterogeneity explains why sanctioning institutions are needed.
- **01-secret-of-our-success** — Camerer reports the cross-cultural ultimatum variation; Henrich explains it. Tension: preferences as parameters vs. as culturally transmitted and changing.
- **03-social-psychology** — reciprocity, fairness heuristics and audience effects are the psychological underpinnings of ch 2.
- **10-networks-crowds-markets** — ch 19 (cascades on networks) formalizes equilibrium selection; Camerer's weak-link and history results are the behavioral counterpart.
- **11-bounds-of-reason** — Gintis builds on Camerer's evidence but wants a unified framework Camerer declines to claim: are BGT's amendments parameters or a different theory?

## Retrieval practice

1. (Recall) In a standard Western student sample, roughly what fraction of ultimatum offers below 20% are rejected, and what is the typical mean offer?
<details>About half of offers below 20% are rejected; mean offers are around 40% of the pie, with a mode at 50%. Both numbers are approximate and vary with stakes and culture.</details>

2. (Explain-why) Why do proposers give much less in the dictator game than in the ultimatum game, and what does that tell you about the motive behind ultimatum offers?
<details>Dictator giving averages 20–30% versus ~40% in ultimatum. The gap shows that much of ultimatum generosity is strategic fear of rejection, not altruism; the residual dictator giving is real but fragile and observation-dependent.</details>

3. (Explain-why) What does Blount's computer-generated-offer treatment show, and which class of models does it favor?
<details>When low offers come from a random device rather than a human, rejection rates fall sharply. People punish inferred intentions, favoring reciprocity/intention-based models over pure outcome-based inequity aversion.</details>

4. (Apply) Your 20-person on-call rotation fails whenever the least prepared engineer is on duty, and preparation has drifted to the minimum. Which Camerer game is this and what are three interventions the evidence supports?
<details>A weak-link (minimum-effort) game. Interventions: shrink the group whose minimum matters (small pods); grow from a coordinated core with visible history (Weber); public leader communication naming the target plus a bonus conditional on the minimum (Brandts & Cooper); reduce the cost of preparing when others don't.</details>

5. (Recall) What did Henrich et al. (2001) find across 15 small-scale societies, and which two variables explained most of the variation?
<details>Mean ultimatum offers ranged from ~26% to ~58%; market integration and the payoffs to cooperation in everyday production explained most between-group variance, while individual demographics explained little.</details>

6. (Spot-the-misconception) "The beauty-contest results show people are irrational." What is wrong with this?
<details>Choices around 35 are consistent with one or two steps of best-response reasoning from a naive belief — bounded but structured thinking, well captured by level-k / cognitive hierarchy (τ ≈ 1.5). And choices converge toward equilibrium with repetition, so it is a first-contact phenomenon, not general irrationality.</details>

7. (Apply) You run a two-team stag-hunt situation: both teams profit if both adopt a shared tooling standard, but each fears the other will not. Communication is cheap. What does the lab predict about one-way versus two-way cheap talk?
<details>Without talk, expect the risk-dominant (safe, inefficient) outcome. One-way announcements raise adoption; two-way mutual announcements raise it more (Cooper et al.). Public, common-knowledge commitments work best.</details>

8. (Explain-why) Why did median-effort groups not collapse the way minimum-effort groups did?
<details>With a median rule a single low chooser cannot drag the outcome down; groups lock in on the first-round median. The aggregation rule determines how fragile coordination is to one defector, and history matters more than drift.</details>

9. (Spot-the-misconception) "Gift exchange in the lab means paying above-market wages will buy sustained extra effort in the field."
<details>Gneezy & List (2006) found the effort boost lasted only a few hours and cost more than it returned; later field studies find positive reciprocity weak and decaying while negative reciprocity to cuts is strong. The lab result is robust, its field magnitude is modest.</details>

10. (Recall) What are EWA's two parent models and what single parameter links them?
<details>Reinforcement learning (update on realized payoffs) and belief learning (update on all payoffs given beliefs). The forgone-payoff weight δ interpolates: δ = 0 is reinforcement-like, δ = 1 (with other settings) is belief-learning-like.</details>

## Common misreadings of this book
- **"Camerer refutes game theory."** He keeps the structure and the equilibrium benchmark; the claim is that the model of the player needs three parametric amendments, and that with experience play often approaches equilibrium.
- **"People are altruists."** The dominant motive is reciprocity and intention-sensitive fairness, conditional on observation and on what others do; unconditional altruism is a small minority behavior, and dictator giving is fragile.
- **"Fairness is a human universal at 50-50."** The 15-society data show the *disposition* to have fairness norms is universal but the *content* varies widely with the economics of daily life.
- **"Coordination failure is a payoff problem."** In weak-link and stag-hunt games the payoffs already favor cooperation; the failure is strategic uncertainty plus history. The fixes are informational and social (talk, leadership, growth, focal labels) more often than monetary.
- **"Lab numbers transfer directly."** Every headline number here comes from students playing unfamiliar one-shot games for small stakes; field magnitudes (gift exchange, high-stakes ultimatum) are smaller. Use the lab for mechanisms and directions, not point estimates.
