#!/usr/bin/env python
#Original code written by https://bitbucket.org/hrojas/learn-pandas/


from glob import glob
from urllib.parse import quote
import re

header = '''
Welcome to the CFD Online Lesson Repository

Lessons
-------
'''



format_item = '* [{name}]({url})'.format

bb_url = 'github.com/barbagroup/CFDPython/blob/master/{}'.format

def notebooks():
    return glob('lessons/*.ipynb')

def lesson_id(filename):
    return int(re.search('[0-9]+', filename).group())

def lesson_name(filename):
    filename = filename.split('/')[1].split('.')[0]
    return filename[filename.find('_')+1:].replace('_',' ')

def nb_url(filename):
    raw_url = bb_url(quote(quote(filename)))
    return 'http://nbviewer.ipython.org/urls/{}'.format(raw_url)

def write_readme(nblist, fo):
    fo.write('{}\n'.format(header))
    for nb in nblist:
        name = lesson_name(nb)
        url = nb_url(nb)
        fo.write('{}\n'.format(format_item(name=name, url=url)))

def main():
    nblist = sorted(notebooks(), key=lesson_id)
    with open('README.md', 'w') as fo:
        write_readme(nblist, fo)

if __name__ == '__main__':
    main()
