
# CFD Python

**CFD Python**, a.k.a. the **12 steps to Navier-Stokes**, is a practical module for learning the basics of Computational Fluid Dynamics (CFD) by coding solutions to the basic partial differential equations used to describe fluid flow.
The module was part of a course taught by [Prof. Lorena Barba](http://lorenabarba.com) between 2009 and 2013 in the Mechanical Engineering department at Boston University (Prof. Barba since moved to the George Washington University). 

The module assumes only basic programming knowledge (in any language) and some foundation in partial differential equations and fluid mechanics. The "steps" were inspired by ideas of Dr. Rio Yokota, who was a post-doc in Prof. Barba's lab until 2011, and the lessons were refined by Prof. Barba and her students over several semesters teaching the CFD course. 
This set of Jupyter notebooks was developed in 2013 to teach an intensive course in Mendoza, Argentina.

Guiding students through these steps (without skipping any!), they learn many valuable lessons. The incremental nature of the exercises means they get a sense of achievement at the end of each assignment, and they feel they are learning with low effort. As they progress, they naturally practice code re-use and they incrementally learn programming and plotting techniques. As they analyze their results, they learn about numerical diffusion, accuracy and convergence. 
In about four weeks of a regularly scheduled course, they become moderately proficient programmers and are motivated to start discussing more theoretical matters.

## How to use this module

In a regular-session university course, students can complete the **CFD Python** lessons in 4 to 5 weeks. 
As an intensive tutorial, the module can be completed in two or three full days, depending on the learner's prior experience. 
The lessons can also be used for self study. 
In all cases, learners should follow along the worked examples in each lesson by re-typing the code in a fresh Jupyter notebook, maybe taking original notes as they try things out. 

Lessons
-------
Steps 1–4 are in one spatial dimension. Steps 5–10 are in two dimensions (2D). Steps 11–12 solve the Navier-Stokes equation in 2D. Three "bonus" notebooks cover the CFL condition for numerical stability, array operations with NumPy, and defining functions in Python.

* [Quick Python Intro](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/00_Quick_Python_Intro.ipynb)
—For Python novices, this lesson introduces the numerical libraries (NumPy and Matplotlib), Python variables, use of whitespace, and slicing arrays.
* [Step 1](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/01_Step_1.ipynb)
—Linear convection with a step-function initial condition (IC) and appropriate boundary conditions (BCs).
* [Step 2](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/02_Step_2.ipynb)
—With the same IC/BCs, _nonlinear_ convection.
* [CFL Condition](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/03_CFL_Condition.ipynb)
—Exploring numerical stability and the Courant-Friedrichs-Lewy (CFL) condition.
* [Step 3](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/04_Step_3.ipynb)
—With the same IC/BCs, _diffusion_ only.
* [Step 4](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/05_Step_4.ipynb)
—Burgers’ equation, with a saw-tooth IC and periodic BCs (with an introduction to Sympy).
* [Array Operations with NumPy](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/06_Array_Operations_with_NumPy.ipynb)
* [Step 5](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/07_Step_5.ipynb)
—Linear convection in 2D with a square-function IC and appropriate BCs.
* [Step 6](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/08_Step_6.ipynb)
——With the same IC/BCs, _nonlinear_ convection in 2D.
* [Step 7](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/09_Step_7.ipynb)
—With the same IC/BCs, _diffusion_ in 2D.
* [Step 8](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/10_Step_8.ipynb)
—Burgers’ equation in 2D
* [Defining Function in Python](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/11_Defining_Function_in_Python.ipynb)
* [Step 9](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/12_Step_9.ipynb)
—Laplace equation with zero IC and both Neumann and Dirichlet BCs.
* [Step 10](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/13_Step_10.ipynb)
—Poisson equation in 2D.
* [Step 11](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/15_Step_11.ipynb)
—Solves the Navier-Stokes equation for 2D cavity flow.
* [Step 12](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/16_Step_12.ipynb)
—Solves the Navier-Stokes equation for 2D channel flow.




## Dependencies

To use these lessons, you need Python 3, and the standard stack of scientific Python: NumPy, Matplotlib, SciPy, Sympy. And of course, you need [Jupyter](http://jupyter.org)—an interactive computational environment that runs on a web browser.

This mini-course is built as a set of [Jupyter notebooks](https://jupyter-notebook.readthedocs.org/en/latest/notebook.html) containing the written materials and worked-out solutions on Python code. To work with the material, we recommend that you start each lesson with a fresh new notebook, and follow along, typing each line of code (don't copy-and-paste!), and exploring by changing parameters and seeing what happens. 


#### Installing via Anaconda
We *highly* recommend that you install the [Anaconda Python Distribution](http://docs.continuum.io/anaconda/install). It will make your life so much easier. 
You can download and install Anaconda on Windows, OSX and Linux. 

After installing, to ensure that your packages are up to date, run the following commands in a terminal:

```Bash
conda update conda
conda update jupyter numpy sympy scipy matplotlib
```

If you prefer Miniconda (a mini version of Anaconda that saves you disk space), install all the necessary libraries to follow this course by running the following commands in a terminal:

```Bash
conda update conda
conda install jupyter
conda install numpy scipy sympy matplotlib
```


#### Without Anaconda
If you already have Python installed on your machine, you can install Jupyter using pip:

```Bash
pip install jupyter
```

Please also make sure that you have the necessary libraries installed by running

```Bash
pip install numpy scipy sympy matplotlib
```


### Running the notebook server

Once Jupyter is installed, open up a terminal and then run 

```Bash
jupyter notebook
```

This will start up a Jupyter session in your browser!

## How to contribute to CFD Python

We accept contributions via pull request—in fact, several users have already submitted pull requests making corrections or small improvements. You can also open an issue if you find a bug, or have a suggestion. 

## Copyright and License

(c) 2017 Lorena A. Barba, Gilbert F. Forsyth. All content is under Creative Commons Attribution [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.txt), and all [code is under BSD-3 clause](https://github.com/engineersCode/EngComp/blob/master/LICENSE) (previously under MIT, and changed on March 8, 2018). 

We are happy if you re-use the content in any way!

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

