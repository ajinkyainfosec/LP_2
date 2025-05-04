# A* Algorithm implementation in Python (2D Grid Maze Example)
from queue import PriorityQueue

# Grid representation (0 = empty, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

ROWS, COLS = len(grid), len(grid[0])
start = (0, 0)
goal = (4, 4)

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))

    came_from = {}
    g_score = {start: 0}

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        x, y = current
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  # 4 directions
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)

            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 0:
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    open_set.put((f_score, neighbor))

    return None  # No path found

# Run A*
path = a_star(start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")
