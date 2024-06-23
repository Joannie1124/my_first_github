def parse_matrix(matrix_str):
    #Parses a matrix input string into a dictionary representation.
    rows = matrix_str.split('|')
    matrix = {}
    for i, row in enumerate(rows):
        elements = list(map(int, row.split(',')))
        for j, elem in enumerate(elements):
            matrix[(i, j)] = elem
    return matrix, len(rows)

def multiply_matrices(U, V, n):
    #Multiplies two nxn matrices represented as dictionaries.
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U.get((i, k), 0) * V.get((k, j), 0) for k in range(n))
    return M

def format_matrix(matrix, n):
    #Formats a dictionary representation of a matrix into a string with square brackets.
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(str(matrix.get((i, j), 0)))
        rows.append(f"[{','.join(row)}]")
    return '\n'.join(rows)

def main():
    # Input matrices
    U_input = input("Enter matrix U: ")  # e.g., "1,2|3,4"
    V_input = input("Enter matrix V: ")  # e.g., "2,3|4,1"
    
    # Parse the matrices
    U, n = parse_matrix(U_input)
    V, _ = parse_matrix(V_input)
    
    # Multiply the matrices
    M = multiply_matrices(U, V, n)
    
    # Format the resulting matrix
    M_output = format_matrix(M, n)
    
    # Print the result
    print("M = U x V")
    print(M_output)

# Execute the main function
if __name__ == "__main__":
    main()
