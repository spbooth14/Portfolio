import urllib.request
import re
import pickle
import argparse
import sys

def storyFinder():
    storyURLSet = set()
    keyWordsList = [["technology", "privacy"], ["technology", "data", "breach"], ["technology", "data", "collection"], ["technology", "data", "sharing"]]
    baseURL1 = "http://www.chicagotribune.com/search/dispatcher.front?Query="
    baseURL2 = "http://www.chicagotribune.com/search/dispatcher.front?page="
    url1part2= "&target=stories&isSearch=true&spell=on"
    url2part2 = "&isSearch=true&target=stories&spell=on&Query="
    url2part3 = "#trb_search"
    print("We are gathering all the stories that are related to technology privacy incidents from the Chicago Tribune...")
    for i in range(len(keyWordsList)):
        pageCount = 1
        url = ""
        while True:
            if len(keyWordsList[i]) == 1:
                if pageCount == 1:
                    url = baseURL1 + str(keyWordsList[i][0]) + url1part2
                else:
                   url = baseURL2 + str(pageCount) + url2part2 + keyWordsList[i][0] + url2part3
            else:
                searchTermsForPage1 = ""
                searchTermsForOthers = ""
                for j in range(len(keyWordsList[i])-1):
                    searchTermsForPage1 += keyWordsList[i][j] + "+"
                    searchTermsForOthers += keyWordsList[i][j] + "%20"
                searchTermsForPage1 += keyWordsList[i][-1]
                searchTermsForOthers += keyWordsList[i][-1]
                if pageCount == 1:
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
                contents = contents.replace('\n', ' ')
                contents = contents.lower()
                resultCount = re.findall('(?<=data-search-resultcount=").+?(?=")', contents)
                resultCount = str(resultCount[0])
                if resultCount == "0":
                    break
                else:
                    matches = re.findall('(?<=<div class="trb_search_result" data-content-id=").+?(?=trb_search_result_icon)', contents) #finds all of the urls                                
                    web_page.close() #closes the web connectiom
                    for match in matches:
                        storyURL = re.findall('(?<=trb_search_result_title" href=").+?(?=")', match)
                        if storyURL[0][0] == "/":
                            storyURL = "http://www.chicagotribune.com" + storyURL[0]
                        else:
                            storyURL = storyURL[0]
                        if "redeye" in storyURL:
                            pass
                        else:
                            storyURLSet.add(storyURL)                        
                    pageCount += 1
    print("All stories have been found and added to the pickle file")
    print("Please run the 'storyCheckerBackup.py' file to check the stories")
    pickle_out = open("storyURLSet.pickle", "wb")
    pickle.dump(storyURLSet, pickle_out)
    pickle_out.close()

def main(*args):
    parser = argparse.ArgumentParser(prog='PROG')
    args = parser.parse_args()
    print(storyFinder())
    
if __name__ == '__main__':
    main(*sys.argv)

