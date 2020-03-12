'''Module to implement the Conway's Game of Life.'''


import sys
import turtle
import random


count=0
CELL_SIZE = 10
HX=15
HY=20


class LifeBoard:
    def __init__(self, xsize, ysize):
        self.state = set()
        self.xsize, self.ysize = xsize, ysize

    def is_legal(self, x, y):
        return (0 <= x < self.xsize) and (0 <= y < self.ysize)

    def set(self, x, y):
        if not self.is_legal(x, y):
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(x, y, self.xsize, self.ysize))

        key = (x, y)
        self.state.add(key)

    def makeRandom(self):
        self.erase()
        for i in range(0, self.xsize):
            for j in range(0, self.ysize):
                if random.random() > 0.5:
                    self.set(i, j)


    def glider(self):
        self.erase()
        self.set(1+HX,0+HY)
        self.set(2+HX,1+HY)
        self.set(2+HX,2+HY) 
        self.set(1+HX,2+HY) 
        self.set(0+HX,2+HY)
    def smallExploder(self):
        self.erase()
        self.set(0+HX,1+HY)
        self.set(0+HX,2+HY)
        self.set(1+HX,0+HY)
        self.set(1+HX,1+HY)
        self.set(1+HX,3+HY)
        self.set(2+HX,1+HY)
        self.set(2+HX,2+HY)
    def Exploder(self):
        self.erase()
        self.set(0+HX,0+HY)
        self.set(0+HX,1+HY)
        self.set(0+HX,2+HY)
        self.set(0+HX,3+HY)
        self.set(0+HX,4+HY)
        self.set(2+HX,0+HY)
        self.set(2+HX,4+HY)
        self.set(4+HX,0+HY)
        self.set(4+HX,1+HY)
        self.set(4+HX,2+HY)
        self.set(4+HX,3+HY)
        self.set(4+HX,4+HY)
    
    def tenCellRow(self):
        self.erase()
        self.set(0+HX,0+HY)
        self.set(1+HX,0+HY)
        self.set(2+HX,0+HY)
        self.set(3+HX,0+HY)
        self.set(4+HX,0+HY)
        self.set(5+HX,0+HY)
        self.set(6+HX,0+HY)
        self.set(7+HX,0+HY)
        self.set(8+HX,0+HY)
        self.set(9+HX,0+HY)
    def lightWeightSpacehip(self):
        self.erase()
        self.set(0+HX,1+HY)
        self.set(0+HX,3+HY)
        self.set(1+HX,0+HY)
        self.set(2+HX,0+HY)
        self.set(3+HX,0+HY)
        self.set(3+HX,3+HY)
        self.set(4+HX,0+HY)
        self.set(4+HX,1+HY)
        self.set(4+HX,2+HY)

    def tumbler(self):
        self.erase()
        self.set(0+HX,3+HY)
        self.set(0+HX,4+HY)
        self.set(0+HX,5+HY)
        self.set(1+HX,0+HY)
        self.set(1+HX,1+HY)
        self.set(1+HX,5+HY)
        self.set(2+HX,0+HY)
        self.set(2+HX,1+HY)
        self.set(2+HX,2+HY)
        self.set(2+HX,3+HY)
        self.set(2+HX,4+HY)
        self.set(4+HX,0+HY)
        self.set(4+HX,1+HY)
        self.set(4+HX,2+HY)
        self.set(4+HX,3+HY)
        self.set(4+HX,4+HY)
        self.set(5+HX,0+HY)
        self.set(5+HX,1+HY)
        self.set(5+HX,5+HY)
        self.set(6+HX,3+HY)
        self.set(6+HX,4+HY)
        self.set(6+HX,5+HY)
    
  
    def toggle(self, x, y):
        # Toggle a cell's state between live and dead
        if not self.is_legal(x, y):
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(x, y, self.xsize, self.ysize))
        key = (x, y)
        if key in self.state:
            self.state.remove(key)
        else:
            self.state.add(key)

    def erase(self):
        # Clear the board
        self.state.clear()

    def step(self):
        # Compute one generation, update the display
        d = set()
        for i in range(self.xsize):
            x_range = range(max(0, i - 1), min(self.xsize, i + 2))
            for j in range(self.ysize):
                s = 0
                live = ((i, j) in self.state)
                for yp in range(max(0, j - 1), min(self.ysize, j + 2)):
                    for xp in x_range:
                        if (xp, yp) in self.state:
                            s += 1

                # Subtract the central cell's value; it doesn't count.
                s -= live
                #print(d)
                ##print(i, j, s, live)
                if s == 3:
                    # Birth
                    d.add((i, j))
                elif s == 2 and live:
                    # Survival
                    d.add((i, j))
                elif live:
                    # Death
                    pass

        self.state = d

    def draw(self, x, y):
        # Update the cell (x,y) on the display
        turtle.penup()
        key = (x, y)
        if key in self.state:
            turtle.setpos(x * CELL_SIZE, y * CELL_SIZE)
            turtle.color('blue')
            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE - 1)
                turtle.left(90)
            turtle.end_fill()

    def display(self):
        # Draw board
        turtle.clear()
        for i in range(self.xsize):
            for j in range(self.ysize):
                self.draw(i, j)
        turtle.update()


def main():
    scr = turtle.Screen()
    turtle.mode('standard')
    xsize, ysize = scr.screensize()
    turtle.setworldcoordinates(0, 0, xsize, ysize)

    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0)
    turtle.penup()

    board = LifeBoard(xsize // CELL_SIZE, 1 + ysize // CELL_SIZE)
    print("\n1.glider\n2.Small Exploder\n3.Exploder\n4.10 Cell Row\n5.Light Weight Spaceship\n6.Tumbler')")
    prefer=int(input('Enter your preference:'))
    print("You have preffered:",prefer)
    
    def switch_demo(argument):
        switcher = {
        1: board.glider(),
        2: board.smallExploder(),
        3: board.Exploder(),
        4: board.tenCellRow(),
        5: board.lightWeightSpacehip(),
        6: board.tumbler(),
        
    }
       
        return switcher.get(argument, "Invalid preference")
    switch_demo(prefer)
    board.display()

    # Continuous movement
    continuous = False

    def step_continuous():
        nonlocal continuous
        continuous = True
        perform_step()

    def perform_step():
        board.step()
        board.display()
        # Setting timer to display another generation
        # after 30 ms
        if continuous:
            turtle.ontimer(perform_step, 30)
            global count
            count+=1
        #    print(count)

    turtle.ontimer(step_continuous)

    # Tk loop
    turtle.listen()
    turtle.mainloop()


if __name__ == '__main__':
    main()
