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
    rules(x_pos,y_pos)
    
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
    rules(x_pos,y_pos)

def South():
    global x_pos
    global y_pos
    if y_pos - 1 > 0:
        y_pos -= 1    
    print (x_pos, y_pos)
    rules(x_pos,y_pos)


def controller():
    control_input = "n"
    rules(x_pos,y_pos, control_input)    
    while True:
        control_input = input("Input Your choice: ").lower()
        if control_input == "e":
            if rules(x_pos,y_pos,control_input):
                East()
            #rules(x_pos,y_pos,control_input)
        if control_input == "w":
            if rules(x_pos,y_pos,control_input):
                West()
            #rules(x_pos,y_pos,control_input)
        if control_input == "s":
            if rules(x_pos,y_pos,control_input):
                rules(x_pos,y_pos,control_input)
                South()
            #rules(x_pos,y_pos,control_input)
        if control_input == "n":
            if rules(x_pos,y_pos,control_input):
                North()
            #rules(x_pos,y_pos,control_input)
        else:

            return False

def rules(x, y, input_check):
    
    if x == 1 and y == 1:
        print("You can travel: ({})orth.".format("N"))
        if input_check != "n":
            print("Not a valid direction!")
        else:
            return True

    if x == 1 and y == 2:
        print("You can travel: ({})outh. ".format("S"))
        print("You can travel: ({})ast. ".format("E"))
        print("You can travel: ({})orth. ".format("N"))
        if input_check != "n" or input_check !="e" or input_check != "s":
            print("Not a valid direction!")
        else:
            return True
            
    if x == 1 and y == 3:
        print("You can travel: ({})outh. ".format("S"))
        print("You can travel: ({})ast. ".format("E"))
        if input_check !="e" or input_check != "s":
            print("Not a valid direction!")
        else:
            return True

    if x == 2 and y == 1:
        print("You can travel: ({})orth. ".format("N"))
        print("You can travel: ({})est. ".format("W"))
        if input_check != "n" or input_check !="w":
            print("Not a valid direction!")
        else:
            return True

    if x == 2 and y == 3:
        print("You can travel: ({})est. ".format("W"))
        print("You can travel: ({})ast. ".format("E"))
        if input_check != "w" or input_check !="e":
            print("Not a valid direction!")
        else:
            return True

    if x == 3 and y == 3:
        print("You can travel: ({})est. ".format("W"))
        print("You can travel: ({})outh. ".format("S"))
        if input_check != "w" or input_check !="s":
            print("Not a valid direction!")
        else:
            return True

    if x == 3 and y == 2:
        print("You can travel: ({})orth. ".format("N"))
        print("You can travel: ({})outh. ".format("S"))
        if input_check != "n" or input_check != "s":
            print("Not a valid direction!")
        else:
            return True

    if x == 3 and y == 1:
        print("Victory")
        return False

    return x, y


    
game()