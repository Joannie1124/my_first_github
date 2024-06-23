n=int(input("Enter the size of the grid:"))   

#construct a matrix
matrix=[["_"for i in range(n)]for j in range(n)]

for i in range(n):
	for j in range(n):
		print(matrix[i][j],end=" ")
	print()

cell_cordinate=""
new_value=""

while True:
	cell_cordinate=input("Enter the cell cordinates to edit:  ") #row,colume
	if cell_cordinate=="done":
		break
	row, col=cell_cordinate.split(",") #str->row,col
	row, col=int(row), int(col) #str->int
	new_value=input("Enter the new value for the cell: ")
	matrix[row][col]=new_value
	
	for i in range (n):
		print(" ".join(matrix[i]))






