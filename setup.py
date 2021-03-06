#!/usr/bin/env python
from setuptools import setup

setup(
    name="omv-torrentcatcher",
    packages=['omv-torrentcatcher'],
    version="2.1.1.1",
    license="GPLv3",
    url="https://github.com/trancen/omv-torrentcatcher",
    description=("Takes torrent or magnet links from rss feeds you provide, "
                 "parses them and sends them to transmission via the "
                 "transmission-remote command line utility. Credit to https://github.com/archangelic/torrentcatcher"),
    author="David",
    author_email="trancen@gmail.com",
    download_url=(
        "https://github.com/trancen/omv-torrentcatcher/tarball/v2.1.0"
    ),
    dependency_links=[
        'http://www.voidspace.org.uk/downloads/validate.py#egg=validate-1.0.1'
    ],
    install_requires=[
        'configobj>=4.7.0',
        'argparse>=1.2.1',
        'validate>=1.0.1',
        'feedparser>=5.1.3',
        'tabulate>=0.7.3'
    ],
    scripts=['bin/omv-torrentcatcher'],
    keywords=['torrent', 'rss', 'transmission'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Internet',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux'
    ]
)
