#!/usr/bin/env python
#Original code written by https://bitbucket.org/hrojas/learn-pandas/


from sys import version_info

if version_info[0] < 3:
    from urllib import quote
else:
    from urllib.request import quote


from glob import glob
import json
import re

header = '''
Welcome to the CFD Online Lesson Repository

Lessons
-------
'''



format_item = '* [{name}]({url})'.format
bb_url = 'bitbucket.org/cfdpython/cfd-python-class/raw/master/{}'.format

def notebooks():
    return glob('lessons/*.ipynb')


def lesson_name(filename):
    with open(filename) as fo:
        return json.load(fo)['metadata']['name'][5:]


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

