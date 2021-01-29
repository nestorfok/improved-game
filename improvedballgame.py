from tkinter import *
from time import time
import random
import time
import re


class Basket(object):
    position_x = 620
    position_y = 540


class Rubbish(object):
    detail = []
    shape = ["rectangle", "circle"]
    colour = ["blue"]
    random_colour = []
    random_shape = []
    movement_x = ["5", "-5"]
    movement_y = 3
    position = [[100, 50], [600, 70], [1000, 10]]
    load_position = []
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
    load = 0
    speed = 0.1
    life = 10
    cheat_activate = 0
    save_detail = []
    load_detail = []


class ScoreBoard(object):
    score_position_y = 200
    all_score = []
    rank = 1


class Setting(object):
    bind_key_list = []
    left_key = None
    right_key = None
    new_name = None
    correct = 0
    default_name = "Player"
    choice = ["a", "b", "c", "d", "e", "f",
              "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "z",
              "y", "z", "Up", "Down", "Right", "Left"]


class Window1:
    def __init__(self, master):

        # Initial set up
        self.master = master
        self.master.title("Menu")
        self.master.geometry("1366x768")

        # Canvas set up
        self.canvas = Canvas(self.master, width=1366, height=768)
        self.canvas.pack(fill=BOTH, expand=True)

        # Background image
        background = PhotoImage(file="background.gif", format="gif -index 2")
        background.image = background
        self.canvas.create_image(0, 0, image=background, anchor="nw")

        # All items in the window
        # Welcome message
        self.canvas.create_text(680, 50, text="Welcome!!!", font="Times, 50")

        # Start button
        start = Button(self.master, text="Start", font=("Times", 30), height=2, width=15,
                       command=self.start)
        self.canvas.create_window(680, 150, window=start)

        # Score board button
        score_board = Button(self.master, text="Score Board", font=("Times", 30), height=2, width=15,
                             command=self.score_board)
        self.canvas.create_window(680, 250, window=score_board)

        # Load button
        load = Button(self.master, text="Load", font=("Times", 30), height=2, width=15,
                      command=self.load)
        self.canvas.create_window(680, 350, window=load)

        # How to play button
        instruction = Button(self.master, text="Instruction", font=("Times", 30), height=2, width=15,
                             command=self.instruction)
        self.canvas.create_window(680, 450, window=instruction)

        # Setting button
        setting = Button(self.master, text="Setting", font=("Times", 30), height=2, width=15,
                         command=self.setting)
        self.canvas.create_window(680, 550, window=setting)

        # Exit button
        exit_game = Button(self.master, text="Exit", font=("Times", 30), height=2, width=15,
                           command=root.destroy)
        self.canvas.create_window(1220, 700, window=exit_game)

    # Define start button
    def start(self):
        root.withdraw()
        start_game = Toplevel(self.master)
        Window2(start_game)

    # Define load
    def load(self):
        GameVariable.load = 1
        root.withdraw()
        start_game = Toplevel(self.master)
        Window2(start_game)

    # Define instruction button
    def instruction(self):
        root.withdraw()
        start_game = Toplevel(self.master)
        Window5(start_game)

    # Define score board button
    def score_board(self):
        root.withdraw()
        start_game = Toplevel(self.master)
        Window4(start_game)

    # Define setting button
    def setting(self):
        root.withdraw()
        start_game = Toplevel(self.master)
        Window3(start_game)

    @staticmethod
    # Show the window again
    def show_window():
        root.update()
        root.deiconify()


