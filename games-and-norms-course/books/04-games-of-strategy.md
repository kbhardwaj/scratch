# Games of Strategy — Avinash Dixit, Susan Skeath & David McAdams (5th ed., Norton 2020; David Reiley co-authored eds. 3–4)
Level: Mechanisms  ·  Priority: Core
Est. reading time saved: ~25h  ·  Your time with this file: ~40 min

## The book in one sentence
The standard toolkit for reasoning about situations where your best move depends on what others will do: draw the game, find its equilibria, then use commitment, information, repetition and rule-design to change which equilibrium you land in.

## The book in one paragraph
Dixit, Skeath and McAdams build game theory from the ground up with little math. Part One fixes the vocabulary (players, strategies, payoffs, information, sequential vs. simultaneous moves). Part Two gives the solution concepts: rollback for sequential games, Nash equilibrium and dominance for simultaneous games, mixed strategies when no pure equilibrium exists. Part Three covers the classes of games that matter most for social life: strategic moves (commitments, threats, promises), uncertainty and information (signaling, screening), the prisoners' dilemma and the repeated-game logic that can rescue cooperation, collective action with many players, and evolutionary games where strategies are inherited or imitated rather than chosen. Part Four applies the toolkit to brinkmanship, incentive design, auctions, voting and bargaining. Throughout, the authors flag where laboratory evidence diverges from prediction and treat the gap as information about real people, not a reason to drop the models.

## Why it's in this curriculum (the question to read it with)
Read it asking: **for the group I care about, what game are the members actually playing, and which lever — payoffs, information, sequencing, repetition, or rules — would move them to a better equilibrium?** The other books explain where payoffs and beliefs come from (Henrich, Laland, Gilovich), show that real people deviate from equilibrium predictions (Camerer, Schelling), or describe institutions that change the game (Ostrom, Bicchieri, Skyrms, Easley & Kleinberg). This book supplies the language those arguments are conducted in. Without it, "incentives", "credible threat", "focal point", "signaling" and "equilibrium" stay buzzwords rather than diagnostic tools.

## Table of contents

Verification status: **Parts One–Four and Chapters 1–15 verified against a search-engine snippet of the Norton / Google Books listing for the 5th edition (2020).** The snippet truncated Chapter 16 after the word "Strategy" and did not show Chapter 17. Those two are reconstructed from the 4th-edition ordering and from a separate snippet describing Part Four's application chapters (brinkmanship, voting, auctions, bargaining); the 5th edition might number or title them slightly differently. Direct fetches of wwnorton.co.uk and books.google.com were blocked by the proxy. From background knowledge (not verified): the 4th edition (Dixit, Skeath & Reiley, 2015) had the same structure except that "Uncertainty and Information" preceded "Strategic Moves" and the incentive chapter was titled "Mechanism Design".

**Part One — Introduction and General Principles**
1. Basic Ideas and Examples
2. How to Think about Strategic Games

**Part Two — Fundamental Concepts and Techniques**
3. Games with Sequential Moves
4. Simultaneous-Move Games: Discrete Strategies
5. Simultaneous-Move Games: Continuous Strategies, Discussion, and Evidence
6. Combining Sequential and Simultaneous Moves
7. Simultaneous-Move Games with Mixed Strategies

**Part Three — Some Broad Classes of Strategies and Games**
8. Strategic Moves
9. Uncertainty and Information
10. The Prisoners' Dilemma and Repeated Games
11. Collective-Action Games
12. Evolutionary Games

**Part Four — Applications to Specific Strategic Situations**
13. Brinkmanship: The Cuban Missile Crisis
14. Incentive Design
15. Auctions, Bidding Strategy, and Auction Design
16. Strategy and Voting (title partly reconstructed)
17. Bargaining (reconstructed)

Core book: every chapter covered; most words on 3, 4, 7–12, which the rest of the curriculum leans on.

## Chapter-by-chapter: the salient knowledge

### Part One / Ch 1–2 — Basic Ideas and Examples; How to Think about Strategic Games
- Core claims: a game is any situation where outcomes depend on choices by two or more decision-makers aware of each other. Strategic thinking means reasoning about what others will do given what they think you will do.
- Six classification questions for any interaction: sequential or simultaneous? pure conflict or some common interest? one-shot or repeated, with the same or changing partners? full information or not? fixed rules or manipulable? enforceable agreements or only self-enforcing ones?
- Vocabulary: players; strategies (complete contingent plans, not single actions); payoffs (numbers that rank outcomes; ordinal usually suffices); rationality (consistent pursuit of your own payoffs, whatever they contain — altruism allowed); common knowledge of the rules; equilibrium (each strategy a best response to the others).
- Examples: route choice with congestion, penalty kicks, a study-group free-rider problem, the "guess two-thirds of the average" game that exposes depth of reasoning.
- So-what: the six questions are the first diagnostic pass on any group. Many cooperation failures are misdiagnosed because a repeated, incomplete-information, mixed-motive game is treated as one-shot pure conflict. "Non-cooperative" in the technical sense means agreements must be self-enforcing — the situation of nearly every community and platform.

