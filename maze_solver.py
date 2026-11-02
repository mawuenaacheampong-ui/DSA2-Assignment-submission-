import random

import matplotlib.pyplot as plt
import numpy as np

MAZE_TEXT = [
    "#########.###########",
    "#.....#.......#...#.#",
    "#.#####.#.###.#.#.#.#",
    "#.#.....#.#.....#...#",
    "#.#.#####.###########",
    "#.#.#...#...........#",
    "#.#.###.#########.#.#",
    "#.#...#.....#...#.#.#",
    "#.###.#.#####.#.#.#.#",
    "#.#...#.#...#.#.#.#.#",
    "#.#.###.#.#.#.#.###.#",
    "#.#.#...#.#.#.#.....#",
    "#.#.###.#.#.#.#####.#",
    "#.#.#...#.#...#.....#",
    "#.#.#.#.#.###.#######",
    "#.#.#.#.#...#.#.....#",
    "#.#.#.#.###.#######.#",
    "#.#...#.#...#.....#.#",
    "#.#####.#.###.#.###.#",
    "#.......#.....#.....#",
    "###########.#########",
]
MAZE = np.array([[0 if ch == "#" else 1 for ch in row] for row in MAZE_TEXT])

START = (0, 9)
EXIT = (20, 11)
DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
MAX_STEPS = 200


def print_maze():
    for r in range(MAZE.shape[0]):
        print("".join("." if MAZE[r, c] else "#" for c in range(MAZE.shape[1])))


def neighbours(pos):
    r, c = pos
    result = []
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < MAZE.shape[0] and 0 <= nc < MAZE.shape[1] and MAZE[nr, nc] == 1:
            result.append((nr, nc))
    return result


def solve_backtracking():
    stack = [START]
    visited = {START}
    order = [START]
    steps = 0
    while stack:
        current = stack[-1]
        if current == EXIT:
            return True, order, stack, steps
        moved = False
        for nxt in neighbours(current):
            if nxt not in visited:
                visited.add(nxt)
                order.append(nxt)
                stack.append(nxt)
                steps += 1
                moved = True
                break
        if not moved:
            stack.pop()
            steps += 1
    return False, order, [], steps


def solve_las_vegas(no_reverse=True):
    pos = START
    previous = None
    walk = [pos]
    for step in range(1, MAX_STEPS + 1):
        options = neighbours(pos)
        if no_reverse and len(options) > 1 and previous in options:
            options.remove(previous)
        previous = pos
        pos = random.choice(options)
        walk.append(pos)
        if pos == EXIT:
            return True, walk, walk, step
    return False, walk, walk, MAX_STEPS


def show_result(name, success, visited, path):
    canvas = np.zeros(MAZE.shape + (3,))
    canvas[MAZE == 1] = (1, 1, 1)
    for r, c in set(visited):
        canvas[r, c] = (0.55, 0.78, 1.0)
    if name == "Backtracking":
        for r, c in path:
            canvas[r, c] = (0.1, 0.7, 0.2)
    canvas[START] = (1, 0.6, 0)
    canvas[EXIT] = (0.9, 0.1, 0.1)
    plt.figure(figsize=(6, 6))
    plt.imshow(canvas)
    result = "SUCCESS" if success else "FAILED"
    plt.title(name + " - " + result + " (" + str(len(set(visited))) + " squares visited)")
    plt.xticks([])
    plt.yticks([])
    plt.show()


def ask_approach():
    while True:
        choice = input("Choose approach - B for Backtracking, L for Las Vegas: ").strip().lower()
        if choice in ("b", "backtracking"):
            return "Backtracking", solve_backtracking
        if choice in ("l", "las vegas", "lasvegas"):
            return "Las Vegas", solve_las_vegas
        print("Invalid choice, please type B or L.")


def main():
    print("Maze (# = wall, . = path):")
    print_maze()
    name, solver = ask_approach()
    success, visited, path, steps = solver()
    print(name, "finished:", "exit found" if success else "exit NOT found")
    print("Steps:", steps, "| Squares visited:", len(set(visited)))
    show_result(name, success, visited, path)


if __name__ == "__main__":
    main()