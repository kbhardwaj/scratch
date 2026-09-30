# Cooperation-designer gaps primer: what the 11 sources do not teach you

This file is the companion to the course's learning design (section 6, "what the reading list omits") and to the claims ledger's open questions (`synthesis/claims-ledger.md` section 6): three of those open questions are answered here as far as practice allows — whether Ostrom's principles transfer to digital commons (sections 5–6), whether empirical and normative expectations can be separated in the field (section 1), and whether gradual growth generalizes (sections 7–8). The 11 books are a knowledge curriculum about *why* cooperation happens; the course goal is to *diagnose a real group and design the norms, incentives, network structure and institutions that fix it*. Between those two sits a layer of practical, measurement, legal and organizational knowledge that none of the sources supplies. This primer does not replace expert help. It exists so you can ask a behavioral scientist, a community-operations lead, a trust-and-safety engineer, an HR/people partner, a lawyer or an economist the right questions, and recognize a weak answer when you hear one.

**How to use it.** Read "Why it matters" and the numbered points of every section once (about 40 minutes). Treat "Read next" as a queue, not an assignment. Do the Critical sections before you write any brief section that proposes a sanction, a metric, a reputation score or a norm campaign; do the Important sections when the brief's group is a team (section 7), a community or platform (sections 4, 6), or is growing (section 8); do the Useful sections when you have time or when the mentor critique flags a gap. Sections are ordered Critical first.

**Tags.** Every point that implies a design decision carries the course tags: **[E]** supported by evidence, **[H]** hypothesis to test in your group, **[V]** value commitment. Two extra tags: **[Jurisdictional]** (depends on the law where you operate) and **[Context-dependent]** (depends on the market, platform or institution; not transferable without checking). The default vantage is a software or product organization operating in the US or EU with an English-speaking membership; where that matters, the tag says so.

**Verification note.** "verified" means the source's title, authors, venue and headline result were confirmed by web search on 2026-09-30. Full texts were not fetched (WebFetch was not relied on; search snippets only), so page-level details and secondary numbers are marked "background" where they come from memory rather than the snippet. A "background" figure is a lead to confirm, not a fact to quote in your brief. Where a number is invented to show a calculation, it says "illustrative arithmetic only".

---

## 1. Measurement: eliciting empirical and normative expectations in a real group — **Critical**

**Why it matters.** The course's central diagnostic (Bicchieri, `08-grammar-of-society`) is that a "norm" is a conditional preference held up by two beliefs, and that the lever depends on which beliefs are actually present. The book gives the theory; it does not give the instrument. Practitioners who skip measurement design the intervention for the norm they imagine (usually "people don't care") and miss the one that exists (usually "people care but think nobody else does"). The failure mode is a values campaign aimed at a pluralistic-ignorance problem, or a "show them everyone does it" message aimed at a group where nobody does.

**Things to know.**

