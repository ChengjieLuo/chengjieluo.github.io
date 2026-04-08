---
layout: page
title: Research
permalink: /research/
nav_order: 2
---

## Phase Separation


Liquid–liquid phase separation is a key mechanism driving the formation of biomolecular condensates in living cells. The formation, structure, and dynamics of these condensates are influenced by various factors, including local and nonlocal molecular interactions, passive and active chemical reactions, and mechanical properties such as viscosity and elasticity. Our research aims to describe the emergent behaviors of such complex systems, uncover the universal physical principles that govern phase separation and its dynamics, and ultimately develop strategies to control the spatiotemporal organization of molecules, both within cells and in broader chemical engineering contexts.



# Influence of long-range interactions on phase coexistence 



# Influence of higher-order physical interactions on phase separation in multicomponent liquids

Biomolecules, like proteins and nucleic acids, exhibit complex, higher-order interactions,
where a single molecule may interact with multiple others simultaneously. Besides, cells comprise a myriad of different components that form various droplets. Both are beyond simple mean field theory such as Flory-Huggins theory. How do such higher-order interactions affect the phase separation in multicomponent system?

We find two types of cubic interactions:
<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/higher_order_schematic.png' | relative_url }}" alt="Higher order schematic" style="max-width: 50%;">
</div>

Interestingly, the two types of cubic interactions have opposing effects: attractive binary cubic interactions promote phase separation and increase the number of coexisting phases, while attractive ternary cubic interactions suppress it.
<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/phase_count_vs_b.png' | relative_url }}" alt="Higher order schematic" style="max-width: 50%;">
</div>
<!-- 
Phase diagram can be complex; Stability analysis of homogeneous states is inadequate to study these systems. -->

The resulting phase diagrams can be remarkably complex, and a conventional stability analysis of homogeneous states alone is insufficient to fully characterize these systems.



<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/higher_order_all_diagrams.png' | relative_url }}" alt="Higher order schematic" style="max-width: 80%;">
</div>

# Influence of physical interactions on spatiotemporal patterns

Ideal diffusion with cyclic dominant reactions, like the seminal rock-paper-scissors game, exhibits spiral waves. How do physical interactions affect the spatiotemporal patterns? 


<!-- ![RPS]({{ "/assets/images/RPS_phase_diagram.png" | relative_url }}) -->
<div style="text-align: center; margin: 20px 0;">
  <img src="{{ '/assets/images/RPS_phase_diagram.png' | relative_url }}" alt="RPS_phase_diagram" style="max-width: 80%;">
</div>

Strong repulsive interactions generate oscillating lattices.

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

Strong attraction leads to an
interplay of phase separation and chemical oscillations, like droplets co-locating with cores of spiral waves.


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

Weak interactions change the
length- and time scales of spiral waves.


<!-- 
<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin: 20px 0;">
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.005_chi-11.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.005, χ=-11.0</em></p>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.005_chi0.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.005, χ=0.0</em></p>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.03_chi-11.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.03, χ=-11.0</em></p>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.03_chi-4.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.03, χ=-4.0</em></p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin: 20px 0;">
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.05_chi-11.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.05, χ=-11.0</em></p>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.05_chi0.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.05, χ=0.0</em></p>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.05_chi5.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.05, χ=5.0</em></p>
  </div>
  <div style="flex: 0 0 23%; text-align: center;">
    <video width="100%" controls autoplay loop muted>
      <source src="{{ '/assets/videos/movie_short_zeta0.6_mu0.05_chi6.0.mp4' | relative_url }}" type="video/mp4">
    </video>
    <p><em>μ=0.05, χ=6.0</em> <span style="color: gold; font-size: 1.2em;">▼</span></p>
  </div>
</div> -->

---

## Glass Transition

Almost any material can be cooled or compressed from a liquid to a glass state. During this process, the relaxation dynamics slows down dramatically, while the disordered microstructure undergoes only minor changes. This apparent disconnect between structure and dynamics is at the heart of the complexity of the glass transition. 

We aim to bridge this gap by developing first-principles theories that connect the dynamic behavior of materials with their static structures, providing new insights into the nature of the glass transition.

# A generalized mode-couping theory

![GMCT]({{ "/assets/images/GMCT.pdf" | relative_url }})
 

# Application to sticky hard spheres
![cover_full]({{ "/assets/images/cover_full.png" | relative_url }})

<!-- ## Motion of membrane proteins -->

<!-- Directed transport of proteins and other molecules in a crowded living cell is often carried out by diffusion at short distances and by motor-driven cargo transport over long distances. We demonstrate, by both experiments and theory, that anchored proteins inside the cell can generate a spatially varying and temporally stable potential landscape for intracellular or membrane transport in the mesoscale. Our findings suggest that anchored proteins may play an essential role in generating an effective potential landscape to guide molecular motion in the mesoscale ranging from protein trapping and directed motion to enhanced protein-protein interactions over a long range. -->

<!-- 
The directed transport of proteins and other molecules within crowded living cells often involves a combination of short-distance diffusion and long-distance motor-driven transport. Our research demonstrates that anchored proteins inside cells can create spatially varying and temporally stable potential landscapes, which guide intracellular or membrane transport at the mesoscale.

These findings suggest that anchored proteins play a crucial role in generating effective potential landscapes, enabling processes such as protein trapping, directed motion, and enhanced long-range protein-protein interactions.  -->
