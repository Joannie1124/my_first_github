import os
import random
import msvcrt
import time
import shutil

# Define game symbols
SNAKE_HEAD = 'O'
SNAKE_BODY = 'o'
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
OBSTACLE = '#'
EMPTY_CELL = ' '

# Define directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# Initialize game variables
snake = [(0, 2), (0, 1), (0, 0)]  # Initial snake position
direction = RIGHT
normal_food_count = 0
special_food_count = 0
game_over = False
paused = False

def generate_food(snake, obstacles, width, height):
    
    
    while True:
        food_pos = (random.randint(0, height - 1), random.randint(0, width - 1))
        if food_pos not in snake and food_pos not in obstacles:
            return food_pos

def generate_obstacles(width, height):
    obstacles = set()
    num_obstacles = int(width * height * 0.05)  # 5% of the game screen
    for _ in range(num_obstacles):
        while True:
            obstacle_length = random.randint(5, 10)
            x = random.randint(0, width - 1)
            y = random.randint(0, height - obstacle_length)
            new_obstacle = [(y + i, x) for i in range(obstacle_length)]
            if all(pos not in obstacles for pos in new_obstacle):
                obstacles.update(new_obstacle)
                break
    return obstacles

def draw_screen(snake, normal_food_pos, special_food_pos, obstacles, width, height):
    os.system('cls' if os.name == 'nt' else 'clear')
    screen = [[EMPTY_CELL] * width for _ in range(height)]
    for y, x in snake:
        screen[y][x] = SNAKE_HEAD if (y, x) == snake[0] else SNAKE_BODY
    screen[normal_food_pos[0]][normal_food_pos[1]] = NORMAL_FOOD
    screen[special_food_pos[0]][special_food_pos[1]] = SPECIAL_FOOD
    for y, x in obstacles:
        screen[y][x] = OBSTACLE
    for row in screen:
        print(' '.join(row))

def main():
    global direction, normal_food_count, special_food_count, game_over, paused
    size = shutil.get_terminal_size()
    width, height = size.columns // 2, size.lines - 2
    obstacles = generate_obstacles(width, height)
    
    normal_food_pos = generate_food(snake, obstacles, width, height)
    
    special_food_pos = generate_food(snake, obstacles, width, height)
    
    while not game_over:
        if not paused:
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            # Wrap around screen
            new_head = (new_head[0] % height, new_head[1] % width)

            if new_head in snake[1:] or new_head in obstacles:
                game_over = True
                break

            snake.insert(0, new_head)

            if new_head == normal_food_pos:
                normal_food_count += 1
                normal_food_pos = generate_food(snake, obstacles, width, height)
            elif new_head == special_food_pos:
                if len(snake) > 1:
                    snake.pop()
                special_food_count += 1
                special_food_pos = generate_food(snake, obstacles, width, height)

            else:
                snake.pop()

            draw_screen(snake, normal_food_pos, special_food_pos, obstacles, width, height)
            time.sleep(0.1)
        
        # Handle key input
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()

            if key == 'w' and direction != DOWN:
                direction = UP
            elif key == 's' and direction != UP:
                direction = DOWN
            elif key == 'a' and direction != RIGHT:
                direction = LEFT
            elif key == 'd' and direction != LEFT:
                direction = RIGHT
            elif key == ' ':
                paused = not paused

    print(f"Game Over! Normal food eaten: {normal_food_count}, Special food eaten: {special_food_count}")
    if new_head in obstacles:
        print("Reason: Snake collided with an obstacle.")
    else:
        print("Reason: Snake collided with itself.")

if __name__ == "__main__":
    main()