1. **The toolkit exists and is short.** Bicchieri's *Norms in the Wild* (2017, verified) is the practitioner sequel to *The Grammar of Society*: chapters on diagnosing norms, measuring consensus and conformity, norm change, tools for change and trendsetters. Its core is a four-question battery per behavior: what do you do; what do most people in your reference group do (empirical expectation); what do most of them think you should do (normative expectation); what happens to someone who does not (sanction expectation). Ask all four; the diagnosis is in the *pattern* across them, not in any single answer. [E] that the four-way distinction predicts behavior in lab and field; [H] that the specific wording transfers to your group.
2. **Empirical expectations usually dominate normative ones when they conflict.** Bicchieri and Xiao (2009, *Journal of Behavioral Decision Making*, verified) manipulated dictators' beliefs and found that what others *do* predicted giving while what others *approve of* added nothing once the empirical belief was controlled. Design consequence: if your group's members privately approve of the cooperative act but believe others do not do it, publishing the approval data will not move them as much as publishing the behavior data. [E] in the lab; [H] for the size of the effect in your setting, and note that in field data the two expectations are usually highly correlated, so separating them needs a manipulation or a vignette, not a survey alone.
3. **Ask about the reference network, not "people in general".** A norm is held relative to the people whose expectations matter to the respondent. Before the battery, ask "whose opinion about this would you actually notice?" and let the answer define the population you measure. On a team this is often a sub-team or a senior pair, not the org. [E] that reference networks differ from formal groups (Bicchieri; Paluck's school work); [H] for who they are in your group.
4. **Use an incentivized coordination game to elicit normative expectations without asking people to confess.** Krupka and Weber (2013, *Journal of the European Economic Association*, verified) pay respondents for matching the *modal* rating of how socially appropriate an action is. Because people are guessing what others think, not reporting their own view, social-desirability bias falls, and the method recovers norms that predict behavior across dictator-game variants. In an organization the money can be a small prize or nothing; the structure ("guess what most colleagues would say") is what matters. [E] as a method; [H] that an unpaid version keeps its properties.
5. **Vignettes beat direct questions for sensitive behaviors.** Ask about a hypothetical third person in a concrete situation ("A reviewer approves a change they have not read because the author is senior. How would most people here react?") rather than about the respondent. Vary one feature across vignette versions (seniority, visibility, stakes) and you get a cheap factorial experiment on what activates the norm. [E] that vignette methods reduce misreporting (survey methodology; background); [H] for your wording.
6. **Norm perception is systematically biased, so measure the gap, not just the level.** Tankard and Paluck (2016, *Social Issues and Policy Review*, verified) review three sources of norm perception (individual behavior observed, summary information about the group, institutional signals) and show that perceived norms rarely match actual rates. The design-relevant number is the difference between what members think others do and what they actually do; when it is large, information alone is an intervention. [E]
7. **Descriptive-norm messaging can boomerang.** Schultz et al. (2007, *Psychological Science*, verified) showed that telling households their neighborhood average moved high users down and low users *up*; adding an injunctive signal (approval) removed the boomerang. Cialdini, Reno and Kallgren (1990, verified) showed that which norm is salient at the moment decides behavior. Never publish a descriptive statistic that some members are already beating without pairing it with approval. [E]
8. **Social referents move norms more than average members.** Paluck, Shepherd and Aronow (2016, *PNAS*, verified) randomized an anti-conflict program across 56 schools, trained a small set of students, and found effects were larger when the trained students were the ones peers actually attended to ("social referents" identified by network nomination). This is the field version of Bicchieri's trendsetter and Henrich's prestige model. Measure who is watched (a two-question sociometric survey: "who do you go to for advice", "whose behavior do you notice") before choosing whom to enlist. [E] at school scale; [H] in an organization.
9. **Instrument the observable behavior too.** Surveys measure beliefs; logs (commits, reviews, posts, attendance) measure the behavior the beliefs are about. Report both in the brief; a belief-behavior mismatch is diagnostic (pluralistic ignorance if behavior exceeds perceived behavior; a dead rule if the reverse). [H] as a practice rule.

**Questions to ask your behavioral scientist or people-analytics partner.**
- For the behavior in my brief, which of the four expectation questions did you ask, in what wording, and to which reference group?
- What is the perceived-versus-actual gap, and in which direction?
- Did you elicit normative expectations directly or via a coordination (Krupka–Weber) task, and why?
- What is the boomerang risk of the message you propose, and what injunctive signal accompanies it?
- Who are the social referents by nomination, and do they overlap with the org chart?

**Read next.**
- Bicchieri, *Norms in the Wild* (Oxford, 2017) — the measurement chapters; verified.
- Krupka & Weber, "Identifying social norms using coordination games" (JEEA 2013) — the elicitation protocol; verified.
- Tankard & Paluck, "Norm perception as a vehicle for social change" (SIPR 2016) — how to change perceived norms; verified.
- Paluck, Shepherd & Aronow, "Changing climates of conflict" (PNAS 2016) — the social-referent field experiment; verified.

**How it connects to the course.** Directly extends `08-grammar-of-society` (the four norm types, pluralistic ignorance, trendsetters); supplies the numbers `03-social-psychology` assumes when it says descriptive and injunctive norms must point the same way; feeds the diagnostic in `11-bounds-of-reason` (the epistemic half of the two-part norm test). The brief's diagnosis sections should not be written without at least one measured expectation.

---

## 2. Sanctioning design in practice: graduated, restorative, anti-social — **Critical**

**Why it matters.** Every Order-level source endorses sanctions (Ostrom's principle 5, Camerer's costly punishment, Gintis's strong reciprocity, Dixit's subgame-perfect threats). None tells you who should sanction, through what channel, at what cost, or what happens when punishment turns on cooperators. The failure mode is a peer-punishment feature that gets used by the wrong people against the wrong targets, a sanction so costly nobody applies it, or a fine that converts a norm into a price.

**Things to know.**

1. **Anti-social punishment is real, large and predictable.** Herrmann, Thöni and Gächter (2008, *Science*, verified) ran public-goods games with punishment in 16 participant pools worldwide; in several, high contributors were punished as much as low contributors, and where that happened punishment failed to raise cooperation at all. Weak civic norms and weak rule of law predicted anti-social punishment. Do not assume your members will only punish free-riders; measure it (section 1) or observe a pilot. [E] cross-societal; [H] for your group's position on that distribution. [Context-dependent]
2. **Punishment works, rewards work about as well, and both work better when costly and repeated.** Balliet, Mulder and Van Lange's meta-analysis (2011, *Psychological Bulletin*, verified) pooled 187 effect sizes: rewards d ≈ 0.51 and punishments d ≈ 0.70 on cooperation, statistically equivalent; effects were larger when the incentive was costly to administer and when groups stayed together across rounds; centralized versus peer administration did not change the average effect. Design consequence: cheap, automatic sanctions (a bot warning) are weaker per use than a visible costly one (a person taking time to object), and sanctions in a rotating-membership group underperform. [E]
3. **People choose sanctioning institutions when allowed to, after initial aversion.** Gürerk, Irlenbusch and Rockenbach (2006, *Science*, verified) let players migrate between a sanctioning and a sanction-free institution; the sanctioning one won the whole population. A 2023 multi-lab replication (PNAS Nexus, verified as existing; result details background) revisited the finding — check it before quoting the original as settled. The design point survives: offer the sanctioning regime as opt-in with visible results rather than imposing it. [E] with a replication caveat.
4. **Fines can turn a norm into a price.** Gneezy and Rustichini (2000, *Journal of Legal Studies*, verified): a fine for late pickup at day-care centers *increased* lateness and the effect persisted after removal. Frey and Jegen (2001, *Journal of Economic Surveys*, verified) review motivation crowding-out and crowding-in. A monetary or point-based penalty tells members the behavior is purchasable and that the relationship is contractual. Prefer reputational and relational sanctions for norm violations; reserve prices for genuinely priced resources. [E] that crowding-out occurs; [H] for whether it happens in your group (crowding-in also occurs when the sanction signals respect for the norm).
5. **Graduated means a ladder with rungs someone will actually climb.** Braithwaite's regulatory pyramid (*Restorative Justice and Responsive Regulation*, 2002, verified) puts dialogue and restoration at the wide base, deterrence in the middle, and incapacitation (removal) at the apex, escalating only after the lower rung fails repeatedly. The empirical claim is that this deters and rehabilitates better than starting punitive. Write the ladder into the brief: rung 1 private note, rung 2 public note, rung 3 temporary loss of a privilege, rung 4 removal, with the trigger for each. [E] for the policy literature; [H] for your ladder. [Jurisdictional] where sanctions touch employment or platform-terms law.
6. **Who sanctions is a legitimacy question, not only an efficiency one.** Baldassarri and Grossman (2011, *PNAS*, verified), lab-in-the-field with 1,543 Ugandan cooperative farmers in 50 cooperatives: a randomly appointed monitor with sanctioning power raised cooperation; an *elected* monitor raised it further and more durably. Section 3 expands this. Give the sanctioner a source of authority members recognize. [E]
7. **Under noise, decentralized punishment hits innocents.** With imperfect observation (a reviewer who missed a bug versus one who skipped the review), peer punishment misfires and provokes counter-punishment feuds; this is the multi-player version of tit-for-tat's fragility (`04-games-of-strategy`). Centralizing sanction power reduces perverse punishment but does not by itself raise cooperation (background: lab studies on monopolized sanctioning under noise). Pair any peer-sanction channel with a cheap appeal (Ostrom's principle 6). [E] mechanism; [H] magnitude.
8. **Explanation is itself a sanction design variable.** Jhaver, Bruckman and Gilbert (2019, CSCW, verified) analyzed 32 million Reddit posts and found that when a removal came with an explanation, the odds of the same user's future posts being removed fell. A sanction that teaches beats one that only costs. [E] observational at platform scale; [H] causally.
9. **Cultural tightness sets the baseline tolerance for sanctioning.** Gelfand et al. (2011, *Science*, verified) measured tightness-looseness across 33 nations; tight cultures have strong norms and low deviance tolerance. Multinational teams and global communities contain both; the same public reprimand reads as proportionate in one subgroup and as humiliation in another. [E] cross-national; [H] for your mix. [Context-dependent]

**Questions to ask your community-ops lead, HR partner or lawyer.**
- Who can sanction whom, at what cost to themselves, and what stops a sanction being used to settle a personal score?
- What does the ladder look like, and how many members have climbed each rung in the last quarter?
- Is any sanction monetary or point-denominated, and what is the crowding-out risk?
- What does a sanctioned member see: the rule, the evidence, the explanation, the appeal?
- [Jurisdictional] Which sanctions in this ladder require documentation, warning periods or process under local employment or consumer law?

