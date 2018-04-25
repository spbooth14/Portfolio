#I211 Homework 5
#Skyler Payne Boooth
#Spbooth
#Group 54

#Part 1

#Algorithm for Part 1:
        
    #Goal: Create a program that opens a CSV document and displays its contents as a lsit
    #Starting point: I210, Python Book, Computer with Python Installed, Starting URL

    #import urllib
    #import csv
    #Define the function
    #Check if valid url- if so start the connection, if not tell the user
    #open a file
    #write the contents of the url to the file
    #close the file
    #open the same file and read it
    #print the contents of it using csv reader

import urllib.request
import csv
import webbrowser

###commented out in order to do part two in a new function



##def getQuakeData():
##    try:
##        earthquakeData = urllib.request.urlopen("http://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2016-09-23%2000:00:00&endtime=2016-09-30%2023:59:59&minmagnitude=4.5&eventtype=earthquake&orderby=time")
##    except:
##        print("The url is invalid!")
##    else:
##        earthquakeCSV = open("earthquakeCSV", "w")
##        earthquakeCSV.write(earthquakeData.read().decode(errors="replace"))
##        earthquakeData.close()
##        earthquakeCSV.close()
##        earthquakeCSV = open("earthquakeCSV", "r")
##        earthquakeInfoList= list(csv.reader(earthquakeCSV))
##        return earthquakeInfoList
##        
##print(getQuakeData())
##data = getQuakeData()
##
##


#Part 2

#Algorithm for Part 2:
        
    #Goal: Create a program that opens a CSV document and displays its contents as a lsit
    #Starting point: I210, Python Book, Computer with Python Installed, function from part 1

    #create a variable argument called orderby and an argument called limit
    #delete the orderby at the end of the web address and add the variable orderby to the end
    #loop through the list and only print the first (limit) elements
    #write the new list to the csv file

def getQuakeData(orderby, limit): #defines the function
    
    try:
        earthquakeData = urllib.request.urlopen("http://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2016-09-23%2000:00:00&endtime=2016-09-30%2023:59:59&minmagnitude=4.5&eventtype=earthquake&orderby="+orderby) #trys to open the url ordered by the users order
    except:
        print("The url is invalid!") #if its invalid it tells the user
    else:
        earthquakeCSV = open("earthquakeCSV.csv", "w") #if its valid it opens a csv file 
        earthquakeCSV.write(earthquakeData.read().decode(errors="replace")) #writes everything from the url file to a local file
        earthquakeData.close() #closes internet connection
        earthquakeCSV.close() #closes the csv file 
        earthquakeCSV = open("earthquakeCSV.csv", "r") #opens it again as a read file
        earthquakeInfoList= list(csv.reader(earthquakeCSV)) #gets the contents as a list
        earthquakeCSV.close() #closes the file
        earthquakeInfoList = [earthquakeInfoList[i] for i in range(int(limit + 1))] #loops through the list and gets the first (limit) elements
        rewritingFile = csv.DictWriter(open("earthquakeCSV.csv", "w"), fieldnames= earthquakeInfoList[0]) #rewrties the local csv file with only the elements above
        rewritingFile.writeheader() #writes the heders, i.e. the elements in the first list in the info list
        for i in range(1, len(earthquakeInfoList)):
            rowDict = {}
            for j in range(22):
                rowDict[earthquakeInfoList[0][j]] = earthquakeInfoList[i][j]
            rewritingFile.writerow(rowDict) #writes each row with the header as the key and the element at the j position in the i list as the value
        #print(earthquakeInfoList)
        return "earthquakeCSV.csv" #returns the name of the file
                              
#Part 3
    #Algorithm for Part 3:
        
    #Goal: Create a program that opens a CSV document and displays its contents as a lsit
    #Starting point: I210, Python Book, Computer with Python Installed, function from part 2

    #Define function
    #use the function getQuakeData to get data
    #print a table using id number, magnitude, location and a time for each quake.

def getTopQuakes(data):
    data = csv.DictReader(open(data, "r")) #opens the csv file that has already went through the getQuakesData function
    print("ID"," "*10, "Mag", " "*2, "Location", " "*41, "Time") #prints the headers
    print("-"*100) #prints 100 dashes
    for earthquake in data: #goes through every earthquake in the file 
        print("{} {} {} {}".format(earthquake["id"] + " "*3, earthquake["mag"] + " "*(6-len(earthquake["mag"])), earthquake["place"] + " "*(50-len(earthquake["place"])), earthquake["time"]))
    #^^^ prints the id magnitude location and time for the top 10 earth quakes in a formatted table
    print() #prints a blank line after
    
#Part 4 and 5
    #Algorithm for Part 4 and 5:
        
    #Goal: Create a program that opens a CSV document and displays its contents as a lsit
    #Starting point: I210, Python Book, Computer with Python Installed, function from part 3

    #Define function
    #open the earth quake csv
    #loop through the earthquaks and se if there is one that matches the users input
    #print out the details of the matching earthquake
    #Ask the user if they want to see a map of the quake location
    #replace the latitude and longitude in the url with the quake's
    #open the map
    

def getQuakeDetails(quake_id):
    data = getQuakeData("magnitude", 10) #gets the csv file that has already went through the getQuakesData function
    data = csv.DictReader(open(data, "r")) #opens the file using dict reader 
    valid = False #sets a valid checker that changes to true if a earthquake matches the user input, if not itll tell the user
    for earthquake in data: #loops through all the quakes in the file
        if earthquake["id"] == quake_id: #checks if the id is equal to the users input
            print() #blank line
            print("ID"," "*10, "Mag", " "*2, "Time", " "*24, "Lat", " "*6, "Long", " "*5, "Place") #prints the header
            print("-"*102) #prints A LOT of dashes, A LOT!!!
            print("{} {} {} {} {} {}".format(earthquake["id"] + " "*3, earthquake["mag"] + " "*(6-len(earthquake["mag"])), earthquake["time"] + " "*5, earthquake["latitude"] +" "*(10 - len(earthquake["latitude"])), earthquake["longitude"] +" "*(10 - len(earthquake["longitude"])), earthquake["place"]))
            #^^^ prints the id magnitude time latitude longitude and location for the user specified earthquake in a formatted table
            print()
            valid = True#changes the valid to true since a earthquake met the user specification
            while True: #creates a while loop incase the user enters something that is illogical
                mapOpen = input("Would you like to open this earthquake in google mapes (yes or no): ").lower() #asks the user if they wanna open a map
                if mapOpen == "yes": #if yes
                    url = "https://maps.googleapis.com/maps/api/staticmap?center=" + earthquake["latitude"] +"," + earthquake["longitude"] +"&zoom=9&markers=" + earthquake["latitude"] +"," + earthquake["longitude"] +"&size=640x640&scale=2&key=AIzaSyADS8f73GSJVtMPMkqCz2bNDoWVrphV5GM"
                    #^^^ changes the given url to open at the earthquake's location by changing the latitue and longitude
                    webbrowser.open(url) #opens the url
                    break #breaks the loop
                elif mapOpen == "no": #thanks the user if they dont wanna open a map
                    print()
                    print("Thank for your time")
                    break #breaks looop
                else:
                    print()
                    print("That was an invalid response") #tells the user if they entered some nonsense            
    if not valid:
        print("The Earthquake ID you entered does not exist.") #tells the user if they entered an invalid ID
    
#TEST CODE
            
data = getQuakeData("magnitude", 10)
getTopQuakes(data)
userInput = input("Please select an earthquake's ID for more details: ")
getQuakeDetails(userInput)   
