import cv2
import numpy as np
import sys
import random
import json

class Solver:
    def __init__(self, i_start, j_start, i_end, j_end, readFile, mapp):
        self.i_start, self.j_start = i_start, j_start
        self.i_end, self.j_end = i_end, j_end
        
        with open(readFile, "r") as json_file:
          data = json.load(json_file)
        l = data[str(mapp)]

        self.mazeA = np.array(l)
        self.row, self.col = self.mazeA.shape
        self.pixelZoomin = 70
        self.mazeB = np.zeros((self.row*self.pixelZoomin, self.col*self.pixelZoomin), np.uint8)
        

        for i in range(self.row):
            for j in range(self.col):
                if self.mazeA[i, j] == 0:
                    self.mazeB[i*self.pixelZoomin:(i+1)*self.pixelZoomin, j*self.pixelZoomin: (j+1)*self.pixelZoomin] = 255

    def reach(self, i, j):
        self.mazeA[i][j] = 1
        '''
        print("print road")
        print(i, j)
        for m in range(mazeA.shape[0]):
            for n in range(mazeA.shape[1]):
                if mazeA[m][n]==2:
                    print("X",end='')
                elif mazeA[m][n]==1:
                    print("o",end='')
                else:
                    print(" ",end='')
        print()
        '''
        # build up the mazeB
        for x in range(self.row):
            for y in range(self.col):
                if self.mazeA[x][y] == 1:
                    self.mazeB[x*self.pixelZoomin+10: (x+1)*self.pixelZoomin-10, y*self.pixelZoomin+10: (y+1)*self.pixelZoomin-10] = 127
                elif self.mazeA[x][y] == 0:
                    self.mazeB[x*self.pixelZoomin: (x+1)*self.pixelZoomin, y*self.pixelZoomin: (y+1)*self.pixelZoomin] = 255

        # OpenCV window
        cv2.imshow("Solver", self.mazeB)
        cv2.waitKey(200)

        # close when endpoint is reached
        if i == self.i_end and j == self.j_end:
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
            sys.exit()

        # recursive
        if self.mazeA[i+1][j] == 0:  # right
            self.reach(i+1, j)
        if self.mazeA[i-1][j] == 0:  # left
            self.reach(i-1, j)
        if self.mazeA[i][j+1] == 0:  # up
            self.reach(i, j+1)
        if self.mazeA[i][j-1] == 0:  # down
            self.reach(i, j-1)

        # No road 
        self.mazeA[i][j] = 0

    def start(self):
        try:
            self.reach(self.i_start, self.j_start)
        except:
            pass
