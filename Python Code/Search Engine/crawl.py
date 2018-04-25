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

def crawler(seedURL, pageLimit, directory, searchAlg): #sets the crawler to take 3 arguments
    if not os.path.exists(directory): #checks if the directory exists, if not it'll make it 
        os.makedirs(directory)
    if int(pageLimit) != pageLimit:
        return "The page limit that was entered wasn't an integer"
    webGraph = {}
    badExtensions = {".a",".asm",".asp",".awk",".bat",".bmp",".btm",".BTM",".c",".class",".cmd",".CPP",".csv", ".css",".cur",".cxx",".CXX",".db",".def",".DES",".dlg",".dll",".don",".dpc",".dpj",".dtd",".dump",".dxp",".eng",".exe",".flt",".fmt",".font",".fp",".ft",".gif",".h",".H",".hdb",".hdl",".hid",".hpp",".hrc",".HRC",".hxx",".Hxx",".HXX",".ico",".idl",".IDL",".ih",".ilb",".inc",".inf",".ini",".inl",".ins",".java",".jar",".jnl",".jpg",".js",".jsp",".kdelnk",".l",".lgt",".lib",".lin",".ll",".LN3",".lng",".lnk",".lnx",".LOG",".lst",".lst",".mac",".MacOS",".map",".mk",".MK",".mod",".NT2",".o",".obj",".par",".pfa",".pfb",".pl",".PL",".plc",".pld",".PLD",".plf",".pm",".pmk",".pre",".PRJ",".prt",".PS",".ptr",".r",".rc",".rdb",".res",".s",".S",".sbl",".scp",".scr",".sda",".sdb",".sdc",".sdd",".sdg",".sdm",".sds",".sdv",".sdw",".sdi",".seg",".SEG",".Set",".sgl",".sh",".sid",".smf",".sms",".so",".sob",".soc",".sod",".soe",".sog",".soh",".src",".srs",".SSLeay",".Static",".tab",".TFM",".thm",".tpt",".tsc",".ttf",".TTF",".txt",".TXT",".unx",".UNX",".urd",".url",".VMS",".vor",".W32",".wav",".wmf",".xml",".xpm",".xrb",".y",".yxx",".zip"}
    #sets a list of file extensions to help weed out non-html files
    successfulcrawls = 1 #counts the succesful crwls
    dfsStack = [] #initializes stack and queue
    bfsQueue = [] 
    if searchAlg.upper() == "DFS": #checks if the user entered dfs or bfs
        dfsStack = [seedURL] #sets the stack to the seed url
    elif searchAlg.upper() == "BFS":
        bfsQueue = deque([seedURL]) #sets the queue to the seed url
    else:
        return "Search Algorithm entered is not BFS or DFS"
    visited = [] #creates a list to keep track of visited urls
    index_dat = [] #creates a list for index.dat file
    while successfulcrawls < int(pageLimit) + 1: #creates a loop to continue until the successul crawls = the page limit
        if dfsStack or bfsQueue: #checks if the stack/queue is empty or not
            if searchAlg.upper() == "DFS":
                url = dfsStack.pop() #if its dfs it pops the stack
            elif searchAlg.upper() == "BFS":
                url = bfsQueue.popleft() #if its bfs it pops left
            req = urllib.request.Request(url, data=None, headers={"User-Agent": "IUB-I427-Spbooth"}) #sets the request to include user agent as IUB-I427-spbooth
            if url not in visited: #checks if the url isnt in the visited list
                try: #trys to open the url
                    web_page = urllib.request.urlopen(req)
                except:
                    time.sleep(1) #if it raises an error the crawler waits 1 second until it crawls the next page
                else:
                    headers = web_page.info() #gets the headers of the page
                    if headers['Content-Type'].upper()=="TEXT/HTML; CHARSET=UTF-8" or headers['Content-Type'].lower()=="text/html": #check if the header content type is a html page               
                        paths = url.split(".com") #splits the url on .com
                        robotURL = paths[0]+".com/robots.txt" #makes the robot.txt url
                        rp = urllib.robotparser.RobotFileParser() #opens the robot.txt file and parses it
                        rp.set_url(robotURL) #sets the robot parser to the robot url
                        try:
                            rp.read()#trys to read the robots.txt file
                        except: #will raise an error if the robots.txt file doesnt exist, if it doesnt exist we assume we can crawl
                            webGraph[url] = set()
                            contents = web_page.read().decode(errors="replace") #reads the web page
                            matches = re.findall('(?<=href=").+?(?=")', contents) #finds all of the urls                                
                            web_page.close() #closes the web connectiom
                            for match in matches: #changes all the relative urls to absolute urls
                                if match[0] == "/":
                                    match = url + match[1:]
                            for match in matches: #only adds urls that start with h (http(s)) and only if the basename isnt a file
                                if match[0] == "h":
                                    if os.path.basename(match) not in badExtensions:
                                        webGraph[url].add(match)
                                        if searchAlg.upper() == "DFS": #checks if the user entered dfs or bfs
                                            dfsStack.append(match)
                                        elif searchAlg.upper() == "BFS":
                                            bfsQueue.append(match)
                            localFile = localFile = open(directory +str(successfulcrawls) + ".html", "w", encoding ="utf-8") #opens a local file
                            localFile.write(contents) #writes the contents of the web page to the local file
                            localFile.close() #closes the file
                            index_dat.append((str(successfulcrawls) + ".html", url)) #adds a tuple of filename and the url
                            successfulcrawls += 1 #adds one to the crawl count
                            visited.append(url) #adds the url to the visited list
                            time.sleep(1) #sleeps for one second in order to not place a big load on the network
                        else: 
                            if rp.can_fetch("*", url): #if the robots.txt file exists and we are allowed to crawl, it crawls the exact same way as above
                                webGraph[url] = set()
                                contents = web_page.read().decode(errors="replace")
                                matches = re.findall('(?<=href=").+?(?=")', contents) #finds all of the urls
                                web_page.close()
                                for match in matches:
                                    if match[0] == "/":
                                        match = url + match[1:]
                                for match in matches:
                                    if match[0] == "h":
                                        webGraph[url].add(match)
                                        if searchAlg.upper() == "DFS": #checks if the user entered dfs or bfs
                                            dfsStack.append(match)
                                        elif searchAlg.upper() == "BFS":
                                            bfsQueue.append(match)
                                localFile = localFile = open(directory +str(successfulcrawls) + ".html", "w", encoding ="utf-8")
                                localFile.write(contents)
                                localFile.close()
                                index_dat.append((str(successfulcrawls) + ".html", url))
                                successfulcrawls += 1
                                visited.append(url)
                                time.sleep(1)
        else: #if there are no more urls in the stack it breaks the loop
            break
    indexDat = open(directory + "index.dat", "w") #opens the index.dat file
    for htmlURLTuple in index_dat: #goes through all the tuples
        indexDat.write(htmlURLTuple[0] + "\t" + htmlURLTuple[1] + "\n") #writes the local file name, a tab, and the url
    graphFile = open(directory + "webGraph.dat", "wb") #opens the doc.dat file
    pickle.dump(webGraph, graphFile)#writes the docsDat list into the Docs.dat file
    graphFile.close()
    return "Done"

#MAIN#
##print(crawler("https://en.wikipedia.org/wiki/Main_Page", 20, "pages/", "BFS"))  # <----- #test file

###COMMAND LINE STUFF GOES BELOW#######
def main(*args):
        parser = argparse.ArgumentParser(prog='PROG')
        parser.add_argument('seedURL' , help='a weblink for the crawler to start at',type = str)
        parser.add_argument('PageLimit', help='number of webpages to be crawled',type=int)
        parser.add_argument('directory', help = 'a subdirectory to store the html files', type = str)
        parser.add_argument('algorithm', help = 'algorithm that is used when crawling websites, bfs or dfs', type = str)
        args = parser.parse_args()
        print(crawler(args.seedURL, args.PageLimit, args.directory, args.algorithm))
if __name__ == '__main__':
    main(*sys.argv)
