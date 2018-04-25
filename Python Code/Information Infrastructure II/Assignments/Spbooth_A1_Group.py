#Skyler Booth
#Spbooth
#Group 54

# create a funcation storm_by_event
# have this funcation take an event type
# have the funcation print info on all events in IN for the year

# create a new funcation date
# have this fuction take a date
# make it print information of every storm in IN on that date

# ask user if they want to search by date or event
# if they answer date ask them for a date then show results for that date
# if they answer event show the events of that type


import csv
import datetime
import time

def storm_by_event(eventType):
    eventTypes = ["Dense Fog", "Blizzard", "Cold/Wind Chill", "Excessive Heat", "Extreme Cold/Wind Chill", "Flash Flood", "Flood", "Hail", "Heat", "Heavy Rain", "Heavy Snow", "Ice Storm", "Lake-Effect Snow", "Lightning", "Strong Wind", "Thunderstorm Wind", "Tornado", "Winter Storm", "Winter Weather"]
    storms = csv.DictReader(open("Indiana_Storms.csv", "r"))
    if eventType in eventTypes:
        for storm in storms:
            if storm["EVENT_TYPE"] == eventType.title():
                print("A", storm["EVENT_TYPE"], "happened on", storm["BEGIN_YEARMONTH"][4:] +"/" + storm["BEGIN_DAY"] +"/" + storm["BEGIN_YEARMONTH"][:4], "in", storm["CZ_NAME"], "county.")
    else:
        print("The Event Type you entered wasn't valid!")

def storm_by_date(date):
    valid = False
    storms = csv.DictReader(open("Indiana_Storms.csv", "r"))
    yearMonth = date.strftime("%Y%m")
    day = date.strftime("%d")
    for storm in storms:
        if storm["BEGIN_YEARMONTH"] == yearMonth and storm["BEGIN_DAY"] == day:
            print("A", storm["EVENT_TYPE"], "happened on", storm["BEGIN_YEARMONTH"][4:] +"/" + storm["BEGIN_DAY"] +"/" + storm["BEGIN_YEARMONTH"][:4], "in", storm["CZ_NAME"], "county.")
            valid = True
    if not valid:
        print("No events happened on this date.")
###MAIN###
while True:
    userInput = input("Would you like to search by date or by event?: ")
    if userInput.title() == "Date" or userInput.title() == "Event":
        if userInput.title() == "Event":
            userEvent = input("Please enter the type of weather you are searching for: ")
            storm_by_event(userEvent)
            break
        else:           
            userDate = input("Please enter your date in YYYY/MM/DD format: ")
            date = datetime.date(int(userDate[:4]), int(userDate[5:7]), int(userDate[8:]))
            storm_by_date(date)
            break
    
    else:
        print("That is not a valid selection. Please try again.")












#storm_by_event("Dense Fog")
#date = datetime.date(2015, 5, 15)
#storm_by_date(date)

