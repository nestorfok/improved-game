from tkinter import *
from time import time
from random import randint as rand
import time


class Window1:
    def __init__(self, master):
        self.master = master
        # Setting up background
        self.master.title("Main Screen")
        self.master.geometry("1366x768")
        self.canvas = Canvas(self.master, width=1366, height=700)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.config(bg="black")

        # Frame
        frame = Frame(self.master, width=1366, height=68)
        frame.pack(fill=BOTH, expand=True)

        # Return menu button
        return_menu = Button(frame, text="Return", height=2, width=15, command=self.master.destroy)
        return_menu.grid(column=4, row=0, columnspan=2, sticky="e")

        # Pause game button
        pause_game = Button(frame, text="Pause", height=2, width=15, command=self.master.destroy)
        pause_game.grid(column=6, row=0, columnspan=2, sticky="e")

        # Resume game button
        resume_game = Button(frame, text="Resume", height=2, width=15, command=self.master.destroy)
        resume_game.grid(column=8, row=0, columnspan=2, sticky="e")

        # Save game button
        save_game = Button(frame, text="Save and Exit", height=2, width=15, command=self.master.destroy)
        save_game.grid(column=10, row=0, columnspan=2, sticky="e")


class GameVariable:
    pause_game = 0
    score = 0
    level = 5
    speed = 0.1
    life = 5
    cheat_activate = 0
    save_detail = []


class Rubbish:
    rubbish_detail = []
    rubbish_shape = ["rectangle", "circle", "polygon"]
    rubbish_colour = ["red", "green", "yellow", "black"]
    rubbish_movement_x = ["5", "-5"]
    rubbish_movement_y = 3
    rubbish_position = [[100, 50], [300, 30], [600, 70], [800, 20], [1000, 10]]


if __name__ == '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()





