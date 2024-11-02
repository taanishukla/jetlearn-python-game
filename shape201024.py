import pgzrun
import random
#setting up the screen
HEIGHT=300
WIDTH=300
#drawing the shape
def draw():
    colour='red'
    shape_height=50
    shape_width=150
    for i in range(10):
        rect=Rect((0,0),(shape_width,shape_height))
        rect.center=(150,150)
        screen.draw.rect(rect,colour)
        shape_height=shape_height+10
        shape_width=shape_width-10
#main program
pgzrun.go()
