import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":#Goutham's 5
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.fd(35)
        tur.right(180)
        tur.fd(35)
        tur.left(90)
        tur.fd(55)
        tur.left(90)
        tur.fd(35)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(25)
        tur.pu()
        tur.right(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(25)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "H":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(55)
        tur.left(180)
        tur.fd(35)
        tur.right(90)
        tur.fd(35)
        tur.left(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(55)
        tur.left(90)
        tur.pu()
        tur.fd(60)
        tur.right(90)
        tur.fd(5)
    elif letter == "I":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.fd(40)
        tur.right(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(40)
        tur.pu()
        tur.left(90)
        tur.fd(60)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        
    elif letter == "J":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.fd(40)
        tur.left(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(25)
        tur.pu()
        tur.fd(40)
        tur.right(90)
        tur.fd(45)
        
    elif letter == "K":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.left(180)
        tur.fd(30)
        tur.right(45)
        tur.fd(45)
        tur.left(180)
        tur.fd(45)
        tur.left(90)
        tur.fd(45)
        tur.left(180)
        tur.fd(45)
        tur.right(45)
        tur.pu()
        tur.fd(35)
        tur.right(90)
        tur.fd(45)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.left(180)
        tur.fd(30)
        tur.right(45)
        tur.fd(45)
        tur.left(180)
        tur.fd(45)
        tur.left(90)
        tur.fd(45)
        tur.left(180)
        tur.fd(45)
        tur.right(45)
        tur.pu()
        tur.fd(35)
        tur.right(90)
        tur.fd(45)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(60)
        tur.left(180)
        tur.fd(30)
        tur.right(45)
        tur.fd(45)
        tur.left(180)
        tur.fd(45)
        tur.left(90)
        tur.fd(45)
        tur.left(180)
        tur.fd(45)
        tur.right(45)
        tur.pu()
        tur.fd(35)
        tur.right(90)
        tur.fd(45)
    elif letter == "L":#Gabe's5
	tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.pu()
    elif letter == "M":
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.setheading(-45)
        tur.pd()
        tur.fd(30)
        tur.setheading(45)
        tur.fd(30)
        tur.setheading(-90)
        tur.fd(30)
        tur.back(30)
        tur.left(90)
        tur.fd(5)
        tur.pu() 
    elif letter == "N":
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.setheading(-60)
        tur.pd()
        tur.fd(35)
        tur.setheading(45)
        tur.setheading(90)
        tur.fd(30)
        tur.right(90)
        tur.pu()
    elif letter == "O":
        tur.pd()
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(35)
        tur.pu()   
    elif letter == "P":
        tur.pd()
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.setheading(270)
        tur.fd(60)
        tur.setheading(90)
        tur.fd(60)
        tur.right(90)
        tur.fd(30)
        tur.pu()		
    elif letter == "Q":#Nick's 5
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(25)
        tur.left(90)
        tur.fd(25)
        tur.right(45)
        tur.fd(10)
        tur.right(180)
        tur.fd(20)
        tur.right(180)
        tur.fd(10)
        tur.left(135)
        tur.fd(25)
        tur.left(90)
        tur.fd(25)
        tur.right(180)
        tur.pu()
        tur.fd(55)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "R":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(15)
        tur.left(135)
        tur.fd(20)
        tur.pu()
        tur.left(135)
        tur.fd(35)
        tur.right(90)
        tur.fd(25)
    elif letter == "S":
        tur.pu()
        tur.fd(35)
        tur.right(90)
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.right(90)
        tur.fd(35)
        tur.right(90)
        tur.fd(35)

    elif letter == "T":
         tur.pu()
         tur.fd(5)
         tur.right(90)
         tur.fd(5)
         tur.left(90)
         tur.pd()
         tur.fd(30)
         tur.right(180)
         tur.fd(15)
         tur.left(90)
         tur.fd(30)
         tur.pu()
         tur.left(180)
         tur.fd(35)
         tur.right(90)
         tur.fd(20)
         
    elif letter == "U":

         tur.fd(10)
         tur.right(90)
         tur.fd(5)
         tur.pd()
         tur.fd(30)
         tur.left(90)
         tur.fd(20)
         tur.left(90)
         tur.fd(30)
         tur.pu()
         tur.fd(5)
         tur.right(90)
         tur.fd(10)
         pass
     elif letter == "V":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(30)
        tur.fd(40)
        tur.left(120)
        tur.fd(40)
        tur.left(30)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)


    elif letter == "W":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(30)
        tur.fd(40)
        tur.left(130)
        tur.fd(15)
        tur.right(130)
        tur.fd(15)
        tur.left(130)
        tur.fd(40)
        tur.left(20)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)

    elif letter == "X":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(45)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.left(45)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)

    elif letter == "Y":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.right(50)
        tur.fd(25)
        tur.right(40)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(40)
        tur.fd(25)
        tur.pu()
        #fix
        tur.left(40)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)


    elif letter == "Z":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()     
        tur.left(90)
        tur.fd(30)
        tur.right(135)
        tur.forward(40)
        tur.left(135)
        tur.forward(30)
        #fix
        tur.pu()
        tur.left(90)
        tur.fd(40)
        tur.right(90)


        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
