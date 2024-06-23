import random
import os

def read_maze(file_name):#讀取file的函數
    try:
        with open(file_name, 'r') as file:
            maze = {}
            lines = file.readlines()
            for r, line in enumerate(lines):
                for c, char in enumerate(line.strip()):
                    if char == '1':
                        maze[(r, c)] = 1
                    else:
                        maze[(r, c)] = 0
            return maze, len(lines), len(lines[0].strip())
    except IOError:#檢測是否有IOError
        print(f"Error: Cannot open {file_name}. Please provide a valid file name.")
        return None, 0, 0

def generate_path(maze, N, M): #路徑
    r, c = 0, 0
    while r < (N - 1 )or c < (M - 1):
        maze[(r, c)] = 2
        if r == N - 1:
            c += 1
        elif c == M - 1:
            r += 1
        else:
            if random.choice([True, False]):
                r += 1
            else:
                c += 1
    maze[(N-1, M-1)] = 2 #maze的大小

def add_obstacles(maze, min_obstacles, N, M):#隨機放入障礙物
    empty_cells = [(r, c) for r in range(N) for c in range(M) if maze[(r, c)] == 0]
    obstacles = random.sample(empty_cells, min_obstacles)
    for (r, c) in obstacles:
        maze[(r, c)] = 1

def set_obstacle(maze, N, M):#擺放障礙物
    try:
        r, c = map(int, input("Enter the coordinates to set an obstacle,e.g. i,j: ").split())
        if (r, c) in maze and 0 <= r < N and 0 <= c < M:
            if maze[(r, c)] == 2:
                print("Error: Cannot place an obstacle on the path.")
            else:
                maze[(r, c)] = 1
        else:
            print("KeyError in set_obstacle function.'Invalid coordinates.Please input coordinates within the range.")
    except ValueError:#檢測是否有ValueError
        print("ValueError in set_obstacle function.Need to be coordinates")

def remove_obstacle(maze, N, M):#移除障礙物
    try:
        r, c = map(int, input("Enter the coordinates to remove an obstacle, e.g. i,j: ").split())
        if (r, c) in maze and 0 <= r < N and 0 <= c < M:
            if maze[(r, c)] == 2:
                print("Error: Cannot remove the path.")
            else:
                maze[(r, c)] = 0
        else:
            print("KeyError in remove_obstacle function.'Invalid coordinates.Please input coordinates within the range.'")
    except ValueError:#檢測是否有ValueError
        print("ValueError in remove_obstacle function.Need to be coordinates ")

def print_maze(maze, N, M):#最後print出maze
    for r in range(N):
        for c in range(M):#選擇放入空格、X或是O
            if maze[(r, c)] == 0:
                print(' ', end='')
            elif maze[(r, c)] == 1:
                print('X', end='')
            else:
                print('O', end='')
        print()

def main():#最後的總函數(包含其他的所有函數)
    default_path = "C:\\Users\\USER\\Downloads\\"#開啟檔案的絕對路徑
    files = ["grid77.txt", "grid99.txt"]
    
    while True:
        file_name = input("Enter the file name : ")
        if file_name in files:
            full_path = os.path.join(default_path, file_name)
            maze, N, M = read_maze(full_path)
            if maze is not None:
                break
        else:
            print("IOError occurred in main function. File not found Please enter a valid file name")

    generate_path(maze, N, M)

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles (0-55): "))
            if min_obstacles < 0 or min_obstacles >= N * M:
                print("ValueError occurred in main function.Invalid number of obstacles.")
            else:
                break
        except ValueError:
            print("ValueError occurred in main function.Invalid number of obstacles.")

    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)

    while True:#選擇要執行什麼
        print("\nOptions:")
        print("1. Set an obstacle")
        print("2. Remove an obstacle")
        print("3. Print the maze")
        print("4. Exit")

        option = input("Enter your choice: ")
        if option == '1':
            set_obstacle(maze, N, M)
            print_maze(maze, N, M)
        elif option == '2':
            remove_obstacle(maze, N, M)
            print_maze(maze, N, M)
        elif option == '3':
            print_maze(maze, N, M)
        elif option == '4':
            break
        else:
            print("Error: Invalid option. Please choose again.")

if __name__ == "__main__":
    main()