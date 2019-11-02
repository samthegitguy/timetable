##################################################################################################################################
#Welcome to the special Blitz(streak) version of this game. It will continue to quiz you until you get something wrong.
#This program was developed by Sam
#It is used to learn timetables. it asks you to choose a timetable to quiz you on, and it asks all the relevant questions, and reports on your success,
#/ failure, and adds score accordingly.
#Detailed description can be found in readme.txt
#these are module importations.
import sys, random
#Function Definitions
repeat = True
while repeat:
    #three vars are taken in. 
    #x to be the first number to check
    #Y to be the second number
    #and thescore to manipulate the score as functions cannot manipulate global variables. See github.com/samthegitguy/timetable/issues/1 for more information.
    def checkanswer(x ,y,correct):
        playersays = input("What is " + str(x) + " times " + str(y) + " ? ")
        if x * y == playersays:
            print ("Correct!")
            correct = True
        else:
            print ("That's incorrect")
            correct = False
        return correct
    def menu ():
        if score != 0:
            print ("Your current score is " + str(score) + ". Let's try and beat it!")
        print ("Please note that you must not enter numbers via number pad, or letters.\n^c to quit at any time.")
        timetable = input ("What table will you practice? ")
        return timetable
#here is setup program
    i = 1
    score = 0
    table = menu ()
#main question loop
    globalcorrect = True
    while globalcorrect == True: 
        globalcorrect = checkanswer (i, table,globalcorrect )
        i = i + 1
    print("Your Score Is..." + str(score) + " ! ")
    repeatcheck = True
    while repeatcheck == True:
        theinput = raw_input("Would you like to try again? (Y/N): ")
        theinput = theinput.lower()
        if theinput == "y":
            repeat = True
            repeatcheck = False
        elif theinput == "n":
            repeat = False
            repeatcheck = False
        else:
            #the variable repeatcheck is a boolean value to tell whether the answer is Y or N. See github.com/samthegitguy/timetable/issues/5 for more details.
            print("You haven't chosen Y or N. Please choose again.")
            repeatcheck = True
print("Thanks for playing. Come again soon!")
time.sleep(2)
exit()



