import tkinter
import random

rows = 25
columns = 25
tile_size = 25
window_width = tile_size * rows
window_height = tile_size * columns


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="Black", width=window_width, height=window_height)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


def restartGame():
    global snake, food, snake_body, gameOver, score, velocity_y, velocity_x
    snake = Tile(tile_size * 5, tile_size * 5)
    food.x = random.randint(0, columns - 1) * tile_size
    food.y = random.randint(0, rows - 1) * tile_size
    snake_body.clear()
    velocity_y = 0
    velocity_x = 0
    gameOver = False
    score = 0


snake = Tile(tile_size * 5, tile_size * 5)
food = Tile(tile_size * random.randint(0, rows - 1), tile_size * random.randint(0, columns - 1))
snake_body = []
velocity_x = 0
velocity_y = 0
gameOver = False
score = 0


def change_direction(e):
    global velocity_x, velocity_y, gameOver, snake, snake_body, score
    if gameOver:
        if e.keysym == "space":
            restartGame()
        return
    if e.keysym == "Up" and velocity_y != 1:
        velocity_x = 0
        velocity_y = -1
    elif e.keysym == "Down" and velocity_y != -1:
        velocity_x = 0
        velocity_y = 1
    elif e.keysym == "Right" and velocity_x != -1:
        velocity_x = 1
        velocity_y = 0
    elif e.keysym == "Left" and velocity_x != 1:
        velocity_x = -1
        velocity_y = 0


def move():
    global snake, food, snake_body, gameOver, score
    if gameOver:
        return
    if snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height:
        gameOver = True
        return
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            gameOver = True
            return
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, columns - 1) * tile_size
        food.y = random.randint(0, rows - 1) * tile_size
        score += 1
    for i in range(len(snake_body) - 1, -1, -1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i - 1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
    snake.x += velocity_x * tile_size
    snake.y += velocity_y * tile_size


def draw():
    global snake
    global food, snake_body, gameOver, score
    move()
    canvas.delete("all")
    canvas.create_rectangle(food.x, food.y, food.x + tile_size, food.y + tile_size, fill="red")
    canvas.create_rectangle(snake.x, snake.y, snake.x + tile_size, snake.y + tile_size, fill="green")
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + tile_size, tile.y + tile_size, fill="green")
    if gameOver:
        canvas.create_text(window_width/2, window_height/2, font="Arial 20", text=f"Game Over: {score}", fill="white")
        canvas.create_text(window_width/2, window_height/2 + 35, font="Arial 20", text=f"Press Space to Play Again",
                           fill="white")
    else:
        canvas.create_text(30, 20, font="Arial 10", text=f"Score: {score}", fill="white")
    window.after(100, draw)


draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()