### Part Two / Ch 3 — Games with Sequential Moves
- Setup: players move in turn and later movers see earlier moves. Draw a tree: decision nodes, branches, terminal payoffs. A strategy specifies a choice at every node the player might reach.
- Result (rollback / backward induction): start at the last decisions, keep each player's best branch, prune the rest, work backward. The surviving path is the rollback equilibrium. Off-path plans — what a player *would* do at nodes never reached — are what make earlier choices rational.
- Worked example: a potential entrant chooses Enter or Stay out; if Enter, the incumbent chooses Fight or Accommodate. Payoffs (entrant, incumbent): Stay out → (0, 10); Enter, Accommodate → (3, 5); Enter, Fight → (−2, 2). At the incumbent's node Accommodate (5) beats Fight (2); the entrant foresees this and enters. "We'll fight" is not credible — the seed of Chapter 8.
- Further: first- vs. second-mover advantage depends on the game; finite perfect-information games always have a rollback solution (chess has one, we cannot compute it); the *centipede game* shows rollback predicting immediate defection where lab players cooperate for several rounds — the first flag that theory and behavior part ways.
- So-what: sequencing and visibility are levers. Rollback also disciplines wishful thinking: "if we do X, will they really respond as we hope, given *their* payoffs?"

### Part Two / Ch 4 — Simultaneous-Move Games: Discrete Strategies
- Setup: players choose without seeing each other's choice; represent as a payoff matrix. A **dominant strategy** is best whatever others do; a **dominated** one is never best. Iterated elimination of dominated strategies shrinks the game.
- Result (Nash equilibrium): a profile where no player gains by switching alone. Best-response method: in each row mark the column player's best cell, in each column the row player's best cell; doubly marked cells are equilibria.
- Worked example — prisoners' dilemma (years in prison, lower is better; row's payoff first):

| | Confess | Deny |
|---|---|---|
| **Confess** | 10, 10 | 1, 25 |
| **Deny** | 25, 1 | 3, 3 |

Confess dominates Deny for both (10 < 25, 1 < 3). Unique equilibrium (Confess, Confess) at 10, 10 — worse for both than (Deny, Deny) at 3, 3. The template for every "individually rational, collectively dumb" outcome.
- Other canonical matrices: **coordination** (two pure equilibria, players want to match); **assurance / stag hunt** (two equilibria, one better for all but riskier); **battle of the sexes** (two equilibria, players disagree which); **chicken** (two equilibria, each prefers the other yields); **matching pennies** (no pure equilibrium). Multiple equilibria are the norm, and the theory alone often cannot say which is played; **focal points** (Schelling) — equilibria that stand out by convention or salience — fill the gap.
- So-what: most cooperation problems are not PDs. A stag hunt is fixed by assurance, battle of the sexes by a fair tie-break, chicken by commitment or turn-taking; only a true PD needs changed payoffs or repetition. Treating a stag hunt as a PD produces heavy enforcement where cheap reassurance would do.

### Part Two / Ch 5 — Simultaneous-Move Games: Continuous Strategies, Discussion, and Evidence
- Setup: when strategies are quantities (price, effort, contribution), draw each player's **best-response function**; Nash equilibrium is where the curves cross. Models: price competition (Bertrand), quantity competition (Cournot), two candidates converging on the median voter.
- Discussion and Evidence: the authors survey failures of the Nash assumptions — no common knowledge of rationality, errors, many equilibria. They cover level-k reasoning (Nash says guess 0 in the two-thirds game; people guess roughly 20–35), learning toward equilibrium over repeated play, and ultimatum-game rejections. Stance: Nash is a benchmark; deviations are systematic and modelable. Camerer's file has the detail.
- Also **rationalizability** — strategies surviving iterated deletion of never-best-responses — a weaker but more defensible concept than Nash.
- So-what: for effort or contribution decisions, ask what each member's best response is to others' levels. Upward-sloping best responses (strategic complements: my effort is worth more when yours is high) make the group tip to a high- or low-effort equilibrium; downward-sloping ones (substitutes: I slack when you work) produce free-riding.

### Part Two / Ch 6 — Combining Sequential and Simultaneous Moves
- Setup: real games mix both; trees contain simultaneous subgames (information sets), or matrices list full contingent strategies.
- Result: **subgame-perfect equilibrium** — Nash in every subgame — rules out incredible threats. Changing the order of moves changes outcomes: making a simultaneous game sequential can create a first- or second-mover advantage; hiding moves can remove one.
- Example: chicken played simultaneously has two pure equilibria (plus a mixed one); if one driver visibly commits first, the sequential version has a unique equilibrium where the other swerves.
- So-what: *who observes what and when* is a design variable. Sealed vs. open bids, blind vs. visible pledges, synchronous vs. asynchronous decisions each change the equilibrium set.

### Part Two / Ch 7 — Simultaneous-Move Games with Mixed Strategies
- Setup: when no pure equilibrium exists, or unpredictability pays, players randomize over pure strategies.
- Result: in a mixed equilibrium each player's mix makes the *opponent* indifferent among the strategies in the opponent's mix. Consequence: your equilibrium mix depends on the *other* player's payoffs, not yours. Nash (1950) proved every finite game has at least one equilibrium once mixing is allowed.
- Worked example — penalty kick, entries are the kicker's scoring probability (kicker maximizes, goalie minimizes):

