# Networks, Crowds, and Markets: Reasoning about a Highly Connected World — David Easley & Jon Kleinberg (Cambridge University Press, 2010)
Level: Order  ·  Priority: Selections
Est. reading time saved: ~14h (selected chapters ~5h; whole book ~30h+)  ·  Your time with this file: ~35 min

## The book in one sentence
Individual choices are shaped by *who is connected to whom* and *what others have already done*, so the same population can settle into wildly different collective outcomes depending on network structure and on the order in which people act.

## The book in one paragraph
Easley (economist) and Kleinberg (computer scientist) wrote an undergraduate text that fuses graph theory, game theory and market economics into one toolkit for reasoning about connected systems. The first third builds the vocabulary of networks (ties, bridges, closure, homophily, balance) and of strategic interaction (games, equilibria, evolutionary stability, auctions, matching and bargaining on networks). The middle third shows how the Web is structured and searched. The last third — the part that matters most for this curriculum — models *dynamics*: why rational people imitate each other into information cascades, why goods with network effects tip between "nobody uses it" and "everybody uses it", how a behavior spreads or stalls across an actual graph depending on thresholds and clusters, why huge societies are nonetheless "small worlds" that people can navigate with local knowledge alone, and how epidemics, markets, votes and property rules aggregate individual behavior. Every model is stated simply enough to compute by hand, which is the point: the book teaches you to *see the mechanism* rather than just name the phenomenon.

## Why it's in this curriculum (the question to read it with)
The other Order-level books (Skyrms, Bicchieri, Ostrom) explain why norms and institutions can stabilize cooperation. This book supplies the missing variable: **structure**. Read it asking: *given the actual web of ties in my group, where will a new norm catch, where will it die, who needs to move first, and which bridges or clusters are helping or blocking?* It also gives the cleanest available account of why groups converge on something that most members privately doubt (cascades), which is the formal backbone of Bicchieri's "pluralistic ignorance" and Schelling's tipping.

