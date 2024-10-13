## Island Perimeter Problem

### Description

This repository contains a solution for the **Island Perimeter** problem using Python. The goal of the problem is to compute the perimeter of an island in a 2D grid. The island is represented by `1`s (land) and `0`s (water). The perimeter is calculated by counting the edges where the island meets water or the boundary of the grid.

### Problem Statement

Given a 2D grid where:

- `1` represents land.
- `0` represents water.

Each cell in the grid is a square with side length 1. The grid is completely surrounded by water, and there is exactly one island (or group of connected 1's). We need to calculate the perimeter of this island.

### Input

- A 2D list `grid` where:
  - `grid[i][j] == 1` represents land.
  - `grid[i][j] == 0` represents water.

### Output

- An integer representing the perimeter of the island.

### Example

```python
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

In this example, the perimeter of the island is 16.

### Solution Explanation

1. **island_perimeter(grid)**:
   - This function iterates through the grid and, whenever it encounters a cell with land (`1`), it calls `perimeter_for_cell()` to calculate the perimeter contributed by that particular cell.

2. **perimeter_for_cell(row, col, grid)**:
   - This helper function calculates the perimeter for a land cell by checking the four adjacent cells (up, down, left, right). If the neighboring cell is water or out of bounds, the perimeter is incremented.

---

### Functions

#### `island_perimeter(grid)`
Calculates the perimeter of the island in the grid.

**Parameters**:
- `grid`: A list of lists where each element is either `1` (land) or `0` (water).

**Returns**:
- `int`: The perimeter of the island.

#### `perimeter_for_cell(row, col, grid)`
Calculates the perimeter contribution of a single land cell by checking its neighbors.

**Parameters**:
- `row`: The row index of the current cell.
- `col`: The column index of the current cell.
- `grid`: A list of lists representing the map of the island.

**Returns**:
- `int`: The perimeter contribution of the cell at `(row, col)`.

---

### Usage

To run the solution, you need Python 3.x. Simply call the `island_perimeter()` function with your grid input, and it will return the perimeter of the island.
