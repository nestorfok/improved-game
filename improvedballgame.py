from tkinter import *
from time import time
import random
import time


class Rubbish(object):
    detail = []
    shape = ["rectangle", "circle"]
    colour = ["red"]
    random_colour = []
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
    level = 0
    speed = 0.1
    life = 10
    cheat_activate = 0
    save_detail = []


class Window2:
    def __init__(self, master):

        # Initial set up
        self.master = master
        self.master.title("Menu")
        self.master.geometry("1366x768")

        # Canvas set up
        self.canvas = Canvas(self.master, width=1366, height=768)
        self.canvas.pack(fill=BOTH, expand=True)

        # All items in the window
        # Welcome message
        self.canvas.create_text(680, 50, text="Welcome!!!", font="Times, 50")

        # Start button
        start = Button(self.master, text="Start", font=("Times", 30), height=2, width=15,
                       command=self.start)
        self.canvas.create_window(680, 150, window=start)

        # Score board button
        score_board = Button(self.master, text="Score Board", font=("Times", 30), height=2, width=15)
        self.canvas.create_window(680, 250, window=score_board)

        # Load button
        load = Button(self.master, text="Load", font=("Times", 30), height=2, width=15)
        self.canvas.create_window(680, 350, window=load)

        # How to play button
        instruction = Button(self.master, text="Instruction", font=("Times", 30), height=2, width=15)
        self.canvas.create_window(680, 450, window=instruction)

        # Setting button
        setting = Button(self.master, text="Setting", font=("Times", 30), height=2, width=15)
        self.canvas.create_window(680, 550, window=setting)

        # Exit button
        exit_game = Button(self.master, text="Exit", font=("Times", 30), height=2, width=15,
                           command=self.master.destroy)
        self.canvas.create_window(1220, 700, window=exit_game)

    # Define start button
    def start(self):
        root.withdraw()
        start_game = Toplevel(self.master)
        Window1(start_game)


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
        self.canvas2 = Canvas(self.master, width=1366, height=68)
        self.canvas2.pack(fill=BOTH, expand=True)

        # Score
        self.score = self.canvas2.create_text(100, 30, text="Score: " + str(GameVariable.score), font=("Times", 30))

        # Life
        self.life = self.canvas2.create_text(250, 30, text="Life: " + str(GameVariable.life), font=("Times", 30))

        # Return menu button
        return_menu = Button(self.master, text="Return", height=2, width=15, command=self.master.destroy)
        self.canvas2.create_window(800, 30, window=return_menu)

        # Pause game button
        pause_game = Button(self.master, text="Pause", height=2, width=15, command=self.pause)
        self.canvas2.create_window(950, 30, window=pause_game)

        # Resume game button
        resume_game = Button(self.master, text="Resume", height=2, width=15, command=self.resume)
        self.canvas2.create_window(1100, 30, window=resume_game)

        # Save game button
        save_game = Button(self.master, text="Save and Exit", height=2, width=15, command=self.master.destroy)
        self.canvas2.create_window(1250, 30, window=save_game)

        # Basket
        self.baskGif = PhotoImage(file="basket.gif")
        self.baskGif.image = self.baskGif
        self.basket = self.canvas.create_image(620, 540, image=self.baskGif, anchor="nw")
        self.master.bind("<Left>", lambda e: self.left())
        self.master.bind("<Right>", lambda e: self.right())

        # Create the rubbish by default
        while Rubbish.number < 3:
            self.num_of_rubbish(0, None)

            # Set the random movement of rubbish
            self.delete_and_respond_movement(0, None)

        # start the main game loop
        while GameVariable.life > 0:

            while GameVariable.pause_game == 1:
                self.master.bind("<Left>", lambda e: self.pause_left())
                self.master.bind("<Right>", lambda e: self.pause_right())
                self.master.update()
                continue

            # Movement of rubbish
            for i in range(3):

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
                            Rubbish.each_movement_xy[i][0] = Rubbish.each_movement_xy[i][0] * -1

                # Check the collision between rubbish and ground
                if self.rubbish_current_position[3] > 700:
                    if Rubbish.random_colour[i] != "red":
                        GameVariable.life -= 1
                    self.canvas2.itemconfig(self.life, text="Life: " + str(GameVariable.life))
                    self.delete_and_respond_rubbish(i)

                # Check the coordinate of basket
                position_of_basket = self.canvas.bbox(self.basket)

                # Detect the collision between basket and rubbish
                if self.rubbish_current_position[0] < position_of_basket[2] and \
                        self.rubbish_current_position[2] > position_of_basket[0] and \
                        self.rubbish_current_position[1] < position_of_basket[3] + 10 and \
                        self.rubbish_current_position[3] > position_of_basket[1] + 10:

                    if Rubbish.random_colour[i] != "red":
                        GameVariable.score += 1
                    else:
                        GameVariable.score -= 1
                        GameVariable.life -= 1
                        self.canvas2.itemconfig(self.life, text="Life: " + str(GameVariable.life))
                    self.canvas2.itemconfig(self.score, text="Score: " + str(GameVariable.score))
                    self.delete_and_respond_rubbish(i)
                    self.delete_and_respond_movement(1, i)

                # Move the rubbish if nothing happen
                self.canvas.move(Rubbish.detail[i],
                                 Rubbish.each_movement_xy[i][0],
                                 Rubbish.each_movement_xy[i][1])

            time.sleep(0.02)
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
    def delete_and_respond_rubbish(self, position):
        self.canvas.delete(Rubbish.detail[position])
        Rubbish.detail.pop(position)
        Rubbish.number -= 1
        self.num_of_rubbish(1, position)

    @staticmethod
    # Delete and respond the movement of rubbish
    def delete_and_respond_movement(delete, position):

        # Set the random movement of rubbish
        rubbish_movement_x = random.choice(Rubbish.movement_of_x)
        rubbish_movement_y = random.choice(Rubbish.movement_of_y)

        if delete == 0:
            Rubbish.each_movement_xy.append([rubbish_movement_x, rubbish_movement_y])

        if delete == 1:
            Rubbish.each_movement_xy.pop(position)
            Rubbish.each_movement_xy.insert(position, [rubbish_movement_x, rubbish_movement_y])

    # Detect the number of rubbish
    def num_of_rubbish(self, delete, position):

        # Detect if the fix position is full
        if Rubbish.fix_position == 3:
            Rubbish.fix_position = 0

        # Random choose the shape and colour of rubbish
        shape = random.choice(Rubbish.shape)
        colour = random.choice(Rubbish.colour)

        # Saving the shape and colour to a list
        Rubbish.random_colour.append(colour)

        # Rectangle rubbish
        if shape == "rectangle":
            shape = self.canvas.create_rectangle(Rubbish.position[Rubbish.fix_position][0],
                                                 Rubbish.position[Rubbish.fix_position][1],
                                                 Rubbish.position[Rubbish.fix_position][0] + 80,
                                                 Rubbish.position[Rubbish.fix_position][1] + 80,
                                                 fill=colour)

        # Circle rubbish
        if shape == "circle":
            shape = self.canvas.create_oval(Rubbish.position[Rubbish.fix_position][0],
                                            Rubbish.position[Rubbish.fix_position][1],
                                            Rubbish.position[Rubbish.fix_position][0] + 80,
                                            Rubbish.position[Rubbish.fix_position][1] + 80,
                                            fill=colour)

        # Add the new shape to the original position of the deleted rubbish
        if delete == 1:
            Rubbish.detail.insert(position, shape)

        # Save the detail to the list
        if delete == 0:
            Rubbish.detail.append(shape)

        # Editing variable
        Rubbish.number += 1
        Rubbish.fix_position += 1

        # Update the window
        self.master.update()

    # pause the left movement of basket
    def pause_left(self):
        pass

    # Pause the right movement of basket
    def pause_right(self):
        pass

    @staticmethod
    # Pause the game
    def pause():
        GameVariable.pause_game = 1

    @staticmethod
    def resume():
        GameVariable.pause_game = 0


if __name__ == '__main__':
    root = Tk()
    app = Window2(root)
    root.mainloop()





