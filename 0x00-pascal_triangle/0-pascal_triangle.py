#!/usr/bin/python3
"""
Function to generate Pascal's triangle up to the nth level.

Returns:
    A list of lists, where each inner list represents a level of Pascal's triangle.
    Returns an empty list if n <= 0.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    
    Args:
        n (int): The number of rows to generate.
    
    Returns:
        list of lists: Shows integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    res = [[1]]  # Initialize the first row

    # Generate rows for Pascal's triangle
    for i in range(1, n):
        # Start the row with 1
        row = [1]  
        
        # Calculate the intermediate values for each row using the previous row
        for j in range(1, i):
            row.append(res[i-1][j-1] + res[i-1][j])
        
        # End the row with 1
        row.append(1)

        # Append the row to the result
        res.append(row)
    return res
