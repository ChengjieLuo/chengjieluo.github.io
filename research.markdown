---
layout: page
title: Research
permalink: /research/
nav_order: 2
---

## Phase Separation


Liquid–liquid phase separation is a key mechanism driving the formation of biomolecular condensates in living cells. The formation, structure, and dynamics of these condensates are governed by a rich interplay of molecular interactions, chemical reactions, and mechanical properties. Our research aims to uncover the universal physical principles underlying phase separation and to develop strategies for controlling the spatiotemporal organization of molecules — both inside cells and in chemical engineering applications.


<details>
<summary><h3 style="display: inline;">Size control of condensates via long-range interactions</h3></summary>

Condensation is typically driven by short-range attractions, but many biomolecules carry charges that also mediate long-range repulsion. What happens when these two competing interactions coexist?

Using molecular dynamics simulations and an equilibrium field theory, we show that the interplay of short-range attraction and long-range repulsion can arrest coarsening, leading to many droplets of well-defined, equal size at equilibrium. Crucially, this size control is governed by the <em>charge asymmetry</em> between molecular constituents, while the strength of the short-range attractions has a weak influence.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/charge_asymmetry_schematic.png' | relative_url }}" alt="Charge asymmetry schematic" style="max-width: 70%;">
</div>

</details>


<details>
<summary><h3 style="display: inline;">Higher-order interactions in multicomponent phase separation</h3></summary>

Biomolecules exhibit complex, higher-order interactions in which a single molecule can engage with multiple partners simultaneously. Moreover, cells contain a vast number of distinct molecular species that form a variety of condensates. Both features lie beyond the reach of classical mean-field theories such as Flory–Huggins theory. How do such higher-order interactions affect phase separation in multicomponent systems?

We identify two fundamentally distinct types of cubic interactions:
<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/higher_order_schematic.png' | relative_url }}" alt="Higher order schematic" style="max-width: 70%;">
</div>

Remarkably, these two types have opposing effects: attractive <em>binary</em> cubic interactions promote phase separation and increase the number of coexisting phases, while attractive <em>ternary</em> cubic interactions suppress it.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/phase_count_vs_b.png' | relative_url }}" alt="Phase count vs b" style="max-width: 70%;">
</div>

The resulting phase diagrams are remarkably complex — conventional stability analysis of homogeneous states alone is insufficient to characterize them, as the number of unstable modes falls short of the actual number of coexisting phases at equilibrium.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/higher_order_all_diagrams.png' | relative_url }}" alt="Higher order all diagrams" style="max-width: 90%;">
</div>

This complexity implies an enormous parameter regime with multiple locally stable states. In biological cells, such multistability could enable control over the formation and dissolution of condensates. More broadly, higher-order interactions offer a largely unexplored avenue for engineering multicomponent phase separation.

</details>


<details>
<summary><h3 style="display: inline;">Spatiotemporal patterns from the interplay of reactions and physical interactions</h3></summary>

Cyclic-dominance reactions — such as the classic rock-paper-scissors game — coupled with ideal diffusion produce spiral waves. But real molecules are not ideal: they attract and repel each other. How do physical interactions reshape these spatiotemporal patterns?

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/RPS_phase_diagram.png' | relative_url }}" alt="RPS phase diagram" style="max-width: 80%;">
</div>

We find three qualitatively distinct regimes:

Strong repulsion suppresses spiral waves and generates oscillating lattice patterns.

<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin: 20px 0;">
  <div style="flex: 0 0 23%; text-align: center;">
    <p><span style="color: green; font-size: 1.2em;">▼</span><em>μ=0.05, χ=5</em></p>
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.05_chi5.0.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <p><span style="color: gold; font-size: 1.2em;">▼</span><em>μ=0.05, χ=6</em></p>
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.05_chi6.0.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
     <p><span style="color: red; font-size: 1.2em;">▼</span><em>μ=0.05, χ=6.5</em></p>
     <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.05_chi6.5.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
</div>

Strong attraction triggers an interplay between phase separation and chemical oscillations — droplets co-localize with the cores of spiral waves.

<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin: 20px 0;">
  <div style="flex: 0 0 23%; text-align: center;">
    <p><span style="color: green; font-size: 1.2em;">▼</span><em>μ=0.03, χ=-11</em></p>
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.03_chi-11.0.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <p><span style="color: gold; font-size: 1.2em;">▼</span><em>μ=0.005, χ=-11</em></p>
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.005_chi-11.0.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
</div>

Weak interactions preserve the spiral-wave morphology but modify their characteristic length and time scales.

These results reveal that even modest physical interactions can qualitatively alter the outcome of reaction-diffusion dynamics, pointing to a rich and largely uncharted interplay between thermodynamics and non-equilibrium chemistry.

</details>


