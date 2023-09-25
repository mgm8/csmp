#!/usr/bin/env python

#
#  setup.py
#
#  Copyright The CSMP Contributors.
#
#  This file is part of CSMP.
#
#  CSMP is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  CSMP is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with CSMP; if not, see <http://www.gnu.org/licenses/>.
#
#


import setuptools
import os

exec(open('csmp/version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name                            = "CSMP",
    version                         = __version__,
    author                          = "Gabriel Mariano Marcelino", 
    author_email                    = "gabriel.mm8@gmail.com",
    maintainer                      = "Gabriel Mariano Marcelino",
    maintainer_email                = "gabriel.mm8@gmail.com",
    url                             = "https://github.com/mgm8/csmp",
    license                         = "GPLv3",
    description                     = "CubeSat Mission Planner",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    classifiers                     = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research"
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        ],
    download_url                    = "https://github.com/mgm8/csmp/releases",
    packages                        = setuptools.find_packages(),
    install_requires                = ['PyGObject'],
    entry_points                    = { 
        'gui_scripts': [
            'csmp = csmp.__main__:main'
            ]
        },
    data_files                      = [ 
        ('share/icons/', ['csmp/data/img/csmp_256x256.png']),
        ('share/applications/', ['csmp.desktop']),
        ('share/csmp/', ['csmp/data/ui/csmp.glade']),
        ],
)
