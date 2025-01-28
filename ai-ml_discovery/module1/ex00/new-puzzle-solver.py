#!/usr/bin/env python3
from collections import deque
import sys
import random

# Goal state of the puzzle
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# Possible moves (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#Check if the current state matches the goal state.
def is_goal(state):
    return state == goal_state

# Return all possible states that can be reached by moving the empty space (0).
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

#Check if the puzzle is solvable based on the number of inversions.
def is_solvable(puzzle):
    inversions = 0
    puzzle = [x for x in puzzle if x != 0]  # Remove the empty space (0)
    
    # Count inversions
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j]:
                inversions += 1

    return inversions % 2 == 0

#Perform breadth-first search to find the shortest solution to the puzzle.
def bfs(start_state):
    if is_goal(start_state):
        print("The puzzle is already solved")
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
    for i in range(0, len(puzzle), 3):
        print(puzzle[i:i+3])
    print()
'''
def load_from_file(filename):
    """Load the puzzle from a file."""
    try:
        with open(filename, 'r') as f:
            return [int(x) for x in f.read().split()]
    except Exception as e:
        print(f"Error reading file: {e}")
        return None'''

def main():
    initial_state = None

    # Accept the initial state from command line argument or generate a random one
    if len(sys.argv) == 10:  # 9 puzzle numbers
        try:
            # Try converting all arguments to integers
            initial_state = [int(arg) for arg in sys.argv[1:]]
            if 0 not in initial_state:  # Check if 0 is missing
                print("Error: Puzzle must include 0 (empty space).")
                return
        except ValueError:
            print("Error: All inputs must be integers. Please provide a valid puzzle configuration.")
            return
        
    elif len(sys.argv) == 2:  # File option
        filename = sys.argv[1]
       #initial_state = load_from_file(filename)
    else:  # Random puzzle generation
        initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
        random.shuffle(initial_state)
        while not is_solvable(initial_state):
            random.shuffle(initial_state)

    # Check if initial state is valid and solvable
    if initial_state is None or not is_solvable(initial_state):
        print("The puzzle is unsolvable.")
        return

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












#for testet generator random puzzle
#python puzzle_solver.py


#Solve Specific Puzzle (Already Solved):clear

# python puzzle_solver.py 1 2 3 4 0 5 6 7 8 
# python puzzle_solver.py 1 2 3 4 5 6 8 7 0 -this is declaration puzzle goal c'est pour ca puzzle is unrouveble - 
# python puzzle_solver.py 1 2 3 4 5 6 7 8 0 - not move because goal puzzle
#  python puzzle_solver.py 1 2 3 4 5 6 7 8 9 - Puzzle must include 0 (empty space).




# not to me for stady

#inversion  An inversion refers to a pair of tiles where a higher-numbered tile appears before a lower-numbered one in the puzzle
#For example, in the list [1, 2, 3, 5, 4], the pair (5, 4) is an inversion because 5 > 4 but 5 appears before 4.
# Purpose of inversions = 0:

#The variable inversions is initialized to 0 at the beginning of the function to keep track of how many inversions there are in the puzzle.
#Each time an inversion is detected (i.e., a higher-numbered tile appears before a lower-numbered tile), inversions is incremented by 1.


#divmod =  Converting Index to Row and Column:For example, if index_of_zero = 4:

#row, col = divmod(4, 3) results in row = 1 and col = 1, which corresponds to the second row and second column in a 3x3 grid.
#random.shuffle(initial_state) is used to generate a random initial state of the puzzle:random.shuffle() is used to randomly reorder the elements of the list.
#BFS -Breadth-first search on the state space tree-This always finds a goal state nearest to the root.BFS explores all neighbor nodes at the present depth before moving on to nodes at the next depth level.