<details>
<summary><h3 style="display: inline;">Coexistence of patterned phases in chemically active mixtures</h3></summary>

Reaction-diffusion equations give rise to spatially patterned states such as Turing patterns, while short-range physical interactions drive the coexistence of multiple homogeneous phases. What emerges when both mechanisms act simultaneously?

The key insight is that linear reactions at steady state and long-range interactions in equilibrium share the same mathematical structure. This deep analogy allows us to reinterpret complex spatiotemporal patterns as the coexistence of <em>patterned phases</em>, and provides an upper bound on the number of coexisting phases via a generalized Gibbs phase rule.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/patterned_phases_schematic.png' | relative_url }}" alt="Patterned phases schematic" style="max-width: 60%;">
</div>

With a minimal four-component model, we demonstrate that phases of distinct morphologies can indeed coexist.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/snapshots.png' | relative_url }}" alt="Coexistence of patterned phases" style="max-width: 90%;">
</div>

Moreover, knowing that each pair of species with short-range repulsion and long-range attraction can create a new phase, we can rationally design patterns of striking complexity — patterns that appear almost random at first glance, yet are now fully explained by our theory.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/snapshot_3phases.png' | relative_url }}" alt="Designed three-phase coexistence" style="max-width: 80%;">
</div>

</details>

---

## Glass Transition

Almost any material can be cooled or compressed from a liquid to a glass state. During this process, the relaxation dynamics slows down by many orders of magnitude, while the disordered microstructure changes only mildly. This apparent disconnect between structure and dynamics lies at the heart of the glass-transition problem and has remained one of the grand challenges in condensed matter physics.

We tackle this challenge by developing first-principles theories that systematically connect the static structure of a material to its dynamical relaxation, providing new insights into the microscopic origin of glassy slowdown.

<details>
<summary><h3 style="display: inline;">Generalized mode-coupling theory</h3></summary>

Standard mode-coupling theory (MCT) relates the slow dynamics of supercooled liquids to the static pair structure, but its quantitative predictions are often inaccurate. To go beyond MCT, we have developed a generalized mode-coupling theory (GMCT) that derives, from first principles, the coupled dynamical equations for many-body density correlation functions. These equations form an infinite hierarchy, where each level feeds back into the others through memory kernels. In principle, the theory becomes exact as the closure level approaches infinity; in practice, we truncate at a finite level and systematically improve the predictions by increasing it.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/GMCT.png' | relative_url }}" alt="GMCT hierarchy schematic" style="max-width: 80%;">
</div>

</details>

<details>
<summary><h3 style="display: inline;">Applying GMCT to glass-forming liquids</h3></summary>

We have applied GMCT to a wide range of glass-forming models, and in every case the predictions improve systematically with increasing closure level.

For hard spheres, GMCT yields progressively more accurate critical packing fractions.

For sticky hard spheres, it not only sharpens the predicted critical temperatures but also captures the re-entrant glass transition behavior.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/critical_points.png' | relative_url }}" alt="Critical points of glass models" style="max-width: 90%;">
</div>

For the Kob–Andersen Lennard-Jones  (KALJ) and WCA mixtures, which share nearly identical static pair structures yet exhibit markedly different dynamics, GMCT detects the subtle structural differences and correctly predicts distinct dynamical behaviors for the two systems.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/KALJ_WCA.png' | relative_url }}" alt="KALJ vs WCA comparison" style="max-width: 80%;">
</div>

We have further proved that, under a mean-field-like closure, GMCT preserves the sharp dynamic glass transition and the well-established scaling laws of standard MCT. However, we must point out that GMCT cannot explain the breakdown of Stokes-Einstein relation.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/F_vs_t.png' | relative_url }}" alt="Relaxation dynamics" style="max-width: 70%;">
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/scaling_GMCT.png' | relative_url }}" alt="GMCT scaling laws" style="max-width: 90%;">
</div>


</details>


<details>
<summary><h3 style="display: inline;">Beyond pair structure: the role of many-body static correlations</h3></summary>

Most liquid-state theories rely solely on pair-level structural information, but the dynamics of a glassy system is also shaped by higher-order static correlations. How important are these conventionally neglected contributions?


We further extend our theory to include the contribution of higher-order static correlations. We find that incorporating even the static triplet direct correlations already qualitatively changes the predicted glass-transition diagram of both binary hard-sphere mixtures and the strong network glass-former silica. Strikingly, there is a nontrivial competition: static triplet correlations tend to stabilize the glass state, while higher-order dynamic correlations act to destabilize it. This competition is present in both fragile and strong glass-formers, demonstrating that many-body static correlations are an essential — yet long-overlooked — ingredient for a quantitative theory of the glass transition.

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/silica.png' | relative_url }}" alt="Silica glass transition diagram" style="max-width: 80%;">
</div>

</details>
