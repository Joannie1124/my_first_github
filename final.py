def pascal_triangle_element(row, col):
    """Recursive function to calculate element at row and col in Pascal's Triangle"""
    if col == 0 or col == row:
        return 1
    else:
        return pascal_triangle_element(row - 1, col - 1) + pascal_triangle_element(row - 1, col)

def generate_pascals_triangle(n):
    """Function to generate Pascal's Triangle up to n rows"""
    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            current_row.append(pascal_triangle_element(row, col))
        triangle.append(current_row)
    return triangle

def print_pascals_triangle(triangle, orientation):
    """Function to print Pascal's Triangle with different orientations"""
    max_row_length = len(' '.join(map(str, triangle[-1])))
    
    if orientation == 'normal':
        for row in triangle:
            print(' '.join(map(str, row)).center(max_row_length))
    
    elif orientation == 'reversed':
        for row in reversed(triangle):
            print(' '.join(map(str, row)).center(max_row_length))
    
    elif orientation == 'right':
        for row in triangle:
            print(' '.join(map(str, row)).ljust(max_row_length))
    
    elif orientation == 'left':
        for row in triangle:
            print(' '.join(map(str, row)).rjust(max_row_length))
    
# Read number of rows and orientation from user
# Loop to repeatedly prompt the user for a valid number of rows
while True:
    try:
        n = int(input("Height of Pascal's triangle: "))
        if n < 1:
            print("Invalid input. Please enter an integer greater than or equal to 1.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer greater than or equal to 1.")

valid_orientations = {'normal', 'reversed', 'left', 'right'}

# Loop to repeatedly prompt the user for a valid orientation
while True:
    orientation = input("Direction of triangle ('normal', 'reversed', 'left' or 'right'):  ").strip().lower()
    if orientation in valid_orientations:
        break
    else:
        print("Invalid input for direction. Please enter 'normal', 'reversed', 'left', or 'right'.")

# Generate Pascal's Triangle with the specified number of rows
pascals_triangle = generate_pascals_triangle(n)

# Print Pascal's Triangle with the specified orientation
print_pascals_triangle(pascals_triangle, orientation)

