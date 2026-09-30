# Networks, Crowds, and Markets: Reasoning about a Highly Connected World — David Easley & Jon Kleinberg (Cambridge University Press, 2010)
Level: Order  ·  Priority: Selections
Est. reading time saved: ~14h (selected chapters ~5h; whole book ~30h)  ·  Your time with this file: ~30 min

## The book in one sentence
Individual choices depend on *who is connected to whom* and *what others have already done*, so the same population can settle into very different collective outcomes depending on network structure and the order in which people act.

## The book in one paragraph
Easley (economist) and Kleinberg (computer scientist) fuse graph theory, game theory and market economics into one toolkit for reasoning about connected systems. The first third builds vocabulary: ties, bridges, homophily, games, equilibria, auctions and markets on networks. The middle third covers the Web. The last third — the part this curriculum needs — models dynamics: why rational people imitate each other into cascades, why network-effect goods and norms tip between "nobody" and "everybody", how a behavior spreads or stalls across a real graph depending on thresholds and clusters, why huge societies are navigable "small worlds", and how epidemics, markets, votes and property rules aggregate behavior. Every model can be computed by hand, which is the point: you learn to see the mechanism, not just name the phenomenon.

## Why it's in this curriculum (the question to read it with)
Skyrms, Bicchieri and Ostrom explain why norms and institutions can stabilize cooperation; this book supplies the missing variable, **structure**. Read it asking: *given the actual web of ties in my group, where will a new norm catch, where will it die, who must move first, and which bridges or clusters help or block?* It also gives the cleanest account of why groups converge on something most members privately doubt — the formal backbone of Bicchieri's pluralistic ignorance and Schelling's tipping.

## Table of contents
TOC verified against web-search snippets of library catalogue records and course syllabi (the free online draft on Kleinberg's Cornell page is blocked by this session's proxy; the catalogue listings mirror it). ★ = covered in depth; other chapters get one paragraph.

**Ch 1 ★ Overview**

**Part I — Graph Theory and Social Networks**: Ch 2 Graphs · Ch 3 ★ Strong and Weak Ties · Ch 4 ★ Networks in Their Surrounding Contexts · Ch 5 Positive and Negative Relationships

**Part II — Game Theory**: Ch 6 ★ Games · Ch 7 Evolutionary Game Theory · Ch 8 Modeling Network Traffic Using Game Theory · Ch 9 Auctions

**Part III — Markets and Strategic Interaction in Networks**: Ch 10 Matching Markets · Ch 11 Network Models of Markets with Intermediaries · Ch 12 Bargaining and Power in Networks

**Part IV — Information Networks and the World Wide Web**: Ch 13 The Structure of the Web · Ch 14 Link Analysis and Web Search · Ch 15 Sponsored Search Markets

**Part V — Network Dynamics: Population Models**: Ch 16 ★ Information Cascades · Ch 17 ★ Network Effects · Ch 18 Power Laws and Rich-Get-Richer Phenomena

**Part VI — Network Dynamics: Structural Models**: Ch 19 ★ Cascading Behavior in Networks · Ch 20 ★ The Small-World Phenomenon · Ch 21 Epidemics

**Part VII — Institutions and Their Aggregate Effects**: Ch 22 Markets and Information · Ch 23 Voting · Ch 24 Property Rights
(Verification gaps: catalogue snippets phrase Part VII as "Institutions and Aggregate Behavior" and one lists Ch 24 as "Property"; the headings here are from background knowledge, not confirmed against the book itself.)

Why these selections: 3, 4, 19 and 20 are the chapters about *social* structure; 16 and 17 are the two population-level models of contagious behavior a norm designer needs; 1 frames the whole; 6 shows how the book attaches games to graphs. The Web and market chapters belong to a different course.

## Chapter-by-chapter: the salient knowledge

