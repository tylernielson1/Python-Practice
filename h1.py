# CSC 333 - Fall 2012 - Homework 1
# Time-stamp: <2012-08-30 21:05:12 CDT>

# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return a value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file as a script: python h1.py

# Feel free to add your own doctests.

# The following makes / always do float division, and turns print into
# a function, both of which are the standard behavior in Python 3.

from __future__ import print_function


def tnp1(n):
    """
    The "three N plus 1" sequence starting from a positive integer n is
    defined as follows: if n is 1, stop; if n is odd, the next number is
    3n+1; if n is even, the next number is n//2. For example, here's the
    sequence starting from 7:

        7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

    The function tnp1 must return the total length of the sequence
    starting from n. There's no need to actually store the sequence.

    >>> tnp1(7)
    17
    >>> tnp1(2)
    2
    >>> tnp1(1)
    1
    >>> tnp1(0)
    0
    >>> tnp1(-100)
    0

    Remember that // performs integer division in Python.
    """


def postfix(xs):
    """
    Given a nonempty list containing a valid postfix expression, return
    the result of the expression. The list can contain integers and the
    strings '+', '-', '*', '/', representing integer addition,
    subtraction, multiplication, and division. You can assume that
    division by zero will not occur. Note that in the second example the
    exact answer is 3.5, but we're using integer operations.

    >>> postfix([3,5,'-'])
    -2
    >>> postfix([1,2,3,'*','+',2,'/'])
    3
    >>> postfix([10])
    10
    >>> postfix([3,2,'/'])
    1
    """

def bowl(frames):
    """
    Find the score for a game of bowling. The argument is a list of ten
    elements. The first nine elements are either the number 10
    (representing a strike), or a tuple containing two numbers that sum
    to at most 10 (either a spare or an open frame). The tenth element
    is either a pair of numbers whose sum is less than 10, or a triple
    of numbers whose sum is at most 30. All numbers are nonnegative and
    less than or equal to 10, and games will always be valid. The lowest
    possible score is 0; the highest is 300. If you don't know how to
    score a game, consult the web.

    The result is a list of ten elements showing the cumulative score.

    You will almost certainly want to write some local helper functions,
    say to help with scoring spares and strikes.

    >>> bowl([10,(3,7),(6,1),10,10,10,(2,8),(9,0),(7,3),(10,10,10)])
    [20, 36, 43, 73, 95, 115, 134, 143, 163, 193]
    >>> bowl([(9,1),10,(2,2),10,(8,1),(9,0),10,10,(2,5),(8,2,9)])
    [20, 34, 38, 57, 66, 75, 97, 114, 121, 140]
    """

def freq(xs):
    """
    Returns a frequency list of the elements of xs, sorted first by
    frequency, then by value. I suggest using a dictionary to track the
    frequencies, then convert it to a list of (count, value) pairs. Once
    you have the list of pairs, Python's 'sorted' function will do the
    sorting for you.

    >>> freq([])
    []
    >>> freq([3,1,2,2,3,1,1,4,2,0])
    [(1, 0), (1, 4), (2, 3), (3, 1), (3, 2)]
    >>> freq(['dog','dog','cat','dog'])
    [(1, 'cat'), (3, 'dog')]
    """


def find_best(f, xs):
    """
    Assume that f(x) gives a measure of the "goodness" of x, where
    larger values are better than smaller ones. Return the best element
    of the nonempty list xs. If two or more elements are equally good,
    return the one that appears earliest in the list.

    >>> find_best(lambda x: x ** 2, [4,-5,2,5,-3,0,1])
    -5
    >>> find_best(lambda s: s[1:], ['fox','moose','frog','goat'])
    'frog'
    """


def between(a, b):
    """
    Returns a new function that, given x, determines if x is greater
    than or equal to a and less than b.

    >>> callable(between(0, 5))
    True
    >>> between(0, 5)(4)
    True
    >>> between(0, 5)(5)
    False
    >>> between('cat', 'dog')('moose')
    False
    """


def among(*xs):
    """
    Note the * in front of xs. This says that 'among' can take zero or
    more arguments, all of which will be collected by Python into a tuple
    and passed in as the argument xs. The return value is a function
    that, given x, determines whether x is one of the values in xs.

    >>> among()(5)
    False
    >>> among(8,4,'bob',False)(4)
    True
    >>> among(8,4,'bob',False)('sam')
    False
    """


def tabulate(f, x0, n=10):
    """
    Returns a list of length n containing

        [x0, f(x0), f(f(x0)), f(f(f(x0))), ...]

    n may be any nonnegative value, so you can't hardcode the number of
    calls to f. You must also call f at most n-1 times total.

    >>> tabulate(lambda x: x + 1, 0)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> tabulate(lambda x: x + 1, 42, 1)
    [42]
    >>> tabulate(lambda s: s[1:] + s[0], 'top', 5)
    ['top', 'opt', 'pto', 'top', 'opt']
    >>> tabulate(lambda x: x + 1, 42, 0)
    []
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()

