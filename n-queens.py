import time

def print_solution(board):
    """Utility to print the board configuration."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_nqueens_exhaustive(board, row, n, solutions, start_time, timeout):
    """Recursive function to solve the N-Queens problem using DFS with timeout."""
    # Check timeout
    if time.time() - start_time > timeout:
        return True  # Signal timeout to caller

    if row == n:
        # Found a solution, add to the list
        solutions.append(["".join("Q" if col else "." for col in r) for r in board])
        return False  # Continue search

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place a queen
            board[row][col] = True
            if solve_nqueens_exhaustive(board, row + 1, n, solutions, start_time, timeout):
                return True  # Propagate timeout
            # Backtrack
            board[row][col] = False
    return False

def exhaustive_nqueens(n, timeout=10):
    """Driver function for solving N-Queens using exhaustive DFS with timeout."""
    board = [[False for _ in range(n)] for _ in range(n)]
    solutions = []
    start_time = time.time()

    timeout_reached = solve_nqueens_exhaustive(board, 0, n, solutions, start_time, timeout)
    exec_time = time.time() - start_time

    if timeout_reached:
        print(f"Timeout reached after {exec_time:.2f} seconds.")
    else:
        print(f"Exhaustive search completed in {exec_time:.2f} seconds.")

    return solutions, exec_time

# Test the function with N = 10
if __name__ == "__main__":
    n = 100
    timeout = 60  # Set timeout in seconds
    solutions, exec_time = exhaustive_nqueens(n, timeout=timeout)

    print(f"Exhaustive Search for N={n}")
    print(f"Solutions Found: {len(solutions)}")
    print(f"Execution Time: {exec_time:.2f} seconds")
    # Uncomment to print solutions
    # for sol in solutions:
    #     for row in sol:
    #         print(row)
    #     print("\n")
