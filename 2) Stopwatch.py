# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
good_stops = 0
total_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(n):
    global t, d
    t = n
    a = t / 600
    if t % 600 == 0:
        b,c,d = 0,0,0
    else:
        d = t % 10
        c = (t % 100 - d)/10
        b = (t - a*600)/100
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
           
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    
def stop():
    global good_stops, d, total_stops
    if timer.is_running():
        total_stops += 1
        if d == 0:
            good_stops += 1
    timer.stop()
    
    
def reset():
    timer.stop()
    global t, good_stops, total_stops
    t, good_stops, total_stops = 0,0,0

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), (90,160), 50, "White")
    canvas.draw_text((str(good_stops) + "/" + str(total_stops)), (250,30), 30, "White")
    
# create frame
f = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
timer = simplegui.create_timer(100,tick)
f.set_draw_handler(draw)
f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)

# start frame
f.start()

# Please remember to review the grading rubric
format(1215)
