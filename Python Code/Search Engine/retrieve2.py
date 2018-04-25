import argparse
import sys
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pickle
from nltk.tokenize import word_tokenize
import re
import string
import math
from bs4 import BeautifulSoup
from html.parser import HTMLParser

def retrieve2(word, *args): #these arguments require a mode and atleast one query word but will accept any number of them
    queryWords = [arg.lower() for arg in args] #makes a list of query words if there are any additional ones
    queryWords.append(word.lower()) #adds the first one to the list
    stop_words = set(stopwords.words('english'))
    queryWords = [word for word in queryWords if word not in stop_words] #takes stop words out of query terms
    ps = PorterStemmer() #brings in the same stemmer used to make the invindex.dat
    tokenqueryWords = [ps.stem(word) for word in queryWords] #stems all the query words
    numberOfTokens = len(tokenqueryWords) #gets the number of query words for later use
    masterDict = {} #makes the master dictionary in order to bring in the invindex
    urlToTitle = {} #creates a url to title dictonary
    urlToLength = {}
    inverIndex = open("invindex.dat", "rb")#.readlines() #opens the invindex on a line by line basis
    masterDict = pickle.load(inverIndex)
    docsDat = open("docs.dat", "rb")#.readlines() #opens the docs file on a line by line basis
    docsTuples = pickle.load(docsDat)
    numberOfFiles = len(docsTuples) #gets the length of it (i.e. the number of lines) because thats how many urls there are
    for tuples in docsTuples: #goes through each line
        url = tuples[2].strip() #strips the \n off the url
        title = tuples[1].strip() #strips the title
        length = tuples[0]
        urlToTitle[url] = title #puts the url as the key and the title as the value in the url to title dictionary
        urlToLength[url] = length
    print("Searching...")
    hitList = []
    numberOfHitsNeeded = 0
    if len(tokenqueryWords)%2 == 0: #checks if there is an even number of query words
        numberOfHitsNeeded = len(tokenqueryWords)/2 #if so it makes the most number half of that amount
    else:
        numberOfHitsNeeded = (len(tokenqueryWords)//2)+1 #if its odd it needs half using int division plus one (i.e 3//2 = 1 + 1 = 2, so for most of 3 it needs atleast 2)
    for i in range(len(tokenqueryWords)):
        if tokenqueryWords[i] in masterDict:
            for value in masterDict.get(tokenqueryWords[i]):
                hitList.append(value[0].strip(" "))
    if len(hitList) > 0:
        mostHitList = set()
        for word in hitList:
            if hitList.count(word) >= numberOfHitsNeeded: #checks if a url has atleast half of the terms in it
                mostHitList.add(word)
        if len(mostHitList) > 0: #checks if there are any in the most hit list
            tfIDFList =[] #sets up a tfidf list to keep track of each of the hits' scores
            print("Hits:")
            for hit in mostHitList: #goes through all the hits
                url = hit #gets the url
                title = urlToTitle.get(hit) #gets the title
                pageDict = {} #sets up a page dict for each hit
                docLength = urlToLength.get(hit) #gets the doc length
                for word in tokenqueryWords: #goes through each of query words
                    values = masterDict.get(word) #gets the values which is a list of lists
                    if values:
                        for value in values: #goes through each value and checks if the url matches the hits url. If it does it adds it to the page dict
                            if value[0] == hit: #the values are the number of times that word appears in the document and the number of documents the word appears in
                                pageDict[word] = [int(value[1]), len(values)]
                    else:
                        pass
                wordTFIDFScore =[] #creates a list for all the individual words tfidf scores
                for key in pageDict: #goes through all the words in the individual page dictionary
                    values = pageDict.get(key) #gets the values
                    tf = values[0] / docLength #gets the tf by divididing the number of times that word appears by the number of words in the document
                    idf = math.log(numberOfFiles/values[1]) #gets the idf by taking the log of the number of documents divided by the number of documents that word appears in
                    wordTFIDFScore.append(tf*idf) #multiplies the tf by the idf and adds it to the word TFIDF list
                tfIDFList.append([sum(wordTFIDFScore), url, title]) #adds the sum of the word tfidf scores, the url, and the title to the tfidf list
            tfIDFList = sorted(tfIDFList) #sorts the list by the tfidf scores
            tfIDFList = tfIDFList[::-1] #reverses the list so its in descending order
            if len(tfIDFList) > 25: 
                for i in range(25): #prints the first 25 hits in order of tf-idf if there are more than 25 hits
                    print("Url:", tfIDFList[i][1])
                    print("Title:", str(tfIDFList[i][2]))
                    print("TF-IDF Score:", round(tfIDFList[i][0], 4))
                    print()
                print("Number of pages searched:", numberOfFiles)
                print("Number of hits:", len(mostHitList))
                return None
            else:
                for page in tfIDFList: #prints each page in the tfidf list
                    print("Url:", page[1])
                    print("Title:", str(page[2]))
                    print("TF-IDF Score:", round(page[0], 4))
                    print()
                print("Number of pages searched:", numberOfFiles)
                print("Number of hits:", len(mostHitList))
                return None
        else:
            print("No matches found")
            return None
    else:
        print("No matches found")
        return None
retrieve2("unit", "jhfksdf")
def main(*args):
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('word', help="This is the first string to be searched for. This is the required argument since you can't do a search without atleast one string", type=str)
    parser.add_argument('words', nargs="*", help="Enter any amount of additional strings (seperated by spaces) as you want to search for.", type=str)
    args = parser.parse_args()
    retrieve2(args.word, *args.words)
if __name__ == '__main__':
    main(*sys.argv)
