#!/usr/bin/env python
# -- coding: utf-8 --

#Original code written by https://bitbucket.org/hrojas/learn-pandas/


# TODO: Fix this code to automate it

from sys import version_info

if version_info[0] < 3:
    from urllib import quote
else:
    from urllib.request import quote


from glob import glob
import json
import re

header = '''
Bievenido al repositorio online de mecánica de fluidos computacional ([CFD](http://es.wikipedia.org/wiki/Mec%C3%A1nica_de_fluidos_computacional))

Estos notebooks forman parte del primer módulo interactivo online de [CFD con Python](https://github.com/barbagroup/CFDPython/) impartido por la profesora [Lorena A. Barba](http://lorenabarba.com/) y llamado **12 Steps to Navier-Stokes.**.
Texto y código sujeto bajo Creative Commons Attribution license, CC-BY-SA. (c) Original por Lorena A. Barba y Gilbert Forsyth en 2013, traducido por F.J. Navarro-Brull para [CAChemE.org](http://www.cacheme.org/)

[@LorenaABarba](https://twitter.com/LorenaABarba) - 
[@CAChemEorg](https://twitter.com/cachemeorg)

Lecciones
-------
'''


format_item = '* [{name}]({url})'.format
bb_url = 'raw.github.com/franktoffel/CFDPython-ES/master{}'.format

def notebooks():
    return glob('lecciones/*.ipynb')


def lesson_name(filename):
    with open(filename) as fo:
        return json.load(fo)['metadata']['name']


def nb_url(filename):
    # The double quote is not an error
    raw_url = bb_url(quote(quote(filename)))
    return 'http://nbviewer.ipython.org/urls/{}'.format(raw_url)


def write_readme(nblist, fo):
    fo.write('{}\n'.format(header))
    for nb in nblist:
        name = lesson_name(nb)
        url = nb_url(nb)
        fo.write('{}\n'.format(format_item(name=name, url=url)))


def lesson_id(filename):
    return int(re.search('[0-9]+', filename).group())

#    return int(re.search('*.ipynb', filename).group())

def main():
    nblist = sorted(notebooks(), key=lesson_id)
    #nblist = glob('*.ipynb')
    with open('README.md', 'w') as fo:
        write_readme(nblist, fo)


if __name__ == '__main__':
    main()
