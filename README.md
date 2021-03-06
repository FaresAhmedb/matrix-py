<h2 align="center">Hackable Matrix module written in pure Python + CLI</h2>

<p align="center">
<a href="https://pypi.python.org/pypi/matrix-py/"><img alt="PyPI version shields.io" src="https://img.shields.io/pypi/v/matrix-py.svg"></a>
<a href="https://pypi.python.org/pypi/matrix-py/"><img alt="PyPI license" src="https://img.shields.io/pypi/l/matrix-py.svg"></a>
<a href="https://www.codacy.com/gh/FaresAhmedb/matrix-py/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=FaresAhmedb/matrix-py&amp;utm_campaign=Badge_Grade"><img alt="Codacy Badge" src="https://app.codacy.com/project/badge/Grade/480bf6060f5a49938991f62a368f8859"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

matrix-py Module is a python module to:

  - Add Matrices :heavy_check_mark:

  - Substract Matrices :heavy_check_mark:

  - Multiply Matrices :heavy_check_mark:

  - Transpose Matrices :heavy_check_mark:

and many other things will come on 1.0 (if the project is still live)

Works with Python3+ 

---

# Installation
As far as I'm concerned it should work on any python3 version but it's always good to have the latest version since it will be the one I am sure it works on

## Using PyPI
```console
$ pip install matrix-py
```

## Manule Installation
```console
$ git clone https://github.com/FaresAhmedb/matrix-py.git
$ cd matrix-py && python setup.py install --user
```

Now Try it! 
```console
$ matrixpy -h
```
On Windows
```console
> python -m matrixpy -h
```

The ouput should be something like this:
```console
usage: __main__.py [-h] [-v] [-s] [-t] [-ma] [-op] [-mb] [-i]

Matrix Minuplation module to add, substract, multiply matrices.

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show program's version number and exit
  -s , --size        Size of A Matrix
  -t , --transpose   Transpose of A Matrix (-t "[[1, 2, 3], [4, 5, 6]]")
  -ma , --matrixa    Matrix A (.. -ma "[[1, 2, 3], [4, 5, 6]]")
  -op , --operator   Operator (.. -op "+", "-", "*")
  -mb , --matrixb    Matrix B (.. -mb "[[1, 2, 3], [4, 5, 6]]")
  -i , --int         Integer (.. -i 69)

Usage: .. -ma "[[1, 2, 3], [4, 5, 6]]" -op "+" -mb "[[7, 8, 9], [10, 11, 12]]"
```

# Usage
Most of what is written here is: old, changed or old, removed or better methods were made
I am planning on writing a REAL documntation but in the mean time if you want to use the module
all the docstring are well written and will tell you about everything.
Avillable on github pages: https://faresahmedb.github.io/matrix-py/reference/
or in python:
```python
>>> import matrixpy
>>> help(matrixpy)
```

## - The Module
Sample code:
```python


from matrixpy import Matrix

A = Matrix("1 2 3; 4 5 6")   # String -> Matrix Object
B = Matrix([[1, 4],
            [2, 5],
            [3, 6]]) # List -> Matrix Object

# Print the multiply of Matrix A * Matrix B
print(A * B)
# Ouput:
# 14 32
# 32 77
# (2x2)

# Print the addition of the negative Matrix A + Matrix B transposed
print(-A + B.transpose()) 
# Ouput:
# 0 0 0
# 0 0 0
# (2x3)

# 0.1% solved this
C = (+A.transpose() - -B) - (B * 3) + (A.transpose() * 5)
print(C)
# Output:
# 4 16
# 8 20
# 12 24
# (3x2)

# Convert the Matrix to a list if you want to manipulate the matrices yourself
C = C.tolist()
print(type(C))
# Output:
# <class 'list'>
```

## - The Command Line Interface (CLI)

The CLI is limited at the moment by one  operation at a time (eg. You can't add 3 matrices) duo to the limitations of argparse 

To get the size of a matrix
```console
$ matrixpy -s '[[1, 2, 3], [4, 5, 6]]'
1 2 3
4 5 6
(2x3)
```
Your matrix is [[1, 2, 3], [4, 5, 6]] \
To get the transpose of a matrix
```console
$ matrixpy -t '[[1, 2, 3], [4, 5, 6]]'
1 4
2 5
3 6
(3x2)
```
To add 2 matrices to each other or add a matrix to an integer:
```console
$ matrixpy -ma '[[1, 2, 3], [4, 5, 6]]' -op '+' -mb '[[1, 2, 3], [4, 5, 6]]'
2 4 6
8 10 12
(2x3)

$ matrixpy -ma '[[1, 2, 3], [4, 5, 6]]' -op '+' -i 2
3 4 5
6 7 8
(2x3)
```
to substract or multiply matrices just change the '+' to '-' or '*' \
and for a list of the all avillable options
```
$ matrixpy --help
```
---

## Alpha Noitce
The Module is right now in Alpha so there's a big chance there's
some bugs so please consider reporting them.

All Contributions are welcomed so consider looking at the source
code on src/matrixpy

## License &copy;
matrix-py module to add, substract, multiply matrices.
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
