import turtle
import math
import random
import tkinter as tk
from tkinter import colorchooser, simpledialog
from tkinter import ttk
import pygame
import threading

# Function to draw an arc with color change
def draw_arc(t, radius, angle, color):
    t.color(color)
    t.circle(radius, angle)

# Function to draw a spirograph with dynamic colors and gradient effect
def draw_spirograph(t, R, r, l, color1, color2):
    t.penup()
    t.goto(R-r, 0)
    t.pendown()
    for i in range(360):
        ratio = i / 360
        color = (
            color1[0] + (color2[0] - color1[0]) * ratio,
            color1[1] + (color2[1] - color1[1]) * ratio,
            color1[2] + (color2[2] - color1[2]) * ratio,
        )
        t.pencolor(color)
        t.setheading(0)
        x = math.radians(i)
        x += l / r * math.radians(i)
        x %= 2 * math.pi
        t.setheading(math.degrees(x))
        draw_arc(t, r, 1, color)

# Function to handle mouse click event
def on_click(x, y):
    t.clear()
    R = random.randint(50, 200)
    r = random.randint(20, 100)
    l = random.randint(10, 80)
    color1 = (random.random(), random.random(), random.random())
    color2 = (random.random(), random.random(), random.random())
    draw_spirograph(t, R, r, l, color1, color2)

# Function to choose colors using color dialog
def choose_colors():
    color1 = colorchooser.askcolor(title="Choose start color")[0]
    color2 = colorchooser.askcolor(title="Choose end color")[0]
    return (
        (color1[0] / 255, color1[1] / 255, color1[2] / 255),
        (color2[0] / 255, color2[1] / 255, color2[2] / 255),
    )

# Function to create GUI with tkinter
def create_gui():
    root = tk.Tk()
    root.title("Spirograph Settings")

    def apply_settings():
        R = int(radius_var.get())
        r = int(small_radius_var.get())
        l = int(offset_var.get())
        color1, color2 = choose_colors()
        t.clear()
        draw_spirograph(t, R, r, l, color1, color2)

    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(main_frame, text="Outer Radius:").grid(row=0, column=0, sticky=tk.W)
    radius_var = tk.StringVar(value="100")
    ttk.Entry(main_frame, textvariable=radius_var).grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(main_frame, text="Inner Radius:").grid(row=1, column=0, sticky=tk.W)
    small_radius_var = tk.StringVar(value="20")
    ttk.Entry(main_frame, textvariable=small_radius_var).grid(row=1, column=1, sticky=(tk.W, tk.E))

    ttk.Label(main_frame, text="Offset:").grid(row=2, column=0, sticky=tk.W)
    offset_var = tk.StringVar(value="50")
    ttk.Entry(main_frame, textvariable=offset_var).grid(row=2, column=1, sticky=(tk.W, tk.E))

    ttk.Button(main_frame, text="Choose Colors", command=choose_colors).grid(row=3, column=0, columnspan=2)
    ttk.Button(main_frame, text="Apply", command=apply_settings).grid(row=4, column=0, columnspan=2)

    root.mainloop()

# Function to play background music
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("background_music.mp3")  # Replace with your music file
    pygame.mixer.music.play(-1)

# Main function
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")

    global t
    t = turtle.Turtle()
    t.speed(0)  # Set maximum speed
    t.width(2)

    # Set up mouse click event
    screen.onclick(on_click)

    # Start background music in a separate thread
    threading.Thread(target=play_music).start()

    # Create GUI in a separate thread
    threading.Thread(target=create_gui).start()

    turtle.done()

if __name__ == "__main__":
    main()
