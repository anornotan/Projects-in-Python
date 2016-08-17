# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos, paddle2_pos = 200, 200
paddle1_vel, paddle2_vel = 0, 0
ball_vel = [0,0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[1] = -random.randrange(1, 3)
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(2, 4)
        
    if direction == "LEFT":
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3) 


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints    
    score1,score2 = 0, 0
    spawn_ball("RIGHT")
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball  
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= RADIUS or ball_pos[1] >= (HEIGHT - 1 - RADIUS):	# make sure ball collides with and
        ball_vel[1] = - ball_vel[1]										# bounces off of the top and bottom walls                                                                                                                                                .                            
    elif ball_pos[0]  <= PAD_WIDTH + RADIUS: 							# to see if ball touches left gutter
        if (paddle1_pos - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT): # to see if ball touches left paddle        
            ball_vel[0] *= -1.1          								# to speed ball up every time it touches paddle
        else:
            score1 += 1
            spawn_ball("RIGHT")											# respawn  ball in the center of the table heading towards the side that won the last point.
    elif (ball_pos[0] + RADIUS) >= (WIDTH - 1 - PAD_WIDTH):   			# to see if ball ball touches right gutter
        if (paddle2_pos - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT): # to see if ball touches right paddle
            ball_vel[0] *= -1.1											# To moderately increase the difficulty of your game, increase the velocity of the ball by 10% each time it strikes a paddle
        else:
            score2 += 1
            spawn_ball("LEFT")
        
    # draw ball
    canvas.draw_circle([ball_pos[0],ball_pos[1]], RADIUS, 5, "Yellow", "Yellow")
    
    # update paddle's vertical position only when paddles are still on the screen  
    if  HALF_PAD_HEIGHT < (paddle1_pos + paddle1_vel) < (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if HALF_PAD_HEIGHT < (paddle2_pos + paddle2_vel) < (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    # draw paddles using draw_line to draw each side of paddles which totals to 8 sides for 2 paddles    
    # canvas.draw_line((0,paddle1_pos - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), 5, "RED")
    # canvas.draw_line((0,paddle1_pos + HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), 5, "RED")       
    # canvas.draw_line((0,paddle1_pos - HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT), 5, "RED") 
    # canvas.draw_line((PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), 5, "RED")    
    # canvas.draw_line((WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos - HALF_PAD_HEIGHT), 5, "RED")
    # canvas.draw_line((WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), 5, "RED")
    # canvas.draw_line((WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), 5, "RED")
    # canvas.draw_line((WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), 5, "RED")

    # OR simply use draw_polygon 
    canvas.draw_polygon ([[0,paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT],\
                          [PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT],[0,paddle1_pos+HALF_PAD_HEIGHT]],\
                         5,"RED","RED")
    canvas.draw_polygon ([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],\
                          [WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH, paddle2_pos+HALF_PAD_HEIGHT],\
                          [WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT]],5,"RED","RED")
    # draw scores, remember to convert to strings first                         
    canvas.draw_text(str(score1), (440,100), 70, "Blue", "sans-serif")
    canvas.draw_text(str(score2), (140,100), 70, "Blue", "sans-serif")
    
    # when any of these keys is pressed down, the function inside will come into effect accordingly                  
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 10						# increase/decrease velocity, not the position itself 
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 10
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 10
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 10
    # for when those keys are not pressed...       
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("restart",new_game,200)

# start frame
new_game()
frame.start()
