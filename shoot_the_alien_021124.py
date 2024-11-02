import random
import pgzrun
WIDTH=700
HEIGHT=700
alien=Actor('alien')
text=''
def draw():
    screen.fill(color=(128,0,0))
    alien.draw()
    screen.draw.text(text, center=(100,100),fontsize=20)
def place_alien():
    alien.x=random.randint(50,WIDTH-50)
    alien.y=random.randint(50,WIDTH-50)
def on_mouse_down(pos):
    global text
    if alien.collidepoint(pos):
        text='good shot'
        place_alien()
    else:
        text='sorry you missed'
place_alien()
pgzrun.go()