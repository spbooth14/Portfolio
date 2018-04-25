#I211 Homework 3
#Skyler Payne Boooth
#Spbooth
#Group 54


#Problem 1: Team Wins

#Algorithm for problem 1:
        
    #Goal: create a function that reads a file and returns the teams with their wins, a list of the team names that the name is shorter than 5 letters, and a list of the three most winning teams
    #Starting point: I210, Python Book, Computer with Python Installed

    #1. Set up the definition with the file name as the argument
    #2. read in the file
    #3. output the data the file gives as The *Team Name* have won *Number* games (the name and number are read from the file)
    #4. determine all the teams that have a name shorter than 5 letters and give it to the user
    #5. Determine the three most winning teams and return them to the user

def teams(filename): #creates the function 'teams'
    file_contents = [line.strip().split() for line in open(filename, "r")] #Reads in the file line by line and strips "/n" and splits it
    teamWins = "".join(["The " + file_contents[i][0] + " have won " + file_contents[i][1] + " games\n" for i in range(len(file_contents))]) #makes the phrase The *Team Name* have won *Number* games in the order the file gives it and makes a new line for each one
    print(teamWins) #prints the wins of each team
    shorterThan5 = [file_contents[i][0] for i in range(len(file_contents)) if len(file_contents[i][0]) < 5] #loops through the list of teams and filters out the teams with length longer than 4
    print("Teams with names shorter than 5 letters:", shorterThan5) #Prints the team names that are shorter than 5 characters
    mostWins = [[int(file_contents[i][1]), file_contents[i][0]] for i in range(len(file_contents))] #Flips the order of team and wins to wins and team in order to sort it by number of wins
    mostWins = sorted(mostWins) #sorts in from lowest number of wins to the highest
    mostWins = mostWins[::-1] #reverses it to be highest wins to lowest
    highestWins = [mostWins[i][1] for i in range(3)] #makes a list of the 3 most winning teams
    print()
    print("The three teams with the highest wins are:", highestWins) #prints the three most winning teams


teams("teams.txt") #test code