class Window2(Basket, Rubbish, GameVariable, Setting):
    def __init__(self, master):
        self.master = master
        # Setting up background
        self.master.title("Main Screen")
        self.master.geometry("1366x768")
        self.canvas = Canvas(self.master, width=1366, height=700)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.config(bg="black")

        # initialise Variable
        self.movement_x = 0
        self.movement_y = 0
        GameVariable.score = 0
        GameVariable.life = 10
        Rubbish.load_position = []
        Rubbish.fix_position = 0
        Rubbish.random_shape = []
        Rubbish.random_colour = []
        Rubbish.number = 0
        Rubbish.each_movement_xy = []
        Rubbish.detail = []
        Basket.position_x = 620
        Basket.position_y = 540

        # Frame
        self.canvas2 = Canvas(self.master, width=1366, height=68)
        self.canvas2.pack(fill=BOTH, expand=True)

        if GameVariable.load == 1:
            self.load()
        GameVariable.load = 0

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
        save_game = Button(self.master, text="Save and Exit", height=2, width=15, command=self.save)
        self.canvas2.create_window(1250, 30, window=save_game)

        # Basket
        self.baskGif = PhotoImage(file="basket.gif")
        self.baskGif.image = self.baskGif
        self.basket = self.canvas.create_image(Basket.position_x, Basket.position_y, image=self.baskGif, anchor="nw")

        # Movement of basket
        open_setting_file = open("setting.txt", "r")
        for i in open_setting_file:
            for data in i.split():
                Setting.bind_key_list.append(data)
        open_setting_file.close()
        self.master.bind("<" + Setting.bind_key_list[0] + ">", lambda e: self.left())
        self.master.bind("<" + Setting.bind_key_list[1] + ">", lambda e: self.right())

        # Create the rubbish by default
        while Rubbish.number < 3:
            self.num_of_rubbish(0, None)

            # Set the random movement of rubbish
            self.delete_and_respond_movement(0, None)

        # start the main game loop
        while GameVariable.life > 0:

            while GameVariable.pause_game == 1:
                self.master.bind("<" + Setting.bind_key_list[0] + ">", lambda e: self.pause_left())
                self.master.bind("<" + Setting.bind_key_list[1] + ">", lambda e: self.pause_right())
                self.master.update()
                continue

            # Movement of rubbish
            for i in range(3):

                # Check the coordinate of each rubbish
                self.rubbish_current_position = self.canvas.bbox(Rubbish.detail[i])

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
                        self.rubbish2_current_position = self.canvas.bbox(Rubbish.detail[a])

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
                        self.rubbish_current_position[1] < position_of_basket[3] and \
                        self.rubbish_current_position[3] > position_of_basket[1]:

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
                                 int(Rubbish.each_movement_xy[i][0]),
                                 int(Rubbish.each_movement_xy[i][1]))

            time.sleep(0.2)
            self.master.update()

        save_score = open("score.txt", "w")
        save_score.write(str(GameVariable.score) + "\n")
        save_score.close()

    # Load the game
    def load(self):
        open_save_file = open("save.txt", "r")

        # Load the data from the file
        for i in open_save_file:
            GameVariable.load_detail.append(i)
        open_save_file.close()

        # Remove space from each data
        for i in range(len(GameVariable.load_detail)):
            GameVariable.load_detail[i] = re.sub("\n", "", GameVariable.load_detail[i])

        # Load the score and life
        GameVariable.score = int(GameVariable.load_detail[22])
        GameVariable.life = int(GameVariable.load_detail[23])

        # Load the colour and shape
        for i in range(3):
            Rubbish.random_colour.append(GameVariable.load_detail[i])
            Rubbish.random_shape.append(GameVariable.load_detail[i+3])

        # Load the position and movement of rubbish
        for i in range(0, 6, 2):
            Rubbish.load_position.append([int(GameVariable.load_detail[12 + i]), int(GameVariable.load_detail[13 + i])])
            Rubbish.each_movement_xy.append([int(GameVariable.load_detail[6 + i]),
                                             int(GameVariable.load_detail[7 + i])])

        # Load the position of basket
        Basket.position_x = int(GameVariable.load_detail[18])
        Basket.position_y = int(GameVariable.load_detail[19])

        # Create the rubbish
        for i in range(3):
            if Rubbish.random_shape[i] == "rectangle":
                rubbish = self.rectangle(Rubbish.load_position, i, Rubbish.random_colour[i])
                Rubbish.detail.append(rubbish)
            if Rubbish.random_shape[i] == "circle":
                rubbish = self.circle(Rubbish.load_position, i, Rubbish.random_colour[i])
                Rubbish.detail.append(rubbish)
            Rubbish.number += 1
            Rubbish.fix_position += 1
            self.master.update()

    # Save the game
    def save(self):
        open_save_file = open("save.txt", "w")

        # save the colour of each rubbish
        for i in range(len(Rubbish.random_colour)):
            open_save_file.write(str(Rubbish.random_colour[i]) + "\n")

        # save the colour of each shape
        for i in range(len(Rubbish.random_shape)):
            open_save_file.write(str(Rubbish.random_shape[i]) + "\n")

        # save the movement of each rubbish
        for i in range(len(Rubbish.each_movement_xy)):
            for j in range(len(Rubbish.each_movement_xy[i])):
                open_save_file.write(str(Rubbish.each_movement_xy[i][j]) + "\n")

        # save the position of each rubbish
        for i in range(3):
            save_current_rubbish_position = self.canvas.bbox(Rubbish.detail[i])
            for j in range(2):
                open_save_file.write(str(save_current_rubbish_position[j]) + "\n")

        # Get and save the position of basket
        save_current_basket_position = self.canvas.bbox(self.basket)
        for i in range(len(save_current_basket_position)):
            open_save_file.write(str(save_current_basket_position[i]) + "\n")

        # save the score
        open_save_file.write(str(GameVariable.life) + "\n" + str(GameVariable.score))
        open_save_file.close()

        Window1.show_window()
        self.master.destroy()

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

    # Delete and produce rubbish
    def delete_and_respond_rubbish(self, position):
        self.canvas.delete(Rubbish.detail[position])
        Rubbish.detail.pop(position)
        Rubbish.random_shape.pop(position)
        Rubbish.random_colour.pop(position)
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

    # produce rubbish
    def num_of_rubbish(self, delete, position):

        # Detect if the fix position is full
        if Rubbish.fix_position == 3:
            Rubbish.fix_position = 0

        # Random choose the shape and colour of rubbish
        shape = random.choice(Rubbish.shape)
        colour = random.choice(Rubbish.colour)
        rubbish = None

        # Rectangle rubbish
        if shape == "rectangle":
            rubbish = self.rectangle(Rubbish.position, Rubbish.fix_position, colour)

        # Circle rubbish
        if shape == "circle":
            rubbish = self.circle(Rubbish.position, Rubbish.fix_position, colour)

        # Add the new shape to the original position of the deleted rubbish
        if delete == 1:
            Rubbish.detail.insert(position, rubbish)
            Rubbish.random_colour.insert(position, colour)
            Rubbish.random_shape.insert(position, shape)

        # Save the detail to the list
        if delete == 0:
            Rubbish.detail.append(rubbish)
            Rubbish.random_colour.append(colour)
            Rubbish.random_shape.append(shape)

        # Editing variable
        Rubbish.number += 1
        Rubbish.fix_position += 1

        # Update the window
        self.master.update()

    # Create rectangle
    def rectangle(self, a, b, colour):
        rubbish = self.canvas.create_rectangle(int(a[b][0]), int(a[b][1]), int(a[b][0]) + 80,
                                               int(a[b][1]) + 80, fill=colour)
        return rubbish

    # Create circle
    def circle(self, a, b, colour):
        rubbish = self.canvas.create_oval(int(a[b][0]), int(a[b][1]), int(a[b][0]) + 80,
                                          int(a[b][1]) + 80, fill=colour)
        return rubbish

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


