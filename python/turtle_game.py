import turtle
import tkinter as TK
import random
import time


# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Game")
screen.bgcolor("black")

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.speed(0)
player.penup()

# Score & Level Tracking
score = 0
level = 1

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(-550, 430)  # Adjusted position

level_display = turtle.Turtle()
level_display.hideturtle()
level_display.penup()
level_display.color("white")
level_display.goto(445, 430)  # Adjusted position

# FPS Display (bottom left)
fps_display = turtle.Turtle()
fps_display.hideturtle()
fps_display.penup()
fps_display.color("yellow")
fps_display.goto(-550, -430)  # Move FPS display to bottom left

# Define FPS variables
fps = 0
last_fps = -1  # Used to prevent text blinking
last_time = time.time()

# Function to update the score, level, and FPS display
def update_display():
    global fps, last_fps

    # Update Score
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 20, "bold"))

    # Update Level
    level_display.clear()
    level_display.write(f"Level: {level}", font=("Arial", 20, "bold"))

    # Update FPS only if changed to avoid blinking
    if int(fps) != last_fps:
        fps_display.clear()
        fps_display.write(f"FPS: {int(fps)}", align="left", font=("Arial", 14, "bold"))
        last_fps = int(fps)  # Store last FPS value

    screen.update()

# Function to increase level based on score
def check_level():
    global level
    if score >= level * 50:  # Level increases every 50 points
        level += 1
        spawn_coins()  # New level = more coins!

# Function to create coins
coins = []
def spawn_coins():
    global coins
    for coin in coins:
        coin.hideturtle()  # Hide existing coins
    coins.clear()

    for _ in range(5 + level):  # More coins as levels increase
        coin = turtle.Turtle()
        coin.shape("circle")
        coin.color("gold")
        coin.penup()
        coin.goto(random.randint(-250, 250), random.randint(-250, 250))
        coins.append(coin)

# Movement functions with infinite movement and coin collection
def move_forward():
    player.forward(10)
    check_coin_collision()

def move_backward():
    player.backward(10)
    check_coin_collision()

def turn_left():
    player.left(10)

def turn_right():
    player.right(10)

def check_coin_collision():
    global score
    for coin in coins[:]:  # Iterate over a copy of the list
        if player.distance(coin) < 15:
            coin.hideturtle()  # Hide the collected coin
            coins.remove(coin)  # Remove it from the list
            score += 10  # Increase score when collecting a coin
            update_display()
            check_level()  # Check if it's time to level up

# Initialize game
spawn_coins()
update_display()  # Ensure display updates correctly

# Key bindings
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")

# FPS update loop (60 FPS)
def update_fps():
    global last_time, fps
    current_time = time.time()
    fps = 10 / (current_time - last_time) if (current_time - last_time) > 0 else 0
    last_time = current_time

    update_display()  # Update UI without blinking
    screen.ontimer(update_fps, 16)  # Set to 16ms (~60 FPS)
    screen.update()

# Start FPS update loop
update_fps()

screen.mainloop()
