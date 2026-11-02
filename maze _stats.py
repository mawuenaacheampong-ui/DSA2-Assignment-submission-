import random

from maze_solver import solve_backtracking, solve_las_vegas

RUNS = 10000


def success_rate(solver):
    wins = 0
    for _ in range(RUNS):
        if solver()[0]:
            wins += 1
    return wins / RUNS


def main():
    print("Running", RUNS, "runs of each approach...")
    backtracking = success_rate(solve_backtracking)
    las_vegas = success_rate(solve_las_vegas)
    pure_random = success_rate(lambda: solve_las_vegas(no_reverse=False))
    print("Backtracking success rate:", f"{backtracking:.2%}")
    print("Las Vegas success rate:", f"{las_vegas:.2%}")
    print("Las Vegas (pure random, no no-reverse rule):", f"{pure_random:.2%}")


if __name__ == "__main__":
    main()