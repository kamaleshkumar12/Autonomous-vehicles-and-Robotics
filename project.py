
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    open_set = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()
    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]
        if current == goal:
            return path
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                heapq.heappush(open_set, (cost + 1 + heuristic((nx, ny), goal), cost + 1, (nx, ny), path))
    return []

def visualize(grid, path, start, goal):
    fig, ax = plt.subplots()
    rows, cols = len(grid), len(grid[0])

    # Draw grid
    for x in range(rows):
        for y in range(cols):
            color = 'black' if grid[x][y] == 1 else 'white'
            rect = patches.Rectangle((y, rows - 1 - x), 1, 1, edgecolor='gray', facecolor=color)
            ax.add_patch(rect)

    # Draw path
    for (x, y) in path:
        rect = patches.Rectangle((y, rows - 1 - x), 1, 1, facecolor='cyan')
        ax.add_patch(rect)

    # Mark start and goal
    ax.add_patch(patches.Rectangle((start[1], rows - 1 - start[0]), 1, 1, facecolor='green'))
    ax.add_patch(patches.Rectangle((goal[1], rows - 1 - goal[0]), 1, 1, facecolor='red'))

    plt.xlim(0, cols)
    plt.ylim(0, rows)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.title("A* Path Planning Visualization")
    plt.show()

# Grid setup
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)
visualize(grid, path, start, goal)
