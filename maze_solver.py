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


def main():
    print("Maze (# = wall, . = path):")
    print_maze()
    

if __name__ == "__main__":
    main()