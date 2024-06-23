import random

#construct a matrix
matrix=[["   "for i in range(0,9)]for j in range(9)]

a=['a','b','c','d','e','f','g','h','i']

print('   a'+'   b'+'   c'+'   d'+'   e'+'   f'+'   g'+'   h'+'   i   ')
for i in range(0,9):
    print(' +'+'---+'*9)
    print(i+1,end='|')
    for j in range(9):
        print(matrix[i][j],end='|')
    print()
print(' +'+'---+'*9)

print("Enter the column followed by the row (ex: a5).To add or remove a flag, add 'f' to the cell (ex: a5f).Type 'help' to show this message again")

while True:
    n=input("Enter the cell(10 mines left):")
    row, col=n.split(" ") #str->row,col
    if row=='a':
        row=0
    if row=='b':
        row=1
    if row=='c':
        row=2
    if row=='d':
        row=3
    if row=='e':
        row=4
    if row=='f':
        row=5
    if row=='g':
        row=6
    if row=='h':
        row=7
    if row=='i':
        row=8
    row, col=int(row), (int(col)-1) #str->int
    matrix[col][row]=' r '

    print('   a'+'   b'+'   c'+'   d'+'   e'+'   f'+'   g'+'   h'+'   i   ')
    for i in range(0,9):
        print(' +'+'---+'*9)
        print(i+1,end='|')
        for j in range(9):
            print(matrix[i][j],end='|')
        print()
    print(' +'+'---+'*9)






    



