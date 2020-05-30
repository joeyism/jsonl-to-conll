from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('jsonl_to_conll/__init__.py').read(),
    re.M
    ).group(1)

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'jsonl_to_conll',
        packages = find_packages(), # this must be the same as the name above
        version = version,
        description = 'A simple tool to convert JSONL files to CONLL',
        long_description = long_description,
        author = 'joeyism',
        author_email = 'joeyism@gmail.com',
        entry_points = {
            "console_scripts": ['jsonl-to-conll = jsonl_to_conll.cli:main']
        },
        url = 'https://github.com/joeyism/jsonl-to-conll', # use the URL to the github repo
        download_url = 'https://github.com/joeyism/jsonl-to-conll/archive/{}.tar.gz'.format(version),
        keywords = ['jsonl', 'conll', 'converter', 'convert', 'machine', 'learning', 'training', 'train', 'data', 'ETL'], 
        install_requires = [package.split("\n")[0] for package in open("requirements.txt", "r").readlines()],
        classifiers = [],
        )
