from databaseEnterance import * #imports the database entrance program
from storyFinderFinal import * #imports the story finder program
from storyChecker import * #imports the story checker program
import argparse #needed to run on linux server
import sys #same as abover

def incidentFinder():
    storyURLSet = storyFinder() #runs the story finder and sets its output(a url set) to a variable
    dic = storyChecker(storyURLSet) #runs the story check program using the set from story finder and then saves its output (a url:story information dictionary) to another variable
    databaseEnterance(dic) #runs the database entrance program using the dictionary from story checker
    print("Incident Finder Complete") #lets the user know that the program is done running
    
def main(*args): #code below is to make the program run on the linux server
    parser = argparse.ArgumentParser(prog='PROG')
    args = parser.parse_args()
    print(incidentFinder())
    
if __name__ == '__main__':
    main(*sys.argv)
