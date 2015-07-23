# "Stopwatch: The Game" AJM 0615

import simplegui

# define global variables
elapsed_time = 0  # toatal elapsed time in tenths of a second
successful = 0  # number of times the clock is stopped when tenths = 0
attempts = 0  # total attempts at stopping clock when tenths = 0
running = False  # Boolean so that "Stop" does not increment game counters unless
                 # clock is running

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    total_seconds = t //10
    seconds = total_seconds % 60
    minutes = total_seconds // 60
    if seconds < 10:
        seconds_zero = "0"
    else:
        seconds_zero = ""
    if minutes > 9:
        reset()
    return str(minutes) + ":" + seconds_zero + str(seconds) + "." + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True
    
def stop():
    global successful, attempts, running
    if running:
        attempts += 1
        if (elapsed_time % 10) == 0:
            successful += 1
        running = False
    timer.stop()
    
def reset():
    global elapsed_time, attempts, successful, running
    elapsed_time = 0
    attempts = 0
    successful = 0
    running = False
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global elapsed_time
    elapsed_time +=1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(elapsed_time), [120, 165], 60, "Red")
    canvas.draw_text(str(successful) + " / " + str(attempts), [280, 45], 36, "Yellow")
    
# create frame
main_frame = simplegui.create_frame("main", 400, 300)
start_button = main_frame.add_button("Start", start, 150)
stop_button = main_frame.add_button("Stop", stop, 150)
reset_button = main_frame.add_button("Reset", reset, 150)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
main_frame.set_draw_handler(draw_handler)

# start frame
main_frame.start()
