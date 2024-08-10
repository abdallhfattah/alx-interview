#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal's triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]
        if i > 0:
            previous_row = triangle[i - 1]
            row.extend(
                [previous_row[j] + previous_row[j + 1] for j in range(len(previous_row) - 1)]
            )
            row.append(1)
        triangle.append(row)
    return triangle
