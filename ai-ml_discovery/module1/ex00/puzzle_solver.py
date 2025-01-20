#!/usr/bin/env phthon3
'''from collections import deque
import random

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

def main():
    # Generate a random solvable puzzle
    initial_state = generate_random_puzzle()

    print("Initial state of the puzzle:")
    print_puzzle(initial_state)

    print("Solving the puzzle...")
    solution = bfs(initial_state)

    if solution is None:
        print("Puzzle is unsolvable!")  # Print unsolvable message if BFS fails
    else:
        print(f"Solution found in {len(solution)} steps.")
        for i, step in enumerate(solution, 1):
            print(f"Step {i}:")
            print_puzzle(step)

if __name__ == "__main__":
    main()'''

# python3 puzzle_solver.py 4 7 8 6 5 4 3 2 1  

#!/usr/bin/env python3
from collections import deque
import sys
import random

# Goal state of the puzzle
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# Possible moves (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_goal(state):
    """Check if the current state matches the goal state."""
    return state == goal_state

def get_possible_moves(puzzle):
    """Return all possible states that can be reached by moving the empty space (0)."""
    index_of_zero = puzzle.index(0)
    row, col = divmod(index_of_zero, 3)
    possible_moves = []

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_puzzle = puzzle[:]
            new_puzzle[index_of_zero], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[index_of_zero]
            possible_moves.append(new_puzzle)

    return possible_moves

def is_solvable(puzzle):
    """Check if the puzzle is solvable based on the number of inversions."""
    inversions = 0
    puzzle = [x for x in puzzle if x != 0]  # Remove the empty space (0)
    
    # Count inversions
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j]:
                inversions += 1

    return inversions % 2 == 0

def bfs(start_state):
    """Perform breadth-first search to find the shortest solution to the puzzle."""
    if is_goal(start_state):
        return [start_state]
    
    queue = deque([(start_state, [])])  # Queue stores (state, path)
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if tuple(current_state) in visited:
            continue
        visited.add(tuple(current_state))

        # Explore all possible moves
        for next_state in get_possible_moves(current_state):
            if is_goal(next_state):
                return path + [current_state, next_state]
            queue.append((next_state, path + [current_state]))

    return None  # If no solution is found

def print_puzzle(puzzle):
    """Print the current state of the puzzle."""
    for i in range(0, len(puzzle), 3):
        print(puzzle[i:i+3])
    print()

def main():
    # Accept the initial state from command line argument or generate a random one
    if len(sys.argv) == 10:
        initial_state = [int(arg) for arg in sys.argv[1:]]
        if not is_solvable(initial_state):
            print("The puzzle is unsolvable.")
            return
    else:
        initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Default solvable puzzle
        random.shuffle(initial_state)
        while not is_solvable(initial_state):
            random.shuffle(initial_state)

    # Display initial puzzle state
    print("Initial state of the puzzle:")
    print_puzzle(initial_state)

    # Solve the puzzle using BFS
    print("Solving the puzzle...")
    solution = bfs(initial_state)

    if solution is None:
        print("The puzzle is unsolvable.")
    else:
        print(f"Solution found in {len(solution) - 1} moves.")
        print("Shortest path found:")
        for i, step in enumerate(solution):
            print(f"Step {i + 1}:")
            print_puzzle(step)

if __name__ == "__main__":
    main()