| | Goalie Left | Goalie Right |
|---|---|---|
| **Kick Left** | 0.5 | 0.9 |
| **Kick Right** | 0.8 | 0.6 |

Kicker picks p = Pr(Left) to make the goalie indifferent: 0.5p + 0.8(1−p) = 0.9p + 0.6(1−p) → p = 1/3. Goalie picks q = Pr(Left) to make the kicker indifferent: 0.5q + 0.9(1−q) = 0.8q + 0.6(1−q) → q = 3/4. Equilibrium scoring rate 70%.
- Evidence: professional penalty takers and tennis servers mix close to equilibrium proportions (Walker & Wooders 2001; Palacios-Huerta 2003 — background knowledge of the literature the book cites), though they alternate too often rather than truly randomizing. Novices do worse. Mixed equilibria in non-zero-sum games exist but are fragile and often make no one better off.
- So-what: unpredictability is a strategy — random audits, rotating inspection. To deter cheating you need probability × penalty ≥ gain, not full surveillance. And the indifference property warns that raising *your* payoff to enforcing does not change *their* cheating rate; it changes your enforcement rate.

### Part Three / Ch 8 — Strategic Moves
- Setup: a strategic move is an action before the main game that changes others' expectations. Following Schelling, three kinds: **commitment** (unconditional), **threat** (conditional punishment), **promise** (conditional reward).
- Core result: a strategic move works only if **credible** — the other side must believe you would carry it out when the moment comes. Since executing a threat usually hurts the threatener too, credibility is manufactured: contracts, reputation, cutting off your own options, delegating to an agent with different incentives, breaking a big move into small steps, brinkmanship (Ch 13), automatic mechanisms. Paradox: reducing your freedom of action can increase your power.
- Worked example: in the entry game the incumbent's threat failed because after entry Accommodate (5) beats Fight (2). Suppose the incumbent signs a contract paying a 4-unit penalty to a third party if it ever accommodates. Now Fight (2) beats Accommodate (5 − 4 = 1); the entrant stays out; the incumbent earns 10 and never pays. The threat became credible by worsening its own alternative.
- Further: threats should be no bigger than needed (oversized threats are less credible and invite escalation); promises must be small enough that keeping them costs less than lost reputation; deterrence and compellence call for different moves; counters include feigned irrationality, cutting communication, and undermining the other's credibility. Lab note: people carry out costly threats and keep costly promises more than self-interest predicts, which is why cheap talk sometimes works.
- So-what: this is the theory of *credible rules*. A norm with a penalty nobody would actually impose is not a norm. Arrange the enforcer's payoff at the moment of enforcement to favor enforcing: rotating monitors, graduated and cheap sanctions (compare Ostrom).

