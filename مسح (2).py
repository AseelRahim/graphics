import turtle
from time import sleep
import sys

CURSOR_SIZE = 20
SQUARE_SIZE = 99
FONT_SIZE = 40
FONT = ('Arial', FONT_SIZE, 'bold')
BOXES = {}
# TRACK BOX
wn = turtle.Screen()
wn = turtle.Screen()
wn.bgcolor("pink")
pen = turtle.Turtle()
pen.penup()

def mouse(x, y):
    print('|--------------X={0} Y={1}--------------|'.format(x, y))
    for key in BOXES:
        minx, miny, maxx, maxy = BOXES[key]
        print(key, BOXES[key])
        if (minx <= x <= maxx) and (miny <= y <= maxy):
            print("Found", key)
            return key
    print('None')
    return None  # Not found.

class TicTacToe:
    global BOXES
    def __init__(self):
        # CREATES 2D LIST FOR INTERROGATION
        self.board = [['?'] * 3 for i in range(3)]

    def minmax(self, points):
        """ Find extreme x and y values in a list of 2-D coordinates. """
        minx, miny, maxx, maxy = points[0][0], points[0][1], points[0][0], points[0][1]
        for x, y in points[1:]:
            if x < minx:
                minx = x
            if y < minx:
                miny = y
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y
        return minx, miny, maxx, maxy


    def drawBoard(self):
        ##############################################
        turtle.shape('square')
        turtle.shapesize(SQUARE_SIZE * 3 / CURSOR_SIZE)
        turtle.color('black')
        turtle.stamp()
        turtle.hideturtle()
        ##############################################
        for j in range(3):
            for i in range(3):
                # CREATES SHAPE AND STORES IN PLACEHOLDER
                turtle.shape('square')
                box = turtle.shape('square')
                # CREATES SHAPE SIZE AND STORES IN PLACEHOLDER
                turtle.shapesize(SQUARE_SIZE / CURSOR_SIZE)
                boxsize = turtle.shapesize()
                # CREATES SHAPE COLOR
                turtle.color('white')
                turtle.penup()
                # CREATES SHAPE POS AND STORES IN PLACEHOLDER
                turtle.goto(i * (SQUARE_SIZE + 2) - (SQUARE_SIZE + 2), j * (SQUARE_SIZE + 2) - (SQUARE_SIZE + 2))
                boxpos = turtle.pos()

                mypos = []

                pen.goto(boxpos[0]-50,boxpos[1]+50)
                ##############################################
                for line in range(0, 4):
                    pen.forward(SQUARE_SIZE)
                    pen.right(90)
                    mypos.append(pen.pos())
                turtle.showturtle()
                turtle.stamp()
                ##############################################
                a = mypos[0]
                b = mypos[1]
                c = mypos[2]
                d = mypos[3]
                self.board[j][i] = [a, b, c, d]
        ##############################################
        BOXES['BOX01'] = self.minmax(self.board[0][0])
        BOXES['BOX02'] = self.minmax(self.board[0][1])
        BOXES['BOX03'] = self.minmax(self.board[0][2])
        ##############################################
        BOXES['BOX11'] = self.minmax(self.board[1][0])
        BOXES['BOX12'] = self.minmax(self.board[1][1])
        BOXES['BOX13'] = self.minmax(self.board[1][2])
        ##############################################
        BOXES['BOX21'] = self.minmax(self.board[2][0])
        BOXES['BOX22'] = self.minmax(self.board[2][1])
        BOXES['BOX23'] = self.minmax(self.board[2][2])
        ##############################################
        turtle.onscreenclick(mouse)

turtle.setup(800, 600)
wn = turtle.Screen()
z = TicTacToe()
z.drawBoard()
turtle.mainloop()
