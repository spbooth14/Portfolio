#I211 Lab practical 2
#Skyler Booth
#spbooth
#Group 54


#Part 1

import urllib.request
import re
import webbrowser

url = "https://www.indiana.edu/news-events/index.html" #sets the url to the one we were given
web_page = urllib.request.urlopen(url) #opens the website
contents = web_page.read().decode(errors="replace") #reads and decodes it
web_page.close() #closes the page

#Part 2
headlines = re.findall('(?<="headline">).+?(?=<)', contents) #finds all the headlines
print("Searching:", url) #lets the user know its searching the url
print()
for headline in headlines: #prints every headline
    print("\t", headline)
    print()

#Part 3 #######COMMENTED OUT FOR PART 4############
##headlines = re.findall('(?<="headline">).+?(?=<)', contents) #finds all the headlines
##print("Searching:", url) #lets the user know its searching the url
##print()
##userIn = input("Please enter a word to search for: ") #asks the user for a word to search for
##print()
##atleastOne = False #this is incase no matches are found
##for headline in headlines: #goes through each headline
##    if userIn.lower() in headline.lower(): #sees if user input is in the headline
##        print("\t", headline) #if it is it prints the headline
##        print()
##        atleastOne = True #changes to true to let the program know atleast one matched
##if not atleastOne:
##    print("I'm sorry, no articles have the input you entered in their healines") #lets the user know if there were no matches


#Part 4
urls = re.findall('(?<=<h1><a itemprop="url" href=").+?(?=")', contents) #finds all urls relating to news articles
headlineURLTuple = [] #makes empty list
for i in range(len(headlines)):
    headlineURLTuple.append([headlines[i].lower(), urls[i]]) #makes tuple like lists inorder to match headlines to its own url
userIn2 = input("Please enter a word to search for: ") #asks the user for input
atleastOnematch = False #this is incase no matches are found
for tuples in headlineURLTuple: #loops through all the "tuples"
    if userIn2.lower() in tuples[0]: #checks if the user input is in the headline
        webbrowser.open_new_tab(tuples[1]) #if so it opens the url in a new tab
        atleastOnematch = True #changes to true to let the program know atleast one matched
if not atleastOnematch:
    print("I'm sorry, no articles have the input you entered in their healines") #lets the user know if there were no matches
