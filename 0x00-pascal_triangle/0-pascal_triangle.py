#!/usr/bin/python3
def pascal_triangle(n):
    # Initialize an empty list to hold the triangle
    triangle = []

    # Handle the case when n is less than or equal to 0
    if n <= 0:
        return triangle

    # Generate Pascal's Triangle row by row
    for i in range(n):
        # Start each row with 1
        row = [1]

        # Fill in the middle elements using values from the previous row
        if i > 0:
            previous_row = triangle[i - 1]
            row.extend(
                [previous_row[j] + previous_row[j + 1] for j in range(len(previous_row) - 1)]
            )
            # End each row with 1
            row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    return triangle
