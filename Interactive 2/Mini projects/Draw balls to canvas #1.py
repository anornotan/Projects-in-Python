# Every time you click the mouse, draw a ball at that position to the canvas. 
# Change the ball's color to green if the second ball is outside any of the previous balls. 
# Keep the list of different balls' coordinates.

import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    changed = False
    for ball in ball_list:
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = "Green" # add one more element to the list besides ball's coordinates
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], "Red"])
    print ball_list
def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball[2])
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    