#!/usr/bin/env python3
import sys
import random
import heapq  # For the priority queue in A*
from collections import deque


# Goal state of the puzzle
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Possible moves (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#Check if the current state matches the goal state.
def is_goal(state):
    return state == goal_state

#Print the current state of the puzzle.
def print_puzzle(puzzle):
    for i in range(0, len(puzzle), 3):
        print(puzzle[i:i+3])
    print()

# Calculate the Manhattan distance heuristic.
def manhattan_distance(state):
    distance = 0
    for i, value in enumerate(state):
        if value != 0:  # Skip the empty space (0)
            goal_position = goal_state.index(value)
            goal_row, goal_col = divmod(goal_position, 3)
            current_row, current_col = divmod(i, 3)
            distance += abs(goal_row - current_row) + abs(goal_col - current_col)
    return distance

#Return all possible states that can be reached by moving the empty space (0).
def get_possible_moves(puzzle):
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

# Check if the puzzle is solvable based on the number of inversions.
def is_solvable(puzzle):
    inversions = 0
    puzzle = [x for x in puzzle if x != 0]  # Remove the empty space (0)
    
    # Count inversions
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j]:
                inversions += 1

    return inversions % 2 == 0

#Solve the puzzle using A* algorithm.
def a_star(start_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state, []))  # (f, g, state, path)
    visited = set()
    visited.add(tuple(start_state))

    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)

        if is_goal(current_state):
            return path + [current_state]

        # Explore all possible moves
        for next_state in get_possible_moves(current_state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                new_path = path + [current_state]
                new_g = g + 1
                new_f = new_g + manhattan_distance(next_state)
                heapq.heappush(open_list, (new_f, new_g, next_state, new_path))

    return []  # No solution found


def main():
    initial_state = None
    if len(sys.argv) == 10:
        try:
            # Try converting each argument to an integer
            initial_state = [int(arg) for arg in sys.argv[1:]]
        except ValueError:
            # Catch the ValueError if any input is not an integer
            print("Error: All inputs must be integers. Please provide a valid puzzle configuration.")
            sys.exit(1)
        if any(x < 0 or x >= 9 for x in initial_state):
            print("Error : All numbers in the puzzle must be between 0 and 8")
            sys.exit(1)
        # Check if 0 is included in the puzzle
        if 0 not in initial_state:
            print("Error: Puzzle must include 0 (empty space).")
            sys.exit(1)
        if len(initial_state) != 9:
            print("Error: Puzzle must contain exactly 9 elements")
        
        if not is_solvable(initial_state):
            print("The puzzle is unsolvable.")
            return
    else:
        # Generate a random state
        initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Start with a solved puzzle
        random.shuffle(initial_state)
        while not is_solvable(initial_state):
            random.shuffle(initial_state)
    
    # Display initial puzzle state
    print("Initial state of the puzzle:")
    print_puzzle(initial_state)

    # Solve the puzzle using A* algorithm
    print("Solving the puzzle with A* algorithm...")
    solution = a_star(initial_state)

    if not solution:
        print("The puzzle is unsolvable.")
    else:
        # Display the number of moves and the solution path
        print(f"Solution found in {len(solution) - 1} moves.")
        print("Solution path:")
        for i, step in enumerate(solution):
            print(f"Step {i + 1}:")
            print_puzzle(step)


if __name__ == "__main__":
    main()
