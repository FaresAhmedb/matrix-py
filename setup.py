"""Matrix Manipulation module to add, substract, multiply matrices.

Copyright (C) 2021 Fares Ahmed

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name                          = 'matrixmanp',
    version                       = '0.1',
    description                   = 'Matrix Manipulation module to add, substract, multiply matrices.',
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    author                        = 'Fares Ahmed',
    author_email                  = 'faresahmed@zohomail.com',
    license                       = 'GPLv2',
    scripts                       = ['bin/matrixmanp'],
    packages                      = ['matrixmanp'],
    package_dir                   = {"": "src"},
    install_requires              = ["setuptools"],
    url                           = "https://github.com/FaresAhmedb/matrixmanp",
    python_requires               = ">=3.1",
    )
