def char_to_num(char):
    if char.isdigit():
        return int(char)
    return ord(char.upper()) - ord('A') + 10 

def num_to_char(num):
    if num <= 9:
        return str(num)
    return chr(num - 10 + ord('A')) 

def print_grid(grid):
    for row in grid:
        print(" ".join(num_to_char(num) for num in row))

def is_valid(grid, row, col, num, n, subgrid_height, subgrid_width):
    for x in range(n):
        if grid[row][x] == num:
            return False
        if grid[x][col] == num:
            return False
    start_row = row - row % subgrid_height
    start_col = col - col % subgrid_width
    for i in range(subgrid_height):
        for j in range(subgrid_width):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid, n, subgrid_height, subgrid_width):
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:
                for num in range(1, n + 1):
                    if is_valid(grid, row, col, num, n, subgrid_height, subgrid_width):
                        grid[row][col] = num
                        if solve_sudoku(grid, n, subgrid_height, subgrid_width):
                            return True
                        grid[row][col] = 0
                return False
    return True

def input_sudoku():
    n = int(input("Enter the size of the grid (e.g., 9 for a 9x9 grid): "))
    subgrid_height = int(input(f"Enter the subgrid height (e.g., 3 for a 9x9 grid with 3x3 subgrids): "))
    subgrid_width = int(input(f"Enter the subgrid width (e.g., 3 for a 9x9 grid with 3x3 subgrids): "))
    
    grid = []
    print(f"Enter the Sudoku grid row by row. Use 0 for empty cells. Use numbers and letters (A-G).")
    for i in range(n):
        while True:
            row = input(f"Enter row {i + 1} ({n} characters separated by spaces): ").strip()
            try:
                row_values = list(map(char_to_num, row.split()))
                if len(row_values) == n:
                    grid.append(row_values)
                    break
                else:
                    print(f"Invalid input. Please enter exactly {n} characters separated by spaces.")
            except ValueError:
                print("Invalid input. Please use numbers or letters.")
    return grid, n, subgrid_height, subgrid_width

if __name__ == "__main__":
    sudoku_grid, n, subgrid_height, subgrid_width = input_sudoku()

    print("Sudoku grid before solving:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid, n, subgrid_height, subgrid_width):
        print("Sudoku solved successfully!")
        print_grid(sudoku_grid)
    else:
        print("No solution exists for the given Sudoku.")
