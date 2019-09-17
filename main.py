x_pos = 1
y_pos = 1

                                                             
def game(): 
    print("You can travel: (N)orth.")                                                                            
    #print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    controller()
     

def West():                                                                            
    global x_pos
    global y_pos
    if x_pos - 1 > 0:                                                                
        x_pos -= 1
    else:
        print("Direction: Not a valid direction!")
    print (x_pos,y_pos)

def East():
    global x_pos
    global y_pos
    if x_pos + 1 <= 3:
        x_pos += 1 
    else:
        print("Direction: Not a valid direction!")   
    print (x_pos, y_pos)
    
def North():
    global x_pos
    global y_pos
    if y_pos + 1 <= 3:
        y_pos += 1    
    else:
        print("Not a valid direction!")
    print (x_pos, y_pos)

def South():
    global x_pos
    global y_pos
    if y_pos - 1 > 0:
        y_pos -= 1
    else:
        print("Not a valid direction!")   
    print (x_pos, y_pos)


def controller():                                                                       
    while True:
        control_input = input("Direction: ")
        if control_input == "e":
            East()
        elif control_input == "w":
            West()
        elif control_input == "s":
            South()
        elif control_input == "n":
            North()
        else:
            return False


game()
