#!/usr/bin/python3
"""
Function to generate Pascal's triangle up to the nth level.

Returns:
    A list of lists, where each inner list represents a level of Pascal's triangle.
    Returns an empty list if n <= 0.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the specified number of rows, n."""
    triangle = []
    if n > 0:
        for current_row in range(1, n + 1):
            row_values = []
            coefficient = 1
            for position in range(1, current_row + 1):
                row_values.append(coefficient)
                coefficient = coefficient * (current_row - position) // position
            triangle.append(row_values)
    return triangle
