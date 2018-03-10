---
title: 'CFD Python: the 12 steps to Navier-Stokes equations'
tags:
- Python
- CFD
- differential equations
- numerical methods
- finite differences
authors:
- name: Lorena A. Barba
  orcid: 0000-0001-5812-2711
  affiliation: 1
- name: Gilbert F. Forsyth
  orcid: 0000-0002-4983-1978
  affiliation: "1, 2"
affiliations:
- name: The George Washington University
  index: 1
- name: Capital One
  index: 2
date: 9 March 2018
bibliography: paper.bib
---

# Summary

The **CFD Python** learning module is a set of Jupyter notebooks, consisting of 12 "core" lessons, 3 "bonus" lessons, and a "lesson zero" as a quick intro to Python for numerical computing.
This practical module takes students through 12 steps, one by one, at the end of which they will have programmed a solver for the two-dimensional Navier-Stokes equations, using finite differences.
The steps are the following:

* Steps 1–4 are in one dimension: (i) linear convection with a step-function initial condition (IC) and appropriate boundary conditions (BC); with the same IC/BCs: (ii) nonlinear convection, and (iii) diffusion only; (iv) Burgers’ equation, with a saw-tooth IC and periodic BCs.
* Steps 5–10 are in two dimensions: (v) linear convection with a square function IC and appropriate BCs; with the same IC/BCs: (vi) nonlinear convection, and (vii) diffusion only; (viii) Burgers’ equation; (ix) Laplace equation, with zero IC and both Neumann and Dirichlet BCs; (x) Poisson equation in 2D.
* Steps 11–12 solve the Navier-Stokes equation in 2D: (xi) cavity flow; (xii) channel flow.

Guiding the students through these steps (without skipping any), they learn many valuable lessons. The incremental nature of the exercises means they get a sense of achievement at the end of each assignment, and they feel they are learning with low effort. As they progress, they naturally practice code re-use and they incrementally learn programming and plotting techniques. As they analyze their results, they learn about numerical diffusion, accuracy and convergence. In about four weeks, they become moderately proficient programmers and are motivated to start discussing more theoretical matters.

# Statement of need

Many university courses in computational fluid dynamics (CFD) follow a similar order of topics. As reflected in various textbooks, the course usually starts with the subject of interpolation, going on to numerical integration of ordinary differential equations, and continuing to standard material on partial differential equations. Students encounter theory of stability, order of convergence, and numerical diffusion, but they often do not gain much experience programming.
This learning module places emphasis on practical experience with _programming_ the solution to fundamental mathematical models that can represent fluid behavior. 
It is unique in its approach of taking a beginner in a step-by-step fashion to complete the solution of a fairly complex numerical problem: two-dimensional cavity flow via the Navier-Stokes equations, discretized with finite differences.

The "12 steps to Navier-Stokes" lessons have proved effectiveness. They were used in the classroom as part of a university course for four years in a row (2009- to 2013), guiding several dozen students to develop their Navier-Stokes solutions. 
Written as a set of Jupyter notebooks, the module was the backbone of an intensive tutorial held as part of the 2013 Latin American Symposium on High-Performance Computing in Mendoza, Argentina (http://ecar2013.hpclatam.org).


