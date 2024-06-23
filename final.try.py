def flood_fill(matrix, x, y, target_color):
    rows = len(matrix)
    cols = len(matrix[0])
    original_color = matrix[x][y]
    if original_color == target_color:
        return
    
    queue = [(x, y)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while queue:
        current_x, current_y = queue.pop(0)
        matrix[current_x][current_y] = target_color
        
        for direction in directions:
            new_x = current_x + direction[0]
            new_y = current_y + direction[1]
            
            if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] == original_color:
                queue.append((new_x, new_y))
                matrix[new_x][new_y] = target_color

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Main program
matrix = []
print("Enter matrix rows (type 'q' to stop):")

# Read matrix until 'q' is entered
while True:
    row_input = input().strip()
    if row_input == 'q':
        break
    row = list(map(int, row_input.split()))
    matrix.append(row)

print("Matrix input complete.")
print_matrix(matrix)

# Process target inputs
while True:
    target_input = input("Enter target location and color (x y k) (type 'q' to stop): ").strip()
    if target_input == 'q':
        break
    x, y, k = map(int, target_input.split())
    
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        target_color = k
        flood_fill(matrix, x, y, target_color)
        print("Matrix after filling from ({},{}) with color {}: ".format(x, y, k))
        print_matrix(matrix)
    else:
        print("Invalid target location.")

print("Program ended.")
