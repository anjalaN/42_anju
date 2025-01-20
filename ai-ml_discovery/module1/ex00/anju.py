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

#Exercise 00
• Launch the program multiple times and verify the expected features:
◦ It must generate a random 3x3 initial puzzle.
◦ It must solve the puzzle or indicate that the puzzle is unsolvable.
◦ It must show the diﬀerent steps, and you have to verify these steps.
• Then try to launch the program with a speciﬁc initial state (from a ﬁle or command line).
If this is not possible, the evaluation stops and the ﬁnal mark is 0.
• Then make the same veriﬁcations as above, in the following cases:
◦ The initial state of the puzzle is an already solved puzzle. In this case, no moves should be needed.
◦ The initial state is an unsolvable puzzle.
◦ Try a random initial state of your choice.
 Yes
 No
Exercise 01
Exercise 01
• Launch the program multiple times and verify the expected features:
◦ It must generate a random 3x3 initial puzzle.
◦ It must solve the puzzle or indicate that the puzzle is unsolvable.
◦ It must display all the diﬀerent solutions found for the puzzle. There should usually be multiple paths.
◦ It must choose the shortest path and show the steps required. You must verify these steps.
• Then try launching the program with a speciﬁc initial state (from a ﬁle or command line).
Perform the same checks as above, in the following cases:
◦ The initial state of the puzzle is an already solved puzzle. In this case, no moves should be needed.
◦ The initial state is an unsolvable puzzle.
◦ Try a random initial state of your choice.Exercise 00
• Launch the program multiple times and verify the expected features:
◦ It must generate a random 3x3 initial puzzle.
◦ It must solve the puzzle or indicate that the puzzle is unsolvable.
◦ It must show the diﬀerent steps, and you have to verify these steps.
• Then try to launch the program with a speciﬁc initial state (from a ﬁle or command line).
If this is not possible, the evaluation stops and the ﬁnal mark is 0.
• Then make the same veriﬁcations as above, in the following cases:
◦ The initial state of the puzzle is an already solved puzzle. In this case, no moves should be needed.
◦ The initial state is an unsolvable puzzle.
◦ Try a random initial state of your choice.
 Yes
 No
Exercise 01
Exercise 01
• Launch the program multiple times and verify the expected features:
◦ It must generate a random 3x3 initial puzzle.
◦ It must solve the puzzle or indicate that the puzzle is unsolvable.
◦ It must display all the diﬀerent solutions found for the puzzle. There should usually be multiple paths.
◦ It must choose the shortest path and show the steps required. You must verify these steps.
• Then try launching the program with a speciﬁc initial state (from a ﬁle or command line).
Perform the same checks as above, in the following cases:
◦ The initial state of the puzzle is an already solved puzzle. In this case, no moves should be needed.
◦ The initial state is an unsolvable puzzle.
◦ Try a random initial state of your choice.


@@@@@@@@@@@@@@@@@@@@exoo@@@@@@@@@
   import random

def generate_random_state():
  """Generates a random initial state for the 8-Puzzle."""
  numbers = list(range(1, 9)) + [0]  # 0 represents the empty space
  random.shuffle(numbers)
  state = [numbers[0:3], numbers[3:6], numbers[6:]]
  return state

def is_solvable(state):
  """Checks if the given puzzle state is solvable."""
  flattened_state = [num for row in state for num in row if num != 0]
  inversions = 0

  for i in range(len(flattened_state)):
    for j in range(i + 1, len(flattened_state)):
      if flattened_state[i] > flattened_state[j]:
        inversions += 1

  blank_row = 0
  for i, row in enumerate(state):
    if 0 in row:
      blank_row = i
      break

  if (inversions % 2 == 0 and blank_row % 2 == 0) or (inversions % 2 == 1 and blank_row % 2 == 1):
    return True
  else:
    return False

