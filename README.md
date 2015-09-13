Bievenido al repositorio online de mecánica de fluidos computacional ([CFD](http://es.wikipedia.org/wiki/Mec%C3%A1nica_de_fluidos_computacional))

Estos notebooks forman parte del primer módulo interactivo online de [CFD con Python](https://github.com/barbagroup/CFDPython/) impartido por la profesora [Lorena A. Barba](http://lorenabarba.com/) y llamado **12 Steps to Navier-Stokes.**.
Texto y código sujeto bajo Creative Commons Attribution license, CC-BY-SA. (c) Original por Lorena A. Barba y Gilbert Forsyth en 2013, traducido por F.J. Navarro-Brull para [CAChemE.org](http://www.cacheme.org/)

[@LorenaABarba](https://twitter.com/LorenaABarba) - 
[@CAChemEorg](https://twitter.com/cachemeorg)

###Instalando Python

El nucleo de este curso ha sido creado mediante [Jupyter (anteriormente conocido como IPython) notebooks](https://jupyter-notebook.readthedocs.org/en/latest/notebook.html), una entorno interactivo de programación que se ejecuta en el navegador.


####Anaconda
Recomendamos *mucho* que instales la [distribución de Python Anaconda](http://docs.continuum.io/anaconda/install) 

Puedes descargar e instalar Anaconda en Windows, OSX y Linux. Para asegurarnos de que tenemos la instalación actualizada con todas las bibliotecas necesarias para seguir este curso, debes de ejecutar lo siguiente en la ventana de comandos (cmd en windows o Bash en Mac/linux) 

```Bash
conda update jupyter
```

y seguidamente

```Bash
conda install numpy scipy sympy
```
Si no te aclaras, puedes ver [este vídeo](https://www.youtube.com/watch?v=x4xegDME5C0&feature=youtu.be&list=PLGBbVX_WvN7as_DnOGcpkSsUyXB1G_wqb).

####Sin Anaconda
Si ya tienes Python instalado y no quieres usar Anaconda, puedes instalar las librerías mediante pip con el siguiente comando

```Bash
pip install jupyter
```
Al igual que con Anaconda, debes asegurarte de que tienes todas las librerías necesarias con el siguiente comando.

```Bash
pip install numpy scipy sympy
```

###Abriendo un notebook (y creando un server de jupyter para ello)

Una vez tenemos jupyter instalado, simplemente abre una terminal (ventana de comandos) y ejecuta: 

```Bash
jupyter notebook
```
¡y se abrirá una sesión de jupyter en tu navegador web!


Lecciones
-------

* [Introduccion rápida a Python](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/00_Introduccion_rapida_a_Python.ipynb)
* [Paso 1](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/01_Paso_1.ipynb)
* [Paso 2](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/02_Paso_2.ipynb)
* [CFL Condition](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/03_CFL_Condition.ipynb)
* [Paso 3](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/04_Paso_3.ipynb)
* [Paso 4](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/05_Paso_4.ipynb)
* [Operaciones matriciales (arrays) con NumPy](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/06_Operaciones_matriciales_%28arrays%29_con_NumPy.ipynb)
* [Paso 5](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/07_Paso_5.ipynb)
* [Paso 6](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/08_Paso_6.ipynb)
* [Paso 7](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/09_Paso_7.ipynb)
* [Paso 8](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/10_Paso_8.ipynb)
* [Definiendo funciones](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/11_Definiendo_funciones.ipynb)
* [Paso 9](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/12_Paso_9.ipynb)
* [Paso 10](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/13_Paso_10.ipynb)
* [Optimizando bucles con Numba](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/14_Optimizando_bucles_con_Numba.ipynb)
* [Paso 11](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/15_Paso_11.ipynb)
* [Paso 12](http://nbviewer.ipython.org/github/franktoffel/CFDPython-ES/blob/master/lecciones/16_Paso_12.ipynb)
