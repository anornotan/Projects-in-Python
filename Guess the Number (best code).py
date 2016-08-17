# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# initialize global variables used in your code here

number_range = 100
rem_guesses = 7
ans = 0

# helper function to start and restart the game

def new_game():
    
    global number_range, rem_guesses, ans
    
    ans = random.randint(0, number_range)
    
    if number_range == 100:
        rem_guesses = 7
    elif number_range == 1000:
        rem_guesses = 10
    
    print "New game. Range is from 0 to ", number_range 
    print "Number of remaining guesses is ", rem_guesses
    print ""
        
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global number_range
    
    number_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global number_range
    
    number_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    global number_range, rem_guesses, ans
    
    rem_guesses = rem_guesses - 1
    
    print "Guess was", guess
    print "Number of remaining guesses is", rem_guesses
    
    if int(guess) > ans and rem_guesses > 0:
        print "Lower!"
        print ""
    elif int(guess) < ans and rem_guesses > 0:
        print "Higher!"
        print ""
    elif int(guess) == ans and rem_guesses >= 0:
        print "Correct!"
        print ""
        new_game()
    elif int(guess) != ans and rem_guesses == 0:    
        print "You ran out of guesses. The number was", ans
        print ""
        new_game()
        
# create frame

frame = simplegui.create_frame("Guess the number", 150, 150)
frame.set_canvas_background("Black")

# register event handlers for control elements and start frame

button_1 = frame.add_button("Range is (0, 100)", range100, 150)
button_2 = frame.add_button("Range is (0, 1000)", range1000, 150)
inp = frame.add_input("Enter a guess", input_guess, 150)
frame.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
