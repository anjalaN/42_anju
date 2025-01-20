#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    puzzle_solver_ad.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/16 15:28:55 by arajapak          #+#    #+#              #
#    Updated: 2024/12/16 15:28:59 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


'''
from collections import deque

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def is_goal(state):
    return state == goal_state

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

def bfs(start_state):
    if is_goal(start_state):
        return [start_state]
    
    queue = deque([(start_state, [])])  # Queue stores (state, path)
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if tuple(current_state) in visited:
            continue
        visited.add(tuple(current_state))

        # Print the current puzzle state at each step
        print("Current Puzzle State:")
        print_puzzle(current_state)

        for next_state in get_possible_moves(current_state):
            if is_goal(next_state):
                return path + [current_state, next_state]
            queue.append((next_state, path + [current_state]))

    return None  # If no solution is found

# Function to print the puzzle state
def print_puzzle(puzzle):
    for i in range(0, len(puzzle), 3):
        print(puzzle[i:i+3])
    print()

def main():
    initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Example starting state
    print("Initial Puzzle:")
    print_puzzle(initial_state)
    
    solution = bfs(initial_state)

    if solution is None:
        print("The puzzle is unsolvable.")
    else:
        print("Solution found:")
        for step in solution:
            print_puzzle(step)
            

if __name__ == "__main__":
    main()'''

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




































































