# Matrix Manpulation
MatrixManp. Module is a python module to:
- Add Matrices :heavy_check_mark:
- Substract Matrices :heavy_check_mark:
- Multiply Matrices :heavy_check_mark:
- Transpose Matrices :heavy_check_mark:

and many other things will come on 1.0 (if the project is still live)

---

# Installation
As far as I'm concerned it should work on any python3 version but it's always good to have the latest version since it will be the one I am sure it works on

The module is currently not on PyPi so you will have to install it manually right now \
NOTE: this assumes you have pip installed on your PC  :warning:
```g
git clone https://github.com/FaresAhmedb/matrixmanp.git
cd matrixmanp/dist
pip install ./matrixmanp-0.1.tar.gz
```

Now Try it! 
```
python -m  matrixmanp -h
```

The ouput should be something like this:
```
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
## - The Module
Sample code:
```python
from matrixmanp.matrix import Matrix

A = Matrix([ [1, 2, 3], [4, 5, 6] ])   # List -> Matrix Object
B = Matrix([ [1, 4], [2, 5], [3, 6] ]) # List -> Matrix Object

# Print the multiply of Matrix A * Matrix B
print(A * B)
# Ouput:
# 14 32
# 32 77
# (2x2)

# Print the addition of the negative Matrix A + Matrix B transposed
print(-A + B.transpose()) 
# Ouput:
# 2 4 6
# 8 10 12
# (2x3)

# 0.1% solved this
C = (+A.transpose() - -B) - (B * 3) + (A.transpose() * 5)
print(C)

# Convert the Matrix to a list if you want to manipulate the matrices yourself
C = C.to_list()
print(type(C))
# Output:
# <class 'list'>
```


## - The Command Line Interface (CLI)
The CLI is limited at the moment by one  operation at a time (You can't add 3 matrices) duo to the limitations of argparse 

To get the transpose of a matrix
```bash
python -m matrixmanp -t '[[1, 2, 3], [4, 5, 6]]'
1 4
2 5
3 6
(3x2)
```
Your matrix is [[1, 2, 3], [4, 5, 6]] \
To add 2 matrices to each other or add a matrix to an integer:
```bash
python -m matrixmanp -ma '[[1, 2, 3], [4, 5, 6]]' -op '+' -mb '[[1, 2, 3], [4, 5, 6]]'
2 4 6
8 10 12
(2x3)

python -m matrixmanp -ma '[[1, 2, 3], [4, 5, 6]]' -op '+' -i 2
3 4 5
6 7 8
(2x3)
```
to substract or multiply matrices just change the '+' to '-' or '*' \
and for a list of the all avillable options

---

## Alpha Noitce
The Module is right now in Alpha so there's a big chance there's
some bugs so please consider reporting them.

All Contributions are welcome so consider looking at the source
code on src/matrixmanp

---

## License &copy;
Matrix Manipulation module to add, substract, multiply matrices.
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
