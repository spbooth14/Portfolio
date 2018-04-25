from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
import re
from html.parser import HTMLParser
import nltk
import os
import sys
import argparse
import pickle

def strip(htmlString): #The function strip takes html file and get rid of tags/javascripts, only left content
    soup = BeautifulSoup(htmlString, "html.parser")
    for script in soup("script"):
        script.extract()
    return soup.get_text()

def index(pagesDirectory, indexFileName):
    cwd = os.getcwd() #gets the current working directory
    newPath = os.path.join(cwd, pagesDirectory) #creates a path to the pages directory
    try:
        os.chdir(newPath) #trys to change the path
    except:
        return "The directory you entered does not exist in the current directory." #tells the user if that directory doesnt exist in the cwd
    else: 
        masterDict = {} #if it does it does all this stuff!... Creates a master dictionary for terms to list of urls
        docsDat = [] #creates a list for the three tuple items of number of terms, title of the page, and the url
        fileNameToURL = {}
        try: #trys to open the index file
            indexDat = open(indexFileName, "r").readlines()
        except:
            return "The index file name you entered does not exist in this directory!"
        else:
            numberOfFiles = len(indexDat) #gets how many html files there should be
            for i in range(numberOfFiles): #goes through each line in index dat
                    indexDat[i] = indexDat[i].strip().split() #strips the \n
                    fileNameToURL[indexDat[i][0]] = indexDat[i][1]
            htmlFilesInCWD = [file for file in os.listdir() if ".html" in file] #gets the html files in the cwd
            if len(htmlFilesInCWD) != numberOfFiles: #checks if the number of html files in the cwd and the number of files in the index.dat are the same
                return ("The amount of files specified in the index file and the number of HTML files in the", pagesDirectory, "directory aren't equal, please fix this and try again")
            for i in htmlFilesInCWD: #goes through each html
                url = fileNameToURL.get(i) #creates a string for the url
                pageDict = {} #creates a term, count dictionary for each page
                htmlPage = open(i, "r", encoding="utf8").read() #opens the html page
                cleanHtml = strip(htmlPage) #strips html tags
                stop_words = set(stopwords.words('english')) #gets the set of english stop words
                word_tokens = word_tokenize(cleanHtml) #gets the text from the html page and tokenizes words
                numberOfTerms = len(word_tokens) #gets the number of words in the file

                #####EXTRA CREDIT SECTION 1######
##                bigrams = []
##                trigrams = []
##                for i in range(len(word_tokens) -1):
##                    bigram = word_tokens[i] + " " + word_tokens[i+1]
##                    bigrams.append(bigram)
                for i in range(len(word_tokens) -1): #gets all the bigrams
##                    trigram = word_tokens[i] + " " + word_tokens[i+1] + " " + word_tokens[i+2]
##                    if trigram not in pageDict: #checks if the phrase is in the page dict
##                        pageDict[trigram] = 1 #sets the phrase as a key and sets count to 1
##                    else:
##                        pageDict[trigram] += 1 #adds 1 to the count if its in there
                    ##trigrams.append(trigram)
                    bigram = word_tokens[i] + " " + word_tokens[i+1]
                    if bigram not in pageDict: #checks if the phrase is in the page dict
                        pageDict[bigram] = 1 #sets the phrase as a key and sets count to 1
                    else:
                        pageDict[bigram] += 1 #adds 1 to the count if its in there
                    ##bigrams.append(bigram)
##                for bigram in bigrams: #goes through each bigram phrase
##                    if bigram not in pageDict: #checks if the phrase is in the page dict
##                        pageDict[bigram] = 1 #sets the phrase as a key and sets count to 1
##                    else:
##                        pageDict[bigram] += 1 #adds 1 to the count if its in there
##                for trigram in trigrams: #goes through each trigram phrase
##                    if trigram not in pageDict: #checks if the phrase is in the page dict
##                        pageDict[trigram] = 1 #sets the phrase as a key and sets count to 1
##                    else:
##                        pageDict[trigram] += 1 #adds 1 to the count if its in there
                #####END OF EXTRA CREDIT SECTION 1######
                        
                filtered_tokens = [word.lower() for word in word_tokens if word not in stop_words] #takes out any stopwords
                ps = PorterStemmer() #gets the stemmer
                stemmed_tokens = [ps.stem(word) for word in filtered_tokens] #stems each token
                stemmed_words = [re.sub(r'[^\w\s]','',word) for word in stemmed_tokens] #takes out punctuation
                for word in stemmed_words: #goes through each stemmed word
                    if word not in pageDict: #checks if the word is in the page dict
                        pageDict[word] = 1 #sets the word as a key and sets count to 1
                    else:
                        pageDict[word] += 1 #adds 1 to the count if its in there
                for key in pageDict: #goes through each key in the local page dictionary
                    if key not in masterDict: #checks if the key is in the master dict
                        value = pageDict[key] #if not it sets the key with the url and the count
                        masterDict[key] = [[url, value]]
                    else: #if it is in it adds the url and count to the key 
                        masterDict[key].append([url, value])
                soup = BeautifulSoup(htmlPage,'html.parser') #creates another beautiful soup opject
                title = "No Title" #initializes title as no title
                try:
                    soup.title.string #gets the title of the local page
                except:
                    title = "No Title"
                else:
                    title = soup.title.string #sets title as the title
                if title == None: 
                    title = "No Title" #sets title as no title if there isn't a title
                title = title.strip() #strips the title
                docsDat.append([numberOfTerms, title, url]) #makes a tuple-like opject of the number of terms, the title of the url, and the url and adds it to the docs.dat list
            inverIndex = open("invindex.dat", "wb") #once it goes through all the html pages in the directory, it opens the new invindex file
            pickle.dump(masterDict, inverIndex) #puts the masterDictionary into the inverIndex file as a python dictionary
            inverIndex.close() #closes the file
            docsDatFile = open("docs.dat", "wb") #opens the doc.dat file
            pickle.dump(docsDat, docsDatFile)#writes the docsDat list into the Docs.dat file
            docsDatFile.close() #closes the file
            return "Done"
    
    
##index("pages/", "index.dat")


def main(*args):
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('directory' , help="This is the directory of where the html pages are located. This directory must be a direct subdirectory of the current working directory", type=str)
    parser.add_argument('indexFile', help="This is the file that links the name of each html file to its url. It must be in the html pages directory.", type=str)
    args = parser.parse_args()
    index(args.directory, args.indexFile)
if __name__ == '__main__':
    main(*sys.argv)
