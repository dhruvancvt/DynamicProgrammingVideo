from collections import deque

# Function to find the shortest path using BFS
def find_shortest_path(bad):
    X, Y = len(bad), len(bad[0])

    # Initialize distance and parent matrices
    dist = [[-1 for _ in range(Y)] for _ in range(X)]
    parent = [[None for _ in range(Y)] for _ in range(X)]

    # If the starting point is blocked, return no path
    if bad[0][0] == "yes":
        return None

    q = deque()
    q.append((0, 0))
    dist[0][0] = 0  # Distance to the start is 0

    # Allow movement in all four directions (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        i, j = q.popleft()

        # If we've reached the destination, reconstruct the path
        if (i, j) == (X - 1, Y - 1):
            path = []
            current = (i, j)
            while current:
                path.append(current)
                current = parent[current[0]][current[1]]
            return path[::-1]  # Reverse to get path from start to end

        # Explore all valid neighbors
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            # Check bounds, ensure not visited (dist == -1), and avoid bad intersections
            if 0 <= ni < X and 0 <= nj < Y and dist[ni][nj] == -1 and bad[ni][nj] != "yes":
                dist[ni][nj] = dist[i][j] + 1
                parent[ni][nj] = (i, j)  # Track the parent for path reconstruction
                q.append((ni, nj))

    return None  # No path found


# Function to display the grid with the shortest path marked
def display_grid_with_path(bad, path):
    X, Y = len(bad), len(bad[0])
    grid = [["#" if bad[i][j] == "yes" else "." for j in range(Y)] for i in range(X)]

    # Overlay path on grid if it exists
    if path:
        for i, j in path:
            grid[i][j] = "*"
        grid[0][0] = "S"         # Start point
        grid[X-1][Y-1] = "E"     # End point

    print("Grid (S=start, E=end, *=path, #=bad):")
    for row in grid:
        print(" ".join(row))


# Example grid: "yes" = bad intersection, "no" = safe
bad = [
    ["no",  "no",  "yes", "no",  "no",  "no",  "no"],
    ["no",  "yes", "yes", "no",  "yes", "yes", "no"],
    ["no",  "no",  "no",  "no",  "no",  "yes", "no"],
    ["yes", "yes", "yes", "yes", "no",  "yes", "no"],
    ["no",  "no",  "no",  "no",  "no",  "no",  "no"],
    ["no",  "yes", "yes", "yes", "yes", "yes", "yes"],
    ["no",  "no",  "no",  "no",  "no",  "no",  "no"],
]

# Find the shortest path
path = find_shortest_path(bad)

# Display the grid with the shortest path
display_grid_with_path(bad, path)

# Output the path details if found
if path:
    print("\nShortest path found:")
    for step in path:
        print(step)
    print(f"\nPath length: {len(path) - 1} steps")
else:
    print("\nNo path found.")
