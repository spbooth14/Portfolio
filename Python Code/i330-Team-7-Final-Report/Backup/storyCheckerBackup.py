import urllib.request
import re
import pickle
import argparse
import sys

def storyChecker():
    pickle_in = open("storyURLSet.pickle", "rb")
    storyURLSet = pickle.load(pickle_in)
    pickle_in.close()
    storyURLDict = {} #storyURL: Author, date, Title
    policyWordsList = ["law", "congress", "hippa", "legal", "policy"]
    print("Currently checking stories for precision and regulatory/legal requirements...")
    for i in range(len(storyURLSet)):
        keywordFound = False
        try: #trys to open the url
            url = storyURLSet.pop()
            req = urllib.request.Request(url, data=None, headers={"User-Agent": "IUB-I330-Group5"}) #sets the request to include user agent as IUB-I427-spbooth
            web_page = urllib.request.urlopen(req)
        except:
            break
        else:
            contents = web_page.read().decode(errors="replace") #reads the web page
            contents = contents.replace('\n', ' ')
            upperCase = contents
            contents = contents.lower()
            body = re.findall('(?<=articlebody).+?(?=trb_ar_cr)', contents)
            if len(body) != 0:
                body = body[0]
            else:
                body = contents
            for keyword in policyWordsList:
                if keyword in body:
                    keywordFound = True
                    break
                else:
                    pass
            if keywordFound == True:
                storyAuthor = re.findall('(?<=meta name="author" content=").+?(?=")', contents)
                storyDate = re.findall('(?<=<meta name="date" content=").+?(?=")', contents)
                storyDescription = re.findall('(?<=meta name="Description" content=").+?(?=")', upperCase)
                storyTitle = re.findall('(?<=<meta name="fb_title" content=").+?(?=")', contents)
                if len(storyAuthor) == 0:
                    storyAuthor = ["None"]
                if len(storyDate) == 0:
                    storyDate = ["None"]
                if len(storyTitle) == 0:
                    storyTitle = ["None"]
                if len(storyDescription) == 0:
                    storyDescription = "None"
                else:
                    storyDescription = storyDescription[0]
                    storyDescription = storyDescription.replace("&amp;", "&")
                    storyDescription = storyDescription.replace("&rsquo;", "")
                    storyDescription = storyDescription.replace("&ldquo;", '"')
                    storyDescription = storyDescription.replace("&rdquo;", '"')
                    storyDescription = storyDescription.replace("&hellip;", '...')
                    storyDescription = storyDescription.replace("&apos;", "")
                    storyDescription = storyDescription.replace("&quot;", '"')
                    storyDescription = storyDescription.replace("'", "")
                storyURLDict[url] = [storyAuthor[0].title(), storyDate[0], storyDescription, storyTitle[0].title()]
                web_page.close()
            else:
                web_page.close()
    print("Stories have been check for precision and regulatory/legal componets and have all be added to a new pickle document")
    print("Please run the 'databaseEnteranceBackup.py' in order to add all the stories to the database and CSV File")
    pickle_out = open("storyURLDict.pickle", "wb")
    pickle.dump(storyURLDict, pickle_out)
    pickle_out.close()

def main(*args):
    parser = argparse.ArgumentParser(prog='PROG')
    args = parser.parse_args()
    print(storyChecker())
    
if __name__ == '__main__':
    main(*sys.argv)          
