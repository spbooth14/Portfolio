#I211 Homework 4
#Skyler Payne Boooth
#Spbooth
#Group 54


import os
import datetime

def pl_translate(word):
    if len(word) <= 1:
        return word+"yay"
    pre = word[0]
    suf = word[1:]
    if pre.upper() == pre:
        cap = True
    else:
        cap = False
    pig = suf + pre.lower() + "ay"
    if cap:
        pig = pig[0].upper() + pig[1:]
    return pig

#PrePhase Test
#print(pl_translate("Please"))

#Phase 1

#Algorithm for Phase 1:
        
    #Goal: Create a function that translates sentences into Pig Latin
    #Starting point: I210, Python Book, Computer with Python Installed, Starting function

    #Split the sentence into words
    #Use the pl_translate function to translate each word
    #use another function to move punctuation
        #define the function
        #go through every letter and see if it is a punctuation mark
        #if so move it to the end
        #go through the letters again to see if there is a 's
        #if so move the ' and the s to the end to translate the possesive into pig latin


def punctuationMover(word): #this is to move punctuation after translation
    punctuation = ["!",".",",","?"] 
    for i in range(len(word)): 
        if word[i] in punctuation: #this checks if a character is a punctuation marke
            word = word[:i] + word[i+1:] + word[i] #this breaks the word into three parts and joins the part before the mark with the part after the mark and moves the mark to the end
    for i in range(len(word) -1): #this looks for the possesive s
        if word[i] == "'" and word[i+1] == "s": #checks if a char is a ' and the one after it is a s
            word = word[:i] + word[i+2:] +word[i] + word[i+1] #if so it moves the possesive s and the ' to the end
    return word
        

def pl_words(phrase):
    phraseList = [word for word in phrase.split()] #splits the phrase into inividual words for translation
    phraseList = [pl_translate(word) for word in phraseList] #translates each word
    phraseList = [punctuationMover(word) for word in phraseList] #Performs the punctuation check
    return phraseList #returns the list of translated words

#Phase 1 Test
#print(pl_words("Please translate me."))
        
#Phase 2 and 4


#Algorithm for Phase 2:
        
    #Goal: Create a function that brings in a file, translates it all to pig latin, then write all the translate words to a new file
    #Starting point: I210, Python Book, Computer with Python Installed

    #import datetime
    #make sure it is a valid file
    #read in the file if its valid
    #translate the file
    #open the writeable file
    #loop through the list of translated words
    #write the word to the output file
    #close the file

#Algorithm for Phase 4:
        
    #Goal: edit the function to include the day, month, year and time the file was translated as well as a thank you note
    #Starting point: I210, Python Book, Computer with Python Installed

    #get the current time and date
    #write in the current time and date in the format given
    #Write a thank you at the bottom of the output file

def pl_converter(inputFilename, outputFilename):
    try:
        fileContents = open(inputFilename, "r") #checks to make sure file is valid
    except:
        print("Not a valid filename")
    else:
        fileContents = fileContents.read().strip() #opens the file as a big string
        fileContents = pl_words(fileContents) #translates the words
        output = open(outputFilename, 'w') #opens the output file
        now_time = datetime.datetime.today() #gets the time
        output.write(now_time.strftime("%A, the %d of %B, %Y, %H:%M") +"/n") #puts the formated time at the top of the output file
        for word in fileContents:
            output.write(word + "\n") #writes every word as its own line
        output.write("Thank you for using the Igpay Atlinlay Translator") #Thank you statement at the end of the file
        output.close() #closes the output file
        
#Phase 2 Test   
#pl_converter("clear.txt", "cipher1.txt")
    
#Phase 3
        
#Algorithm for Phase 3:
        
    #Goal:
    #Starting point: I210, Python Book, Computer with Python Installed, Previous Functions

    #import os
    
    #Create a variable that equals the cwd
    #Change to the directory to the starting directory
    #List all of the directories in the cwd
    #ask the user to select one, if it is invalid go back to step 2
    #Change to the directory the user said
    #list all of thae available files
    #Show the user the list
    #tell the user to pick one, if not valid go back to step 2
    #create the name for the output file based on the input file name
    #call the pl_converter function on the input and output file
    #Tell the user the file has been translated
        
startingDir = os.getcwd() #gets the starting directory incase a directory or file doesnt exist it will change back to the original directory when it starts over
while True:
    os.chdir(startingDir) #This changes to the original directory
    directories = [file for file in os.listdir(os.getcwd()) if os.path.isdir(file)] #lists the directories
    userInput = input("Please select a directory: ") #gets a directory name for the user
    if userInput in directories: #checks validity 
        home = os.getcwd() 
        path = os.path.join(home, userInput) #creates a new path with the user defined directory
        os.chdir(path) #changes to said directory
        files = [file for file in os.listdir(os.getcwd()) if os.path.isfile(file)] #lists the files
        print("Files in this directory:") 
        print(files) #prints the list of files
        userFile = input("Please select a file to translate: ") #gets a file from the user
        if userFile in files: #checks validity
            transFile = userFile[:len(userFile)-4] + "(pig)" + userFile[len(userFile)-4:] #splits the input file name into two chunks, name (i.e. novel) and extension (i.e. .txt) and then places the word (pig) between them to get the output file name
            pl_converter(userFile, os.path.join(path, "translations", transFile)) #runs the converter, also notice that the path of the transFile is wrote out. This is so it gets output in the translations folder
            print("Your file was successfully tanslated into Pig Lating and will be found in the translations folder.") #success print statement
            break
        else: #if the file doesn't exist it gives this message and starts the loop over
            print("I'm sorry but it looks like you had a typing issue, cant spell, or just can't read since the thing you entered is not a file in this directory. So let's try this again.") #hope you enjoy my jokes
    else: #if the directory doesn't exist it gives this message and starts the loop over
        print("That is not a valid directory. Try again.")

    


