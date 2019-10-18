##################################################################################################################################
#This program was developed by Sam
#It is used to learn timetables. it asks you to choose a timetable to quiz you on, and it asks all the relevant questions, and reports on your success,
#/ failure, and adds score accordingly.
#Detailed description can be found in readme.txt
#these are module importations.
import sys, random
#Function Definitions
def checkanswer(x ,y,thescore):
    playersays = input("What is " + str(x) + " times " + str(y) + " ? ")
    if x * y == playersays:
        print ("Correct!")
        thescore += 1
    else:
	print ("That's incorrect")
    return thescore
def menu ():
    print ("Your current score is " + str(score) + ". Let's try and beat it!")
    timetable = input ("What table will you practice? ")
    return timetable
#here is main program
i = 1
score = 0
table = menu ()
#main question loop
for i in range (1,10): 
    score = checkanswer (i, table, score)
    i = i + 1
print("Your Score Is..." + str(score) + " ! ")


