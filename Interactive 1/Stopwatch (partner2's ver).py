# "Stopwatch: The Game"
import simplegui

# define global variables
tenth_of_seconds = 0
watch_stopped = 0
watch_stopped_on_second = 0

# define helper function
def format(t):
    """
    Gets an integer input representing tenths of seconds
    and converts it to the format M:SS.T, where
        M is the number of minutes, 
        SS is the number of seconds (with a leading zero if 
            necesary)
        T is the number of tenth of seconds
    and returns this format as a string
    """
    tenths = t % 10
    total_seconds = t / 10
    minutes = total_seconds / 60
    seconds = total_seconds % 60
    return str(minutes) + ":" + str(seconds).rjust(2, '0') + "." + str(tenths)
    
# define event handlers
def start():
    """
    Event handler of the Start button.
    Starts the timer.
    """
    timer.start()
    
def stop():
    """
    Event handler of the Stop button.
    Stops the timer and increases the stop counters.
    """
    global watch_stopped_on_second, watch_stopped
    if timer.is_running():
        timer.stop()
        watch_stopped += 1
        if tenth_of_seconds % 10 == 0:
            watch_stopped_on_second += 1
    
def reset():
    """
    Event handler of the Reset button.
    Stops the timer and resets the stop counters and the watch.
    """
    global tenth_of_seconds, watch_stopped_on_second, watch_stopped
    timer.stop()
    tenth_of_seconds = 0
    watch_stopped = 0
    watch_stopped_on_second = 0

def tick():
    """
    Event handler of the timer.
    Increments the watch.
    """
    global tenth_of_seconds
    tenth_of_seconds += 1

def draw(canvas):
    """
    Draw handler of the canvas.
    Draws the watch and the counter texts.
    """
    canvas.draw_text(format(tenth_of_seconds), [110, 110], 34, "White")
    hits = str(watch_stopped_on_second) + "/" + str(watch_stopped) 
    canvas.draw_text(hits, [260, 20], 24, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

