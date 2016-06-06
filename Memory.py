# implementation of card game - Memory

import simplegui
import random

ls1 = range(0,8,1)
ls2 = range(0,8,1)
c_list = ls1 + ls2
WIDTH = 800
HEIGHT = 100
exposed = []

# helper function to initialize globals
def new_game():
    global exposed, state, c_list, turns
    exposed = [False]*16
    random.shuffle(c_list)
    state = 0
    turns = 0
    label.set_text("Turns = 0")
     
# define event handlers
def mouseclick(pos):
    global r, c1,c2, exposed, state, turns
    r = pos[0] // 50
    #exposed[r] = True
    if exposed[r] == 0:
        if state == 0:
            c1 = r
            exposed[c1] = True
            state = 1
        elif state == 1:
            c2 = r
            exposed[c2] = True
            turns += 1
            label.set_text("Turns = " + str(turns))
            state = 2
        elif state == 2:
            if c_list[c1] != c_list[c2]:
                exposed[c1] = False
                exposed[c2] = False
            c1,c2= 0,0
            c1 = r
            exposed[c1] = True
            state = 1
        else:
            state = 1
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global c_list, x, exposed
    x = 50
    for i in range(0,len(c_list)): 
        if exposed[i] == False:
            canvas.draw_polygon([[i*x,0],[i*x, 100],[i*x+50,100],[i*x+50,0]], 5, 'Black', 'Green')
        else:   
            canvas.draw_text(str(c_list[i]),[i * WIDTH // 16 + 20, HEIGHT/2 + 10], 40, 'Red')
            

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()