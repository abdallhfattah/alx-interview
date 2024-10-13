#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 1:
                perimeter += perimeter_for_cell(row, col, grid)
    return perimeter


def perimeter_for_cell(row, col, grid):
    perimeter = 0
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for x, y in direction:
        nrow = x + row
        ncol = y + col
        inside = (nrow >= 0 and nrow < len(grid)) and (
            ncol >= 0 and ncol < len(grid[0])
        )
        perimeter += (grid[row + x][col + y] == 0) if inside else 1
    return perimeter
