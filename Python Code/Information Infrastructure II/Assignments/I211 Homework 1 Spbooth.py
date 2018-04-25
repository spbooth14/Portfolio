#I211 Homework 1
#Skyler Payne Boooth
#Spbooth

#Problem #1 Rock Paper Scissors

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

#Sorry I made the game before I realized that it said only the algorithm


import random
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










#Problem #2 List Checker
        
lst1 = ["Sam", "Bob", "Skyler"] #test list
lst2 = ["Jerry", "Samantha"] #test list
lst3 = ["Bob"] #test list
def listChecker(listOne, listTwo): #defines the program list checker.
    #gives a welcome statement for fun
    print("Welcome to the list checker. This check identifies if there is a common element in the two lists you enter: if so, you will see the word 'True' appear, if not, the word 'False' will appear.")
    trueFalse = "False" #Gives automatic value of false and only changes if they share a common element
    for item in listOne: #loops through all values in list one
        if item in listTwo: #checks to see if any items in list one are in list two
            trueFalse = "True" #if so it changes the value from false to true
    print(trueFalse) #Tells user whether or not they had a match

listChecker(lst1, lst2) #test code
listChecker(lst1, lst3) #test code







#Problem #3 Back those words up

print("Welcome to Back As Words, where we like to take your input and reverse it!") #Fun Welcome message

while True: #creates while loop
    word = input("Please enter a string or Stop: ") #Asks the user to input any string and sets the string to a variable
    if word.upper() == "STOP": #Checks to make sure the user didnt say stop, if so it ends the program
        print("Thank you for using Back As Words. Try not to say things backwards after this experience.") #Fun goodbye message
        break #breaks while loop
    else:
        print("You entered the string", word + ",", "this string backwards is", word[::-1]) #tells the user their string they entered and then the [::-1] prints the string backwards