### Part Three / Ch 9 — Uncertainty and Information
- Setup: external risk (nature's moves) and, more importantly, **asymmetric information** — one side knows its type, quality or intentions and the other does not. Two workhorse mechanisms: **signaling** (the informed party takes a costly action that reveals type) and **screening** (the uninformed party designs choices that make types reveal themselves).
- Core result: a signal is credible only if it is *too costly to fake* — its cost must differ across types so only the "good" type finds it worthwhile (Spence 1973 on education; warranties; sunk commitments). Cheap talk informs only when interests are aligned. Equilibria are **separating** (types act differently, are identified), **pooling** (all act alike, nothing revealed) or semi-separating.
- Worked example: an employer will pay 100 for a high-ability worker, 50 for low, but cannot tell them apart. A certification costs the high type 20 in effort and the low type 60. Paying 100 only to certified workers: high type certifies (100 − 20 = 80 > 50); low type does not (100 − 60 = 40 < 50). Separating equilibrium — the certification works even if it teaches nothing. At a cost of 40 for both, both certify and it reveals nothing.
- Also: adverse selection (Akerlof's 1970 lemons market — hidden quality drives out good types), moral hazard (hidden action), Bayesian updating after signals, and the extension to **Bayesian Nash** and **perfect Bayesian equilibrium** (beliefs consistent with strategies on the path and reasonable off it).
- So-what: every heterogeneous group faces the question "who is a cooperator, who is competent, who is committed?" Costly signals (onboarding effort, visible sunk contributions, rituals) and screening menus (tiers, probation) are the formal version of Henrich's credibility-enhancing displays and Ostrom's boundary rules. Design the signal to be cheap for the types you want and expensive for the rest.

### Part Three / Ch 10 — The Prisoners' Dilemma and Repeated Games
- Setup: three families of solutions to the PD — **repetition**, **penalties/rewards** (changing payoffs), and **leadership** (a large player who gains enough to cooperate unilaterally).
- Core result (repetition): with an indefinite horizon and enough weight on the future, cooperation is sustainable as an equilibrium via *contingent strategies* (tit-for-tat, grim trigger): the one-period gain from cheating is outweighed by discounted future losses. With a *known finite* horizon, rollback unravels cooperation from the last round back. Key variables: discount factor or continuation probability, temptation relative to the cooperative payoff, and speed of detection and response.
- Worked example: per-round payoffs — both cooperate (3, 3); both defect (1, 1); defect against cooperator (5, 0). Under grim trigger, cheating once yields 5 then 1 forever; cooperating yields 3 forever. With discount factor δ: cooperate if 3/(1−δ) ≥ 5 + δ/(1−δ), i.e. 3 ≥ 5(1−δ) + δ → δ ≥ 1/2. Cooperation holds if next period is worth at least half of this one (or the game continues with probability ≥ 50%). Raise the temptation to 8 and δ must exceed 5/7.
- Axelrod's tournaments (described in the book): tit-for-tat won by being nice, retaliatory, forgiving and clear — but it is not uniquely optimal and is fragile under noise (two TFT players who misread one move feud forever); contrite or generous variants do better.
- Evidence: one-shot lab PDs show 30–60% cooperation, rising with communication, sequential moves and smaller groups; contributions decay across rounds in finite public-goods games but recover when punishment is allowed (Fehr & Gächter 2000). Detail in Camerer's file.
- So-what: this formalizes the "shadow of the future." Levers: keep interaction indefinite (no announced endpoints), make defection observable fast, keep groups small enough for reputations to travel, and make punishments proportionate and forgiving so noise does not trigger feuds. Where repetition is impossible, change payoffs directly or find a leader who benefits enough to carry the cost.

### Part Three / Ch 11 — Collective-Action Games
- Setup: many players each choose whether to contribute. Model with two curves — payoff to a participant and payoff to a shirker, each as a function of how many others participate. Three shapes: **PD** (shirking dominant; nobody contributes), **chicken** (someone must act; each hopes another will), **assurance** (I contribute if enough others do; two equilibria).
- Core result: the equilibrium number of contributors is where the curves cross; the *social optimum* is generally higher. The gap is the externality: each contributor confers benefits on others they do not count. Marginal social benefit = private benefit + change in everyone else's payoffs.
- Worked example: ten herders each decide whether to add a cow; a cow yields 10 to its owner and cuts every other cow's yield by 1. Privately, adding always pays (10 > 0). Socially, the 10th cow adds 10 and costs 9 others 1 each — net +1; a 12th would cost 11 — net −1. Yet each herder still adds. Overgrazing (Hardin 1968).
- Solutions catalogued: Olson's small groups and selective incentives; a large-player leader; repetition and reciprocity; norms enforced by social sanction (treated as payoff changes); and Ostrom's field evidence that communities solve commons problems without external enforcers. **Tipping** via Schelling-style participation curves: when the payoff to joining rises with the number joining, small pushes flip the group between low and high equilibria.
- So-what: the bridge to the Order books. Identify the shape, estimate where the curves cross, choose the lever: selective incentives for PD, rotation or pre-assignment for chicken, assurance mechanisms (visible pledges, thresholds, matching) for stag hunt. An internalized norm shifts the participant curve up and moves the crossing.

### Part Three / Ch 12 — Evolutionary Games
- Setup: drop rationality. Players carry strategies (phenotypes, habits, cultural rules); higher-payoff strategies reproduce or are imitated more; the population mix shifts. An **evolutionarily stable strategy (ESS)** (Maynard Smith & Price 1973) cannot be invaded by a small group of mutants.
- Core results: every ESS is a Nash equilibrium but not vice versa. In a PD, Always-Defect is the ESS; in a repeated PD, TFT resists invasion by Always-Defect if play lasts long enough, though drift lets nicer strategies creep in. In hawk-dove (chicken), the ESS is a *mixed* population, with more hawks as the prize rises and fewer as the cost of fighting rises. In assurance games both pure equilibria are ESS and the starting mix decides which the population reaches — history and basins of attraction matter.
- Worked example — hawk-dove, prize V = 4, fighting cost C = 6 (row's payoff):

| | Hawk | Dove |
|---|---|---|
| **Hawk** | (4−6)/2 = −1 | 4 |
| **Dove** | 0 | 2 |

All-Hawk is invadable by Dove (0 > −1); all-Dove by Hawk (4 > 2). Stable hawk fraction h makes both types earn the same: −h + 4(1−h) = 2(1−h) → h = 2/3. Raise C to 10 and h falls to 4/7.
- Also: replicator dynamics drawn graphically; cooperation invading via assortment (cooperators who meet cooperators); the "bourgeois" strategy (fight if owner, yield if intruder) as an ESS that turns an arbitrary asymmetry into a property convention — a bridge to Skyrms.
- So-what: the engine behind Henrich, Laland and Skyrms. Norms need not be chosen rationally to persist; they need to be uninvadable. Ask what happens if a few members behave differently — does it spread or die? A cooperative stag-hunt equilibrium is stable only inside its basin; a shock that pushes enough people to defect flips the group, and recovery needs coordinated, not individual, moves.

### Part Four / Ch 13 — Brinkmanship: The Cuban Missile Crisis
- Setup: a *probabilistic* threat. Instead of a certain punishment too costly to be credible, the player deliberately creates a risk that events get out of hand (Schelling's threat that leaves something to chance), controlling the *level* of risk rather than the outcome.
- Result: brinkmanship works when some risk level is high enough that the other side prefers to concede and low enough that the threatener prefers running it to conceding. Since resolve is unknown, raise the risk gradually and let the other side reveal its type. Actual disaster is a real possibility, not a mistake.
- The 1962 crisis is worked in detail: the naval quarantine as a risk-raising step short of attack, multiple decision-makers creating genuine chance, mutual concession. The rational-actor reading is presented as one of several (Allison's organizational and bureaucratic models are alternatives).
- So-what: escalating disputes inside organizations follow this logic. Design off-ramps and graduated steps so parties can escalate a little without catastrophe; recognize that ambiguity about sanctions is sometimes what makes them credible.

### Part Four / Ch 14 — Incentive Design
- Setup (principal-agent): the principal wants effort it cannot observe, only noisy output. The **participation constraint** (agent accepts) and the **incentive-compatibility constraint** (agent chooses the desired effort) determine the contract.
- Results: observable effort → flat wage conditional on effort. Unobservable → pay on output, shifting risk to a risk-averse agent who must be compensated; the optimal contract trades incentive strength against risk-sharing. Under **hidden information** (agent knows its type), offer a menu and let types self-select — Chapter 9's screening as mechanism design. Multiple tasks: incentives on the measurable task crowd out the unmeasured; tournaments filter common noise but invite sabotage. The 5th edition expanded this with McAdams's market-design perspective.
- Worked example: output is "good" with probability 0.8 under high effort, 0.4 under low; high effort costs the agent 10; bonus b paid only on good output. Incentive compatibility: 0.8b − 10 ≥ 0.4b → b ≥ 25. A risk-neutral principal pays 25 on success; a risk-averse agent needs more than the expected 20 to accept — the price of unobservability.
- So-what: pay on what you can measure only if it tracks what you want; otherwise you buy gaming. Where output is noisy and members risk-averse, strong incentives are expensive and norm- or reputation-based motivation is cheaper — but explicit incentives can crowd out those motivations (evidence in Camerer and Gilovich files).

### Part Four / Ch 15 — Auctions, Bidding Strategy, and Auction Design
- Setup: formats — English (ascending), Dutch (descending), first-price sealed, second-price sealed (Vickrey), all-pay. Environments — **private values** (each knows their own value) vs. **common value** (same value for all, noisy estimates).
- Results: second-price with private values → bidding your true value is dominant (Vickrey 1961), since your bid sets only whether you win, not what you pay. First-price → shade below value, more with fewer rivals. **Revenue equivalence**: with risk-neutral bidders and independent private values, all standard formats yield the same expected revenue. **Winner's curse**: in common-value settings the winner has the most optimistic estimate, so winning is bad news; rational bidders shade, real ones (oil leases, free agents) often do not.
- Worked example: values 10 and 6 in a second-price auction; each bids their value; the 10-bidder wins and pays 6. Bidding 8 instead still wins at 6; bidding 5 loses a profitable object. Truthfulness is dominant.
- Design (McAdams): reserve prices, entry fees, collusion-proofing (rings are easier in open ascending formats), FCC spectrum auctions, the school-milk collusion case. All-pay auctions model lobbying, patent races and status contests where losers still pay.
- So-what: allocating scarce slots, resources or tasks inside a group is an auction in disguise. Vickrey-style rules make honesty easy; open formats reveal information but invite collusion; all-pay structures (compete for status by visible effort) waste effort. When members estimate a common value (project cost), the most enthusiastic volunteer is the likeliest to have overestimated.

### Part Four / Ch 16 — Strategy and Voting
- Setup: rules covered — plurality, runoff, pairwise majority (Condorcet), Borda count, approval voting, single transferable vote.
- Core results: the **Condorcet paradox** (majority preferences can cycle, so "the group's preference" may not exist); **Arrow's theorem** (1951: no aggregation rule satisfies a short list of reasonable conditions at once); **Gibbard–Satterthwaite** (any non-dictatorial rule over three or more options can be manipulated by insincere voting); the **median voter theorem** (with single-peaked preferences on one dimension, the median voter's ideal wins pairwise majority and cannot be manipulated). Agenda control decides the outcome when preferences cycle.
- Worked example: Alice A > B > C; Bob B > C > A; Carol C > A > B. Pairwise: A beats B, B beats C, C beats A. An agenda-setter who wants A schedules B vs. C first (B wins), then A vs. B (A wins).
- So-what: any group that "decides by vote" has a gameable rule, and the choice of rule is itself a decision. Make preferences single-peaked where possible (one dimension at a time), prefer rules whose manipulation is hard or harmless (approval voting is relatively robust), publish the agenda process, and distrust "the group wants X" when preferences are multidimensional.

### Part Four / Ch 17 — Bargaining
- Setup: two parties split a surplus that exists only if they agree. **Cooperative/axiomatic** approach: the Nash bargaining solution (1950) maximizes the product of each side's gain over its outside option (BATNA), weighted by bargaining power. **Non-cooperative** approach: alternating offers (Rubinstein 1982), where impatience determines the split.
- Core results: each party gets its outside option plus a share of the remaining surplus; improving your BATNA is the most reliable way to improve your deal. In alternating offers the more patient party gets more; with equal patience and rapid offers the split approaches 50/50. Complete-information models predict immediate agreement, so real delays (strikes, stalls) come from incomplete information (testing resolve) or strategic commitment (Ch 8).
- Worked example: buyer values a bike at 300, seller's outside option is 100; surplus 200. Equal power → split the surplus → price 200. If the buyer can credibly show another bike available at 220, the buyer's outside option rises and the price falls toward the 160s.
- Also: multi-issue bargaining (trading across issues with different valuations creates integrative deals), multi-party bargaining, and manipulating BATNAs and information as strategic moves. Behavioral note: ultimatum responders reject low offers and proposers offer 40–50%, far from the subgame-perfect prediction — see Camerer.
- So-what: dividing credit, workload or budget is bargaining. Outside options move deals more than tactics; fairness norms set the reference point real people bargain around; delay usually signals an information problem that transparency fixes more cheaply than pressure.

## The 5-10 ideas you must carry out of this book
1. **Draw the game before arguing about the outcome.** Players, strategies, payoffs, order, information. Most disputes about "why people won't cooperate" dissolve once the matrix is written down.
2. **Nash equilibrium is a stability condition, not a verdict on goodness.** Mutual defection is an equilibrium because it is stable, not because anyone wants it.
3. **Most cooperation problems are not prisoners' dilemmas.** Stag hunts, chicken and battle of the sexes fail differently and need assurance, turn-taking or tie-breaks rather than enforcement.
4. **Credibility is manufactured, usually by limiting yourself.** Threats and promises work only if executing them is in your interest at the time; commitment devices, delegation, reputation and small steps create that interest.
5. **The shadow of the future rescues cooperation only when it is long, uncertain and observable.** Announced endpoints unravel cooperation; noise demands forgiving strategies.
6. **Information asymmetry is solved by costly signals and self-selecting menus.** A signal works when it is cheaper for the good type; a screen works when each type reveals itself by choice.
7. **Collective action has three shapes and the fix depends on the shape.** Find where participant and shirker payoff curves cross; norms shift the curves.
8. **Stability without rationality.** A norm persists if it cannot be invaded; which of several stable norms you get depends on where you started.
9. **Rules are games too.** Voting rules, auction formats, contracts and agendas shape outcomes and can be gamed; honest-is-dominant designs (Vickrey, median voter on single-peaked issues) are rare and valuable.
10. **The theory is a benchmark and the deviations are systematic.** Real players cooperate more in one-shot PDs, reject unfair splits, over-bid in common-value auctions and reason to limited depth. Design with these facts, not against them.

## Mental models & vocabulary
- **Strategy** — a complete contingent plan, not a single move — bites when a rule is judged only by its expected path, ignoring what it commits you to off-path.
- **Rollback** — solve sequential games from the end — bites when you ask "and then what will they do?" one step beyond intuition.
- **Nash equilibrium** — no one gains by deviating alone — bites in diagnosing why a bad state is sticky.
- **Dominant / dominated strategy** — best (never best) regardless of others — bites in checking whether a problem is really a PD.
- **Subgame-perfect equilibrium** — Nash in every subgame; no incredible threats — bites in judging whether a sanction would actually be applied.
- **Opponent's indifference** — your equilibrium mix depends on their payoffs — bites in random-audit design and in why raising your own stake does not change their behavior.
- **Focal point** — equilibrium chosen by salience or convention — bites whenever a group has several ways to coordinate and needs a default.
- **Strategic move** — commitment, threat or promise; must be credible, observed and understood — bites in every enforcement design.
- **Signaling / screening; separating vs. pooling** — costly actions that reveal type; menus that induce self-revelation — bites in membership, hiring and trust-building.
- **Discount factor / shadow of the future** — weight on future payoffs; the price of defection — bites in deciding whether repetition alone can hold a group together.
- **Trigger strategies** — grim, tit-for-tat, generous TFT; trade harshness for noise-robustness — bites in designing graduated sanctions.
- **Collective-action shapes (PD / chicken / assurance)** — bites in choosing between incentives, assignment and assurance.
- **Externality** — my action's effect on others' payoffs not counted in mine — bites as the root of every commons problem.
- **ESS and basin of attraction** — uninvadable strategy; the starting mixes that lead to it — bites in judging whether a norm survives a shock.
- **Winner's curse** — winning a common-value contest implies overestimation — bites in volunteer allocation and estimates.
- **BATNA** — what you get without agreement — bites in every internal negotiation.
- **Incentive compatibility / participation constraint** — the desired action must be the agent's own best choice, and the deal worth accepting — bites in any pay-for-performance or points scheme.

## Evidence strength & limits
- **Robust:** the mathematics. Existence of Nash equilibria, rollback in finite perfect-information games, ESS conditions, Vickrey dominance, Arrow and Gibbard–Satterthwaite, revenue equivalence under its assumptions are theorems and the book's exposition is standard. The folk-theorem logic of repeated games is also a theorem — but an *existence* result: cooperation *can* be an equilibrium, alongside permanent defection and much else. The theory does not say which occurs.
- **Well supported empirically:** professionals' mixed-strategy play in zero-sum sports settings; winner's-curse over-bidding in labs and field data; cooperation in repeated PDs rising with continuation probability (Dal Bó 2005; Dal Bó & Fréchette 2011 — background knowledge, not verified for this file); median-voter and agenda effects in legislatures. Lab results on ultimatum, dictator and public-goods-with-punishment games have replicated broadly, with effect sizes varying across cultures (Henrich et al. 2001, the small-scale-societies study).
- **Where the theory is thin:** (1) *Equilibrium selection* — with multiple equilibria the theory is silent; focal points, learning and evolutionary dynamics are patched on, and the book admits it. (2) *Depth of reasoning* — humans reason a few steps (level-k), not to a fixed point; the centipede and two-thirds games show it. (3) *Social preferences* — "put fairness in the payoffs" is formally fine but says nothing about how much or when; Camerer and Bicchieri supply the content. (4) *Backward induction* is philosophically contested (what should a player believe at a node rollback says is unreachable?); mentioned, not resolved. (5) The repeated-game rescue needs observability and patience many groups lack, and with more than two players the question of who punishes whom is hard — Ostrom's monitoring principles are the empirical answer.
- **Author stance:** a textbook, so more shown than argued, but the authors do hold that rationality is a useful benchmark even when violated, that deviations should be modeled rather than used to discard the framework, and that market and mechanism design is the theory's most practical payoff. Behavioral and evolutionary critics say the benchmark framing privileges model over data; economists say it underplays how fragile many-equilibrium results are. The missile-crisis chapter is explicitly one interpretation among several.
- **Replication:** the game-theory lab literature drawn on here is among the better-replicated parts of experimental social science; the replication-crisis issues in classic social psychology live in Gilovich's file.

## Design implications for cooperation in real groups
- **Write the matrix first.** Name the players, their real options and payoffs as *they* see them; classify the shape (PD, stag hunt, chicken, battle of the sexes, coordination). [E] The shapes are formally distinct with distinct remedies.
- **Prefer assurance over enforcement in a stag hunt.** Visible pledges, thresholds ("we start when 10 sign up") and matching commitments move a group to the payoff-dominant equilibrium cheaply. [E] formal / [H] that your group's shape is a stag hunt.
- **Make sanctions cheap and subgame-perfect.** A sanction that costs the enforcer more than ignoring the violation will not be applied and will not deter. Graduated, low-cost, fast responses and rotating or delegated enforcers keep the threat credible. [E]
- **Lengthen and blur the shadow of the future.** No announced end dates; stable membership; defection observed within a round or two. [E] theory and lab / [H] for magnitude in a given group.
- **Build forgiveness into reciprocity.** Grim triggers are fragile to noise; use one-warning-then-escalate variants. [E] simulation results under noise.
- **Sort types at the boundary with costly signals.** Onboarding effort, probationary contribution and time-consuming rituals separate committed members from opportunists when the cost is asymmetric. [E] signaling theory / [H] that a given ritual has the asymmetry.
- **Screen with menus, not interrogations.** Tiered roles let members self-select honestly. [E] mechanism design / [H] in practice.
- **Randomize monitoring.** A known inspection probability with a proportionate penalty deters as well as full monitoring; required probability ≈ gain/penalty. [E]
- **Set the order of moves deliberately.** Visible first-mover commitment resolves chicken and some coordination; sealed simultaneous choices prevent bandwagons and intimidation. [E] formal effect / [H] which suits your case.
- **Choose decision rules on purpose.** Approval voting or one-dimension-at-a-time decisions; published agenda rules. [E] Condorcet/Gibbard–Satterthwaite / [V] that manipulation-resistance deserves priority.
- **Allocate scarce resources with truth-dominant rules.** Vickrey-style mechanisms reduce politicking. [E]
- **Beware measuring what is measurable.** Partial-metric incentives displace unmeasured effort; with noisy output lean on norms and reputation. [E] multi-task theory; crowding-out evidence more mixed / [H] for your setting.
- **Treat the predicted equilibrium as a floor, not a forecast.** Groups often start more cooperative than the PD predicts; the job is usually to *protect* initial cooperation from decay. [E] lab decay curves / [V] that protecting the cooperative default is the right target.

## Connections
- **05-micromotives-and-macrobehavior** — Agrees: focal points, commitment, brinkmanship and the Ch 11 tipping diagrams are Schelling's. Tension: Schelling stresses emergent, unintended aggregates; Dixit et al. stress solvable equilibria and design.
- **06-behavioral-game-theory** — The companion file: this book states benchmarks, Camerer catalogues the departures (social preferences, learning, limited depth). Read Camerer ch 2, 6, 7 as empirical footnotes to Chs 4, 5, 10, 11 here.
- **07-stag-hunt** — Skyrms takes the assurance game plus Ch 12 and asks how populations move from the risk-dominant to the payoff-dominant equilibrium via correlation, signaling and networks. Direct extension.
- **08-grammar-of-society** — Bicchieri's norms are, in this language, payoff changes plus conditional expectations that turn PDs into coordination games; her empirical and normative expectations are the beliefs that select among Ch 4's multiple equilibria.
- **09-governing-the-commons** — Ostrom answers Ch 11 with field evidence; her principles map onto observability, credible cheap sanctions (Chs 8, 10) and screening (Ch 9). Tension: she argues the PD framing itself misled policy.
- **10-networks-crowds-markets** — Ch 6 there compresses Chs 3–7 and 12 here; their cascade and network-effects chapters extend Ch 11's tipping logic to network structure.
- **01-secret-of-our-success / 02-darwins-unfinished-symphony** — Ch 12 supplies the ESS machinery behind cultural evolution; Henrich's credibility-enhancing displays are Ch 9 costly signals.
- **03-social-psychology** — Fills in the payoffs (conformity, reciprocity, self-serving bias) and explains limited-depth reasoning.
- **11-bounds-of-reason** — Gintis argues game theory cannot explain coordination without norms as correlating devices (correlated equilibrium); this book's reliance on focal points is the gap he attacks.

## Retrieval practice

1. **(Recall)** What distinguishes a strategy from a move, and why does it matter for evaluating a rule?
<details>A strategy specifies an action at every decision point that could arise; a move is one action. A rule's credibility depends on what it commits you to at nodes off the expected path — those off-path responses are what deter.</details>

2. **(Explain why)** Why is mutual defection the equilibrium of a one-shot PD when both prefer mutual cooperation?
<details>Defection is dominant: whatever the other does, defecting pays more. Cooperation is a best response to nothing, so no profile containing it is stable against unilateral deviation. Preferring an outcome does not make it an equilibrium.</details>

3. **(Apply)** A volunteer group needs eight people to run an event; everyone wants the event but would rather not be one of the eight. Which shape, and the cheapest fix?
<details>If each person's payoff to attending is higher *given* enough others attend, it is a threshold assurance game: fix with public or conditional pledges ("I'm in if seven others are"), not sanctions. If each strictly prefers others do it regardless, it is chicken: fix with assignment or rotation.</details>

4. **(Misconception)** "To make my threat credible I should make it as severe as possible."
<details>Wrong. Severity lowers credibility when execution is costly to the threatener; the other side expects you not to follow through. Size threats to what deters and structure them so executing is in your interest at the time, or make them probabilistic (brinkmanship).</details>

5. **(Compute)** PD per round: mutual cooperation 4, mutual defection 1, defect-against-cooperator 6, cooperate-against-defector 0. Under grim trigger, what δ sustains cooperation?
<details>4/(1−δ) ≥ 6 + δ/(1−δ) → 4 ≥ 6 − 5δ → δ ≥ 0.4.</details>

6. **(Explain why)** Why does raising the goalie's payoff from a save not change how often the goalie dives left in equilibrium?
<details>Each player's mix is set to make the *other* indifferent. The goalie's mix is pinned by the kicker's payoffs; changing the goalie's payoffs changes the kicker's mix.</details>

7. **(Apply)** A community wants to tell long-term members from tourists. Propose a signal and say what makes it work.
<details>Require a contribution cheap for committed members and expensive for tourists — a multi-week task before privileges unlock, or sustained participation. It works only if the cost differs by type (separating). Equal cost yields pooling and reveals nothing.</details>

8. **(Recall)** State the winner's curse and where it arises.
<details>In common-value auctions the winner is the bidder with the highest, likely over-optimistic, estimate. Winning is bad news about value; rational bidders shade, real bidders often do not.</details>

9. **(Misconception)** "Game theory proves rational people cannot cooperate."
<details>It shows cooperation is not an equilibrium of a one-shot PD, but also that it *is* one in indefinitely repeated PDs with patience and observability, in assurance games, and under credible sanctions or norms. Whether cooperation is stable depends on the game's structure, which is designable.</details>

10. **(Apply)** Three co-founders rank options A>B>C, B>C>A, C>A>B. One proposes pairwise votes "starting with the two most controversial." What should the others notice?
<details>Preferences cycle, so whichever option enters the last pairwise vote wins; the agenda-setter decides. Use a less agenda-sensitive rule (approval, Borda) or restructure the question so preferences are single-peaked.</details>

## Common misreadings of this book
- **"It's about competition."** Most of the content is coordination, cooperation and mechanism design; zero-sum games are a small special case.
- **"Nash equilibrium predicts behavior."** It identifies stable profiles; with multiple equilibria it predicts nothing, and lab play often departs. The book says so in its "Discussion and Evidence" sections, which readers skip.
- **"Rationality means selfishness."** Rationality here is consistent pursuit of whatever your payoffs contain; fairness and spite are allowed in. The framework does not assume them away — nor tell you how to fill them in.
- **"Tit-for-tat is optimal."** It won Axelrod's tournaments but is not uniquely optimal and is fragile under noise; what matters are the properties (nice, retaliatory, forgiving, clear).
- **"Commitment means stubbornness."** A strategic move works only if credible, observed and understood by the other side. Private resolve does nothing.
- **"Signals must be informative."** A costly signal can sort types while transmitting no content; the cost differential across types is what matters.
- **"Repetition solves the PD."** Repetition *permits* cooperation as one equilibrium among many; it does not select it. Groups also need to coordinate on the cooperative equilibrium and detect defection fast — the selection problem the Order-level books address.
