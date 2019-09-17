
def rules(x, y):

    if x == 1 and y == 1:
        print("you can travel: ({})orth)".format("N"))

    if x == 1 and y == 2:
        print("you can travel: ({})orth) ".format("S"))
        print("you can travel: ({})orth) ".format("E"))
        print("you can travel: ({})orth) ".format("N"))

    if x == 1 and y == 3:
        print("you can travel: ({})orth) ".format("S"))
        print("you can travel: ({})orth) ".format("E"))

    if x == 2 and y == 1:
        print("you can travel: ({})orth) ".format("N"))
        print("you can travel: ({})orth) ".format("W"))

    if x == 2 and y == 3:
        print("you can travel: ({})orth) ".format("W"))
        print("you can travel: ({})orth) ".format("E"))

    if x == 3 and y == 3:
        print("you can travel: ({})orth) ".format("W"))
        print("you can travel: ({})orth) ".format("S"))

    if x == 3 and y == 2:
        print("you can travel: ({})orth) ".format("N"))
        print("you can travel: ({})orth) ".format("S"))

    if x == 3 and y == 1:
        print("you can travel: ({})orth) ".format("N"))

    return x, y




x_pos = 1
y_pos = 1

                                                             
def game():                                                                             
    #print(STRING[:x_pos-1] + "o"+ STRING[0:(10 - x_pos)])                         
    #print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    controller()
     

def West():                                                                            
    global x_pos
    global y_pos
    if x_pos - 1 > 0:                                                                
        x_pos -= 1
    print (x_pos,y_pos)

def East():
    global x_pos
    global y_pos
    if x_pos + 1 <= 3:
        x_pos += 1    
    print (x_pos, y_pos)
    
def North():
    global x_pos
    global y_pos
    if y_pos + 1 <= 3:
        y_pos += 1    
    print (x_pos, y_pos)

def South():
    global x_pos
    global y_pos
    if y_pos + 1 <= 3:
        y_pos -= 1    
    print (x_pos, y_pos)


def controller():                                                                       
    while True:
        control_input = input("Input your choice: ").lower()
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
rules(x_pos,y_pos)
    
game()