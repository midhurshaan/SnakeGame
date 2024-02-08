import tkinter
import random

#constants
GAME_WIDTH = 1100
GAME_HEIGHT = 700
SPEED = 60
SPACE_SIZE = 20
BODY_PARTS = 1
SNAKE_COLOR = "#A40E4C"
FOOD_COLOR = "#F4D06F"
BACKGROUND_COLOR = "#111214"

#classes
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")


#methods
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if(direction == "up"):
        y -= SPACE_SIZE
    elif(direction == "down"):
        y += SPACE_SIZE
    elif(direction == "left"):
        x -= SPACE_SIZE
    elif(direction == "right"):
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")

    snake.squares.insert(0, square)

    if (x == food.coordinates[0]) and (y == food.coordinates[1]):
        global score
        score += 1

        label.config(text=f"Score:{score}")

        canvas.delete("food")

        food = Food()
    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if(check_collisions(snake)):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction    #getting the old direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if (x < 0 or x >= GAME_WIDTH):
        return True
    elif (y < 0 or y >= GAME_HEIGHT):
        return True
    
    for body_part in snake.coordinates[1:]:    #check everything after the head of the snake
        if (x == body_part[0] and y == body_part[1]):
            return True
        
    return False

def game_over():
    canvas.delete("snake")
    canvas.delete("food")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('Ariel',  70), text="GAME OVER", fill="#F4D06F", tag="gameover")


window = tkinter.Tk()
window.title("Middy's Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = tkinter.Label(window, text=f"Score:{score}", font=('Ariel', 40))
label.pack()

canvas = tkinter.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# centering the gui
windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth / 2) - (windowWidth / 2))
y = int((screenHeight / 2) - (windowHeight / 2)) #these originally return floats

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}") #x & y need to be ints here (why casted earlier)

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

#initializing snake and food
snake = Snake()
food = Food()
next_turn(snake, food)



window.mainloop()