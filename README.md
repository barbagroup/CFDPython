
##Welcome to CFD Python

Hello! Welcome to the **12 steps to Navier-Stokes**. This is a practical module that is used in the beginning of an interactive Computational Fluid Dynamics (CFD) course taught by [Prof. Lorena Barba](lorenabarba.com) between 2009 and 2013 at Boston University (Prof. Barba since moved to the George Washington University). The course assumes only basic programming knowledge (in any language) and of course some foundation in partial differential equations and fluid mechanics. The practical module was inspired by the ideas of Dr. Rio Yokota, who was a post-doc in Prof. Barba's lab, and has been refined by Prof. Barba and her students over several semesters teaching the course. The course is taught entirely using Python and students who don't know Python just learn as we work through the module.

###Installing Python

The core of this mini-course is built around [Jupyter(formerly IPython) notebooks](https://jupyter-notebook.readthedocs.org/en/latest/notebook.html), an interactive computational environment that is run in a web-browser.


####Anaconda
We *highly* recommend that you install the [Anaconda Python Distribution](http://docs.continuum.io/anaconda/install) 

You can download and install Anaconda on Windows, OSX and Linux.  To ensure that it's up to date and to install all the necessary libraries to follow this course, run (in a terminal)

```Bash
conda update jupyter
```

and then

```Bash
conda install numpy scipy sympy
```

####Without Anaconda
If you already have Python installed, you can install the notebooks using pip

```Bash
pip install jupyter
```

Please also make sure that you have the necessary libraries installed by running

```Bash
pip install numpy scipy sympy
```


###Running a notebook server

Once jupyter is installed, just open up a terminal and then run 

```Bash
jupyter notebook
```

to start up a jupyter session in your browser!

Lessons
-------

* [Quick Python Intro](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/00_Quick_Python_Intro.ipynb)
* [Step 1](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/01_Step_1.ipynb)
* [Step 2](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/02_Step_2.ipynb)
* [CFL Condition](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/03_CFL_Condition.ipynb)
* [Step 3](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/04_Step_3.ipynb)
* [Step 4](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/05_Step_4.ipynb)
* [Array Operations with NumPy](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/06_Array_Operations_with_NumPy.ipynb)
* [Step 5](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/07_Step_5.ipynb)
* [Step 6](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/08_Step_6.ipynb)
* [Step 7](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/09_Step_7.ipynb)
* [Step 8](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/10_Step_8.ipynb)
* [Defining Function in Python](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/11_Defining_Function_in_Python.ipynb)
* [Step 9](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/12_Step_9.ipynb)
* [Step 10](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/13_Step_10.ipynb)
* [Step 11](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/15_Step_11.ipynb)
* [Step 12](http://nbviewer.ipython.org/urls/github.com/barbagroup/CFDPython/blob/master/lessons/16_Step_12.ipynb)
