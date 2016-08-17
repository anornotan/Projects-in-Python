#"Guess the number" mini-project

import random
import math
import simplegui

num_range = 100
guesses_left = 7
secret_number = random.randrange(0,num_range)

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,num_range)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "New game. Range is from 0 - 100."
    global num_range
    global guesses_left
    num_range = 100
    guesses_left = round(math.log((num_range+1), 2))
    print "Number of remaining guesses is", int(guesses_left)
    new_game()
    print""
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "New game. Range is from 0 - 1000."
    global num_range
    global guesses_left
    num_range = 1000
    guesses_left = round(math.log((num_range+1), 2))
    print "Number of remaining guesses is", int(guesses_left)
    new_game()
    print ""
    
def input_guess(guess):
    # main game logic goes here	
    global guesses_left
    int_guess = int(guess)
    print "Guess was",guess
    guesses_left -= 1
    print "Number of remaining guesses is", int(guesses_left)
    if int_guess > secret_number:
        print "Lower! \n"
    elif int_guess < secret_number:
        print "Higher! \n"
    elif int_guess == secret_number:
        print "Correct! \n"
        if num_range == 100:
            range100()
        if num_range == 1000:
            range1000()
    if guesses_left == 0:
        print "You ran out of guesses. The number was", secret_number, "\n"
        if num_range == 100:
            range100()
        if num_range == 1000:
            range1000()
    
# create frame
f = simplegui.create_frame("Guess my number",1, 150)

# register event handlers for control elements and start frame
button0_100 = f.add_button("Range: 0 - 100", range100, 220)
button0_1000 = f.add_button("Range: 0 - 1000", range1000,220)
inp = f.add_input("Enter your guess:", input_guess, 200)


