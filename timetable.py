##################################################################################################################################
#This program was developed by Sam
#It is used to learn timetables. it asks you to choose a timetable to quiz you on, and it asks all the relevant questions, and reports on your success,
#/ failure, and adds score accordingly.
#these are module importations.
import sys, random, 
#Function Definitions
def checkanswer(x ,y ):
    playersays = input()
    if x * y == playersays:
        print ("Correct!")
        score += 1
    else:
	print ("That's incorrect")
def menu (returning):
    if returning == True:
        print ("Your current score is " + score + ". Let's try and beat it!")
    timetable = input ("What table will you practice? ")
    return timetable
#here is main program
i = 1
score = 0
Returning = False
table = menu (Returning)
#main question loop
for i in range (1,10): 
    checkanswer (i, table)
    i = i + 1
#tells the menu to display score next time round
    Returning = True



