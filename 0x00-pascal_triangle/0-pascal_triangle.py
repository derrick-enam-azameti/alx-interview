#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for x in range(1, n + 1):
            level = []
            R = 1
            for y in range(1, x + 1):
                level.append(R)
                R = R * (x - y) // y
            res.append(level)
    return res
