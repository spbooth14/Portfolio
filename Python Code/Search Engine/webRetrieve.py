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

def minimum(numberOfQueryTerms, mode):
    if numberOfQueryTerms != int(numberOfQueryTerms):
        return "Error: the number of query terms isn't an integer"
    if mode.lower() == "or":
        return int(1)
    elif mode.lower() == "and":
        return int(numberOfQueryTerms)
    elif mode.lower() == "most":
        return int(numberOfQueryTerms//2)+1
    elif mode.lower() == "bigram":
        return int(1)
    elif mode.lower() == "trigram":
        return int(1)
    else:
        return "The mode you entered was invalid"

def calculateTFIDF(masterDict, hit, docLength, tokenqueryWords, numberOfFiles):
    pageDict = {} #sets up a page dict for each hit
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
    return sum(wordTFIDFScore)

def totalScore(tfidfScore, pageRankDict, url):
    rank = pageRankDict.get(url)
    total = tfidfScore * rank
    return total
    
def retrieve(mode, lst): #these arguments require a mode and atleast one query word but will accept any number of them
    queryWords = [arg.lower() for arg in lst] #makes a list of query words if there are any additional ones
    ##queryWords.append(word.lower()) #adds the first one to the list
    pageRankFile =open("pageRankDict.dat", "rb")#.readlines() #opens the invindex on a line by line basis
    pageRankDict = pickle.load(pageRankFile)
    stop_words = set(stopwords.words('english'))
    queryWords = [word for word in queryWords if word not in stop_words] #takes stop words out of query terms
    if mode.lower() == "or" or mode.lower() == "most" or mode.lower() == "and":
        ps = PorterStemmer() #brings in the same stemmer used to make the invindex.dat
        tokenqueryWords = [ps.stem(word) for word in queryWords] #stems all the query words
    elif mode.lower() == "bigram":
        if len(queryWords) == 2:
            phrase = queryWords[0] + " " +queryWords[1]
            tokenqueryWords = [phrase]
        else:
            errorMessage = "You searched for a bigram but entered " + str(len(queryWords)) +  " term(s)"
            return errorMessage
##    elif mode.lower() == "trigram":
##        if len(queryWords) == 3:
##            phrase = queryWords[2] + " " + queryWords[0] + " " + queryWords[1]
##            tokenqueryWords = [phrase]
##        else:
##            errorMessage = "You searched for a trigram but entered " + str(len(queryWords)) +  " term(s)"
##            return errorMessage
    else:
        return "The mode you entered is invalid"
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
    hitList = [] #creates a set hit list 
    for i in range(len(tokenqueryWords)): #goes through each of the query terms
        if tokenqueryWords[i] in masterDict: #checks if the query term is a key in master dict
            for value in masterDict.get(tokenqueryWords[i]): #goues through each of the values
                hitList.append(value[0].strip(" ")) #gets the url and adds it to the hit list (which is a set so it doesnt show duplicates 
    if len(hitList) > 0: #if the hit list has one or more hits it prints them
        termCount = {}
        for hit in hitList:
            if hit not in termCount:
                termCount[hit] = 1
            else:
                termCount[hit] += 1
        numberNeed = minimum(len(tokenqueryWords), mode)
        hitSet = set()
        for key in termCount:
            if int(termCount.get(key)) >= int(numberNeed):
                   hitSet.add(key)
        if len(hitSet) > 0:
            scoreList =[] #sets up a tfidf list to keep track of each of the hits' scores
            for hit in hitSet: #goes through all the hits
                url = hit #gets the url
                title = urlToTitle.get(hit) #gets the title
                docLength = urlToLength.get(hit) #gets the doc length
                tfIDFScore = calculateTFIDF(masterDict, hit, docLength, tokenqueryWords, numberOfFiles)
                rankTimesTFIDF = totalScore(tfIDFScore, pageRankDict, url)
                scoreList.append([rankTimesTFIDF, url, title]) #adds the sum of the word tfidf scores, the url, and the title to the tfidf list
            return scoreList
        else:
            return "No matches found" 
    else: #if the hit list has no hits it tells the user
        return "No matches found"

print(retrieve("most", ['germany']))

