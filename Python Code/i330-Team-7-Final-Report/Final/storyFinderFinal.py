import urllib.request
import re

def storyFinder():
    storyURLSet = set() #keeps track of the URLs in the results pages
    keyWordsList =[["technology", "privacy"], ["technology", "data", "breach"], ["technology", "data", "collection"], ["technology", "data", "sharing"]] #keywords to be searched on Chicago Tribune
    baseURL1 = "http://www.chicagotribune.com/search/dispatcher.front?Query=" #base URL for results page 1
    baseURL2 = "http://www.chicagotribune.com/search/dispatcher.front?page=" #base URL for results page 2+
    url1part2= "&target=stories&isSearch=true&spell=on" #2nd part of the url for page 1 results 
    url2part2 = "&isSearch=true&target=stories&spell=on&Query=" #2nd part of the url for page 2+ results
    url2part3 = "#trb_search" #3rd part of the url for page 2+ results
    print("We are gathering all the stories that are related to technology privacy incidents from the Chicago Tribune...") #lets the user know the program is running
    for i in range(len(keyWordsList)): #goes through each set of keywords
        pageCount = 1 #starts the page count at 1
        url = "" #sets the url variable
        while True: #creates a loop so the results pages keep getting downloaded until their arent any
            if len(keyWordsList[i]) == 1: #chekcs if their is only one keyword in the set in order to set up the approprite url
                if pageCount == 1:
                    url = baseURL1 + str(keyWordsList[i][0]) + url1part2
                else:
                   url = baseURL2 + str(pageCount) + url2part2 + keyWordsList[i][0] + url2part3
            else:
                searchTermsForPage1 = ""
                searchTermsForOthers = ""
                for j in range(len(keyWordsList[i])-1): #creates the string of keywords for page one and other pages
                    searchTermsForPage1 += keyWordsList[i][j] + "+"
                    searchTermsForOthers += keyWordsList[i][j] + "%20"
                searchTermsForPage1 += keyWordsList[i][-1]
                searchTermsForOthers += keyWordsList[i][-1]
                if pageCount == 1: #checks if the page count is 1 or not so it can set up the appropriate url
                    url = baseURL1 + str(searchTermsForPage1) + url1part2
                else:
                    url = baseURL2 + str(pageCount) + url2part2 + searchTermsForOthers + url2part3
            try: #trys to open the url
                req = urllib.request.Request(url, data=None, headers={"User-Agent": "IUB-I330-Group-7"}) #sets the request to include user agent as IUB-I330-Group-7
                web_page = urllib.request.urlopen(req)
            except:
                break
            else:
                contents = web_page.read().decode(errors="replace") #reads the web page
                contents = contents.replace('\n', ' ') #replaces the newline characters with a space
                contents = contents.lower() #lowercases the html page
                resultCount = re.findall('(?<=data-search-resultcount=").+?(?=")', contents) #gets the number of results since it changes to 0 if you go beyond the final page of results
                resultCount = str(resultCount[0])
                if resultCount == "0": #moves to the next keyword set if the last results page has been downlaoded
                    break
                else:
                    matches = re.findall('(?<=<div class="trb_search_result" data-content-id=").+?(?=trb_search_result_icon)', contents) #finds all of the urls                                
                    web_page.close() #closes the web connection
                    for match in matches: #goes through all the results
                        storyURL = re.findall('(?<=trb_search_result_title" href=").+?(?=")', match) #pulls out the urls
                        if storyURL[0][0] == "/": #changes local url to full url
                            storyURL = "http://www.chicagotribune.com" + storyURL[0]
                        else:
                            storyURL = storyURL[0]
                        if "redeye" in storyURL: #deletes redeye sponsored stories
                            pass
                        else:
                            storyURLSet.add(storyURL) #adds the url to the set                        
                    pageCount += 1
    print("All stories have been found") #lets the user know its done running
    return storyURLSet #returns the url set
