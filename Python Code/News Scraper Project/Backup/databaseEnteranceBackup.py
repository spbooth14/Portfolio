#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb
import csv
import pickle
import argparse
import sys

def databaseEnterance():
    pickle_in = open("storyURLDict.pickle", "rb")
    dic = pickle.load(pickle_in)
    pickle_in.close()
    string = "i211f16_spbooth" 		#change username to yours!!!
    password = "my+sql=i211f16_spbooth" 	#change username to yours!!!
    db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string, charset='utf8')
    cursor = db_con.cursor()
    print("Stories are being added to the incidents database")
    with open('incidentsBackup.csv', 'w') as csvfile:
        fieldnames = ["URL", "Title", "Author", "Publishing_Date", "Description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for story in dic:
            url = story
            storyInfo = dic.get(story)
            storyTitle= storyInfo[3]
            storyAuthor = storyInfo[0]
            storyDate = storyInfo[1]
            storyDesc = storyInfo[2]
            writer.writerow({'URL': url, 'Title': storyTitle, 'Author': storyAuthor, 'Publishing_Date': storyDate, 'Description': storyDesc})
            try:    #Always surround .execute with a try!
                SQL = "INSERT INTO incidentsBackup (url, title, author, postdate, description) VALUES ('{}', '{}', '{}', '{}', '{}');".format(url, storyTitle, storyAuthor, storyDate, storyDesc)
                #print(SQL)
            except:		#Here we handle the error
                pass
            else: #This runs if there was no error
                cursor.execute(SQL)
                db_con.commit()
                print("Story Added Successfully")
        csvfile.close()
    print("Stories have finished populating the incidents database and the CSV File")

def main(*args):
    parser = argparse.ArgumentParser(prog='PROG')
    args = parser.parse_args()
    print(databaseEnterance())
    
if __name__ == '__main__':
    main(*sys.argv)
