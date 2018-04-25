#I211 Homework 2
#Skyler Payne Boooth
#Spbooth
#Group 54

import random


#Problem 1: Days of the week

#Algorithm for problem 1:::
        
    #Goal: create a function that gets an abbreviation and returns the related full name of that day
    #Starting point: I210, Python Book, Computer with Python Installed

    #1. Set up the definition
    #2. title the user input
    #3. create a dictionary for the days of the week with the key being the abbreviation and the value being the full name
    #4. Return the day of the week

def fullweek(abbreviation):
    #This function asks for a week day abreviation and then returns the full day
    titleAbbreviation = abbreviation.title() #titles the input
    days = {'M': 'Monday', 'T':'Tuesday', 'W': 'Wednesday','R': 'Thursday', 'F': 'Friday', 'S': 'Saturday','U':'Sunday'} #Dictionary of the days of the week
    if titleAbbreviation in days:
        return days[titleAbbreviation] #since it is a function it should return the result if the key is in the dictionary 
    else:
        return "That was not a valid input"

#Test Code for problem 1

print(fullweek("M")) #Should pass
print(fullweek("MOO")) #Should fail



#Problem 2: Loop for the days

#Algorithm for problem 2:::
        
    #Goal: Create a loop that asks a the user for a day abbreviation and give them the day
    #Starting point: I210, Python Book, Computer with Python Installed

    #1. Ask the user for an input (in this case a week day abreviation or 'DONE')
    #2. Check if the user entered the word 'DONE'
        #if so break
    #3. use the fullweek function to return the full day
    #4. Repet from step 1 if the program did not break out

while True:
    userInput = input("Please input a abbreviation or the string 'DONE': ") #Asks the user for their input

    if userInput.upper() == "DONE":
        print("You made it out of the loop... This time...")
        break
    else:
        print(fullweek(userInput))



#Problem 3: Rock Paper Scissors
#Algorithm for problem 3:::
        
    #Goal: Create a python-based Rock, Paper, Scissors game
    #Starting point: I210, Python Book, Computer with Python Installed

    #1. Create list of options for computer to choose from (i.e. Rock, paper, scissors)
    #2. Ask user to input rock paper scissors or stop to stop playing
    #3. Check if the user entered to word stop and if so end the game
    #4. If not, Check to make sure they actually entered the words rock, paper, or scissors and if not let them know that was an invalid input
    #5. Have the computer choose a value randomly from the list of possible choices.
    #6. Determine winner by comparing the computers choice and the users. Rock beats scissors, sciossors cut paper, and paper covers rock. If they chose the same, they tie.
    #7. Tell user who won (or if they tied)
    #8. Repeat from step 2.

print("Welcome to the wonderful game of Rock, Paper, Scissors! May the odds ever be in your fist.")
#Make list of possible choices for computer
rockPaperScissors = ["Rock", "Paper", "Scissors"]
#Make While loop
while True:
    #ask user for input of rock paper scissors or stop
    userInput = input("Please Pick Rock, Paper, or Scissors. You may also enter 'Stop' to quit: ")
    #stops if the user enters stop
    if userInput.upper() == "STOP":
        print("Thank you for playing Rock, Paper, Scissors. Hopefully you did not suffer any physical injuries.")
        break
    elif userInput.title() in rockPaperScissors: #checks to see if user entered Rock paper or scissors
        computerChoice = random.choice(rockPaperScissors) #computer makes random choice
        wonLostTied = "" #sets variable to empty string
        if userInput.title() == computerChoice: #if the user and computer pick the same thing, it's a tie
            wonLostTied = "Tied"
        elif userInput.title() == "Rock" and computerChoice == "Scissors": #The next three check the possible ways the user could win and changes the variable to won if it satisfies any of the three ways, if not it changes the variable to lost.
            wonLostTied = "Won"
        elif userInput.title() == "Scissors" and computerChoice == "Paper":
            wonLostTied = "Won"
        elif userInput.title() == "Paper" and computerChoice == "Rock":
            wonLostTied = "Won"
        else:
            wonLostTied = "Lost"
        print("You chose:", userInput.title() +",", "the computer chose:", computerChoice) #shows the user what they picked and what the computer picked
        print("You", wonLostTied + "!") #shows the user if they won lost or tied
    #tells user error occurs if the user enters anything other than rock paper scissors or stop
    else:
        print("That was an invalid input")
