"""
Prodigy Infotech - Task 04
Sudoku Solver

Solves a 9x9 Sudoku puzzle using the backtracking algorithm.
Input: a 9x9 grid where 0 represents an empty cell.
Output: the completed, solved Sudoku grid printed to the console.
"""


def print_grid(grid):
    """Nicely print the 9x9 Sudoku grid with box separators."""
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        row_str = ""
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row_str += "| "
            row_str += (str(grid[r][c]) if grid[r][c] != 0 else ".") + " "
        print(row_str)


def find_empty_cell(grid):
    """Return the (row, col) of the next empty cell (0), or None if full."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None


def is_valid(grid, row, col, num):
    """Check if placing `num` at grid[row][col] breaks Sudoku rules."""
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in (grid[r][col] for r in range(9)):
        return False

    # Check 3x3 sub-grid
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == num:
                return False

    return True


def solve_sudoku(grid):
    """
    Solve the Sudoku puzzle in-place using backtracking.
    Returns True if solved, False if no solution exists.
    """
    empty = find_empty_cell(grid)
    if not empty:
        return True  # No empty cells left -> solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num  # Tentatively place the number

            if solve_sudoku(grid):  # Recurse
                return True

            grid[row][col] = 0  # Backtrack: undo and try next number

    return False  # Triggers backtracking in the caller


def get_puzzle_from_user():
    """
    Let the user type in their own puzzle, row by row.
    Each row: 9 digits (0 for blank), space or no space separated.
    Example row: 5 3 0 0 7 0 0 0 0
    """
    print("Enter the Sudoku puzzle row by row (use 0 for empty cells).")
    print("You can type digits with or without spaces, e.g. '530070000' or '5 3 0 0 7 0 0 0 0'.\n")
    grid = []
    for r in range(9):
        while True:
            raw = input(f"Row {r + 1}: ").strip().replace(" ", "")
            if len(raw) == 9 and raw.isdigit():
                grid.append([int(ch) for ch in raw])
                break
            print("Invalid input. Please enter exactly 9 digits (0-9).")
    return grid


def main():
    # A classic sample puzzle (0 = empty cell)
    sample_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("=" * 40)
    print("       SUDOKU SOLVER - Task 04")
    print("=" * 40)
    print("\n1. Solve the built-in sample puzzle")
    print("2. Enter your own puzzle")
    choice = input("\nChoose an option (1/2): ").strip()

    if choice == "2":
        puzzle = get_puzzle_from_user()
    else:
        puzzle = sample_puzzle

    print("\nPuzzle to solve:\n")
    print_grid(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku:\n")
        print_grid(puzzle)
    else:
        print("\nNo solution exists for the given puzzle.")


if __name__ == "__main__":
    main()