**Read next.**
- Herrmann, Thöni & Gächter, "Antisocial punishment across societies" (Science 2008) — the one paper on this list every designer should read; verified.
- Balliet, Mulder & Van Lange, "Reward, punishment, and cooperation: a meta-analysis" (Psych. Bulletin 2011); verified.
- Braithwaite, *Restorative Justice and Responsive Regulation* (OUP 2002) — chapter on the pyramid; verified.
- Gneezy & Rustichini, "A fine is a price" (J. Legal Studies 2000); verified.

**How it connects to the course.** Refines `09-governing-the-commons` (principle 5 and the "nuclear first strike" warning), `06-behavioral-game-theory` (costly punishment as a social preference), `11-bounds-of-reason` ("budget for legitimate punishment") and `01-secret-of-our-success` (norm psychology is content-neutral, so the sanctioning disposition needs channeling). It supplies the tension the books gesture at but do not resolve: sanctions are necessary and dangerous.

---

## 3. Legitimacy, procedural justice and leadership — **Critical**

**Why it matters.** The sources model compliance as a function of payoffs, expectations and sanctions. A large empirical literature says people also comply because they judge the *process* fair and the authority legitimate, largely independent of outcomes. A designer who ignores this builds rules that are followed only while enforced (Ostrom's imposed-rule failure) and misattributes the resulting decay to incentives. The failure mode is a technically sound rule announced by the wrong person in the wrong way.

**Things to know.**

1. **Legitimacy predicts compliance better than deterrence.** Tyler, *Why People Obey the Law* (1990; 2006 edition with new afterword, verified) found in a Chicago panel that people comply with law primarily because they see the authority as legitimate, and that legitimacy is driven by perceived procedural fairness more than by favorable outcomes. The afterword reports subsequent replications and refinements. [E] in the legal domain; [H] that it transfers to a team's rules with the same weights (organizational-justice research suggests it does; background).
2. **Procedural justice has four components you can operationalize.** Voice (people are heard before a decision), neutrality (rules applied consistently and explained), respect (dignity in treatment), and trustworthy motives (the decision-maker is seen to care about members' welfare). Each maps to a design choice: a comment period, a published rule with reasons, a tone standard for sanctions, and visible costs borne by the leadership. [E] that these dimensions carry the effect (Tyler and successors; background for the specific four-factor structure).
3. **Election confers legitimacy that appointment does not, even with identical powers.** Baldassarri and Grossman (2011, verified; details in section 2) is the cleanest causal evidence: same sanctioning power, elected monitor, more cooperation. For a team this can mean a rotating role chosen by the team rather than assigned; for a community, elected moderators. [E]
4. **Rules members made are followed more.** This is Ostrom's principle 3 (`09-governing-the-commons`) and it is corroborated in online communities (Fiesler et al. 2018, verified, on 100,000 subreddits, citing Ostrom on self-made rules). The design cost is time; the benefit is that enforcement becomes by-product monitoring rather than policing. [E]
5. **Legitimacy is transferable and losable.** External recognition (Ostrom's principle 7) is the institution-level version: a team's rule that management can override on appeal is not the team's rule. Write into the brief who has explicitly ceded authority over the domain and in what form. [E] that missing recognition predicts fragility (Ostrom); [H] for your case.
6. **Leaders' CREDs decide which norm transmits.** Henrich's credibility-enhancing displays (`01-secret-of-our-success`) apply to leaders: one visible exception by the leader outweighs many statements. The procedural-justice literature adds that the exception also damages the trustworthy-motives component. Make the leader's own compliance the most visible compliance in the group. [E] for CREDs; [H] for magnitude.
7. **Transparency of moderation decisions raises subsequent compliance.** Jhaver et al. (2019, verified; section 2) is the platform evidence. The mechanism is procedural-justice: an explained removal reads as neutral, an unexplained one as arbitrary. [E] observational.

**Questions to ask your leadership coach, HR partner or governance lead.**
- Who decided the rule, who was consulted, and can members show where their input changed it?
- What is the written reason attached to each sanction or allocation decision?
- Is the sanctioner elected, appointed or self-appointed, and does the group know which?
- What is the leadership's most visible recent compliance with the rule, and its most visible exception?
- What would members say if asked "does the person deciding this care what happens to you?"

**Read next.**
- Tyler, *Why People Obey the Law* (Princeton, 2006 ed.) — chapters 1–4 and the afterword; verified.
- Baldassarri & Grossman, "Centralized sanctioning and legitimate authority promote cooperation in humans" (PNAS 2011); verified.
- Fiesler et al., "Reddit rules! Characterizing an ecosystem of governance" (ICWSM 2018); verified.

**How it connects to the course.** Supplies the missing "why do imposed rules fail" mechanism behind Ostrom's principles 3 and 7; extends Henrich's prestige/dominance and CRED ideas to formal authority; gives `11-bounds-of-reason`'s "choreographer" a source of authority. The brief's institutions section should state, for every rule, its legitimacy source.

---

## 4. Trust, reputation and identity systems — **Critical for platforms and communities; Important otherwise**

**Why it matters.** The course explains why reputation sustains cooperation (indirect reciprocity, the shadow of the future, Ostrom's monitoring). It does not explain how to build a reputation system that carries real information, resists inflation and gaming, and does not itself destroy the cooperation it is meant to protect. The failure mode is a five-star system where everyone has 4.9 stars, a karma score that rewards volume, or an identity layer that lets a bad actor return under a new name.

**Things to know.**

1. **Feedback is provided voluntarily but is inflated.** Resnick and Zeckhauser (2002, verified) analyzed 1999 eBay data: feedback was left more than half the time despite the free-rider incentive not to, was almost always positive, and profiles did predict future performance, but eBay's displayed net score was a poor predictor compared with what was available. A reputation system's first design question is whether its displayed statistic preserves the information the raw data contains. [E]
2. **Reciprocity and retaliation corrupt two-sided ratings.** Fradkin, Grewal and Holtz (2021, *Marketing Science*, verified) ran an Airbnb experiment hiding each review until both parties submitted (simultaneous reveal): more reviews were written, retaliation and reciprocation fell, ratings became lower and more honest, but adverse selection on the platform did not measurably fall. Two lessons: unveiling design matters for information quality; better information does not automatically change who transacts. [E]
3. **Reputation systems have known limits and known repairs.** Tadelis (2016, *Annual Review of Economics*, verified) surveys the biases (positive inflation, fear of retaliation, selection into who reviews) and repairs (simultaneous reveal, prompting all users, using non-review signals such as disputes). Nosko and Tadelis (NBER 2015, verified) show that eBay's realized buyer experience was much worse than displayed ratings implied and that a hidden quality score improved outcomes. Do not equate displayed reputation with quality. [E]
4. **Dellarocas's framing still holds.** "The digitization of word of mouth" (2003, *Management Science*, verified) sets out why online feedback differs from village gossip: scale, anonymity, ease of entry, strategic manipulation. The village mechanisms in Ostrom's cases assume repeat interaction among known people; a platform must manufacture that with identity persistence and history. [E]
5. **Identity persistence is the load-bearing feature.** Cheap pseudonym re-entry ("whitewashing") lets a defector reset reputation, which collapses the shadow of the future (`04-games-of-strategy`). Countermeasures: entry costs (verification, waiting periods, probation), reputation that starts below neutral, and Sybil resistance for anything with votes or matching funds (Gitcoin's collusion problems and its responses — pairwise matching, Passport-based Sybil resistance — verified as existing; efficacy background). [E] for the mechanism; [H] for the right entry cost in your community.
6. **Reputation must be scoped to the behavior it is meant to predict.** A single global score aggregates unlike things (helpfulness, reliability, taste) and invites volume gaming. Karma-style points reward activity, which is not cooperation. Prefer several narrow, verifiable signals (on-time rate, review acceptance rate, dispute rate) to one number. [H] as a design rule; [E] that single aggregate scores lose predictive power (Resnick & Zeckhauser).
7. **Reputation is a sanction and inherits section 2's problems.** A public score enables anti-social punishment (down-voting the competent) and retaliation; a private score to the platform enables opacity and procedural-justice failures. Decide which failure you prefer and mitigate it. [V] on the trade-off; [E] on both failure modes.
8. **In a team, the "reputation system" is gossip, and it is already running.** It is fast, informal and biased toward the visible. The design question is what work is visible (`02-darwins-unfinished-symphony`: make the best behavior visible) rather than whether to add a score. Introducing explicit peer scores into a communal team risks the market-framing damage noted in `03-social-psychology`. [H]

**Questions to ask your trust-and-safety or marketplace engineer.**
- What does the displayed reputation statistic predict, measured against realized outcomes (disputes, churn, complaints)?
- What is the review-completion rate, the share of ratings at the top of the scale, and the reveal timing?
- How much does it cost to abandon an identity and start again, and what is the evidence on whitewashing?
- Is any part of reputation a single aggregate score, and what volume behavior does it reward?
- What is the dispute path, and how long does it take?

**Read next.**
- Tadelis, "Reputation and feedback systems in online platform markets" (Annual Review of Economics 2016) — the survey; verified.
- Resnick & Zeckhauser, "Trust among strangers in Internet transactions" (2002); verified.
- Fradkin, Grewal & Holtz, "Reciprocity and unveiling in two-sided reputation systems" (Marketing Science 2021); verified.
- Dellarocas, "The digitization of word of mouth" (Management Science 2003); verified.

**How it connects to the course.** Operationalizes indirect reciprocity (section 9), the shadow of the future (`04-games-of-strategy`), Ostrom's monitoring and conflict-resolution principles, and the PageRank-style "deference from structure" note in `10-networks-crowds-markets`. The brief's incentives section should say what reputation signal exists, what it predicts, and how it can be gamed.

---

## 5. Mechanism design and incentive engineering in practice — **Important**

**Why it matters.** `04-games-of-strategy` teaches the theory of mechanisms (Vickrey, median voter, incentive contracts) and `10-networks-crowds-markets` says "institutions are edits to the game". Neither teaches what practitioners learn the first time they ship an incentive: the mechanism you deploy is not the mechanism you designed, because participants find the seams, metrics displace unmeasured effort, and prices crowd out norms. The failure mode is a points, bounty or token scheme that produces the metric and kills the behavior.

**Things to know.**

1. **Design economics is engineering, not theorem-proving.** Roth (2002, *Econometrica*, "The economist as engineer", verified) argues from the medical residency match and spectrum auctions that theory, lab experiments and computation are complements: the theory gives the shape, the experiment finds the failure modes, the simulation checks scale. Roth's *Who Gets What and Why* (2015, verified) is the accessible version. Treat any incentive in your brief as a prototype with a test plan, not a rule. [E] as a methodology; [V] that the effort is worth it for small groups.
2. **The three recurring failures: congestion, unraveling, unsafe participation.** Roth's diagnosis of markets applies to internal mechanisms: too many options to evaluate (congestion, e.g. review queues), people acting early to lock in (unraveling, e.g. grabbing tasks before triage), and participants who will not reveal true preferences because doing so is punished (unsafe, e.g. honest estimates penalized). Ask which one your process has. [E] for markets; [H] for internal processes.
3. **Goodhart and multitasking are not folklore.** The Holmström–Milgrom multitask result in `04-games-of-strategy` implies that rewarding the measurable dimension pulls effort from unmeasured ones; the field evidence (teacher test-score incentives, sales quotas; background) is consistent. Rule for the brief: if a behavior has an unmeasured quality dimension, do not attach a strong incentive to the measured one; use norms and reputation instead. [E] theory; [H] magnitude.
4. **Coin-voting governance is a cautionary case, not a model.** Buterin's 2021 essay "Moving beyond coin voting governance" (verified) lists the acknowledged failures: vote-buying, whale capture, low turnout, treasury politics; DAOs in practice have converged on multisigs, delegates and councils, which are Ostrom's nested layers re-invented. Quadratic funding's collusion vulnerability (two accounts of one person donating to each other; verified via Gitcoin's own documentation) shows that any mechanism whose guarantees assume one-person-one-identity fails without Sybil resistance (section 4). [E] descriptive; [V] on whether token governance is worth the complexity. [Jurisdictional] token-based incentives may be securities.
5. **Ostrom's principles have been checked against many cases, and reformulated.** Cox, Arnold and Villamayor Tomás (2010, *Ecology and Society*, verified) reviewed 91 studies and found the principles well supported, splitting three of them (boundaries into user and resource boundaries; congruence into local-conditions fit and proportionality; monitoring into monitors' presence and their accountability). Use the 11-item version as the checklist in the brief. [E]
6. **The principles transfer to online commons with observable adaptations.** Frey and Sumner (2019, *PLOS ONE*, verified) analyzed about 5,000 self-governing Minecraft servers and found that governance complexity and integration grew with community size, and that larger communities relied on more, and more integrated, rule types. Fiesler et al. (2018) found the same rule-ecosystem pattern on Reddit. Online groups do reinvent Ostrom, imperfectly and with more emphasis on entry and exclusion than on monitoring. [E] observational.
7. **Every mechanism has an attack surface; enumerate it before launch.** Borrow the security habit: for each rule, ask who benefits from gaming it, what the cheapest game is, and what the detection signal would be. A mechanism with no listed attacks has not been reviewed. [H] as a practice; [E] that unreviewed mechanisms get gamed (the DAO and reputation-system record).
8. **Small groups can use simple honest-revelation devices.** Sealed simultaneous estimates before discussion (`10-networks-crowds-markets`, cascades), "I cut, you choose" for splits, lotteries for unequal allocations (`06-behavioral-game-theory`), approval voting for multi-option choices (`04-games-of-strategy`). These are the mechanisms worth writing into a team brief; auctions and tokens usually are not. [E]

**Questions to ask your economist or platform-strategy lead.**
- What is the test plan for this incentive: pilot population, duration, metric, and the unmeasured dimension we will watch for displacement?
- Which of congestion, unraveling and unsafe participation does the current process exhibit?
- What does the cheapest attack on this mechanism look like and what would we see if it happened?
- What is the identity assumption (one person, one account) and what enforces it?
- [Jurisdictional] Does any incentive, token or reward create tax, employment-status or securities exposure?

**Read next.**
- Roth, "The economist as engineer" (Econometrica 2002); verified. Or *Who Gets What and Why* (2015) for the narrative; verified.
- Cox, Arnold & Villamayor Tomás, "A review of design principles for community-based natural resource management" (Ecology and Society 2010); verified.
- Buterin, "Moving beyond coin voting governance" (2021 blog essay); verified.
- Frey & Sumner, "Emergence of integrated institutions in a large population of self-governing communities" (PLOS ONE 2019); verified.

**How it connects to the course.** The applied layer over `04-games-of-strategy` Part Four and `09-governing-the-commons`; the crowding-out and Goodhart points are the practical content of `11-bounds-of-reason`'s "prefer the norm". The brief's incentives section should carry a test plan and an attack list for every mechanism.

---

## 6. Online community governance, moderation and polarization — **Important; Critical if the brief's group is a community or platform**

**Why it matters.** The Order-level sources are about pastures, fisheries and lab groups. Online communities differ in scale, anonymity, exit cost, tooling and law, and there is now a substantial empirical literature on what works. The failure mode is applying Ostrom's village recipe to a 100,000-member forum without the moderation, onboarding and information-architecture layers that make it work, or fighting polarization with a remedy (exposure to the other side) that the evidence says can backfire.

**Things to know.**

1. **Moderation has a small vocabulary.** Grimmelmann, "The virtues of moderation" (2015, *Yale J. of Law and Technology*, verified) taxonomizes moderation as four verbs (exclude, price, organize, norm-set) applied ex ante or ex post, by humans or by software, with case studies of MetaFilter, Reddit, Wikipedia and the LA Times wikitorial. Use the grid to describe your community's current moderation before changing it; most communities over-rely on one cell (ex-post human exclusion). [E] as a framework.
2. **The evidence-based design manual exists.** Kraut and Resnick, *Building Successful Online Communities: Evidence-Based Social Design* (MIT Press 2012, verified) converts social-science findings into design claims on contribution, commitment, newcomer socialization, regulation of behavior and starting a community. It is the closest thing to a textbook for the community and platform variants of the brief. [E]
3. **Posting the rules where people act changes behavior.** Matias (2019, *PNAS*, verified) randomized a pinned rules reminder across 2,190 r/science threads: newcomers' comments were more likely to comply (about 8 percentage points, verified from snippet) and first-time commenters were substantially more likely to participate (about 70% relative increase, verified from snippet). Cheap salience beats distant policy pages, exactly as `08-grammar-of-society` predicts (cues activate norms). [E]
4. **Quality control that scales can kill newcomer retention.** Halfaker, Geiger, Morgan and Riedl (2013, *American Behavioral Scientist*, verified) showed that Wikipedia's response to 2005-era growth (automated reverts, more rules) raised the share of good-faith newcomers whose first edits were reverted and drove the long editor decline. The by-product-monitoring principle has a dark side at scale: automated monitoring treats newcomers as attackers. Track first-session rejection rate of good-faith newcomers as a health metric. [E] observational, well-replicated within Wikipedia research.
5. **Explanations reduce repeat violations** (Jhaver et al. 2019; sections 2 and 3). Make removal explanations a default in tooling, not a moderator's optional effort. [E]
6. **Governance tooling is the missing layer.** Schneider et al., "Modular politics" (2021, verified) argue that platforms default to "implicit feudalism" (one admin, arbitrary power) because their software offers nothing else; Schneider's *Governable Spaces* (2024, verified) develops the argument. Frey and Schneider's "effective voice" (2021, verified) defines the property to design for: member speech that has a binding effect through a transparent process. Check whether your platform's admin model even permits Ostrom's principle 3. [E] descriptive; [V] that democratic tooling is worth its cost.
7. **Exposure to the other side can increase polarization.** Bail et al. (2018, *PNAS*, verified) paid Twitter users to follow a bot posting opposing-party content for a month; Republicans became measurably more conservative, Democrats slightly more liberal (not significant). Do not prescribe "mix the feeds" as a polarization fix without a test. [E] one large field experiment; [H] generality.
8. **Echo chambers depend on platform mechanics.** Cinelli et al. (2021, *PNAS*, verified), on more than 100 million items across Gab, Facebook, Reddit and Twitter, found homophilic clustering dominates on Facebook and Twitter but is largely absent on Reddit, where users control feed algorithms. Structure (`10-networks-crowds-markets`, homophily; `05-micromotives-and-macrobehavior`, sorting) is a design variable, not a fact of nature. [E] observational.
9. **Law sets the outer boundary.** Grimmelmann's paper discusses Section 230 and DMCA 512 immunities; the EU Digital Services Act imposes notice, statement-of-reasons and appeal duties on platforms of size (background). Any community brief for a platform needs a legal review of its moderation ladder. [Jurisdictional]

**Questions to ask your community-ops or trust-and-safety lead.**
- Which cells of the Grimmelmann grid does our moderation occupy, and which are empty?
- What is the first-session rejection rate of good-faith newcomers, and how has it moved?
- Where are the rules displayed at the moment of action?
- Do members have effective voice — a process by which their input binds — or only exit and affect?
- [Jurisdictional] Which of our removals require a statement of reasons and an appeal path by law?

**Read next.**
- Kraut & Resnick, *Building Successful Online Communities* (MIT Press 2012) — chapters on regulation and newcomers; verified.
- Grimmelmann, "The virtues of moderation" (Yale JOLT 2015); verified.
- Halfaker et al., "The rise and decline of an open collaboration system" (ABS 2013); verified.
- Matias, "Preventing harassment and increasing group participation through social norms in 2,190 online science discussions" (PNAS 2019); verified.

**How it connects to the course.** The platform-scale test of `09-governing-the-commons` (retrieval question 7 in that file is this section in miniature), `08-grammar-of-society` (cues), `10-networks-crowds-markets` (homophily, cascades, strong ties) and `05-micromotives-and-macrobehavior` (sorting). The brief's network-structure section should say which contagions are simple and which are complex, and where the wide bridges are.

---

## 7. Team culture: psychological safety and team size — **Important; Critical if the brief's group is a team**

**Why it matters.** The course explains cooperation between members with given preferences and beliefs; it says nothing about the organizational-behavior literature on what makes a work team speak up, admit error and learn, nor about the well-replicated effects of headcount on effort and coordination. This is management knowledge, not game theory; nothing in the sources helps except by analogy. The failure mode is a brief that engineers incentives for a team whose real problem is that nobody will say the plan is wrong.

**Things to know.**

1. **Psychological safety is a group-level belief with a specific definition.** Edmondson (1999, *Administrative Science Quarterly*, verified) studied 51 teams in one manufacturing firm and defined team psychological safety as a shared belief that interpersonal risk-taking (questions, error admission, dissent) is safe. Her earlier hospital finding: better-led teams *reported* more medication errors, because they admitted them. Design consequence: error counts rise when safety improves; do not read that as decline. [E]
2. **The meta-analytic effects are moderate and real.** Frazier et al. (2017, *Personnel Psychology*, verified): 136 samples, over 22,000 individuals and nearly 5,000 groups; psychological safety associates strongly with engagement, satisfaction and commitment, moderately with task performance and citizenship behavior; leadership behavior and supportive context are the main antecedents. It is not a magic variable; it is a moderate, robust one. [E]
3. **Safety is the precondition for the course's norm machinery.** Bicchieri's "relevant discussion" and Camerer's "leader names the target equilibrium" both assume members will say what they expect. Without safety, elicitation (section 1) returns what people think the leader wants. Measure safety first (Edmondson's seven-item scale; background for the exact items). [E] for the scale; [H] for the sequencing claim.
4. **Team size has a well-documented cost curve.** Steiner's process-loss framework (1972; verified as the origin), Hackman's guidance (*Leading Teams*, 2002; four to six members ideal, not above ten; verified from secondary sources) and Mueller's relational-loss finding (2012; larger teams lower perceived support and thereby individual performance; verified from secondary source) converge: per-member effort and coordination decay with size, and the decay is driven by identifiability (`03-social-psychology`, loafing), coordination links and perceived support. Amazon's "two-pizza" rule is the same claim as folklore, not evidence. [E] for the direction; [H] for the exact threshold in your team.
5. **Weak-link tasks are the worst case for size.** Camerer's minimum-effort results (`06-behavioral-game-theory`): pairs reach the best equilibrium, groups of 14–16 collapse. For any process whose output is the minimum (release readiness, on-call), the size of the group whose minimum matters is the design variable. [E]
6. **Safety and accountability are orthogonal, not opposed.** Edmondson's later framework (*The Fearless Organization*, 2018, verified) crosses safety with performance standards: high-high is the learning zone. The course's sanctions (section 2) live on the standards axis; a graduated ladder applied with procedural justice (section 3) does not lower safety. [E] framework; [H] in practice.
7. **Stable membership is a precondition for almost everything else.** Ostrom's situational variable (small stable groups), Dixit's shadow of the future and Balliet's "same group across rounds" moderator all say the same thing: rotation and churn are the enemy. Put a tenure or stability target in the brief. [E]

**Questions to ask your engineering manager or organizational psychologist.**
- What is the team's psychological-safety score, by whom measured, and what did the leader do with it?
- How many people are in the group whose minimum effort determines the outcome?
- What is annual membership churn on this team, and what is the rate at which newcomers join?
- What happens, concretely, to the last person who reported a mistake?

**Read next.**
- Edmondson, "Psychological safety and learning behavior in work teams" (ASQ 1999); verified.
- Frazier et al., "Psychological safety: a meta-analytic review and extension" (Personnel Psychology 2017); verified.
- Hackman, *Leading Teams* (HBS Press 2002) — the chapter on team design; verified as a title, size guidance from secondary sources.

**How it connects to the course.** Supplies the organizational preconditions for `03-social-psychology` (dissent, loafing, groupthink), `06-behavioral-game-theory` (weak-link size effects) and `08-grammar-of-society` (relevant discussion). The brief for a team should include a safety measurement and a size decision before any incentive.

---

## 8. Scaling: from small groups to large, nested and polycentric — **Important**

**Why it matters.** Almost every mechanism in the course is demonstrated at the scale of a lab group, a village or a team. The brief's group may be, or become, much larger. What breaks with size is by-product monitoring, reputation memory, common knowledge and the stag-hunt basin; what replaces them is nesting. The failure mode is a community that worked at 40 members and was governed the same way at 4,000.

**Things to know.**

1. **Dunbar's number is a contested estimate, not a constant.** Dunbar's 150 (*How Many Friends Does One Person Need?*, 2010, verified) rests on a primate brain-size regression. Lindenfors, Wartel and Lind (2021, *Biology Letters*, verified) reran it with modern phylogenetic methods and found point estimates from about 16 to 109 depending on method, with 95% intervals of roughly 4–520; they conclude no single number is defensible. Bernard and Killworth's independent estimates of personal network size average about 290 (median about 231; verified). Design consequence: do not set a governance threshold at 150 because of Dunbar; set it where your monitoring actually stops working, which you can measure. [E] on the contestation; [H] for your threshold.
2. **Polycentricity is Ostrom's answer to scale.** Ostrom's Nobel lecture (2010, *American Economic Review*, verified) argues for multiple overlapping decision centers rather than one center or pure decentralization. Principle 8 (nested enterprises) is the structural form: sub-units handle local rules, higher layers handle inter-unit conflict and shared infrastructure. Cox et al. (2010) found the principle supported in the multi-scale cases. [E]
3. **Online communities nest spontaneously and imperfectly.** Frey and Sumner (2019) found rule complexity and integration growing with server size; Reddit's subreddit structure is polycentricity with weak upper layers; Wikipedia built WikiProjects, arbitration and policy layers as it grew (Halfaker et al. 2013 shows the cost). The pattern is that lower layers form fast and upper layers (conflict resolution across units) lag, which is where growth crises appear. [E] descriptive; [H] for your community's lagging layer.
4. **Structure can substitute for size-limited monitoring.** Rand, Nowak, Fowler and Christakis (2014, *PNAS*, verified) showed experimentally that fixed network structure with few neighbors relative to the benefit-cost ratio sustains cooperation where well-mixed or shuffled populations decay. This is Skyrms's correlation result (`07-stag-hunt`) with human subjects: keep interaction local and stable as the group grows, rather than pooling everyone. [E]
5. **Growth rate is a design variable, and so is who arrives.** Weber's (2006) gradual-growth result in `06-behavioral-game-theory` (grow from a small successful core) and Halfaker's newcomer-rejection finding bracket the problem: too fast and the norm cannot be transmitted; too defensive and newcomers are rejected. Set an onboarding capacity (how many newcomers per experienced member per period) and treat it as a constraint. [H]

**Questions to ask your community-ops lead or organizational designer.**
- At what size did by-product monitoring stop catching violations here, and what replaced it?
- What is the upper governance layer for conflicts between sub-units, and how many cases has it handled?
- What is the newcomer-to-veteran ratio per period, and is it capped?
- Which processes aggregate by minimum, which by sum, and which by average?

**Read next.**
- Ostrom, "Beyond markets and states: polycentric governance of complex economic systems" (AER 2010); verified.
- Lindenfors, Wartel & Lind, "'Dunbar's number' deconstructed" (Biology Letters 2021); verified.
- Rand, Nowak, Fowler & Christakis, "Static network structure can stabilize human cooperation" (PNAS 2014); verified.

**How it connects to the course.** The scale limits of `09-governing-the-commons` (principle 8, situational variables), `07-stag-hunt` (correlation and location), `10-networks-crowds-markets` (small worlds, clusters) and `01-secret-of-our-success` (collective brain grows with connectivity, which cuts the other way). The brief should state the group's size, its projected size, and the layer that appears when the first breaks.

---

## 9. The evolution-of-cooperation classics the list assumes — **Useful**

**Why it matters.** Skyrms, Gintis, Henrich and Dixit all argue *with* Axelrod's tournaments, Nowak's mechanisms and indirect reciprocity, and treat them as known. A learner without them will misread "tit-for-tat" as a strategy recommendation and "reputation" as a synonym for gossip. This section is a 30-minute background fill, not a gap in the design sense; the design content is already in the books.

**Things to know.**

1. **Axelrod's tournaments (1984, verified) are a demonstration, not a proof.** Two computer tournaments of the iterated prisoner's dilemma were won by Rapoport's tit-for-tat; Axelrod attributed success to being nice, retaliatory, forgiving and clear. Later work (and a 2025 reproduction of the second tournament, verified as a preprint) shows the result depends on the field of entrants and on noise; `04-games-of-strategy` already carries the "fragile under noise, generous variants do better" caveat. Carry the four properties, not the rule. [E]
2. **Nowak's five mechanisms are the organizing map.** Kin selection, direct reciprocity, indirect reciprocity, network (spatial) reciprocity and group selection (Nowak 2006; Rand & Nowak 2013, *Trends in Cognitive Sciences*, verified). Each is a reason for cooperators to interact with cooperators more than chance, which is Skyrms's correlation thesis in `07-stag-hunt`. For a design brief, the question "which mechanism is my group's cooperation running on?" is the same as "what would break it?" [E]
3. **Indirect reciprocity is the mechanism reputation systems implement.** Nowak and Sigmund (2005, *Nature*, verified): "I help you and somebody else helps me" works when reputations are tracked and the assessment rule is stable; it demands increasing cognitive load (and, online, infrastructure). Section 4 is the applied version. [E]
4. **Kollock's taxonomy is a compact bridge to design.** Kollock (1998, *Annual Review of Sociology*, verified) sorts solutions to social dilemmas into motivational (change preferences), strategic (repeated play, reciprocity) and structural (change the rules). The course's three levels map onto it, and it is a good one-page checklist for the brief: for each proposed fix, which of the three is it? [E] as a framework.

**Read next.**
- Rand & Nowak, "Human cooperation" (TICS 2013) — the review; verified.
- Nowak & Sigmund, "Evolution of indirect reciprocity" (Nature 2005); verified.
- Kollock, "Social dilemmas: the anatomy of cooperation" (ARS 1998); verified.

**How it connects to the course.** Background to `07-stag-hunt`, `11-bounds-of-reason`, `01-secret-of-our-success` and `04-games-of-strategy` ch 10–11. No new brief section; a vocabulary check.

---

## 10. Ethics and consent in engineering norms — **Important** (value-heavy)

**Why it matters.** Everything above is a technology for changing what people believe others do and approve of, and for making them comply. The course requires every decision to carry an [E]/[H]/[V] tag, and the [V] tags are hollow if the designer has not thought about manipulation, consent, and who bears the costs. The failure mode is a norm intervention that works, is discovered, and destroys the trust it depended on; or one that succeeds in making people comply with something they would have rejected if asked.

**Things to know.**

1. **The nudge debate supplies the vocabulary.** Thaler and Sunstein (*Nudge*, 2008, verified) defend choice architecture with a transparency principle: the means and intent should be recognizable. Bovens ("The ethics of nudge", 2009 in an edited volume; verified as existing, year background) asks whether nudges change preferences, build character, and what constraints apply. Hansen and Jespersen (2013, *European Journal of Risk Regulation*, verified) classify nudges by whether they engage reflective or automatic processing and whether they are epistemically transparent; the automatic-and-opaque quadrant is where manipulation lives. Classify each of your brief's interventions on that grid. [V] on the standard; [E] that the grid is the accepted framing.
2. **Most norm interventions in this course are transparent by construction, if you let them be.** Publishing measured expectations, holding relevant discussion, posting rules at the point of action, electing monitors — all are reflective and visible. The ones to worry about are cue engineering (`08-grammar-of-society`'s implications: "design the cues"), default-setting and seeded first rounds, which work partly because they are not noticed. [V]
3. **Transparency does not necessarily reduce effectiveness.** A review of empirical studies on transparent nudging (Cambridge, 2024, verified as existing) finds that disclosed nudges generally retain their effect. The practical rule "tell them, it still works" is [E] for defaults and reminders; [H] for social-norm messages, where disclosure may change the inference members draw.
4. **Consent has a collective form.** Ostrom's principle 3 (those bound by rules can change them) is the institutional consent mechanism, and it is what separates norm design from norm imposition. If the brief's rules were made without the members, the ethics question is answered already. [V]
5. **Sanctions and reputation redistribute harm.** Public sanctions, visible scores and social-referent campaigns concentrate costs on identifiable people. Section 2, point 1 (anti-social punishment) means the costs may fall on the cooperative. Include in the brief who bears the cost of each mechanism when it misfires. [V] on the obligation; [E] that misfires happen.
6. **Experimentation on members needs a stated standard.** Bond et al. (2012), Matias (2019) and Fradkin et al. (2021) are all experiments on people who did not individually consent; the Facebook emotional-contagion controversy (2014; background) shows the reputational cost of getting this wrong. If the brief includes A/B tests on norms, state the review process, the opt-out and the debrief. [V] [Jurisdictional] (research-ethics, employment and data-protection law vary).
7. **Write down the exit.** Hirschman's exit/voice/loyalty (background) and Frey and Schneider's "effective voice" (2021, verified) give the test: a member who disagrees with a norm should have a way to be heard that binds, or a way to leave at a known cost. A design with neither is one the designer should not want to defend. [V]

**Questions to ask your ethics reviewer, legal counsel or works council.**
- For each intervention, is it reflective or automatic, and disclosed or not?
- Who was consulted, who can change the rule, and who can leave?
- What is the worst case if the intervention is discovered and reported as manipulation?
- [Jurisdictional] Does testing norms on members require consent, notice or consultation under local law or a collective agreement?

**Read next.**
- Hansen & Jespersen, "Nudge and the manipulation of choice" (EJRR 2013) — the grid; verified.
- Bovens, "The ethics of nudge" (2009); verified as existing.
- Frey & Schneider, "Effective voice: beyond exit and affect in online communities" (2021); verified.

**How it connects to the course.** Gives content to the [V] tag throughout; bears on `08-grammar-of-society` (cues, seeding), `03-social-psychology` (commitment and dissonance as compliance tools), `01-secret-of-our-success` (conformity used deliberately) and `09-governing-the-commons` (principle 3 as consent). The brief's critique prompt asks for mistagged [V]s; this section is how to catch them.

---

## Cross-cutting: the ten questions a cooperation designer should be able to answer cold

1. **What are the four expectation questions, and which answer pattern indicates pluralistic ignorance?** (Do, others do, others approve, sanction; high private approval with low perceived approval. Section 1; `08-grammar-of-society`.)
2. **In how many of Herrmann et al.'s 16 participant pools did anti-social punishment cancel the benefit of punishment, and what predicted it?** (Several — enough to remove the effect; weak civic norms and weak rule of law. Section 2.)
3. **What are the meta-analytic effect sizes for reward and punishment on cooperation, and which two moderators matter most?** (d ≈ 0.51 and 0.70; costliness and stable group membership. Section 2.)
4. **What single change in Baldassarri and Grossman's design raised cooperation beyond an appointed monitor?** (Electing the monitor. Section 3.)
5. **What did simultaneous review reveal on Airbnb change, and what did it not change?** (More, more honest, lower ratings; not adverse selection. Section 4.)
6. **What happened when a day-care center fined late parents?** (Lateness rose and stayed up after the fine was removed. Sections 2 and 5.)
7. **What did Wikipedia's 2005-era quality tooling do to good-faith newcomers, and what is the health metric?** (Raised first-session reversion; track first-session rejection rate. Section 6.)
8. **What is the 95% interval on Dunbar's number under modern methods?** (Roughly 4–520; no single number. Section 8.)
9. **How many samples and individuals in the psychological-safety meta-analysis, and how strong is the link to task performance?** (136 samples, 22,000+ individuals; moderate. Section 7.)
10. **On the Hansen–Jespersen grid, which quadrant is manipulation, and which of your brief's interventions sits there?** (Automatic and non-transparent; reread section 10 and check each cue or default in the brief.)

---

## Verification log

**Method.** Each named source was searched by title, authors and venue on 2026-09-30. "verified" marks a source whose existence, authorship, venue and headline result appeared in search snippets. Full texts were not read; the proxy environment made fetching unreliable and it was not attempted for most sources, so any page-level detail, exact chapter title or secondary statistic that was not in a snippet is marked "background".

**Verified (existence and headline result).** Bicchieri *Norms in the Wild* 2017; Bicchieri & Xiao 2009; Krupka & Weber 2013; Tankard & Paluck 2016; Paluck, Shepherd & Aronow 2016; Schultz et al. 2007; Cialdini, Reno & Kallgren 1990; Herrmann, Thöni & Gächter 2008; Balliet, Mulder & Van Lange 2011; Fehr & Gächter 2002; Gürerk, Irlenbusch & Rockenbach 2006 and the 2023 multi-lab replication (existence only); Gneezy & Rustichini 2000; Frey & Jegen 2001; Braithwaite 2002; Baldassarri & Grossman 2011; Jhaver, Bruckman & Gilbert 2019; Gelfand et al. 2011; Tyler 1990/2006; Fiesler et al. 2018; Resnick & Zeckhauser 2002; Fradkin, Grewal & Holtz 2021; Tadelis 2016; Nosko & Tadelis 2015; Dellarocas 2003; Roth 2002 and 2015; Cox, Arnold & Villamayor Tomás 2010; Frey & Sumner 2019; Buterin 2021; Gitcoin quadratic-funding collusion documentation; Grimmelmann 2015; Kraut & Resnick 2012; Matias 2019; Halfaker et al. 2013; Schneider et al. 2021; Schneider 2024; Frey & Schneider 2021; Bail et al. 2018; Cinelli et al. 2021; Bond et al. 2012; Edmondson 1999 and 2018; Frazier et al. 2017; Google Project Aristotle (as reported); Steiner 1972, Hackman 2002 and Mueller 2012 (via secondary sources only); Dunbar 2010; Lindenfors, Wartel & Lind 2021; Bernard–Killworth estimates (via secondary source); Ostrom 2005 and 2010; Rand, Nowak, Fowler & Christakis 2014; Rand & Nowak 2013; Nowak & Sigmund 2005; Axelrod 1984 and the 2025 tournament reproduction (preprint); Kollock 1998; Thaler & Sunstein 2008; Bovens (existence; year background); Hansen & Jespersen 2013; the 2024 Cambridge review of transparent nudging (existence only). Count: about 60 verified citations.

**Background (not re-checked; confirm before quoting).** Dunbar's circle sizes; Edmondson's seven-item scale wording; the four-factor structure of procedural justice; the field evidence on teacher and sales incentives; public-goods decay with marginal per-capita return; the Facebook emotional-contagion controversy; Hirschman's exit/voice/loyalty; EU Digital Services Act duties; Section 230 and DMCA 512 details beyond Grimmelmann's mention; the monopolized-sanctioning-under-noise lab result; the specific result of the 2023 Gürerk replication; the Bovens publication year. Count: about 12 background items.

**Searched and not found, or dropped.** A 2023 paper attributed to Mazar, Elbaek and Mitkidis on experience with anti-social punishment could not be located and is not cited. Bryan, Adams and Monin (2013) on noun-label framing of cheating was not found in search and is not cited. No search was made for organizational-justice meta-analyses (Colquitt et al.), which would strengthen section 3, point 1; treat that transfer as [H] until checked.

**Numbers.** Every number in the text is either from a verified snippet (16 pools; d = 0.51/0.70 over 187 effect sizes; 1,543 farmers in 50 cooperatives; 32 million posts; 2,190 threads, about 8 points and about 70%; 100,000 subreddits; about 5,000 servers; 91 studies; 136 samples, 22,000+ individuals, about 5,000 groups; 51 teams; 180 teams; 33 nations; 61 million users; 100 million items; 56 schools; 4–520 and 16–109; 290 and 231; 14–16 players) or marked background. No illustrative arithmetic was needed in this file.
