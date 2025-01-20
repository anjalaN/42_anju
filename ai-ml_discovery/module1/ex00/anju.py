'''#!/usr/bin/env python3
from collections import deque
import random

# Define the goal state of the puzzle
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Define the possible moves (left, right, up, down) in the grid
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def is_solvable(puzzle):
   
    inversions = 0
    puzzle = [x for x in puzzle if x != 0]  # Remove the empty space (0)
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def print_puzzle(puzzle):
    """
    Print the puzzle in a 3x3 grid format.
    """
    for i in range(0, 9, 3):
        print(" ".join(map(str, puzzle[i:i+3])))
    print()

def get_neighbors(state):
    """
    Get all possible states that can be reached by moving the empty space (0).
    """
    zero_pos = state.index(0)  # Position of the empty space
    row, col = zero_pos // 3, zero_pos % 3
    neighbors = []

    for dr, dc in MOVES:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(new_state)

    return neighbors

def bfs(initial_state):
    """
    Perform breadth-first search (BFS) to find the shortest solution to the puzzle.
    Returns the steps to reach the goal state if solvable, or None if unsolvable.
    """
    # Queue for BFS: each element is (current_state, path)
    queue = deque([(initial_state, [])])
    seen = set()
    seen.add(tuple(initial_state))

    while queue:
        current_state, path = queue.popleft()

        # If we reach the goal state
        if current_state == GOAL_STATE:
            return path

        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            if tuple(neighbor) not in seen:
                seen.add(tuple(neighbor))
                queue.append((neighbor, path + [neighbor]))

    return None  # No solution found

def generate_random_puzzle():
    """
    Generate a random puzzle and check if it is solvable.
    If it's unsolvable, keep generating new random puzzles.
    """
    while True:
        puzzle = random.sample(range(9), 9)
        if is_solvable(puzzle):
            return puzzle
        else:
            # If the puzzle is unsolvable, try again
            continue

def test_case(initial_state):
    """
    Test the puzzle with a given initial state, solving it and printing the steps.
    """
    print("Initial state of the puzzle:")
    print_puzzle(initial_state)

    # Check if the puzzle is already solved
    if initial_state == GOAL_STATE:
        print("Puzzle is already solved!")
        return

    print("Solving the puzzle...")
    solution = bfs(initial_state)

    if solution is None:
        print("Puzzle is unsolvable!")  # Print unsolvable message if BFS fails
    else:
        print(f"Solution found in {len(solution)} steps.")
        for i, step in enumerate(solution, 1):
            print(f"Step {i}:")
            print_puzzle(step)

def main():
    # Test case 1: Solved puzzle
    solved_puzzle = GOAL_STATE[:]
    test_case(solved_puzzle)

    # Test case 2: Unsolvable puzzle (this will generate an unsolvable puzzle)
    unsolvable_puzzle = random.sample(range(9), 9)
    while is_solvable(unsolvable_puzzle):
        unsolvable_puzzle = random.sample(range(9), 9)
    test_case(unsolvable_puzzle)

    # Test case 3: Random solvable puzzle
    random_puzzle = generate_random_puzzle()
    test_case(random_puzzle)

if __name__ == "__main__":
    main()'''


#!/usr/bin/env python3
from collections import deque
import random
import sys

# Define the goal state of the puzzle
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Define the possible moves (left, right, up, down) in the grid
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def is_solvable(puzzle):
    """
    Check if the puzzle is solvable based on the inversion count rule.
    An inversion is when a higher-numbered tile precedes a lower-numbered tile.
    A puzzle is solvable if the number of inversions is even.
    """
    inversions = 0
    puzzle = [x for x in puzzle if x != 0]  # Remove the empty space (0)
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def print_puzzle(puzzle):
    """
    Print the puzzle in a 3x3 grid format.
    """
    for i in range(0, 9, 3):
        print(" ".join(map(str, puzzle[i:i+3])))
    print()

def get_neighbors(state):
    """
    Get all possible states that can be reached by moving the empty space (0).
    """
    zero_pos = state.index(0)  # Position of the empty space
    row, col = zero_pos // 3, zero_pos % 3
    neighbors = []

    for dr, dc in MOVES:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(new_state)

    return neighbors

def bfs(initial_state):
    """
    Perform breadth-first search (BFS) to find the shortest solution to the puzzle.
    Returns the steps to reach the goal state if solvable, or None if unsolvable.
    """
    # Queue for BFS: each element is (current_state, path)
    queue = deque([(initial_state, [])])
    seen = set()
    seen.add(tuple(initial_state))

    while queue:
        current_state, path = queue.popleft()

        # If we reach the goal state
        if current_state == GOAL_STATE:
            return path

        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            if tuple(neighbor) not in seen:
                seen.add(tuple(neighbor))
                queue.append((neighbor, path + [neighbor]))

    return None  # No solution found

def generate_random_puzzle():
    """
    Generate a random puzzle and check if it is solvable.
    If it's unsolvable, keep generating new random puzzles.
    """
    while True:
        puzzle = random.sample(range(9), 9)
        if is_solvable(puzzle):
            return puzzle
        else:
            # If the puzzle is unsolvable, try again
            continue

def test_case(initial_state):
    """
    Test the puzzle with a given initial state, solving it and printing the steps.
    """
    print("Initial state of the puzzle:")
    print_puzzle(initial_state)

    # Check if the puzzle is already solved
    if initial_state == GOAL_STATE:
        print("Puzzle is already solved!")
        return

    print("Solving the puzzle...")
    solution = bfs(initial_state)

    if solution is None:
        print("Puzzle is unsolvable!")  # Print unsolvable message if BFS fails
    else:
        print(f"Solution found in {len(solution)} steps.")
        for i, step in enumerate(solution, 1):
            print(f"Step {i}:")
            print_puzzle(step)

def main():
    # Check if an initial state is passed as a command line argument
    if len(sys.argv) == 10:
        # If an initial state is provided, use it (the user must provide the state in a list format)
        initial_state = list(map(int, sys.argv[1:]))
    else:
        # Generate a random solvable puzzle
        initial_state = generate_random_puzzle()

    test_case(initial_state)

if __name__ == "__main__":
    main()

