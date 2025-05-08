
````markdown
# City Grid Pathfinding

## Overview
This project provides solutions for pathfinding across a city grid, where some intersections are "bad" neighborhoods that we wish to avoid. The goal is to walk from the upper left-hand corner of the grid to the lower right-hand corner, while avoiding bad neighborhoods.

We offer three main tasks:
- **Part (a)**: Provide an example where there is **no path** across the grid avoiding bad neighborhoods.
- **Part (b)**: Find **any path** across the grid avoiding bad neighborhoods.
- **Part (c)**: Find the **shortest path** across the grid, avoiding bad neighborhoods.

## Problem Definition
- The city is represented as an **X×Y grid**.
- The intersections are defined by a matrix `bad` where:
  - `"yes"` means the intersection is a bad neighborhood (blocked).
  - `"no"` means the intersection is open for walking.

### Task (a): Example of No Valid Path

In **Part (a)**, we are asked to provide an example of a grid where no valid path exists. This can happen when the bad neighborhoods form a complete block between the start `(0, 0)` and end `(X-1, Y-1)`.

#### Example Input (Part a)

```python
bad = [
    ["yes", "yes", "yes", "yes", "no"],
    ["yes", "yes", "yes", "yes", "no"],
    ["yes", "yes", "yes", "yes", "no"],
    ["yes", "yes", "yes", "yes", "no"],
    ["no", "no", "no", "no", "no"]
]
````

In this case, no valid path exists because the bad neighborhoods block the way completely.

### Task (b): Find Any Path

In **Part (b)**, we implement a **Breadth-First Search (BFS)** algorithm to find **any path** from the top-left corner `(0, 0)` to the bottom-right corner `(X-1, Y-1)`, avoiding the bad neighborhoods.

* **BFS** explores all available paths level by level, ensuring that a path will be found if one exists.
* The path is reconstructed using a `parent` matrix, which tracks how each cell was reached.

#### Code Example (Part b)

```python
path = find_any_path(bad)
display_grid_with_path(bad, path)
```

This will display the grid with the path taken (if found). The path will be marked with `*`, the start with `S`, and the end with `E`.

### Task (c): Find the Shortest Path

In **Part (c)**, we extend the **BFS** algorithm to find the **shortest path** by ensuring the smallest number of steps are taken. The shortest path is reconstructed in the same way as in (b), but it guarantees that the fewest number of steps are used.

* BFS is particularly suitable for this task since it guarantees the shortest path in unweighted grids.
* The `dist` matrix keeps track of the distance from the start point to each grid cell.

#### Code Example (Part c)

```python
path = find_shortest_path(bad)
display_grid_with_path(bad, path)
```

This will display the grid with the shortest path taken (if found).

## How to Run the Code

### Requirements

* Python 3.x
* `collections` module (standard Python library)

### Code Structure

* `find_any_path(bad)`: **Part (b)** - Returns any valid path from `(0, 0)` to `(X-1, Y-1)` avoiding bad neighborhoods.
* `find_shortest_path(bad)`: **Part (c)** - Returns the shortest valid path from `(0, 0)` to `(X-1, Y-1)` avoiding bad neighborhoods.
* `display_grid_with_path(bad, path)`: Displays the grid with the path marked.

### Example Input

```python
bad = [
    ["no", "no", "yes", "no", "no", "no", "no"],
    ["no", "yes", "yes", "no", "yes", "yes", "no"],
    ["no", "no", "no", "no", "no", "yes", "no"],
    ["yes", "yes", "yes", "yes", "no", "yes", "no"],
    ["no", "no", "no", "no", "no", "no", "no"],
    ["no", "yes", "yes", "yes", "yes", "yes", "yes"],
    ["no", "no", "no", "no", "no", "no", "no"]
]
```

### Running Part (b) - Find Any Path

```python
path = find_any_path(bad)
display_grid_with_path(bad, path)
```

This will display the grid with the path taken (if found).

### Running Part (c) - Find the Shortest Path

```python
path = find_shortest_path(bad)
display_grid_with_path(bad, path)
```

This will display the grid with the shortest path taken (if found).

## Example Output

For a sample grid like the one shown above, running **Part (b)** might give an output like:

```
Grid (S=start, E=end, *=path, #=bad):
S * * # . . . 
# . # . # . # 
. . # . . # . 
# # # # . # . 
. . . . . . . 
. # # # # # # 
. . . . . . E

Path found:
(0, 0)
(0, 1)
(0, 2)
...
```

### Assumptions

* The grid is **rectangular**.
* The starting point is `(0, 0)` and the end point is `(X-1, Y-1)`.
* The intersections marked with `"yes"` are blocked (bad neighborhoods), and we cannot pass through them.

### Notes

* **Part (a)** provides an example where no valid path exists due to blocking bad neighborhoods.
* **Part (b)** finds any path (if it exists).
* **Part (c)** finds the shortest path by considering all possible moves and ensuring the path with the fewest steps is chosen.

---

## License

MIT License


