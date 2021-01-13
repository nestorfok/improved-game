from tkinter import *
from time import time
import random
import time


class Rubbish(object):
    rubbish_detail = []
    rubbish_shape = ["rectangle", "circle"]
    rubbish_colour = ["red", "green", "yellow", "blue", "purple", "pink", "grey", "brown"]
    rubbish_movement_x = ["5", "-5"]
    rubbish_movement_y = 3
    rubbish_position = [[100, 50], [600, 70], [1000, 10]]
    fix_position = 0
    number_of_rubbish = 0
    movement_of_rubbish_x = [5, -5, 7, -7, 8, -8, 9, -9]
    movement_of_rubbish_y = [5, 7, 8, 9]
    each_rubbish_movement_xy = []


class GameVariable(object):
    pause_game = 0
    score = 0
    level = 5
    speed = 0.1
    life = 5
    cheat_activate = 0
    save_detail = []


class Window1(Rubbish, GameVariable):
    def __init__(self, master):
        self.master = master
        # Setting up background
        self.master.title("Main Screen")
        self.master.geometry("1366x768")
        self.canvas = Canvas(self.master, width=1366, height=700)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.config(bg="black")

        # Variable
        self.movement_x = 0
        self.movement_y = 0

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

        # Basket
        self.baskGif = PhotoImage(file="basket.gif")
        self.baskGif.image = self.baskGif
        self.basket = self.canvas.create_image(620, 554, image=self.baskGif, anchor="nw")
        self.master.bind("<Left>", lambda e: self.left())
        self.master.bind("<Right>", lambda e: self.right())

        while Basket.life > 0:

            # Create rubbish
            while Rubbish.number_of_rubbish < 3:

                # Random choose the shape and colour of rubbish
                shape = random.choice(Rubbish.rubbish_shape)
                colour = random.choice(Rubbish.rubbish_colour)

                # Rectangle rubbish
                if shape == "rectangle":
                    rectangle = self.canvas.create_rectangle(Rubbish.rubbish_position[Rubbish.fix_position][0],
                                                             Rubbish.rubbish_position[Rubbish.fix_position][1],
                                                             Rubbish.rubbish_position[Rubbish.fix_position][0] + 80,
                                                             Rubbish.rubbish_position[Rubbish.fix_position][1] + 80,
                                                             fill=colour)

                    # Save the detail to the list
                    Rubbish.rubbish_detail.append(rectangle)

                # Circle rubbish
                if shape == "circle":
                    circle = self.canvas.create_oval(Rubbish.rubbish_position[Rubbish.fix_position][0],
                                                     Rubbish.rubbish_position[Rubbish.fix_position][1],
                                                     Rubbish.rubbish_position[Rubbish.fix_position][0] + 80,
                                                     Rubbish.rubbish_position[Rubbish.fix_position][1] + 80,
                                                     fill=colour)

                    # Save the detail to the list
                    Rubbish.rubbish_detail.append(circle)

                # Editing variable
                Rubbish.number_of_rubbish += 1
                Rubbish.fix_position += 1

                # Update the screen
                self.master.update()

            # Movement of rubbish
            for i in range(Rubbish.number_of_rubbish):

                # Set the random movement of rubbish
                for j in range(3):
                    rubbish_movement_x = random.choice(Rubbish.movement_of_rubbish_x)
                    rubbish_movement_y = random.choice(Rubbish.movement_of_rubbish_y)
                    Rubbish.each_rubbish_movement_xy.append([rubbish_movement_x, rubbish_movement_y])

                # Check the coordinate of each rubbish
                self.rubbish_current_position = self.canvas.coords(Rubbish.rubbish_detail[i])

                # Check if the rubbish touches the wall and code it to bounce back
                if self.rubbish_current_position[0] < 0 or self.rubbish_current_position[2] > 1366:
                    Rubbish.each_rubbish_movement_xy[i][0] = -Rubbish.each_rubbish_movement_xy[i][0]

                # Detect and bounce back if the rubbishes collide together
                for a in range(3):

                    # Detect if we are checking the same ball
                    if i == a:
                        continue

                    # Bounce back if collide
                    else:

                        # Check the position of another rubbish
                        self.rubbish2_current_position = self.canvas.coords(Rubbish.rubbish_detail[a])

                        if self.rubbish_current_position[0] < self.rubbish2_current_position[2] and \
                                self.rubbish_current_position[2] > self.rubbish2_current_position[0] and \
                                self.rubbish_current_position[1] < self.rubbish2_current_position[3] and \
                                self.rubbish_current_position[3] > self.rubbish2_current_position[1]:
                            Rubbish.each_rubbish_movement_xy[i][0] = -Rubbish.each_rubbish_movement_xy[i][0]



                # Move the rubbish if nothing happen
                self.canvas.move(Rubbish.rubbish_detail[i],
                                 Rubbish.each_rubbish_movement_xy[i][0],
                                 Rubbish.each_rubbish_movement_xy[i][1])
                self.master.update()

    # Move the basket left
    def left(self):
        self.movement_x = -40
        self.canvas.move(self.basket, self.movement_x, self.movement_y)
        self.basket_collision_detect()
        self.master.update()

    # Move the basket right
    def right(self):
        self.movement_x = 40
        self.canvas.move(self.basket, self.movement_x, self.movement_y)
        self.basket_collision_detect()
        self.master.update()

    # Detect and bounce if the basket collide with the wall
    def basket_collision_detect(self):
        basket_current_position = self.canvas.coords(self.basket)
        if basket_current_position[0] < 0 or basket_current_position[0] > 1220:
            self.movement_x = -self.movement_x
            self.canvas.move(self.basket, self.movement_x, self.movement_y)


class Basket(Window1):
    movement_x = 0
    movement_y = 0


if __name__ == '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()





