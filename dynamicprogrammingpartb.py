from collections import deque  # Import deque for efficient queue operations (used in BFS)

# Function to find any valid path from top-left to bottom-right avoiding bad intersections
def find_any_path(bad):
    X, Y = len(bad), len(bad[0])  # Dimensions of the grid

    # Initialize visited matrix and parent matrix to track visited nodes and path reconstruction
    visited = [[False for _ in range(Y)] for _ in range(X)]
    parent = [[None for _ in range(Y)] for _ in range(X)]

    # If the starting point is bad, return no path
    if bad[0][0] == "yes":
        return None

    q = deque()
    q.append((0, 0))  # Start BFS from (0, 0)
    visited[0][0] = True  # Mark start as visited

    directions = [(1, 0), (0, 1)]  # Only allow moves to the right and down

    while q:
        i, j = q.popleft()

        # If we've reached the bottom-right cell, reconstruct the path
        if (i, j) == (X - 1, Y - 1):
            path = []
            current = (i, j)
            while current:
                path.append(current)
                current = parent[current[0]][current[1]]  # Move to the parent node
            return path[::-1]  # Reverse the path to start from (0, 0)

        # Explore neighbors (right and down)
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            # Check bounds, if not visited, and not a bad cell
            if 0 <= ni < X and 0 <= nj < Y and not visited[ni][nj] and bad[ni][nj] != "yes":
                visited[ni][nj] = True
                parent[ni][nj] = (i, j)  # Store parent to reconstruct path later
                q.append((ni, nj))  # Enqueue the neighbor

    return None  # No path found


# Function to display the grid with the path marked
def display_grid_with_path(bad, path):
    X, Y = len(bad), len(bad[0])

    # Create visual representation of grid
    grid = [["#" if bad[i][j] == "yes" else "." for j in range(Y)] for i in range(X)]

    # Overlay the path on the grid
    if path:
        for i, j in path:
            grid[i][j] = "*"
        grid[0][0] = "S"         # Mark start
        grid[X-1][Y-1] = "E"     # Mark end

    print("Grid (S=start, E=end, *=path, #=bad):")
    for row in grid:
        print(" ".join(row))


# Example grid: "yes" = bad intersection, "no" = safe
bad = [
    ["no", "no", "no", "no"],
    ["yes", "no", "no", "no"],
    ["yes", "yes", "no", "no"],
    ["no", "no", "yes", "no"]
]

# Run the pathfinder
path = find_any_path(bad)

# Display the result visually
display_grid_with_path(bad, path)

# Print path coordinates if found
if path:
    print("\nPath found:")
    for step in path:
        print(step)
else:
    print("\nNo path found.")
