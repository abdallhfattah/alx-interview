#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    The grid is a 2D list where:
    - 1 represents land
    - 0 represents water

    For each land cell, the perimeter is calculated based on how many sides
    are adjacent to water or the boundary of the grid.

    Args:
    - grid (list of list of int): 2D list where 1 represents land and 0 represents water.

    Returns:
    - int: The perimeter of the island in the grid.
    """
    perimeter = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 1:
                perimeter += perimeter_for_cell(row, col, grid)
    return perimeter


def perimeter_for_cell(row, col, grid):
    """
    Calculate the perimeter contribution of a single land cell at (row, col).

    A land cell has up to 4 neighboring cells (up, down, left, right). If any of
    these neighbors is water (0) or outside the grid, it contributes to the perimeter.

    Args:
    - row (int): The row index of the current cell.
    - col (int): The column index of the current cell.
    - grid (list of list of int): 2D list representing the map of the island.

    Returns:
    - int: The perimeter contributed by this cell.
    """
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