## Table of contents
TOC verified against web search snippets of library catalogue records and course syllabi (the free online draft at Kleinberg's Cornell page was blocked by the proxy, so chapter titles below come from catalogue listings that mirror it; one discrepancy is noted). Chapters marked with ★ are covered in depth in this file; the others get one paragraph each.

**Ch 1 ★ Overview** (stands alone, before Part I)

**Part I — Graph Theory and Social Networks**
- Ch 2 Graphs
- Ch 3 ★ Strong and Weak Ties
- Ch 4 ★ Networks in Their Surrounding Contexts (homophily, selection vs. influence, affiliation)
- Ch 5 Positive and Negative Relationships

**Part II — Game Theory**
- Ch 6 ★ Games (brief here; Dixit covers the substance)
- Ch 7 Evolutionary Game Theory
- Ch 8 Modeling Network Traffic Using Game Theory
- Ch 9 Auctions

**Part III — Markets and Strategic Interaction in Networks**
- Ch 10 Matching Markets
- Ch 11 Network Models of Markets with Intermediaries
- Ch 12 Bargaining and Power in Networks

**Part IV — Information Networks and the World Wide Web**
- Ch 13 The Structure of the Web
- Ch 14 Link Analysis and Web Search
- Ch 15 Sponsored Search Markets

**Part V — Network Dynamics: Population Models**
- Ch 16 ★ Information Cascades
- Ch 17 ★ Network Effects
- Ch 18 Power Laws and Rich-Get-Richer Phenomena

**Part VI — Network Dynamics: Structural Models**
- Ch 19 ★ Cascading Behavior in Networks
- Ch 20 ★ The Small-World Phenomenon
- Ch 21 Epidemics

**Part VII — Institutions and Their Aggregate Effects** (some catalogue records phrase this part as "Institutions and Aggregate Behavior"; the book's own heading is, to my knowledge, the former — unverified)
- Ch 22 Markets and Information
- Ch 23 Voting
- Ch 24 Property Rights (one catalogue snippet lists it as just "Property"; the full title is from background knowledge)

Why these selections: chapters 3, 4, 19 and 20 are the ones about *social* structure; 16 and 17 are the two population-level models of contagious behavior every designer of norms needs; 1 frames the whole; 6 is included only to show how the book attaches games to graphs. The web-search, auction, matching and market chapters are excellent but belong to a different course.

## Chapter-by-chapter: the salient knowledge

### Ch 1 — Overview
- Core claims: (1) Connectedness has two faces: a *structural* face (the graph of who is linked to whom) and a *behavioral* face (people's choices depend on what others choose). Neither alone explains collective outcomes; the book's method is to keep both in view. (2) The same handful of ideas — ties, bridges, homophily, cascades, tipping, feedback — recur across friendships, the Web, markets, epidemics and politics, so it pays to learn them once in abstract form. (3) Aggregate behavior can be surprising relative to individual intent: a population of sensible people can produce panics, fads, bubbles and lock-in.
- Key examples: the chapter previews the book's set pieces — a high-school romantic network (Bearman, Moody & Stovel 2004) that looks like a single sprawling chain with almost no short cycles; Milgram's six-degrees experiment; the Web as a directed graph; the rise and crash of financial contagion; and the Bikhchandani-Hirshleifer-Welch idea that imitation can be rational.
- So-what: whenever you diagnose a group, separate two questions — "what does the tie structure look like?" and "what does each person's decision depend on?" — and then ask how the two interact. Most cooperation failures are misdiagnosed because only one of these is examined.

### Ch 2 — Graphs (one paragraph)
Nodes, edges, paths, distance, connected components, breadth-first search, and the giant component are defined. The load-bearing empirical fact is that real social networks almost always have one giant connected component containing most nodes, and that distances inside it are short. The design point: in any group above a few dozen people you should expect *reachability* (everyone is a few steps from everyone) but not *uniform* reachability — some regions are much better connected than others, which is what the later chapters exploit.

### Ch 3 — Strong and Weak Ties
- Core claims:
  1. **Triadic closure**: if A is strongly tied to both B and C, then B and C are very likely to become tied. Three reasons: opportunity (they meet through A), trust (a shared friend vouches), and strain (an open triangle is uncomfortable for A). The clustering coefficient measures how much closure a node's neighborhood has.
  2. **Granovetter's strength of weak ties** (1973; his job-search interviews found most jobs came via acquaintances, not close friends). The explanation is structural: weak ties are disproportionately *bridges* or *local bridges* — edges whose endpoints share no other neighbors — because strong ties get closed into triangles. Novel information lives on the other side of a bridge; your close friends mostly know what you know.
  3. The **Strong Triadic Closure** property makes this precise: if a node has strong ties to two others, there must be at least a weak tie between them. From this one assumption it follows that any local bridge must be a weak tie. (Easy to check: if it were strong and one endpoint had another strong tie, closure would force a third edge and the bridge would no longer be local.)
  4. **Tie strength in big data**: Onnela and colleagues' (2007) analysis of a national mobile-phone call graph found that ties with high *neighborhood overlap* (many shared contacts) also carried the most call minutes, and that deleting weak ties first shattered the network into pieces while deleting strong ties first merely thinned it. Weak ties hold the whole together.
  5. **Closure vs. structural holes** (Coleman vs. Burt): a person embedded in a closed cluster gets trust, enforceability and shared norms; a person spanning a structural hole between clusters gets information advantage, brokerage and power. These are different kinds of social capital and they trade off.
- Tiny example: A is strongly tied to B and C. Under Strong Triadic Closure, B–C must exist. If B–C were absent and A's only path to D ran through B, the edge A–B would be a local bridge; the argument above says it can only be a *weak* tie. Neighborhood overlap of A–B = (common neighbors) / (neighbors of A or B, excluding A and B themselves); a bridge has overlap 0.
- So-what: cooperation needs *both* closure (so people can be sanctioned and trust each other) and bridges (so ideas and resources arrive). A group that is all closure becomes an echo chamber that enforces stale norms; a group that is all bridges cannot enforce anything. Deliberately identify who your local bridges are and protect them — they are usually weak ties, thus fragile, and losing one can disconnect a whole subgroup.

### Ch 4 — Networks in Their Surrounding Contexts (homophily)
- Core claims:
  1. **Homophily**: ties form disproportionately between similar people (age, ethnicity, class, beliefs, role). Moody's (2001) school-friendship diagrams where race predicts the community structure are the canonical picture.
  2. **How to measure it**: if a fraction p of nodes have trait X and q = 1 − p do not, then random mixing would make a fraction 2pq of edges cross the trait boundary. Significantly fewer cross-edges than 2pq is evidence of homophily. Tiny example: 40% women, 60% men → 2 × 0.4 × 0.6 = 0.48 of edges should be mixed-gender at random; if only 20% are, the network is strongly homophilous.
  3. **Two mechanisms produce homophily and they are hard to tell apart**: *selection* (people choose similar friends) and *social influence* (friends make each other similar). Only longitudinal data with timestamps can separate them. Christakis & Fowler (2007) argued obesity spreads by influence; critics (e.g. Cohen-Cole & Fletcher 2008; Shalizi & Thomas 2011) showed that latent homophily can produce identical patterns — the book itself flags the identification problem, and later work has sharpened the skepticism.
  4. **Affiliation networks and foci**: people are tied to activities, places and groups (foci, after Feld 1981). Three closure processes then run in parallel: *triadic closure* (friend of a friend), *focal closure* (two people who share a focus become friends), and *membership closure* (you join a focus your friend belongs to). Kossinets & Watts (2006) measured these in a university email network and found the probability of a new tie rises with each additional shared friend, with diminishing returns.
  5. Crandall et al.'s (2008) Wikipedia study is the book's showcase for the selection/influence question: editors' similarity rises sharply *before* their first interaction (selection) and keeps rising afterwards (influence), so both are real.
- So-what: a group's "culture" may be mostly selection (who joined) rather than influence (what membership did to them). If you want to change behavior you must know which is operating: selection problems are solved at the recruiting boundary, influence problems by changing who talks to whom. Also, homophily is the engine that turns a network into clusters — and clusters (ch 19) are exactly what block cascades of new behavior.

### Ch 5 — Positive and Negative Relationships (one paragraph)
Signed graphs and **structural balance**: triangles with three positive edges or exactly one positive edge are stable ("friend of my friend", "enemy of my enemy"); the other two types are under strain. Harary's balance theorem says a fully balanced complete signed network must split into at most two mutually hostile camps of internal friends — the book illustrates with the pre-WWI alliance system collapsing into two blocs. The generalization (weak balance) allows many mutually hostile camps. Design relevance: latent negative ties matter as much as positive ones, and balance pressure predicts that a group with unresolved antagonisms will polarize into two factions unless cross-cutting positive ties are maintained.

### Ch 6 — Games (network framing only; substance is in 04-games-of-strategy)
- The chapter builds the standard toolkit — payoff matrices, dominant strategies, best responses, Nash equilibrium, mixed strategies, Pareto optimality and social optimality — using the Prisoner's Dilemma, the exam-vs-presentation coordination game and Hawk-Dove. What is distinctive is the framing: the authors treat a game as a **template that will later be played on every edge of a graph**, so a node's payoff becomes the sum of pairwise games with its neighbors. That is the seed for ch 19 (coordination games on networks) and ch 7 (evolutionary dynamics). Their treatment of coordination games with multiple equilibria stresses that theory alone cannot pick one; something outside the game — history, communication, focal points, network position — must. Tiny example: in a 2-player coordination game where matching on A pays 3 and matching on B pays 2, both (A,A) and (B,B) are equilibria; the question of *which* the group ends up at is answered by the dynamics of chapters 16–19, not by the game.

### Ch 7 — Evolutionary Game Theory (one paragraph)
Strategies are treated as heritable or imitated traits; a strategy is **evolutionarily stable (ESS)** if a population playing it cannot be invaded by a small mutant group. In Hawk-Dove the ESS is mixed; in coordination games each pure equilibrium is an ESS, so history decides. The chapter also relates ESS to Nash equilibrium (every ESS is Nash; not every Nash is an ESS). This is the bridge to Skyrms (07-stag-hunt): it supplies the rigorous definition Skyrms's replicator dynamics rely on, and it explains why a cooperative convention, once common, can be self-protecting.

### Ch 8 — Modeling Network Traffic Using Game Theory (one paragraph)
Drivers (or packets, or workers) choose routes selfishly; the equilibrium can be strictly worse for everyone than a coordinated assignment, and adding a shortcut can make travel *slower* for all (Braess's paradox, 1968). The **price of anarchy** bounds how bad selfish equilibria can be relative to the optimum (Roughgarden & Tardos: at most 4/3 for linear costs). Design point: adding options or capacity to a system of self-interested agents does not automatically help and can hurt; the fix is usually a change of incentives, not more edges.

### Ch 9 — Auctions (one paragraph)
First-price, second-price (Vickrey), English and Dutch auctions; the central result is that in a second-price sealed-bid auction, bidding your true value is a dominant strategy, because the price you pay is set by others. Revenue equivalence links the formats. For this curriculum the auction chapters matter as examples of *institutional design that makes honesty the best response* — a pattern worth carrying to norm design.

### Ch 10 — Matching Markets (one paragraph)
Bipartite graphs of buyers and sellers (or students and schools); a perfect matching exists unless some set of buyers has too few acceptable sellers (a *constricted set*). Prices adjust so that each buyer's preferred seller at the going prices form a matching: market-clearing prices always exist, and the auction-like procedure that finds them raises the price of over-demanded goods step by step. The takeaway: prices are a decentralized coordination device that resolves constricted sets without any central planner knowing valuations.

### Ch 11 — Network Models of Markets with Intermediaries (one paragraph)
Buyers and sellers who cannot trade directly go through traders; each trader's profit depends on whether they are a monopolist over some pair or compete with another trader. Nodes that are the *only* path between a buyer and a seller capture all the surplus; where two traders both connect the same pair, competition drives their margin to zero. Power, in other words, is a structural fact about being on the only route.

### Ch 12 — Bargaining and Power in Networks (one paragraph)
Experimental "exchange networks" (Cook & Emerson and successors) show that a node's bargaining power depends on its alternatives, not simply its degree: a node with two partners who each have no one else is powerful; a central node in a long chain may be weak because its partners have other options. The Nash bargaining solution and the concept of *stable*, *balanced* outcomes formalize the intuition, and the theory matches experimental splits reasonably well. For designers: power in a team is about exclusive access, and you can flatten it by giving people alternatives.

### Ch 13 — The Structure of the Web (one paragraph)
The Web as a directed graph: a giant strongly connected core, an IN set that reaches it, an OUT set reachable from it, plus tendrils (Broder et al. 2000's "bow-tie"). Directed reachability is a different notion from undirected connectedness; in a group where influence flows one way (leaders broadcast, members cannot reply), the bow-tie shape says who can affect whom.

### Ch 14 — Link Analysis and Web Search (one paragraph)
Hubs and authorities (Kleinberg's HITS) and PageRank: a page is important if important pages point to it, computed by repeated averaging until the scores converge. The random-surfer interpretation of PageRank, with a small reset probability to escape traps, is the key intuition. Relevance for groups: "whom people defer to" can be computed from the structure of deference itself, which is what reputation and prestige systems do implicitly.

### Ch 15 — Sponsored Search Markets (one paragraph)
Ad slots are sold by generalized second-price auctions; the chapter connects matching markets (ch 10) to the Vickrey-Clarke-Groves mechanism and shows that Google's actual auction is not truthful but has equilibria that replicate VCG outcomes. It is the book's main example of an institution engineered to align self-interest with an efficient allocation.

### Ch 16 — Information Cascades
- Core claims:
  1. When people act *in sequence* and can see what others did but not what they knew, it can be perfectly rational to ignore your own private signal and copy the crowd. Once two or three early movers agree, everyone after them copies regardless of their own information: an **information cascade** (Banerjee 1992; Bikhchandani, Hirshleifer & Welch 1992).
  2. Cascades are fragile because they rest on very little actual information: the choices after the cascade starts carry *no* new information, so a small shock (a public signal, a credible dissenter) can reverse them.
  3. Cascades can be wrong even when every individual reasons correctly and even when most people's private signals point the right way, as long as the first few happened to point the wrong way.
  4. This is distinct from conformity for social reasons (ch 3–4 style influence) and from network effects (ch 17, where copying is valuable *because* others copy). Here copying is purely informational.
- **The urn model (BHW), stated plainly**: An urn is either *majority-blue* (2 blue marbles, 1 red) or *majority-red* (2 red, 1 blue), each equally likely. People come one at a time, draw one marble, look at it privately, put it back, and then publicly announce a guess about which urn it is. Each wants to guess right.
  - Person 1 has only her own draw. Seeing blue, the probability the urn is majority-blue is 2/3 (Bayes: (1/2 × 2/3) / (1/2 × 2/3 + 1/2 × 1/3)). She guesses "blue" — so her announcement reveals her draw.
  - Person 2 knows person 1's draw and his own. If both are blue: P(majority-blue) = (2/3 × 2/3)/(2/3 × 2/3 + 1/3 × 1/3) = (4/9)/(5/9) = 4/5 → guess blue. If they conflict, the two signals cancel to 1/2; assume he follows his own draw. Either way his guess still reveals his draw.
  - Person 3 arrives after two "blue" announcements and draws **red**. She computes P(majority-blue | blue, blue, red) = (1/2 × 2/3 × 2/3 × 1/3) / (1/2 × 2/3 × 2/3 × 1/3 + 1/2 × 1/3 × 1/3 × 2/3) = (4/27 × 1/2)/((4/27 + 2/27) × 1/2) = 4/6 = 2/3. Still above 1/2, so she guesses blue *against her own evidence*.
  - Person 4 now sees three "blue" guesses, but knows the third was uninformative. Her situation is identical to person 3's: whatever she draws, she guesses blue. The cascade is locked; it will run forever unless something external breaks it.
  - Probability check: with a majority-blue urn, the cascade goes the *wrong* way (two reds first, probability 1/3 × 1/3 = 1/9) or the right way (two blues, 4/9); the rest of the time (4/9) the first two conflict and the process restarts from person 3. Over the long run a wrong cascade has probability roughly 1/5 in this setup — high, given that every signal is 2/3 accurate.
- Empirical anchors: Milgram, Bickman & Berkowitz (1969) had confederates stare up at a building; the fraction of passers-by who joined rose with the size of the staring group. Salganik, Dodds & Watts's (2006) "music lab" experiment (also used in ch 17) showed that visible download counts make song success unpredictable and path-dependent across parallel worlds.
- So-what: whenever your group decides sequentially and publicly (a meeting where the senior person speaks first, a vote taken by show of hands, a Slack thread where early reactions are visible), you are running an urn model, and the outcome may reflect two people's noise rather than the room's knowledge. Fixes follow directly: collect private signals *before* anyone announces (blind votes, written estimates), randomize or reverse speaking order so the least informed do not anchor the most, and make disagreement cheap so a dissenter can break a cascade. And note the good news: cascades are easy to overturn because they are shallow.

### Ch 17 — Network Effects
- Core claims:
  1. Some goods and behaviors have **positive externalities**: the value to me rises with the number of others who use it (phones, file formats, a language, a norm of showing up to standup). Copying here is not informational but *payoff-driven*.
  2. Aggregate demand then has multiple equilibria, some stable and some unstable; the unstable one is a **tipping point**. Below it the behavior collapses to zero; above it, it grows to a high stable level.
  3. Because the middle equilibrium is unstable, expectations are self-fulfilling: if everyone believes the fraction adopting will be z, they act on that and it becomes true. Marketing, subsidies and public commitments work by moving beliefs across the tipping point.
  4. Outcomes are path-dependent and can lock in an inferior technology (the book discusses QWERTY-style arguments with appropriate caution, since the historical evidence there is contested).
- **The model, plainly**: consumers are indexed by x on a line from 0 to 1, in decreasing order of how much they intrinsically want the good, r(x). If a fraction z of the population uses the good, consumer x's willingness to pay is r(x)·f(z), where f is increasing (the network effect). At price p, consumer x buys if r(x)·f(z) ≥ p. Because r is decreasing, the buyers are exactly those with x below some cutoff; in equilibrium the cutoff *is* z, so the condition for a self-consistent adoption level is r(z)·f(z) = p, plus z = 0 (nobody buys, so the good is worth nothing to anyone, so nobody buys).
- **Tiny numeric example**: let r(x) = 1 − x and f(z) = z, so willingness to pay is (1 − x)·z, and set price p = 0.2. Solve (1 − z)·z = 0.2 → z² − z + 0.2 = 0 → z ≈ 0.28 or z ≈ 0.72. Three equilibria: z = 0, z' ≈ 0.28, z'' ≈ 0.72. Suppose 30% currently use it: the marginal consumer at x = 0.30 values it at 0.7 × 0.3 = 0.21 > 0.2, so more people join; at 50%, 0.5 × 0.5 = 0.25 > 0.2, still growing; at 80%, 0.2 × 0.8 = 0.16 < 0.2, so some drop out. The process converges to 0.72. But if only 25% use it, the marginal value is 0.75 × 0.25 ≈ 0.19 < 0.2 and adoption unravels to zero. **z' = 0.28 is the tipping point.**
- **The Z-shaped diagram**: plot the price the marginal consumer will pay, r(z)·f(z), against z. It starts at 0 (nobody else uses it), rises, peaks and falls back to 0 at z = 1 (the last consumers have no intrinsic interest). A horizontal line at price p cuts this hump at z' and z''. Reading the picture dynamically: where the curve is *above* the price line, adoption grows; where it is below, adoption shrinks. So the arrows point away from z' (unstable) and toward 0 and z'' (stable). Some course presentations instead draw the *equilibrium adoption level as a function of price*, which gives a backwards-Z (or S) shape: at high prices only z = 0 survives; as price falls below the peak two interior equilibria appear; at very low prices adoption jumps to a high level. Both pictures encode the same three-equilibrium structure, and the lesson is the same: a small price cut or a small nudge in expectations near the tipping point produces a discontinuous jump in outcome.
- Empirical anchor: Salganik, Dodds & Watts (2006) is the cleanest demonstration that social influence plus positive feedback makes success unpredictable: the same 48 songs ranked very differently across eight artificial "worlds" once download counts were visible, though the best songs rarely did badly and the worst rarely did well.
- So-what: for any behavior whose value depends on how many others do it (a shared tool, a documentation norm, a code-review convention, contributing to a commons), do not ask "is it a good idea?"; ask "are we above the tipping point?" If not, you need a concentrated push — subsidize early adopters, seed a critical mass in one subgroup, make a public commitment that shifts expectations — because gradual, diffuse encouragement below z' simply leaks away. Conversely, once above z'' the behavior is self-sustaining and you can stop paying for it.

### Ch 18 — Power Laws and Rich-Get-Richer Phenomena (one paragraph)
Popularity distributions (links, citations, city sizes, followers) have heavy tails: the fraction of items with popularity k falls like k^(−c). A simple generative model — each newcomer copies the choice of a random earlier node with probability p, otherwise chooses at random (**preferential attachment**, Price 1976; Barabási & Albert 1999) — produces exactly such tails. Two consequences the authors stress: extreme inequality of attention is the *default* outcome of copying, not evidence of extreme quality differences; and early luck is amplified, so unpredictability (as in the music lab) is structural. The "long tail" discussion shows the same distribution read from the other end.

### Ch 19 — Cascading Behavior in Networks
- Core claims:
  1. Ch 16 assumed everyone sees everyone. Here each person only sees and cares about their **neighbors**, and the reason to copy is payoff (a coordination game on each edge), not information. This is the model of *norm spread*.
  2. Whether a new behavior A spreads from a seed set depends on a single number — the threshold q — and on the *structure* of the rest of the network. The obstacle to spread is not distance but **density of tightly-knit communities**.
  3. Weak ties and bridges (ch 3) cut both ways: they carry the *awareness* of a new behavior across clusters, but because a bridge is only one of many edges for the node it lands on, it is rarely enough to make that node *switch* a high-threshold behavior. Simple contagion (information, disease) crosses bridges easily; complex contagion (costly behaviors) does not.
  4. Extensions: **bilinguality** — allowing a node to adopt both A and B at some cost can change who spreads what; heterogeneous thresholds; and Granovetter's (1978) threshold model of collective action plus the role of **common knowledge** (Chwe 2001): people join a risky action only if they know enough others will, and know that those others know, which explains why public rituals and visible cliques matter for revolts and strikes.
- **The model, plainly**: on every edge, the two endpoints play a coordination game: both choose A → each gets a; both choose B → each gets b; mismatch → 0. A node with d neighbors, a fraction p of whom use A, gets p·d·a from choosing A and (1 − p)·d·b from choosing B. It prefers A when p·a ≥ (1 − p)·b, i.e. when
  **p ≥ q = b / (a + b).**
  Start with a seed set of A-adopters in a network of B-users; every other node repeatedly switches to A when at least a fraction q of its neighbors use A (A is assumed better, so switches are one-way). If eventually everyone uses A, the seed set causes a **complete cascade** at threshold q.
- **Cluster, defined**: a set of nodes is a *cluster of density p* if every node in the set has at least a fraction p of its neighbors inside the set. (The whole network is trivially a cluster of density 1; a single node with any outside neighbor is a cluster of low density.)
- **The cluster-density theorem, stated precisely** (the book's main result of the chapter): Consider a set of initial adopters of A, with all other nodes using B, and a threshold q for switching. Then
  (i) if the network *outside the initial adopters* contains a cluster of density greater than 1 − q, the initial adopters do **not** cause a complete cascade; and
  (ii) conversely, whenever the initial adopters do **not** cause a complete cascade, the network outside them contains a cluster of density greater than 1 − q.
  Why (i) holds: take the first node inside such a cluster that would switch. At that moment no other cluster member has switched, so all of its A-neighbors are outside the cluster, which is less than a fraction q of its neighbors (because more than 1 − q of them are inside). So it cannot be the first; nobody switches. Why (ii) holds: run the process to its end; the set of nodes still using B is itself a cluster of density greater than 1 − q, because each of them has fewer than q of its neighbors using A, hence more than 1 − q inside the B-set.
- **Tiny numeric example**: let a = 3, b = 2, so q = 2/5 = 0.4 and 1 − q = 0.6. Network: seeds s1 and s2 both link to c; c links to d; d, e, f form a triangle. Round 1: c has neighbors {s1, s2, d}, of which 2/3 ≈ 0.67 use A ≥ 0.4 → c switches. Round 2: d has neighbors {c, e, f}; 1/3 ≈ 0.33 < 0.4 → d stays with B. Nothing else changes; the cascade stops with {d, e, f} on B. Check the theorem: {d, e, f} is a cluster — d has 2 of 3 neighbors inside (0.67), e and f have all neighbors inside (1.0) — so its density is 0.67 > 0.6 = 1 − q, exactly as (i) predicts. Now change payoffs to a = 3, b = 1: q = 0.25, 1 − q = 0.75, and the triangle's density 0.67 no longer exceeds 0.75. Indeed d switches (0.33 ≥ 0.25), then e has neighbors {d, f} with 1/2 ≥ 0.25 → switches, f follows: complete cascade.
- Empirical anchors: the chapter cites diffusion-of-innovations work (Ryan & Gross's 1943 hybrid-corn study, Coleman-Katz-Menzel on physicians adopting tetracycline) and Centola & Macy's (2007) argument that complex contagions need wide bridges (multiple parallel ties), not single bridges. Centola's (2010) online health-community experiment later confirmed that clustered networks spread costly behavior *faster* than random ones — the opposite of what holds for information.
- So-what: this is the most directly actionable chapter in the book for norm design. (a) Compute or estimate the threshold: how much of my neighborhood needs to change before switching is worth it for me? Lower it (make A cheaper, B costlier, or provide bilingual compatibility) and clusters that were impenetrable become porous. (b) Seed *inside* the dense clusters rather than at the periphery; a cluster is only a barrier while none of its members has switched. (c) Do not expect a norm to jump across a single weak tie; complex contagion needs several independent neighbors to move, so invest in wide bridges or move whole sub-teams together. (d) For risky collective action (whistleblowing, strikes, calling out a bad norm), create common knowledge through visible, simultaneous signals rather than private one-to-one persuasion.

### Ch 20 — The Small-World Phenomenon
- Core claims:
  1. **Six degrees**: Milgram's 1967 experiment (Travers & Milgram 1969) asked people in Nebraska (and Boston) to forward a letter toward a Boston stockbroker via personal acquaintances; of the chains that arrived, the median length was about six. Dodds, Muhamad & Watts (2003) replicated by email with 18 targets in 13 countries; most chains died, but completed ones were again around 5–7 steps. Full-graph measurements (e.g. Leskovec & Horvitz 2008 on 240 million Messenger users; later Facebook studies) confirm average distances of about 4–7.
  2. There are *two* surprises, not one. First, paths are short despite heavy clustering. Second, ordinary people could **find** the short paths with only local knowledge — no map of the network.
  3. **Watts & Strogatz (1998)** explain the first: start from a clustered lattice (everyone knows their near neighbors, so lots of triangles) and add a few random long-range links. Very few shortcuts collapse the average distance to logarithmic size while barely changing clustering. Homophily gives the lattice; weak ties give the shortcuts.
  4. **Kleinberg (2000)** shows Watts-Strogatz *cannot* explain the second surprise, and finds what does. If long-range links are uniformly random, a greedy forwarder (pass the letter to the neighbor closest to the target) has no way to home in — its long links point anywhere — and takes on the order of n^(2/3) steps in 2D (in the hundreds for a million nodes). If long links are chosen with probability proportional to distance^(−q), decentralized search is efficient **only when q equals the dimension of the underlying space** (q = 2 on a plane, q = 1 on a line); then greedy forwarding reaches the target in about (log n)² steps. For q below the dimension, links are too random to be useful; for q above it, links are too local to make progress. The "just right" exponent means each person has roughly one long-range acquaintance at every *scale* of distance (in the next town, the next region, the next country), so at each step you can halve your distance to the target.
  5. **Empirical check** (Liben-Nowell et al. 2005, LiveJournal): geography on a real map is lumpy, so the authors use *rank* instead of distance — the probability of a friendship with w falls like 1/(number of people living closer to you than w). The observed exponent was close to this ideal, and the same rank-based prediction holds for the discrete version of the theorem. Watts, Dodds & Newman (2002) and Adamic & Adar (2005) extended the idea from geography to social hierarchies and organizational charts (people search by the most specific shared category), where similar results hold. Core-periphery structure explains why chains to well-connected, high-status targets complete more often.
- **Tiny numeric example**: a line of n = 1,024 people, each knowing their two immediate neighbors plus one long-range contact. With q = 1 (matching the dimension), the chance your long link lands at distance between D and 2D is about the same for every doubling scale (1–2, 2–4, …, 512–1024): ten scales, each with probability about 1/10. Greedy search starting 512 away needs about 10 halvings, and at each halving you expect to wait about 10 steps before someone's long link is in the right band, giving on the order of 10 × 10 = 100 steps — i.e. (log₂ n)². With q = 0 (uniform), the chance a random link lands within distance 32 of the target is 64/1024 ≈ 6%, so you walk a long way before luck helps; the expected path is a power of n rather than a power of its logarithm.
- So-what: (a) short paths exist in almost any group larger than a village — the bottleneck for coordination is never *distance*, it is *awareness and thresholds*. (b) Findability is a design property: a group is navigable when each member has some contacts at every "scale" — inside the team, across the org, across the industry. Org charts and directories are an artificial substitute for missing scales. (c) Homophily and weak ties are not enemies; the navigable structure is exactly a homophilous lattice with a specific sprinkling of cross-cutting ties, which tells you what kind of cross-team contacts to cultivate: not random ones, but a spread across scales.

### Ch 21 — Epidemics (one paragraph)
Branching processes, the basic reproductive number R₀ (each case infects R₀ others on average; below 1 the outbreak dies, above 1 it may explode), SIR and SIS models on graphs, and the effect of structure: contact networks with high-degree nodes make R₀ larger than the average degree suggests, and quarantine works by removing edges, not nodes. Contrast with ch 19: disease is a *simple* contagion (one contact suffices), so bridges help it and clusters merely slow it, which is why the two kinds of spreading behave so differently on the same network.

### Ch 22 — Markets and Information (one paragraph)
Markets as aggregators of dispersed private information: betting odds, prediction markets and stock prices can reveal the crowd's aggregate belief (the "wisdom of crowds" as a market phenomenon, with the Bayesian machinery from ch 16). The chapter contrasts this with cascades: when traders learn from prices they can also herd, and the difference between healthy aggregation and a bubble is whether individual signals keep entering the price.

### Ch 23 — Voting (one paragraph)
Aggregating preferences rather than information: majority rule over pairwise comparisons can cycle (Condorcet paradox), single-peaked preferences restore a stable median outcome (median voter theorem), and Arrow's impossibility theorem shows no ranking rule satisfies a short list of fairness conditions at once. Voting to *aggregate information* (jury theorems) is different from voting to *aggregate preferences*, and sequential public voting reintroduces the cascade problem of ch 16.

### Ch 24 — Property Rights (one paragraph)
The tragedy of the commons and the role of property rights as an institution that changes the game: with open access, each user ignores the cost imposed on others and the resource is overused; assigning property rights (or, in Ostrom's spirit, community rules) changes payoffs so the equilibrium moves toward the social optimum. The chapter closes the book by showing that *institutions* are engineered changes to the game people play, tying the game-theory half of the book to the network half.

## The 5-10 ideas you must carry out of this book
1. **Two faces of connectedness.** Diagnose structure (who is tied to whom) and behavior (whose choices depend on whose) separately, then ask how they interact. Most collective failures are misread because one face is ignored.
2. **Weak ties are bridges; strong ties close triangles.** Novelty enters a group through weak ties, enforcement lives in closed clusters; you need both, and the bridges are the fragile part.
3. **Homophily has two sources — selection and influence — and they are almost impossible to tell apart without timing data.** Assume selection until proven otherwise.
4. **Rational herding is real and shallow.** Sequential public choices create information cascades that carry almost no information and reverse easily. Collect private signals before anyone announces.
5. **Network-effect goods and norms have a tipping point.** Below it, diffuse encouragement leaks away; above it, the behavior sustains itself. Design pushes to cross the point, then stop pushing.
6. **Threshold q = b/(a + b), and clusters of density > 1 − q block cascades.** This is the exact condition for a behavior to stall; you can change q (payoffs) or the seeding (inside clusters), and nothing else matters.
7. **Complex contagions need wide bridges.** Information crosses one weak tie; costly behavior needs several independent adopting neighbors.
8. **Small worlds are navigable only when ties are spread across scales.** Short paths exist almost everywhere; findability is a separate, designable property.
9. **Rich-get-richer is the default consequence of copying.** Extreme inequality of attention or adoption is not evidence of extreme quality differences.
10. **Institutions are edits to the game.** Auctions, matching prices, property rights: each is a change of rules that makes honest or cooperative behavior a best response.

## Mental models & vocabulary
- **Triadic closure** — friends of friends become friends — explains why closed teams stop hearing new ideas.
- **Local bridge / neighborhood overlap** — an edge whose endpoints share no neighbors (overlap 0) — the channel through which novelty arrives; usually a weak tie.
- **Strong Triadic Closure** — strong ties to two people imply at least a weak tie between them — the assumption that makes "bridges are weak" a theorem.
- **Structural hole vs. closure** — brokerage advantage vs. trust advantage — the trade-off between innovation and enforcement in a group's shape.
- **Homophily / 2pq test** — ties are between likes; fewer cross-edges than 2pq means homophily — a quick check of how siloed a group is.
- **Selection vs. social influence** — join because similar vs. become similar after joining — decides whether to intervene at recruitment or at interaction.
- **Foci; focal and membership closure** — shared activities generate ties — the cheapest way to create cross-cluster ties is a shared focus.
- **Structural balance** — stable signed triangles; balanced networks split into two camps — the early-warning model of factionalization.
- **Information cascade** — copying earlier public choices while ignoring private signals — meetings, votes and threads with visible early reactions.
- **Network effect / positive externality** — value rises with adoption — any tool, format or norm whose usefulness is shared.
- **Tipping point (unstable equilibrium z')** — adoption below it decays, above it grows — where to concentrate a launch effort.
- **Threshold q = b/(a + b)** — fraction of neighbors needed before switching pays — the dial you can turn by changing payoffs.
- **Cluster of density p** — every member has at least fraction p of neighbors inside — the object that blocks cascades when p > 1 − q.
- **Complete cascade** — seed set eventually converts everyone — the target of any norm rollout.
- **Simple vs. complex contagion** — one exposure suffices vs. several needed — why information and behavior spread differently.
- **Common knowledge** — everyone knows, knows everyone knows, … — required for risky collective action; produced by public rituals.
- **Watts-Strogatz shortcut** — a few random long links make a clustered graph small — why distance is never the bottleneck.
- **Kleinberg's inverse-square (q = dimension) condition** — long-range ties spread evenly across distance scales — what makes a group navigable.
- **Preferential attachment / rich-get-richer** — new links copy existing links — the origin of heavy-tailed popularity.
- **R₀** — average number of new cases per case — the epidemic analogue of the threshold.
- **Price of anarchy / Braess's paradox** — selfish equilibrium can be worse than optimum; adding options can hurt — a caution against fixing coordination by adding capacity.

## Evidence strength & limits
- **Robust**: short average path lengths in large real networks (measured directly on hundreds of millions of nodes); heavy-tailed degree/popularity distributions; the association between weak ties, low overlap and bridging (Onnela et al. 2007 and many replications); homophily as a pervasive statistical regularity (McPherson, Smith-Lovin & Cook 2001 review); the existence of cascades in laboratory sequential-choice experiments (Anderson & Holt 1997 ran essentially the urn model and found cascades, though subjects deviated from perfect Bayesian play a fair amount); Salganik-Dodds-Watts's unpredictability result.
- **Contested or over-read**: (1) Granovetter's original job-search finding is small-sample and retrospective; the *structural* argument that bridges tend to be weak is the robust part, the claim that weak ties are always the source of useful information is not (Gee, Jones & Burke 2017 on Facebook found most individual jobs came via strong ties even though weak ties were more useful *per tie*; Rajkumar et al. 2022 on LinkedIn found moderately weak ties best). (2) Influence-vs-selection in the Christakis-Fowler contagion papers is unresolved; the book's own caution has been vindicated by later critiques. (3) The exact "six" in six degrees is a median over completed chains; most Milgram chains never completed, so the number is biased downward and the modern full-graph figures (about 4–6) are the ones to quote. (4) QWERTY-style lock-in stories are historically disputed (Liebowitz & Margolis); the model is sound, the canonical example is shaky. (5) Preferential attachment is *one* generator of power laws among many; that a distribution is heavy-tailed does not establish the copying mechanism.
- **What the authors argue vs. show**: every model is a theorem about an idealization; the book is honest that the real-world evidence is usually qualitative agreement (e.g. the LiveJournal exponent is *close to* the ideal). Treat the models as tools for reasoning about mechanisms and as generators of hypotheses, not as calibrated predictors.
- **Known limits of scope**: the models are mostly static or one-shot; there is little on repeated interaction, reputation, punishment or norm enforcement, which is where Ostrom, Bicchieri and Skyrms take over. Payoffs are exogenous; where they come from (culture, moral emotions) is Henrich's and Gintis's territory.

## Design implications for cooperation in real groups
- Map the group's ties and find the local bridges; protect and reward the people who hold them, because they are usually weak ties and will decay unattended. [E]
- Check the 2pq ratio for the traits you care about; if the group is heavily homophilous on a trait, expect it to be split into clusters that will resist any norm that starts in only one of them. [E]
- Before attributing a group's culture to its practices, test whether it is selection (who joins) by looking at newcomers' behavior *at entry*. [E]
- For any decision made sequentially in public, collect private judgments first and reveal them simultaneously; rotate or reverse speaking order. [E]
- Treat dissent as a public good: make it cheap to break a cascade (anonymous flags, a designated skeptic). [H]
- For a norm or tool with network effects, estimate whether adoption is above the tipping point; if not, concentrate the launch in one dense subgroup rather than spreading effort thinly. [E] for the model, [H] for your group's threshold.
- Lower the threshold q by making the new behavior cheaper (tooling, templates, compatibility with the old way) or the old behavior costlier — this widens the set of clusters the cascade can penetrate. [E]
- Seed inside the most cohesive resisting cluster, not around it; a cluster only blocks a cascade while none of its members has switched. [E]
- Expect costly behaviors to need multiple adopting neighbors; build "wide bridges" (several parallel ties between subgroups) rather than single liaisons. [E]
- Create common knowledge for risky collective moves via simultaneous, visible signals (all-hands commitments, public pledges). [E] for the mechanism, [V] that risky collective action is the goal.
- Cultivate cross-scale ties for navigability (someone in the next team, next department, next company) so people can find help in a few hops without a directory. [H]
- Do not fix coordination failures by adding options or capacity by default; check for Braess-type effects and fix incentives instead. [H]
- Interpret extreme inequality of contribution or attention as partly the arithmetic of copying, and design counter-feedback (rotating visibility, randomized ordering) if you want broader participation. [H]
- Use institutional edits (rules that make honesty or contribution a best response — second-price-style mechanisms, clear property/credit rules) rather than exhortation. [V] that alignment beats exhortation; [E] that the mechanisms work in their domains.

## Connections
- **01-secret-of-our-success** — Henrich's conformist and prestige-biased learning are the psychological engines that the cascade models (ch 16, 19) formalize; Henrich adds *why* copying is adaptive, Easley-Kleinberg add *when* it goes wrong. Tension: Henrich treats copying as usually beneficial; ch 16 shows it can lock in error cheaply.
- **02-darwins-unfinished-symphony** — Laland's cultural transmission on populations is ch 18's copying model with biology attached; both see rich-get-richer dynamics in cultural traits.
- **03-social-psychology** — Conformity studies (Asch, Milgram et al. 1969 staring) are the informal versions of ch 16; the identification problem for influence (ch 4) is a warning against over-reading social-influence field studies.
- **04-games-of-strategy** — Supplies the game-theoretic content that ch 6–9 compress; this book adds the graph on which the games are played.
- **05-micromotives-and-macrobehavior** — Schelling's tipping and critical-mass models are the ancestors of ch 17 and of Granovetter's threshold model in ch 19; Easley-Kleinberg add the network and the exact cluster condition.
- **06-behavioral-game-theory** — Camerer's coordination experiments show real thresholds are noisy and learning-driven; ch 19 assumes deterministic thresholds. Anderson & Holt's cascade experiments sit between the two.
- **07-stag-hunt** — Skyrms's local-interaction results (cooperation spreads on lattices when it cannot in mixed populations) are exactly ch 19's point that structure decides which equilibrium wins; ch 7 supplies the ESS vocabulary.
- **08-grammar-of-society** — Bicchieri's pluralistic ignorance is an information cascade over beliefs about norms; her "trendsetters" are ch 19's seed set and low-threshold nodes. Tension: Bicchieri emphasizes changing *expectations* directly; this book emphasizes structure and payoffs.
- **09-governing-the-commons** — Ch 24 is the textbook version of the problem Ostrom studies; ch 3's closure-as-social-capital is the network basis for the monitoring and graduated sanctions she documents.
- **11-bounds-of-reason** — Gintis's insistence on common knowledge and correlated equilibria as the foundation of social norms connects to ch 19's common-knowledge discussion and ch 6's equilibrium-selection problem.

## Retrieval practice
1. **Recall.** State the Strong Triadic Closure property and the consequence it has for local bridges.
<details>If a node has strong ties to two others, those two must be tied at least weakly. Consequence: any local bridge must be a weak tie, because a strong bridge from A to B combined with any other strong tie of A would force a closing edge and destroy the bridge.</details>

2. **Explain-why.** Why does the third person in the urn model ignore her own red draw after two blue announcements?
<details>Because the two earlier guesses reveal two blue draws, and two blue signals outweigh one red: P(majority-blue | b, b, r) = 2/3 > 1/2. Guessing blue is the correct Bayesian choice even though it discards her own evidence, and from then on nobody's guess adds information.</details>

3. **Apply.** A team of 12 runs a public show-of-hands vote on adopting a new process. The two most senior engineers vote first and both say yes; ten others follow. What do you actually know about the team's opinion, and what would you change?
<details>Very little: after two visible agreeing signals, everyone else's vote may be a cascade carrying no private information. Change to simultaneous private votes (or written positions before discussion), and have juniors or randomly chosen members speak first.</details>

4. **Recall / compute.** With payoffs a = 4 for both-A and b = 1 for both-B, what threshold fraction of neighbors must use A before a node switches? What cluster density blocks the cascade?
<details>q = b/(a + b) = 1/5 = 0.2. A cluster of density greater than 1 − q = 0.8 outside the seed set blocks a complete cascade; any cluster of density 0.8 or less does not.</details>

5. **Explain-why.** Why do dense clusters block behavioral cascades but not the spread of a rumor?
<details>Behavior is a complex contagion: a node switches only when a fraction q of neighbors has, and cluster members have most neighbors inside the cluster, so the first would-be switcher never sees enough adopters. A rumor is a simple contagion: one exposure suffices, so the first bridge into the cluster is enough.</details>

6. **Apply.** You want a documentation norm to spread across an org of five sub-teams that rarely interact. Where do you seed it and why?
<details>Seed inside each dense sub-team (or at least inside the most resistant one), not via liaisons between teams, because a cohesive cluster only blocks a cascade while none of its members has switched. Also lower the threshold (templates, tooling) so the required fraction of adopting neighbors is smaller.</details>

7. **Spot the misconception.** "Watts and Strogatz explained the small-world phenomenon: a few random shortcuts make the world small." What is missing?
<details>They explained why short paths exist, not why people can find them. With uniformly random shortcuts, greedy local search takes polynomially many steps. Kleinberg showed navigability requires long-range ties whose probability falls with distance to the power of the dimension (q = 2 on a plane), giving roughly one contact at every distance scale.</details>

8. **Apply.** Adoption of an internal tool is at 22%, and the marginal user just below that level values it slightly less than its (time) cost. What does ch 17 predict, and what are your options?
<details>You are below the tipping point z', so adoption will unravel toward zero under its own dynamics. Options: reduce the cost (price) so the tipping point drops below 22%; raise the network value f(z) for early users; or concentrate adoption in one subgroup to push local adoption past the tipping point and let feedback carry it.</details>

9. **Explain-why.** Why is "our best people are all similar, so our culture shapes them" a weak inference?
<details>Homophily arises from selection as well as influence; similarity among members may reflect who was recruited or self-selected, not what membership did. Only data on similarity before and after joining (as in Crandall et al.'s Wikipedia study) can separate the two.</details>

10. **Spot the misconception.** "Weak ties are more valuable than strong ties." Correct this.
<details>Weak ties are more likely to be bridges, so they are disproportionately the *source of novel information*; strong ties provide trust, support, enforcement and closure. Neither is more valuable in general, and recent large-scale job-market studies show strong ties still deliver most jobs even where weak ties are more productive per tie. The design lesson is to hold both.</details>

## Common misreadings of this book
- **Reading it as a book about the Internet.** Half the chapters are about the Web, but the models of ties, homophily, cascades and thresholds are about any group; the Web is the data source, not the subject.
- **Confusing the three kinds of copying.** Information cascades (ch 16: I copy because you probably know something), network effects (ch 17: I copy because the thing is worth more when you use it), and coordination on a graph (ch 19: I copy my *neighbors* because matching them pays). They have different fixes: reveal private information; cross the tipping point; change q or seeding.
- **Taking six degrees as a fact about everyone.** It is a median over the minority of chains that completed; the robust claim is "short paths exist", the fragile one is the number.
- **Treating the cluster theorem as "clusters are bad".** Clusters block *new* behavior but also protect *established* cooperation from invasion by defection — the same density that stops a good norm from entering also stops a bad one. Skyrms's local-interaction results are the flip side.
- **Assuming weak ties carry behavior because they carry information.** They carry awareness; adoption of anything costly needs multiple adopting neighbors.
- **Reading the models as predictions.** Every result is a theorem about a stylized process; the empirical chapters show qualitative agreement, which is enough to guide diagnosis and intervention design, not to forecast numbers.
