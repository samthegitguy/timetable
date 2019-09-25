#This program is used to learn timetables. below are improts of modules
import sys, random
#Function Def
def checkanswer(x,y)
    playersays = input("What is " + x + " plus " + y + " ?")
    if x * y == playersays:
        print ("Correct!")
        score += 1
    else print ("Oops! That's incorrect")
def menu (returning)
    if returning == True:
        print ("Your current score is " + score + ". Let's try and beat it!")
    timetable = input ("What table will you practice? ")
    return timetable
i = 1
score = 0
Returning = False
table = menu (Returning)
for i in range (1,10): 
    checkanswer (x, table)
    i = i + 1
Returning = True



