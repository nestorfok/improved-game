from tkinter import *
from time import time
import random
import time


class Rubbish(object):
    detail = []
    shape = ["rectangle", "circle"]
    colour = ["red", "green", "yellow", "blue", "purple", "pink", "grey", "brown"]
    movement_x = ["5", "-5"]
    movement_y = 3
    position = [[100, 50], [600, 70], [1000, 10]]
    fix_position = 0
    number = 0
    movement_of_x = [5, -5, 7, -7, 8, -8, 9, -9]
    movement_of_y = [5, 7, 8, 9]
    each_movement_xy = []
    speed = 0.1


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

        # Create the rubbish by default
        while Rubbish.number < 3:
            self.num_of_rubbish()

        # start the main game loop
        while GameVariable.life > 0:

            # Movement of rubbish
            for i in range(3):

                # Set the random movement of rubbish
                for j in range(3):
                    rubbish_movement_x = random.choice(Rubbish.movement_of_x)
                    rubbish_movement_y = random.choice(Rubbish.movement_of_y)
                    Rubbish.each_movement_xy.append([rubbish_movement_x, rubbish_movement_y])

                # Check the coordinate of each rubbish
                self.rubbish_current_position = self.canvas.coords(Rubbish.detail[i])

                # Check if the rubbish touches the wall and code it to bounce back
                if self.rubbish_current_position[0] < 0 or self.rubbish_current_position[2] > 1366:
                    Rubbish.each_movement_xy[i][0] = -Rubbish.each_movement_xy[i][0]

                # Detect and bounce back if the rubbishes collide together
                for a in range(3):

                    # Detect if we are checking the same ball
                    if i == a:
                        continue

                    # Bounce back if collide
                    else:

                        # Check the position of another rubbish
                        self.rubbish2_current_position = self.canvas.coords(Rubbish.detail[a])

                        if self.rubbish_current_position[0] < self.rubbish2_current_position[2] and \
                                self.rubbish_current_position[2] > self.rubbish2_current_position[0] and \
                                self.rubbish_current_position[1] < self.rubbish2_current_position[3] and \
                                self.rubbish_current_position[3] > self.rubbish2_current_position[1]:
                            Rubbish.each_movement_xy[i][0] = -Rubbish.each_movement_xy[i][0]

                # Check the collision between rubbish and ground
                if self.rubbish_current_position[3] > 700:
                    GameVariable.life -= 1
                    self.delete_and_respond_rubbish(i)

                # Check the coordinate of basket
                position_of_basket = self.canvas.bbox(self.basket)
                if self.rubbish_current_position[0] < position_of_basket[2] and \
                        self.rubbish_current_position[2] > position_of_basket[0] and \
                        self.rubbish_current_position[1] < position_of_basket[3] + 10 and \
                        self.rubbish_current_position[3] > position_of_basket[1] + 10:
                    GameVariable.score += 1
                    self.delete_and_respond_rubbish(i)

                # Move the rubbish if nothing happen
                self.canvas.move(Rubbish.detail[i],
                                 Rubbish.each_movement_xy[i][0],
                                 Rubbish.each_movement_xy[i][1])

            time.sleep(Basket.speed)
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

    # Delete and respond rubbish
    def delete_and_respond_rubbish(self, a):
        self.canvas.delete(Rubbish.detail[a])
        Rubbish.detail.pop(a)
        Rubbish.number -= 1
        self.num_of_rubbish()

    # Detect the number of rubbish
    def num_of_rubbish(self):

        # Detect if the fix position is full
        if Rubbish.fix_position == 3:
            Rubbish.fix_position = 0

        # Random choose the shape and colour of rubbish
        shape = random.choice(Rubbish.shape)
        colour = random.choice(Rubbish.colour)

        # Rectangle rubbish
        if shape == "rectangle":
            rectangle = self.canvas.create_rectangle(Rubbish.position[Rubbish.fix_position][0],
                                                     Rubbish.position[Rubbish.fix_position][1],
                                                     Rubbish.position[Rubbish.fix_position][0] + 80,
                                                     Rubbish.position[Rubbish.fix_position][1] + 80,
                                                     fill=colour)

            # Save the detail to the list
            Rubbish.detail.append(rectangle)

        # Circle rubbish
        if shape == "circle":
            circle = self.canvas.create_oval(Rubbish.position[Rubbish.fix_position][0],
                                             Rubbish.position[Rubbish.fix_position][1],
                                             Rubbish.position[Rubbish.fix_position][0] + 80,
                                             Rubbish.position[Rubbish.fix_position][1] + 80,
                                             fill=colour)

            # Save the detail to the list
            Rubbish.detail.append(circle)

        # Editing variable
        Rubbish.number += 1
        Rubbish.fix_position += 1

        # Update the window
        self.master.update()


class Basket(Window1):
    movement_x = 0
    movement_y = 0


if __name__ == '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()





