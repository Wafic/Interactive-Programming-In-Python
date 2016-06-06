# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
sw = 0
attempt = 0
win = 0
score = "0/0"
run = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(sw):
    A = str(sw / 600)
    B = str(sw / 100 % 6 )
    C = str(sw % 100 / 10)
    D = str(sw % 10)
    return A + ":" + B + C + "." + D 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global run
    timer.start()
    run = True
    
def stop_handler():
    global attempt, win, score, run
    timer.stop()
    if run == True:
        attempt += 1
        win_template = '.0'
        if win_template in format(sw):
            win += 1
        score = str(win) + '/' + str(attempt)
    run = False

def reset_handler():
    global sw, attempt, win, score, run
    timer.stop()
    # set everything back to zero
    sw = 0
    attempt = 0
    win = 0
    score = "0/0"
    run = False
      
# define event handler for timer with 0.1 sec interval
def inc_timer():
    global sw
    if sw < 5999:
        sw += 1
    else:
        reset_handler()

# define draw handler
def draw_time(canvas):
    canvas.draw_text(format(sw), (100, 150), 48, 'White')
    canvas.draw_text(score, (250, 30), 24, 'Blue')
    
    
# create frame
frame = simplegui.create_frame('Stop Watch', 300, 300)
frame.set_draw_handler(draw_time)
start = frame.add_button('Start', start_handler)
stop = frame.add_button('Stop', stop_handler)
reset = frame.add_button('Reset', reset_handler)

# register event handlers
timer = simplegui.create_timer(100, inc_timer)

# start frame
frame.start()