### Ch 1 — Overview
- Core claims: connectedness has a *structural* face (the graph) and a *behavioral* face (choices that depend on others' choices); neither alone explains collective outcomes. The same few ideas — ties, bridges, homophily, cascades, tipping, feedback — recur across friendships, markets, epidemics and politics, and sensible individuals aggregate into panics, fads and lock-in.
- Key examples: a high-school romantic network (Bearman, Moody & Stovel 2004) that is one sprawling chain with almost no short cycles; Milgram's six degrees.
- So-what: diagnose a group with two separate questions — what does the tie structure look like, and what does each decision depend on — then ask how they interact.

### Ch 2 — Graphs
Nodes, edges, paths, distance, components. The load-bearing fact: real social networks almost always have one giant component containing most nodes, with short distances inside it — so expect reachability in any sizeable group, but not *uniform* reachability.

### Ch 3 — Strong and Weak Ties
- Core claims:
  1. **Triadic closure**: if A is strongly tied to B and C, B and C are likely to become tied — through opportunity, trust and the strain of open triangles.
  2. **Granovetter's strength of weak ties** (1973; most jobs in his interviews came through acquaintances, not close friends). The explanation is structural: weak ties are disproportionately *local bridges* (edges whose endpoints share no neighbors) because strong ties get closed into triangles. Novel information sits across a bridge; your close friends know what you know.
  3. **Strong Triadic Closure**: if a node has strong ties to two others, at least a weak tie must exist between them. From this alone, every local bridge is a weak tie: a strong bridge from A to B plus any other strong tie of A would force a closing edge, and the bridge would stop being local.
  4. **Large-scale data**: Onnela et al. (2007), on a national mobile-phone graph: ties with high *neighborhood overlap* carried the most call time, and deleting weak ties first shattered the network while deleting strong ties first merely thinned it.
  5. **Closure vs. structural holes** (Coleman vs. Burt): a closed cluster gives trust, enforceability and shared norms; spanning a hole between clusters gives information and brokerage power. Two kinds of social capital that trade off.
- Tiny example: overlap of edge A–B = shared neighbors ÷ all neighbors of A or B; a local bridge has overlap 0.
- So-what: cooperation needs closure (sanctioning, trust) *and* bridges (ideas, resources); all-closure groups enforce stale norms, all-bridge groups enforce nothing. Find your local bridges and protect them — they are usually weak, hence fragile, and losing one can cut off a subgroup.

### Ch 4 — Networks in Their Surrounding Contexts (homophily)
- Core claims:
  1. **Homophily**: ties form disproportionately between similar people (Moody's 2001 school-friendship maps, where race predicts community structure).
  2. **Measuring it**: if fraction p of nodes have a trait and q = 1 − p do not, random mixing puts 2pq of edges across the boundary. Tiny example: 40% women, 60% men → 0.48 of edges should be mixed-gender; if only 0.20 are, the network is strongly homophilous.
  3. **Two mechanisms, hard to separate**: *selection* (choosing similar friends) and *social influence* (friends making each other similar); only longitudinal data can distinguish them. The book flags this for Christakis & Fowler's (2007) obesity-contagion claim, and later critiques (Shalizi & Thomas 2011) showed latent homophily produces identical patterns.
  4. **Foci** (Feld 1981): people are tied to activities and groups, so three closures run in parallel — *triadic* (friend of a friend), *focal* (sharing an activity) and *membership* (joining a friend's activity). Kossinets & Watts (2006): the chance of a new tie rises with each shared friend, with diminishing returns.
  5. Crandall et al. (2008), Wikipedia editors: similarity rises sharply *before* first interaction (selection) and keeps rising after (influence) — both are real.
- So-what: a group's "culture" may be mostly who joined, not what membership did; selection is fixed at the recruiting boundary, influence by changing who talks to whom. Homophily also turns a network into clusters — and clusters (ch 19) block cascades of new behavior.

### Ch 5 — Positive and Negative Relationships
**Structural balance** in signed graphs: triangles with three positive edges or exactly one are stable; the others are strained. Harary's theorem: a fully balanced network splits into at most two mutually hostile camps (the book's example is the pre-WWI alliance system). Balance pressure predicts a two-faction split unless cross-cutting positive ties are maintained.

### Ch 6 — Games (network framing only; substance is in 04-games-of-strategy)
Standard toolkit — dominant strategies, best responses, Nash equilibrium, mixed strategies, Pareto and social optimality — via the Prisoner's Dilemma, a coordination game and Hawk-Dove. The distinctive framing: a game is a **template later played on every edge of a graph**, so a node's payoff is the sum of pairwise games with its neighbors (the seed of ch 19). With multiple coordination equilibria theory cannot pick one; history, focal points or network position must. Tiny example: matching on A pays 3, on B pays 2; both (A,A) and (B,B) are equilibria, and *which* a group lands on is answered by chapters 16–19, not by the game.

### Ch 7 — Evolutionary Game Theory
Strategies as imitated traits; an **evolutionarily stable strategy** cannot be invaded by a small mutant group. In coordination games each pure equilibrium is an ESS, so history decides. This is the bridge to Skyrms (07-stag-hunt) and explains why a cooperative convention, once common, is self-protecting.

### Ch 8 — Modeling Network Traffic Using Game Theory
Selfish route choice can be worse for everyone than coordination, and adding a shortcut can slow everyone (Braess's paradox); the **price of anarchy** bounds the damage. Adding capacity to self-interested agents does not automatically help; fix incentives, not edges.

### Ch 9 — Auctions
Auction formats; truthful bidding is dominant in a second-price auction because others set the price. The pattern to carry: institutions that make honesty the best response.

### Ch 10 — Matching Markets
A perfect buyer–seller matching exists unless some *constricted set* of buyers has too few acceptable sellers; market-clearing prices always exist and resolve constriction without any planner knowing valuations.

### Ch 11 — Network Models of Markets with Intermediaries
A trader who is the *only* path between a buyer and seller captures all the surplus; two traders serving the same pair compete their margin to zero. Power is being on the only route.

### Ch 12 — Bargaining and Power in Networks
Exchange-network experiments show bargaining power depends on outside options, not degree: a node whose partners have no alternatives is powerful; a central node in a long chain can be weak. To flatten power in a team, give people alternatives.

### Ch 13 — The Structure of the Web
The Web as a directed graph with a giant strongly connected core, IN and OUT sets and tendrils (the bow-tie). Where influence flows one way, the bow-tie says who can affect whom.

### Ch 14 — Link Analysis and Web Search
Hubs and authorities, and PageRank: a page matters if pages that matter point to it. "Whom people defer to" can be computed from the structure of deference — what reputation systems do implicitly.

### Ch 15 — Sponsored Search Markets
Ad slots sold by generalized second-price auctions, tied to matching markets and the VCG mechanism: the book's main example of an institution engineered to align self-interest with efficiency.

### Ch 16 — Information Cascades
- Core claims:
  1. When people act in sequence and see what others *did* but not what they *knew*, it can be rational to ignore your own signal and copy the crowd. Once two or three early movers agree, everyone after copies: an **information cascade** (Banerjee 1992; Bikhchandani, Hirshleifer & Welch 1992).
  2. Cascades are fragile: choices after the cascade starts carry *no* new information, so a public signal or credible dissenter can reverse them.
  3. Cascades can be wrong even when everyone reasons correctly and most private signals point the right way, if the first few pointed wrong.
  4. Distinct from network effects (ch 17, where copying pays *because* others copy): here copying is purely informational.
- **The urn model, plainly**: an urn is either *majority-blue* (2 blue, 1 red) or *majority-red* (2 red, 1 blue), each equally likely. People arrive one at a time, draw a marble privately, replace it, and publicly guess the urn type.
  - Person 1 draws blue. P(majority-blue | blue) = (½ × ⅔)/(½ × ⅔ + ½ × ⅓) = 2/3. She guesses blue; her guess reveals her draw.
  - Person 2 sees "blue" and his own draw. Two blues: P = 4/5 → blue. Blue then red: the signals cancel to ½; assume he follows his own draw. Either way his guess reveals his draw.
  - Person 3 sees two "blue" guesses and draws **red**. P(majority-blue | b, b, r) = (⅔ × ⅔ × ⅓)/(⅔ × ⅔ × ⅓ + ⅓ × ⅓ × ⅔) = (4/27)/(6/27) = 2/3 > ½. She guesses blue *against her own evidence*.
  - Person 4 sees three blue guesses but knows the third was uninformative; her situation is identical to person 3's. The cascade is locked until something external breaks it.
  - Probability check: with a majority-blue urn, the first two draws are both red with probability 1/9 (wrong cascade), both blue with 4/9 (right cascade), conflicting with 4/9 (restart) — so a wrong cascade occurs about 1/5 of the time, though every signal is 2/3 accurate.
- Empirical anchors: Milgram, Bickman & Berkowitz (1969), passers-by joining confederates staring at a building; Anderson & Holt (1997), the urn model in the lab.
- So-what: any sequential public decision (the senior person speaks first, a show of hands, a thread with visible early reactions) is an urn model, and the outcome may reflect two people's noise. Fixes: collect private signals *before* anyone announces; randomize or reverse speaking order; make dissent cheap. Good news: cascades are shallow and easy to overturn.

### Ch 17 — Network Effects
- Core claims:
  1. Some goods and behaviors have **positive externalities**: their value to me rises with the number of others using them (phones, file formats, a norm of showing up). Copying here is payoff-driven, not informational.
  2. Aggregate demand then has multiple equilibria; the unstable one is a **tipping point**. Below it the behavior collapses to zero; above it, it grows to a high stable level.
  3. Expectations are self-fulfilling: if everyone believes adoption will be z, they act on it and it becomes true. Marketing, subsidies and public commitments work by moving beliefs across the tipping point.
- **The model, plainly**: consumers are indexed by x from 0 to 1 in decreasing order of intrinsic interest r(x). If fraction z adopts, x's willingness to pay is r(x)·f(z), with f increasing (the network effect); x adopts at price p if r(x)·f(z) ≥ p. Adopters are those below a cutoff, and in equilibrium the cutoff *is* z, so self-consistent adoption levels solve **r(z)·f(z) = p**, plus z = 0 (nobody adopts, so it is worth nothing).
- **Tiny numeric example**: r(x) = 1 − x, f(z) = z, price p = 0.2. Solve (1 − z)·z = 0.2 → z ≈ 0.28 or 0.72. Three equilibria: 0, z' ≈ 0.28, z'' ≈ 0.72. If 30% adopt, the marginal user at x = 0.30 values it at 0.70 × 0.30 = 0.21 > 0.2, so more join; at 50%, 0.25, still growing; at 80%, 0.16 < 0.2, some drop out; the process converges to 0.72. If only 25% adopt, the marginal value is 0.19 < 0.2 and adoption unravels to zero. **z' = 0.28 is the tipping point.**
- **The Z-shaped diagram**: plot the marginal user's willingness to pay r(z)·f(z) against z: it starts at 0, rises, peaks and falls to 0 at z = 1, and a horizontal price line cuts the hump at z' and z''. Where the curve is *above* the price line adoption grows; below it, adoption shrinks — arrows point away from z' (unstable) and toward 0 and z'' (stable). Plotting *equilibrium adoption against price* instead gives the backwards-Z: at high prices only 0 survives, below the peak two interior equilibria appear, and at low prices adoption jumps to a high level. Near the tipping point a small price cut or nudge in expectations produces a discontinuous jump.
- Empirical anchor: Salganik, Dodds & Watts (2006) — the same songs ranked very differently across eight artificial "worlds" once download counts were visible.
- So-what: for any behavior whose value depends on how many others do it (a shared tool, a documentation norm, a commons), the question is not "is it good?" but "are we above the tipping point?" If not, diffuse encouragement leaks away; you need a concentrated push — subsidize early adopters, seed critical mass in one subgroup, make public commitments. Above z'' the behavior sustains itself.

### Ch 18 — Power Laws and Rich-Get-Richer Phenomena
Popularity has heavy tails (fraction with popularity k falls like k^(−c)), and a simple copying model — newcomers copy a random earlier node's choice with probability p (**preferential attachment**) — produces them. Lessons: extreme inequality of attention is the default outcome of copying, not evidence of quality differences; early luck is amplified.

### Ch 19 — Cascading Behavior in Networks
- Core claims:
  1. Here each person sees and cares only about **neighbors**, and copies for payoff (a coordination game on each edge), not information. This is the model of *norm spread*.
  2. Whether a behavior A spreads from a seed set depends on one number — the threshold q — and on the *structure* of the rest of the network. The obstacle is not distance but the **density of tightly-knit communities**.
  3. Weak ties carry *awareness* across clusters, but a bridge is one of many edges for the node it reaches, so it rarely makes that node *switch*. Simple contagion (information, disease) crosses bridges; complex contagion (costly behavior) does not.
  4. Extensions: **bilinguality** (adopting both A and B at a cost); Granovetter's (1978) threshold model of collective action; and **common knowledge** (Chwe 2001) — people join risky action only if they know enough others will, and know that those others know, which is why public rituals matter for revolts.
- **The model, plainly**: on each edge the endpoints play a coordination game — both A → each gets a; both B → each gets b; mismatch → 0. A node with d neighbors, fraction p of them on A, gets p·d·a from A and (1 − p)·d·b from B, so it prefers A when
  **p ≥ q = b / (a + b).**
  Start with a seed set on A in a network of B-users; every other node switches to A when at least fraction q of its neighbors use A (switches are one-way). If eventually everyone uses A, the seed set causes a **complete cascade** at threshold q.
- **Cluster, defined**: a set of nodes is a *cluster of density p* if every node in it has at least fraction p of its neighbors inside the set.
- **The cluster-density theorem, precisely**: take a seed set of initial A-adopters and threshold q. (i) If the network *outside the seed set* contains a cluster of density greater than 1 − q, the seed set does **not** cause a complete cascade. (ii) Conversely, if the seed set does **not** cause a complete cascade, the network outside it contains a cluster of density greater than 1 − q.
  Why (i): the first cluster member to switch would have all its A-neighbors outside the cluster — fewer than fraction q, since more than 1 − q are inside — so it cannot switch, and nobody does. Why (ii): at the end of the process the nodes still on B each have fewer than q of their neighbors on A, so they form a cluster of density greater than 1 − q.
- **Tiny numeric example**: a = 3, b = 2, so q = 0.4 and 1 − q = 0.6. Seeds s1 and s2 both link to c; c links to d; d, e, f form a triangle. Round 1: c's neighbors {s1, s2, d} are 2/3 on A ≥ 0.4 → c switches. Round 2: d's neighbors {c, e, f} are 1/3 on A < 0.4 → d stays. The cascade stops. Check: {d, e, f} is a cluster of density 2/3 (d has 2 of 3 neighbors inside; e and f have all), and 2/3 > 0.6, as (i) predicts. Change payoffs to a = 3, b = 1: q = 0.25, 1 − q = 0.75, and 2/3 no longer exceeds 0.75. Now d switches (1/3 ≥ 0.25), then e (1/2 ≥ 0.25), then f: complete cascade.
- Empirical anchors: Centola & Macy (2007) on complex contagions needing wide bridges; Centola's (2010) online experiment found clustered networks spread costly behavior *faster* than random ones — the reverse of information.
- So-what: the most actionable chapter for norm design. (a) Lower the threshold (make A cheaper, B costlier, or allow bilingual compatibility) and impenetrable clusters become porous. (b) Seed *inside* dense clusters; a cluster blocks only while none of its members has switched. (c) Do not expect a norm to jump a single weak tie; build wide bridges or move whole sub-teams. (d) For risky collective action, create common knowledge through visible simultaneous signals.

### Ch 20 — The Small-World Phenomenon
- Core claims:
  1. **Six degrees**: Milgram's experiment (Travers & Milgram 1969) asked Nebraskans to forward a letter toward a Boston stockbroker via acquaintances; completed chains had a median of about six. Dodds, Muhamad & Watts (2003) replicated by email (most chains died; completed ones averaged 5–7); full-graph measurements (Leskovec & Horvitz 2008; Facebook) give roughly 4–7.
  2. There are *two* surprises: short paths exist despite heavy clustering, and ordinary people can **find** them with only local knowledge.
  3. **Watts & Strogatz (1998)** explain the first: a clustered lattice plus a few random long-range links has logarithmic average distance while keeping its clustering. Homophily gives the lattice; weak ties give the shortcuts.
  4. **Kleinberg (2000)** shows Watts-Strogatz cannot explain the second. With uniformly random shortcuts, a greedy forwarder (pass to the neighbor closest to the target) cannot home in and needs on the order of n^(2/3) steps on a 2-D grid. If long links are chosen with probability proportional to distance^(−q), decentralized search is efficient **only when q equals the dimension** of the space (q = 2 on a plane, q = 1 on a line): greedy forwarding then takes about (log n)² steps. Below the dimension links are too random; above it, too local. The right exponent gives roughly one long-range acquaintance at every *scale* of distance, so each step can halve the remaining distance.
  5. **Empirical check** (Liben-Nowell et al. 2005, LiveJournal): with lumpy real geography, use *rank* — friendship probability with w falls like 1/(number of people living closer than w). The observed exponent was close to ideal; Adamic & Adar (2005) found the analogue in an org chart.
- **Tiny numeric example**: a line of n = 1,024 people, each knowing two immediate neighbors plus one long-range contact. With q = 1, the long link lands in each of the ten doubling scales (1–2, …, 512–1024) with roughly equal probability, 1/10. Greedy search from 512 away needs ten halvings, and each halving waits about ten steps for a long link in the right band: about 10 × 10 = 100 steps, i.e. (log₂ n)². With q = 0, a random link lands within 32 of the target only 64/1024 ≈ 6% of the time, and the expected path grows as a power of n.
- So-what: short paths exist in any group larger than a village, so the coordination bottleneck is never distance — it is awareness and thresholds. Findability is a separate, designable property: a group is navigable when each member has contacts at every scale (team, org, industry) — a homophilous lattice with one cross-cutting tie per scale, not random ones.

### Ch 21 — Epidemics
R₀ (below 1 an outbreak dies; above 1 it may explode), SIR/SIS models on graphs, and the effect of high-degree nodes. Contrast with ch 19: disease is a *simple* contagion, so bridges help it and clusters merely slow it.

### Ch 22 — Markets and Information
Prices and prediction markets aggregate dispersed private information via the Bayesian machinery of ch 16 — but traders learning from prices can also herd; a bubble is aggregation in which individual signals stop entering the price.

### Ch 23 — Voting
Majority rule can cycle (Condorcet); single-peaked preferences give a stable median outcome; Arrow's theorem rules out a fully fair ranking rule. Aggregating *information* differs from aggregating *preferences*, and sequential public voting reintroduces ch 16's cascades.

### Ch 24 — Property Rights
The tragedy of the commons and property rights as an institution that changes the game: assigning rights (or, in Ostrom's spirit, community rules) shifts payoffs toward the social optimum. Institutions are engineered edits to the game people play.

## The 5-10 ideas you must carry out of this book
1. **Two faces of connectedness.** Diagnose structure and behavior separately, then ask how they interact.
2. **Weak ties are bridges; strong ties close triangles.** Novelty enters through weak ties, enforcement lives in closed clusters; you need both, and the bridges are fragile.
3. **Homophily has two sources — selection and influence — hard to separate without timing data.** Assume selection until shown otherwise.
4. **Rational herding is real and shallow.** Sequential public choices create cascades that carry almost no information and reverse easily. Collect private signals before anyone announces.
5. **Network-effect goods and norms have a tipping point.** Below it, diffuse encouragement leaks away; above it, the behavior sustains itself. Push to cross the point, then stop.
6. **Threshold q = b/(a + b); clusters of density > 1 − q block cascades.** The exact stall condition; change q (payoffs) or the seeding (inside clusters).
7. **Complex contagions need wide bridges.** Information crosses one weak tie; costly behavior needs several adopting neighbors.
8. **Small worlds are navigable only when ties span scales.** Short paths exist almost everywhere; findability is a separate, designable property.
9. **Rich-get-richer is the default consequence of copying.** Extreme inequality of attention is not evidence of extreme quality differences.
10. **Institutions are edits to the game.** Auctions, prices and property rights change rules so that honest or cooperative behavior becomes a best response.

## Mental models & vocabulary
- **Local bridge / neighborhood overlap** — an edge whose endpoints share no neighbors (overlap 0) — the channel through which novelty arrives; usually weak.
- **Structural hole vs. closure** — brokerage advantage vs. trust advantage — the innovation/enforcement trade-off.
- **2pq test** — fewer cross-edges than 2pq means homophily — a quick measure of how siloed a group is.
- **Tipping point (unstable equilibrium z')** — adoption below it decays, above it grows — where to concentrate a launch.
- **Threshold q = b/(a + b)** — fraction of neighbors needed before switching pays — the dial you turn by changing payoffs.
- **Cluster of density p** — every member has at least fraction p of neighbors inside — blocks cascades when p > 1 − q.
- **Common knowledge** — everyone knows, knows everyone knows, … — required for risky collective action; produced by public rituals.

## Evidence strength & limits
- **Robust**: short average paths in large real networks; heavy-tailed popularity; weak ties as bridges (Onnela et al. 2007); homophily as a pervasive regularity (McPherson, Smith-Lovin & Cook 2001); laboratory cascades (Anderson & Holt 1997, though subjects often deviated from Bayesian play); Salganik-Dodds-Watts unpredictability.
- **Contested or over-read**: (1) Granovetter's job-search finding is small-sample and retrospective; the *structural* claim (bridges tend to be weak) is robust, "useful information comes from weak ties" is not — Gee, Jones & Burke (2017, Facebook) found most jobs still came via strong ties; Rajkumar et al. (2022, LinkedIn) found moderately weak ties best. (2) Influence vs. selection in Christakis-Fowler remains unresolved. (3) "Six" is a median over the minority of Milgram chains that completed; quote the full-graph 4–6 figures. (4) Preferential attachment is one generator of power laws among many; a heavy tail does not establish copying.
- **Argued vs. shown**: every model is a theorem about an idealization with qualitative empirical support; use them to reason about mechanisms, not to predict numbers.
- **Scope limits**: mostly one-shot models; little on repeated interaction, reputation or enforcement, where Ostrom, Bicchieri and Skyrms take over. Payoffs are exogenous; their origin is Henrich's and Gintis's territory.

## Design implications for cooperation in real groups
- Find the group's local bridges and protect the people who hold them; they are usually weak ties and decay unattended. [E]
- Check the 2pq ratio for traits you care about; heavy homophily means clusters that will resist a norm starting in one of them. [E]
- For any sequential public decision, collect private judgments first and reveal them simultaneously; reverse speaking order. [E]
- For a norm or tool with network effects, estimate whether adoption is above the tipping point; if not, concentrate the launch in one dense subgroup. [E] for the model; [H] for your group's threshold.
- Lower q by making the new behavior cheaper (tooling, templates, compatibility) or the old one costlier. [E]
- Seed inside the most cohesive resisting cluster; it only blocks while none of its members has switched. [E]
- Build wide bridges (parallel ties between subgroups) rather than single liaisons; costly behaviors need several adopting neighbors. [E]
- Create common knowledge for risky collective moves through simultaneous visible signals. [E] for the mechanism; [V] that the move is worth it.
- Prefer institutional edits (rules that make contribution a best response) over exhortation. [V] that alignment beats exhortation; [E] that the mechanisms work.

## Connections
- **01-secret-of-our-success** — Henrich's conformist and prestige-biased learning are the psychology ch 16 and 19 formalize; Henrich says *why* copying is adaptive, this book *when* it goes wrong.
- **03-social-psychology** — Conformity studies are informal ch 16; ch 4's identification problem warns against over-reading influence studies.
- **04-games-of-strategy** — Supplies the game theory ch 6–9 compress; this book adds the graph on which games are played.
- **05-micromotives-and-macrobehavior** — Schelling's tipping and critical mass are the ancestors of ch 17 and ch 19; this book adds the network and the exact cluster condition.
- **07-stag-hunt** — Skyrms's local-interaction results (cooperation spreads on lattices when it cannot in mixed populations) are ch 19's point that structure decides which equilibrium wins; ch 7 supplies ESS vocabulary.
- **08-grammar-of-society** — Bicchieri's pluralistic ignorance is a cascade over beliefs about norms; her trendsetters are ch 19's seed set and low-threshold nodes. Tension: she targets expectations directly; this book targets structure and payoffs.
- **09-governing-the-commons** — Ch 24 is the textbook version of Ostrom's problem; ch 3's closure underpins the monitoring and sanctions she documents.
- **11-bounds-of-reason** — Gintis's emphasis on common knowledge connects to ch 19 and to ch 6's equilibrium-selection problem.

## Retrieval practice
1. **Recall.** State the Strong Triadic Closure property and its consequence for local bridges.
<details>If a node has strong ties to two others, they must be at least weakly tied. Consequence: every local bridge is a weak tie, since a strong bridge plus any other strong tie would force a closing edge.</details>

2. **Explain-why.** Why does the third person in the urn model ignore her own red draw after two blue announcements?
<details>The two earlier guesses reveal two blue draws, and two blue signals outweigh one red: P(majority-blue | b, b, r) = 2/3 > 1/2. Guessing blue is correct Bayesian play; from then on nobody's guess adds information.</details>

3. **Apply.** Twelve engineers vote by show of hands; the two most senior vote first, both yes; ten follow. What do you know, and what would you change?
<details>Very little — after two visible agreeing signals the rest may be a cascade carrying no private information. Switch to simultaneous private votes, and have juniors or random members speak first.</details>

4. **Compute.** With a = 4 for both-A and b = 1 for both-B, what fraction of neighbors must use A before a node switches, and what cluster density blocks the cascade?
<details>q = 1/(4 + 1) = 0.2. A cluster of density greater than 0.8 outside the seed set blocks a complete cascade; any cluster of density 0.8 or less does not.</details>

5. **Explain-why.** Why do dense clusters block behavioral cascades but not rumors?
<details>Behavior is a complex contagion: a node switches only when fraction q of neighbors has, and cluster members have most neighbors inside, so the first would-be switcher never sees enough adopters. A rumor needs one exposure, so one bridge in is enough.</details>

6. **Apply.** You want a documentation norm to spread across five sub-teams that rarely interact. Where do you seed it?
<details>Inside each dense sub-team, not via liaisons, because a cluster only blocks while none of its members has switched. Also lower the threshold with templates and tooling.</details>

7. **Spot the misconception.** "Watts and Strogatz explained the small-world phenomenon: a few random shortcuts make the world small." What is missing?
<details>They explained why short paths exist, not why people can find them. Kleinberg showed navigability needs long-range ties whose probability falls with distance to the power of the dimension — one contact at every scale.</details>

8. **Apply.** Adoption of an internal tool sits at 22%, and the marginal user values it slightly less than its time cost. What does ch 17 predict, and what are your options?
<details>You are below the tipping point, so adoption will unravel toward zero. Options: cut the cost so the tipping point drops below 22%; raise the value for early users; or concentrate adoption in one subgroup to push past the tipping point locally.</details>

9. **Explain-why.** Why is "our best people are all similar, so our culture shapes them" a weak inference?
<details>Similarity may be selection (who was recruited or self-selected) rather than influence; only before-and-after data, as in Crandall et al.'s Wikipedia study, can separate the two.</details>

10. **Spot the misconception.** "Weak ties are more valuable than strong ties." Correct this.
<details>Weak ties are more likely to be bridges, so they are the main source of novel information; strong ties provide trust and enforcement. Neither is more valuable in general; hold both.</details>

## Common misreadings of this book
- **Reading it as a book about the Internet.** The Web is the data source, not the subject; the models apply to any group.
- **Confusing the three kinds of copying.** Cascades (ch 16: you probably know something), network effects (ch 17: it is worth more when you use it), coordination on a graph (ch 19: matching neighbors pays). Fixes differ: reveal private information; cross the tipping point; change q or the seeding.
- **Taking six degrees as a fact about everyone.** It is a median over the minority of completed chains; "short paths exist" is robust, the number is not.
- **Reading the cluster theorem as "clusters are bad".** The density that stops a good norm entering also protects established cooperation from a bad one (see Skyrms).
- **Assuming weak ties carry behavior because they carry information.** They carry awareness; adopting anything costly needs several adopting neighbors.
