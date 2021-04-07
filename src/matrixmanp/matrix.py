#!/usr/bin/python3

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

# pylint: disable=C0103 # Variable name "m" is "iNvAlId-nAmE"

import argparse
import json


name = 'matrixmanp'
__version__ = '0.1'
__all__     = ['Matrix']


class MatrixError(Exception):

    """Error for the Matrix Object invalid operations"""


class Matrix:

    """Matrix Object: add, sub, mul, and a lot more"""

    # Object Creation: START
    def __init__(self, matrix) -> None:
        """Initialize matrix object."""
        self.matrix = matrix

    def __str__(self, dims=True):
        """Return the Matrix, the size of it (Activated when using print)"""
        for row in self.matrix:
            print(' '.join(map(str,row)))

        if dims:
            return self.__repr__()

        return ''

    def __repr__(self):
        """Return the matrix size (string representation of the object)"""
        return '({}x{})'.format(len(self.matrix), len(self.matrix[0]))
    # Object Creation: END

    # Object Expressions: START
    def __pos__(self):
        """Positive operator: +A | Return the matrix * 1 (copy)"""
        result = list()

        for i in range(len(self.matrix)):
            result.append([])
            for m in range(len(self.matrix[0])):
                result[i].append(+self.matrix[i][m])

        return Matrix(result)

    def __neg__(self):
        """Negative operator: -A. | Returns the matrix * -1"""
        result = list()

        for i in range(len(self.matrix)):
            result.append([])
            for m in range(len(self.matrix[0])):
                result[i].append(-self.matrix[i][m])

        return Matrix(result)
    # Object Expressions: END

    # Object Math operations: START
    def __add__(self, other):
        """Matrix Addition: A + B or A + INT."""
        if isinstance(other, Matrix):
            # A + B
            result = list()

            if (len(self.matrix)    != len(other.matrix) or
                len(self.matrix[0]) != len(other.matrix[0])):
                raise MatrixError('To add matrices, the matrices must have'
                ' the same dimensions')

            for m in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[0])):
                    result[m].append(self.matrix[m][j] + other.matrix[m][j])

        else:
            # A + INT
            result = list()

            for m in range(len(self.matrix)):
                result.append([])
                for i in range(len(self.matrix[0])):
                    result[m].append(self.matrix[m][i] + other)

        return Matrix(result)

    def __sub__(self, other):
        """Matrix Subtraction: A - B or A - INT."""
        if isinstance(other, Matrix):
            # A + B
            result = list()

            if (len(self.matrix)    != len(other.matrix) or
                len(self.matrix[0]) != len(other.matrix[0])):
                raise MatrixError('To sub matrices, the matrices must have'
                ' the same dimensions')

            for m in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[0])):
                    result[m].append(self.matrix[m][j] - other.matrix[m][j])
        else:
            # A + INT
            result = list()

            for m in range(len(self.matrix)):
                result.append([])
                for i in range(len(self.matrix[0])):
                    result[m].append(self.matrix[m][i] - other)

        return Matrix(result)

    def __mul__(self, other):
        """Matrix Multiplication: A * B or A * INT."""
        if isinstance(other, Matrix):
            # A * B
            if len(self.matrix[0]) != len(other.matrix):
                raise MatrixError('The number of rows in matrix A must be'
                ' equal to the number of columns in B matrix')

            # References:
            # https://www.geeksforgeeks.org/python-program-multiply-two-matrices
            result = [[sum(a * b for a, b in zip(A_row, B_col))
                            for B_col in zip(*other.matrix)]
                                    for A_row in self.matrix]
        else:
            # A * INT
            result = list()

            for m in range(len(self.matrix)):
                result.append([])
                for i in range(len(self.matrix[0])):
                    result[m].append(self.matrix[m][i] * other)

        return Matrix(result)
    # Object Math opertaions: END

    # Object Manpulation: START
    def transpose(self: list):
        """Return a new matrix transposed"""
        result = [list(i) for i in zip(*self.matrix)]
        return Matrix(result)


    def to_list(self):
        """Convert Matrix object to a list"""
        return self.matrix
    # Object Manpulation: END

def main():
    """The CLI for the module"""
    parser=argparse.ArgumentParser(
        description = 'Matrix Minuplation module to add, substract, multiply'
        'matrices.',
        epilog = 'Usage: .. -ma "[[1, 2, 3], [4, 5, 6]]" -op "+" -mb'
        ' "[[7, 8, 9], [10, 11, 12]]"')

    parser.add_argument('-v', '--version',
        action="version",
        version=__version__,
    )

    parser.add_argument('-s', '--size',
        type=json.loads,
        metavar='',
        help='Size of A Matrix'
    )

    parser.add_argument('-t', '--transpose',
        type=json.loads,
        metavar='',
        help='Transpose of A Matrix (-t "[[1, 2, 3], [4, 5, 6]]")'
    )

    parser.add_argument('-ma', '--matrixa',
        type=json.loads,
        metavar='',
        help='Matrix A (.. -ma "[[1, 2, 3], [4, 5, 6]]")'
    )

    parser.add_argument('-op', '--operator',
        type=str,
        metavar='',
        help='Operator (.. -op "+", "-", "*")'
    )

    parser.add_argument('-mb', '--matrixb',
        type=json.loads,
        metavar='',
        help='Matrix B (.. -mb "[[1, 2, 3], [4, 5, 6]]")'
    )

    parser.add_argument('-i', '--int',
        type=int,
        metavar='',
        help='Integer (.. -i 69)'
    )

    args = parser.parse_args()

    if args.size:
        return Matrix(args.size)

    elif args.transpose:
        return Matrix(args.transpose).transpose()

    elif args.matrixa:
        if args.operator == '+':
            return Matrix(args.matrixa) + Matrix(args.matrixb) \
            if args.matrixb else \
            return Matrix(args.matrixa) + args.int
        elif args.operator == '-':
            return Matrix(args.matrixa) - Matrix(args.matrixb) \
            if args.matrixb else \
            return Matrix(args.matrixa) - args.int
        elif args.operator == '*':
            return Matrix(args.matrixa) * Matrix(args.matrixb) \
            if args.matrixb else \
            return Matrix(args.matrixa) * args.int
        else:
            raise SyntaxError('The avillable operations are +, -, *')
    else:
        return parser.print_help()


if __name__ == '__main__':
    main()
