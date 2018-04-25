import urllib.request #needed to access webpages
import re #needed to search webpage and extract information

def storyChecker(storyURLSet):
    storyURLDict = {} #storyURL: [Author, date, Title, description]
    policyWordsList = ["law", "congress", "hippa", "legal", "policy"] #list of regulatory/legal keywords used to see if article deals with these issues
    print("Currently checking stories for precision and regulatory/legal requirements...") #lets the user know that the program is running
    for i in range(len(storyURLSet)): #goes through each url in the url set
        keywordFound = False #sets a variable to false that the story contains one of the keywords
        try: #trys to open the url
            url = storyURLSet.pop() #gets the last url in the set
            req = urllib.request.Request(url, data=None, headers={"User-Agent": "IUB-I330-Group-7"}) #sets the request to include user agent as IUB-I330-Group-7 so the Chicago Tribune knows we are the ones crawling their site
            web_page = urllib.request.urlopen(req) #trys to open the url
        except:
            break #if the webpage fails to connect, it moves on to the next
        else:
            contents = web_page.read().decode(errors="replace") #reads the web page
            contents = contents.replace('\n', ' ') #replaces all the newline characters with a space
            upperCase = contents #keeps the content in its current capital form (this is used for extracting the description
            contents = contents.lower() #lowercases all the content
            body = re.findall('(?<=articlebody).+?(?=trb_ar_cr)', contents) #finds the body of the article to be searched through
            if len(body) != 0: #changes the body from a list item to a string (findall returns a list even if there is only one result)
                body = body[0] 
            else: #changes the body to the entire page if Re.Findall had an error
                body = contents
            for keyword in policyWordsList: #goes through each keyword and sees if the article contians one, if it does the article goes for data extraction, if not it gets tossed
                if keyword in body:
                    keywordFound = True
                    break
                else:
                    pass
            if keywordFound == True:
                storyAuthor = re.findall('(?<=meta name="author" content=").+?(?=")', contents) #pulls the story's author
                storyDate = re.findall('(?<=<meta name="date" content=").+?(?=")', contents) #pulls the date the story was published
                storyDescription = re.findall('(?<=meta name="Description" content=").+?(?=")', upperCase) #Gets the description of the story
                storyTitle = re.findall('(?<=<meta name="fb_title" content=").+?(?=")', contents) #grabs the title of the story
                if len(storyAuthor) == 0: #if any of the story peices do not have a value that was found (either it didn't have one or Re.Findall had an error) it defienes the section as None
                    storyAuthor = ["None"]
                if len(storyDate) == 0:
                    storyDate = ["None"]
                if len(storyTitle) == 0:
                    storyTitle = ["None"]
                if len(storyDescription) == 0:
                    storyDescription = "None"
                else:
                    storyDescription = storyDescription[0] #replaces common HTML character mark-ups with their correlating utf8 character
                    storyDescription = storyDescription.replace("&amp;", "&")
                    storyDescription = storyDescription.replace("&rsquo;", "")
                    storyDescription = storyDescription.replace("&ldquo;", '"')
                    storyDescription = storyDescription.replace("&rdquo;", '"')
                    storyDescription = storyDescription.replace("&hellip;", '...')
                    storyDescription = storyDescription.replace("&apos;", "")
                    storyDescription = storyDescription.replace("&quot;", '"')
                    storyDescription = storyDescription.replace("'", "")
                storyURLDict[url] = [storyAuthor[0].title(), storyDate[0], storyDescription, storyTitle[0].title()] #adds the story and it's information to the dictionary 
                web_page.close() #closes the webpage
            else:
                web_page.close() #if the story had no keywords, it gets closed and nothing from that story is added to the dictionary
    print("Stories have been check for precision and regulatory/legal componets") #lets the user know that the program is done running
    return storyURLDict #returns the dictionary for the database entrance program to use
            
