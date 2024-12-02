import numpy as np
import tkinter as tk
from functools import partial
from PIL import Image, ImageTk
import sys
import time
import json
import random

class Control:
    def __init__(self, readFile):
        # only first map
        with open(readFile, "r") as json_file:
          data = json.load(json_file)
        what = str(random.randint(1, 3))
        l = data[what]

        # set axis(1, 1) to be gray
        l[1][1] = 1

        # tkinter window setting
        self.mazeA = np.array(l)
        self.pixelZoomin = 70
        self.currentPos = [1, 1]
        self.window = tk.Toplevel()  # not tk.Tk() because tkinter error will appear
        self.window.title(f"Control - Map {what}")
        self.window.geometry("1100x750+0+0")
        self.window.configure(bg="black")

        # create buttons
        self.create_controls()


    def create_controls(self):
        # create buttons
        # up
        b1 = tk.Button(self.window, text="↑", font=("微軟正黑體", 24), command=partial(self.main, 1))
        b1.place(x=880, y=450)
        # down
        b2 = tk.Button(self.window, text="←", font=("微軟正黑體", 24), command=partial(self.main, 3))
        b2.place(x=780, y=550)
        # left
        b3 = tk.Button(self.window, text="↓", font=("微軟正黑體", 24), command=partial(self.main, 2))
        b3.place(x=880, y=550)
        # right
        b4 = tk.Button(self.window, text="→", font=("微軟正黑體", 24), command=partial(self.main, 4))
        b4.place(x=980, y=550)


    def run(self):
        # build up the mazeB
        row, col = self.mazeA.shape
        mazeB = np.zeros((row*self.pixelZoomin, col*self.pixelZoomin), np.uint8)
        for i in range(row):
            for j in range(col):
                if self.mazeA[i, j] == 0 or self.mazeA[i, j] == 1:
                    mazeB[i*self.pixelZoomin: (i+1)*self.pixelZoomin, j*self.pixelZoomin: (j+1)*self.pixelZoomin] = 255
                if self.mazeA[i, j] == 1:
                    mazeB[i*self.pixelZoomin+10: (i+1)*self.pixelZoomin-10, j*self.pixelZoomin+10: (j+1)*self.pixelZoomin-10] = 127
        
        # show the image
        img = Image.fromarray(mazeB.astype(np.uint8))
        imgtk = ImageTk.PhotoImage(img)
        l = tk.Label(self.window, image=imgtk)
        l.place(x=20, y=20)
        self.window.update()
        
        # check if win
        if self.endIfWin(self.currentPos):
            time.sleep(1)
            self.window.destroy()

        self.window.mainloop()


    def update_map(self, currentPos_old, currentPos):
        self.mazeA[currentPos_old[0]][currentPos_old[1]] = 0
        self.mazeA[currentPos[0]][currentPos[1]] = 1


    def check_path(self, direction, currentPos):
        currentPos_old = currentPos.copy()
        currentPos_new = currentPos.copy()

        if direction == 1:
            currentPos_new[0] -= 1  # up
        elif direction == 2:
            currentPos_new[0] += 1  # down
        elif direction == 3:
            currentPos_new[1] -= 1  # left
        elif direction == 4:
            currentPos_new[1] += 1  # right

        # check for walls
        if self.mazeA[currentPos_new[0]][currentPos_new[1]] == 2:
            flag = 0
        else:
            flag = 1
        return flag, currentPos_old, currentPos_new


    def endIfWin(self, pos):
        return True if pos[0] == 8 and pos[1] == 8 else None


    def main(self, button_status):
        flag, currentPos_old, currentPos_new = self.check_path(button_status, self.currentPos)

        if flag == 0:
            self.currentPos = currentPos_old  # hit a wall
        else:
            self.currentPos = currentPos_new  # valid move
            self.update_map(currentPos_old, self.currentPos)
            self.run()  


    def start(self):
          self.run()


'''
# Test
game = Control()
game.start()
'''