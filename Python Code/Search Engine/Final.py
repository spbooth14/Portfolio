import os
import sys
import subprocess
import urllib.request
import re
import time
from collections import deque
import urllib.robotparser
import argparse
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from crawl import *
from index import *
from pageRank import *

def final(seedURL, pageLimit, directory, searchAlg):
    crawler(seedURL, pageLimit, directory, searchAlg) #runs the crawler
    index(directory, "index.dat") #indexes all the files that the cralwer found
    webGraphFile = open("webGraph.dat", "rb") #opens the webGraph that the crawler made
    webGraph = pickle.load(webGraphFile)
    pageRank(webGraph) #runs pagerank on the web graph
    return "Done"
    
#MAIN#
##print(final("https://en.wikipedia.org/wiki/World_War_II", 2000, "pages/", "BFS", "index.dat"))  # <----- #test file
##print(index("pages/", "index.dat"))
##webGraphFile = open("pages/webGraph.dat", "rb")
##webGraph = pickle.load(webGraphFile)
##print(pageRank(webGraph))
##pageRankFile = open("pageRankDict.dat", "rb")
##pageRanks = pickle.load(pageRankFile)
##for page in pageRanks:
##    print(page)
##    print(pageRanks.get(page))
##    print("-"*50)

###COMMAND LINE STUFF GOES BELOW#######
def main(*args):
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('seedURL' , help='a weblink for the crawler to start at',type = str)
    parser.add_argument('PageLimit', help='number of webpages to be crawled',type=int)
    parser.add_argument('directory', help = 'a subdirectory to store the html files', type = str)
    parser.add_argument('algorithm', help = 'algorithm that is used when crawling websites, bfs or dfs', type = str)
    args = parser.parse_args()
    print(final(args.seedURL, args.PageLimit,args.directory, args.algorithm))
if __name__ == '__main__':
    main(*sys.argv)