# Setting page
class Window3:
    def __init__(self, master):

        # Basic setting
        self.master = master
        self.master.title("Setting")
        self.master.geometry("1366x768")

        # Canvas set up
        self.canvas = Canvas(self.master, width=1366, height=700,
                             bg="powder blue")
        self.canvas.pack(fill=BOTH, expand=True)

        # Canvas text
        self.canvas.create_text(680, 40, text="Setting", font=("Times", 60))
        self.canvas.create_text(300, 100, text="Default setting", font=("Times", 40))
        self.canvas.create_text(1066, 100, text="Instruction", font=("Times", 40))
        self.canvas.create_text(300, 150, text="Left: left arrow", font=("Times", 20))
        self.canvas.create_text(300, 180, text="Right: right arrow", font=("Times", 20))
        self.canvas.create_text(950, 150, text="Key", font=("Times", 30))
        self.canvas.create_text(1176, 150, text="How to do", font=("Times", 30))
        self.canvas.create_text(950, 190, text="A-Z", font=("Times", 20))
        self.canvas.create_text(1176, 190, text="Type A-Z in lowercase", font=("Times", 20))
        self.canvas.create_text(950, 250, text="Arrow keys", font=("Times", 20))
        self.canvas.create_text(1176, 250, text="Type 'Up' for up arrow key", font=("Times", 20))
        self.canvas.create_text(1176, 275, text="Type 'Down' for down arrow key", font=("Times", 20))
        self.canvas.create_text(1176, 300, text="Type 'Left' for left arrow key", font=("Times", 20))
        self.canvas.create_text(1176, 325, text="Type 'Right' for right arrow key", font=("Times", 20))

        # Canvas entry
        self.canvas.create_text(510, 400, text="Left:", font=("Times", 20))
        self.entry_left = Entry(self.master)
        self.canvas.create_window(670, 400, window=self.entry_left)
        self.canvas.create_text(510, 450, text="Right:", font=("Times", 20))
        self.entry_right = Entry(self.master)
        self.canvas.create_window(670, 450, window=self.entry_right)

        # Button
        enter = Button(self.master, text="Enter", height=2, width=15, font=("Times", 20), bg="powder blue",
                       command=self.enter)
        self.canvas.create_window(550, 500, window=enter)
        reset = Button(self.master, text="Reset", height=2, width=15, font=("Times", 20), bg="powder blue",
                       command=self.reset)
        self.canvas.create_window(750, 500, window=reset)
        return_menu = Button(self.master, text="Exit", height=2, width=15, font=("Times", 20), bg="powder blue",
                             command=self.return_menu)
        self.canvas.create_window(1220, 700, window=return_menu)

    # Define enter button
    def enter(self):

        # Get the key
        left_key = self.entry_left.get()
        Setting.bind_key_list.append(left_key)
        right_key = self.entry_right.get()
        Setting.bind_key_list.append(right_key)

        # Check the key input
        for i in Setting.bind_key_list:
            if i not in Setting.choice:
                output = self.canvas.create_text(680, 650, text="Incorrect input! Try again!", font=("Times", 50))
                self.master.update()
                time.sleep(1)
                self.canvas.delete(output)
                self.master.update()
                break
            else:
                Setting.correct += 1

        # Change the key if the inputs are correct
        if Setting.correct == 2:
            open_setting_file = open("setting.txt", "w")
            open_setting_file.write(left_key + "\n")
            open_setting_file.write(right_key + "\n")
            open_setting_file.close()
            output = self.canvas.create_text(680, 650, text="Change Saved!", font=("Times", 50))
            self.master.update()
            time.sleep(1)
            self.canvas.delete(output)
            self.master.update()

        # Reset the variables
        Setting.correct = 0
        Setting.bind_key_list = []

    # Define reset button
    def reset(self):
        open_setting_file = open("setting.txt", "w")
        open_setting_file.write("Left\nRight")
        open_setting_file.close()
        output = self.canvas.create_text(680, 650, text="Reset!", font=("Times", 50))
        self.master.update()
        time.sleep(1)
        self.canvas.delete(output)
        self.master.update()

    # Define return menu button
    def return_menu(self):
        Window1.show_window()
        self.master.destroy()