def generate_moves(state):
  """Generates all possible moves from the given state."""
  moves = []
  empty_row, empty_col = find_empty_space(state)

  if empty_row > 0:  # Move empty space up
    moves.append(("up", move_empty_space(state, empty_row, empty_col, empty_row - 1)))

  if empty_row < 2:  # Move empty space down
    moves.append(("down", move_empty_space(state, empty_row, empty_col, empty_row + 1)))

  if empty_col > 0:  # Move empty space left
    moves.append(("left", move_empty_space(state, empty_row, empty_col, empty_col - 1)))

  if empty_col < 2:  # Move empty space right
    moves.append(("right", move_empty_space(state, empty_row, empty_col, empty_col + 1)))

  return moves

def move_empty_space(state, empty_row, empty_col, new_row, new_col):
  """Moves the empty space in the given direction."""
  new_state = [row[:] for row in state]  # Create a copy of the state
  new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
  return new_state

def find_empty_space(state):
  """Finds the row and column of the empty space (0)."""
  for row in range(3):
    for col in range(3):
      if state[row][col] == 0:
        return row, col

def dfs(state, goal_state, moves):
  """Performs Depth-First Search to find a solution."""
  if state == goal_state:
    return moves
  
  for next_state, move in generate_moves(state):
    path = dfs(next_state, goal_state, moves + [move])
    if path:
      return path
  return None

def solve_puzzle(initial_state):
  """Solves the 8-Puzzle."""
  if not is_solvable(initial_state):
    return "Unsolvable Puzzle"

  goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0 represents the empty space
  solution = dfs(initial_state, goal_state, [])
  if solution:
    print("Solution:")
    for move in solution:
      print(move)
  else:
    return "No solution found"

# Generate random initial state
initial_state = generate_random_state()

# Print initial state
print("Initial State:")
for row in initial_state:
  print(row)

# Solve the puzzle and print the solution
solution = solve_puzzle(initial_state)
print(solution)





@@@@@@@@@@@@@@@@@@@@@@ex2@@@@@@@@@@@@@@@@@
import random
from collections import deque
import sys

# Goal state for the 3x3 puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Directions for moving the empty space: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col)

# Function to print the puzzle state in a readable way
def print_puzzle(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else ' ' for x in row))

# Function to check if a given state is solvable
def is_solvable(state):
    flattened_state = [num for row in state for num in row if num != 0]
    inversions = 0
    for i in range(len(flattened_state)):
        for j in range(i + 1, len(flattened_state)):
            if flattened_state[i] > flattened_state[j]:
                inversions += 1
    blank_row = next(i for i, row in enumerate(state) if 0 in row)
    if (inversions % 2 == 0 and blank_row % 2 == 0) or (inversions % 2 == 1 and blank_row % 2 == 1):
        return True
    return False

# Function to get all possible moves from the current puzzle state
def get_possible_moves(state):
    moves = []
    zero_row, zero_col = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)
    
    for dr, dc in directions:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]  # Make a copy of the state
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
            moves.append(new_state)
    
    return moves

# BFS to solve the puzzle
def bfs(initial_state):
    if not is_solvable(initial_state):
        print("The puzzle is unsolvable.")
        return None
    
    # Queue holds tuples of (state, path)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        
        # Check if the goal state is reached
        if current_state == goal_state:
            return path  # Return the steps that lead to the solution
        
        visited.add(tuple(tuple(row) for row in current_state))
        
        for next_state in get_possible_moves(current_state):
            state_tuple = tuple(tuple(row) for row in next_state)
            if state_tuple not in visited:
                queue.append((next_state, path + [next_state]))
    
    return None

# Generate a random puzzle state
def generate_random_state():
    numbers = list(range(1, 9)) + [0]
    random.shuffle(numbers)
    state = [numbers[0:3], numbers[3:6], numbers[6:]]
    return state

def main():
    # Read initial state from command line arguments or generate random state
    if len(sys.argv) > 1:
        initial_state = [list(map(int, sys.argv[i:i+3])) for i in range(1, len(sys.argv), 3)]
    else:
        initial_state = generate_random_state()

    print("Initial state of the puzzle:")
    print_puzzle(initial_state)

    print("Solving the puzzle...")
    path = bfs(initial_state)
    
    if path:
        print(f"Solution found in {len(path)} moves.")
        for i, step in enumerate(path, start=1):
            print(f"Step {i}:")
            print_puzzle(step)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
