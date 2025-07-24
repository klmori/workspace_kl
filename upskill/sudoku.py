def is_clear_path_with_zeros(grid, x1, y1, x2, y2):
    """Check if the path between (x1, y1) and (x2, y2) contains only zeros."""
    
    # *Vertical Check (Same Column)*
    if x1 == x2:
        y_start, y_end = sorted([y1, y2])
        return all(grid[x1][y] == 0 for y in range(y_start + 1, y_end))

    # *Horizontal Check (Same Row)*
    if y1 == y2:
        x_start, x_end = sorted([x1, x2])
        return all(grid[x][y1] == 0 for x in range(x_start + 1, x_end))

    # *Diagonal Check*

    if abs(x1 - x2) == abs(y1 - y2):
        x_step = 1 if x2 > x1 else -1
        y_step = 1 if y2 > y1 else -1
        print(f"Diagonal Check: ({x1}, {y1}) to ({x2}, {y2})")
        print(f"Step: ({x_step}, {y_step})")
        x, y = x1 + x_step, y1 + y_step
        while (x, y) != (x2, y2):
            if grid[x][y] != 0:
                return False
            x += x_step
            y += y_step
        return True
    
    # *Cross-Row Check* (Allow if numbers are in different rows with only zeros in between)
    min_x, max_x = sorted([x1, x2])
    min_y, max_y = sorted([y1, y2])
    print(f'min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}')
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in [(x1, y1), (x2, y2)] and grid[x][y] != 0:
                return False
    return True


def remove_numbers(grid, x1, y1, x2, y2):
    """Remove numbers if they are the same or sum to 10, and only zeros exist between them."""
    if grid[x1][y1] == 0 or grid[x2][y2] == 0:
        return False  # One of the selected cells is already empty

    if is_clear_path_with_zeros(grid, x1, y1, x2, y2):
        num1, num2 = grid[x1][y1], grid[x2][y2]
        if num1 == num2 or num1 + num2 == 10:
            grid[x1][y1] = grid[x2][y2] = 0  # Remove numbers
            return True
    return False


# Example Grid
grid = [
    [3, 0, 7, 0, 5],
    [0, 4, 0, 6, 9],
    [2, 0, 8, 0, 5],
    [0, 1, 0, 9, 0],
    [7, 9, 3, 0, 2]
]

# Example: Selecting (0, 2) and (2, 0) → Allowed if only zeros are between them
x1, y1 = 4, 2  
x2, y2 = 1, 3  
print(grid[y1][x1],'number at (x1, y1)') 
print(grid[y2][x2],'number at (x2, y2)')
if remove_numbers(grid, x1, y1, x2, y2):
    print("Numbers removed!")
else:
    print("Invalid selection!")

# Print updated grid
for row in grid:
    print(row)