# Score board page
class Window4(ScoreBoard):
    def __init__(self, master):

        # Initial setting
        self.master = master
        self.master.title("Score Board")
        self.master.geometry("1366x768")

        # Canvas set up
        self.canvas = Canvas(self.master, width=1366, height=768)
        self.canvas.pack(fill=BOTH, expand=True)

        # Background picture
        background_pic = PhotoImage(file="scoreboardbg.gif")
        background_pic.image = background_pic
        self.canvas.create_image(0, 0, image=background_pic, anchor="nw")

        # Canvas text
        self.canvas.create_text(680, 50, text="Score Board", font=("Times", 50), fill="blue")
        self.canvas.create_text(400, 150, text="Score", font=("Times", 40), fill="blue")
        self.canvas.create_text(966, 150, text="Rank", font=("Times", 40), fill="blue")

        # Canvas button
        return_menu = Button(self.master, text="Exit", font=("Times", 30),
                             height=2, width=15, command=self.return_menu)
        self.canvas.create_window(1220, 700, window=return_menu)

        # Extract all the score from the file
        open_score_file = open("score.txt", "r")
        for i in open_score_file:
            for data in i.split():
                ScoreBoard.all_score.append(int(data))
        open_score_file.close()

        # Sort the score in descending order
        ScoreBoard.all_score.sort(reverse=True)

        # Make sure a maximum if 10 scores are displayed
        if len(ScoreBoard.all_score) > 10:
            del ScoreBoard.all_score[10:len(ScoreBoard.all_score)]

        # Print the score and rank
        for i in ScoreBoard.all_score:
            self.canvas.create_text(400, ScoreBoard.score_position_y, text=str(i), font=("Times", 25),
                                    fill="blue")
            self.canvas.create_text(966, ScoreBoard.score_position_y, text=str(ScoreBoard.rank),
                                    font=("Times", 25), fill="blue")
            ScoreBoard.score_position_y += 40
            ScoreBoard.rank += 1

        # Reset variable
        ScoreBoard.score_position_y = 200
        ScoreBoard.rank = 1
        ScoreBoard.all_score = []

    def return_menu(self):
        Window1.show_window()
        self.master.destroy()


# Instruction page
class Window5:

    def __init__(self, master):

        # Initial setting
        self.master = master
        self.master.title("Instruction")
        self.master.geometry("1366x768")

        # Canvas set up
        self.canvas = Canvas(self.master, width=1366, height=768)
        self.canvas.pack(fill=BOTH, expand=True)

        # Instruction
        self.canvas.create_text(680, 50, text="Instruction page", font=("Times", 60))

        self.canvas.create_text(680, 150, text="Use the basket to catch as many rubbishes as possible!",
                                font=("Times", 30))

        self.canvas.create_text(680, 250, text="Every rubbish you catch will add 1 to your score",
                                font=("Times", 30))

        self.canvas.create_text(680, 350, text="However, every rubbish that drops to the floor will minus 1 to your "
                                               "life. You will lose when your life is 0",
                                font=("Times", 30))

        # Button to return menu
        return_menu = Button(self.master, text="Exit", font=("Times", 30),
                             height=2, width=15, command=self.return_menu)
        self.canvas.create_window(680, 600, window=return_menu)

    # Define return menu button
    def return_menu(self):
        Window1.show_window()
        self.master.destroy()


if __name__ == '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()





