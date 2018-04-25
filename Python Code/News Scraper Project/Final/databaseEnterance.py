#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb
import csv

def databaseEnterance(dic):
    string = "i211f16_spbooth" #change username to yours!!!
    password = "my+sql=i211f16_spbooth" #change username to yours!!!
    db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string, charset='utf8') #connects to MySQL database
    cursor = db_con.cursor() #creates the cursor
    print("Stories are being added to the incidents database") #notifies the user that the stories are being added
    with open('incidents.csv', 'w') as csvfile: #opens the csv file in order to add the stories too it
        fieldnames = ["URL", "Title", "Author", "Publishing_Date", "Description"] #creates the headers for the CSV File
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
        writer.writeheader() #writes the headers to the CSV file
        for story in dic: #goes through each story in the dictionary
            url = story #the url equals the key in the dictionary because thats what each story was saved under since they're unique identifiers
            storyInfo = dic.get(story) #gets the list of information from the story
            storyTitle= storyInfo[3] #sets the variable title to the title of the story
            storyAuthor = storyInfo[0] #sets the variable title to the title of the story
            storyDate = storyInfo[1] #sets the variable title to the title of the story
            storyDesc = storyInfo[2] #sets the variable title to the title of the story
            writer.writerow({'URL': url, 'Title': storyTitle, 'Author': storyAuthor, 'Publishing_Date': storyDate, 'Description': storyDesc}) #writes the story to the CSV File
            try:    #Always surround .execute with a try!
                SQL = "INSERT INTO incidents (url, title, author, postdate, description) VALUES ('{}', '{}', '{}', '{}', '{}');".format(url, storyTitle, storyAuthor, storyDate, storyDesc) #creates the insert statement for the SQL database using the story information
            except:		#Here we handle the error
                pass #if there is an error with the story, we assume that the story is missing information somehow, so we discard it
            else: #This runs if there was no error
                cursor.execute(SQL) #executes the SQL statement which adds the story to the database
                db_con.commit() #commits the change to the database, so it basically saves the changes made
                print("Story Added Successfully") #lets the user know that the story was successfully added
        csvfile.close() #after all stories are done being added, it closes the open CSV file
    print("Stories have finished populating the incidents database") #lets the user know that the code is done running
 
