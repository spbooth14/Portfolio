import sys
import pickle
import argparse

def normalizeGraph(graph):  #This function takes in a graph and deletes nodes that arent referenced as keys (in the search engine application, it takes out any page thats a vaule if it was never crawled
    newGraph = {} #sets a new graph
    keys = list(graph.keys()) #gets the keys of the graph
    for key in graph: #goes through each key
        values = set(graph.get(key)) #gets the values 
        uselessValues = set() #creates a usesless set
        for value in values: #goes through each value and adds a value to usesless if it doesnt appear in the key list
            if value not in keys:
                uselessValues.add(value)
        newGraph[key] = set(values - uselessValues) #uses set subtraction to give the key its new set of values
        ##if len(values) == 0:
            ##values = keys
    return newGraph #returns the new graph

def outlinkGraphToInlinkGraph(graph): #this inverts the link to set of outlinks graph to a link with a set of inlinks
    inLinkGraph = {} #makes the new graph
    for key in graph: #goes through all the keys
        values = graph.get(key) #gets its values
        for value in values: #goes through all the values  
            if value not in inLinkGraph: #checs if the value is in the inlinkGraph or not, if not it sets it as a key with a set value of the key in the original graph, if it is a key it adds the original graph key to the set
                inLinkGraph[value] = {key}
            else:
                inLinkGraph[value].add(key)
    return inLinkGraph #returns the new graph

def numberOfOutlinks(graph): #gets the number of outlinks for each node
    nodeToOutLinks = {} #initalized dict
    for key in graph: #goes through the original graph
        values = graph.get(key) #gets its outlinks
        if len(values) == 0: #if it has none, it sets to 1 (to avoid 0 division)
            nodeToOutLinks[key] = 1
        else: # if not it sets the number of outlinkes to the length of the outlink list
            nodeToOutLinks[key] = len(values)
    return nodeToOutLinks #returns the dictionary

def pageRank(graph, p=.15, epsilon= .000001): #takes in a graph, a p, and a epsilon to calculate each pages rank
    numberOfLoopsToConverge = 0 #counter for visiual of how long it too to converge
    graph = normalizeGraph(graph) #normalizes the graph
    inLinkGraph = outlinkGraphToInlinkGraph(graph) #inverts the graph
    nodeToNumberOfOutLinks = numberOfOutlinks(graph) #gets the number of nodes for each key
    pageRankDict = {} #sets the page rank dict
    keys = set(graph.keys()) #gets the set of keys in the graph
    for node in graph: #goes through each node
        pageRankDict[node] = 1/len(keys) #gives a initial PR to 1/n
    pOverN = p / len(keys) #calculates p/n
    oneMinusp = 1 - p #calculates p - 1
    while True:
        newPageRankDict = {} #sets a new page rank dictionary
        converge = set() #this is the fail safe for when the page rank converges
        for node in pageRankDict: #goes through each node in the page rank dict
            sumOfAdjPageRanks = 0 #sets the sum for the ajacent page rank scores
            nodeValues = inLinkGraph.get(node) #gets all the adjacent nodes
            if nodeValues == None: #if none, it gives a sum of adj page ranks to 0
                sumOfAdjPageRanks += 0
            else: #if it does have incoming nodes
                for link in nodeValues: #it goes through each of those nodes and calculates its page ranks
                    sumOfAdjPageRanks += (pageRankDict.get(link) / nodeToNumberOfOutLinks.get(link)) #each page rank is its rank divide by the number of outlinks
            nodeRank = pOverN + (oneMinusp*sumOfAdjPageRanks) #then the node rank equals p/n + (1-p)(sumOfAdjRanks)
            newPageRankDict[node] = nodeRank #adds the nodes PR to the new page rank dictionary
        for node in pageRankDict: #goes through the nodes inthe old page rank dict
            old = pageRankDict.get(node) #gets the old rank
            new = newPageRankDict.get(node) #gets the new rank
            diff = abs(old - new) #gets the difference
            if diff < epsilon: #checks if that differce is less than epsilon
                pass
            else:
                converge.add("fail") #if not it adds fail to the converge set               
        pageRankDict = newPageRankDict #sets the old PR dictionary to the new one
        numberOfLoopsToConverge += 1 #adds one to the counter
        if len(converge) == 0: #checks the length of the converge set (it'll only be 0 if all the links difference between the old PR and the new PR is less than epsilon
            #print(numberOfLoopsToConverge)
            pageRankFile = open("pageRankDict.dat", "wb") #opens the doc.dat file
            pickle.dump(pageRankDict, pageRankFile)#writes the docsDat list into the Docs.dat file
            pageRankFile.close() #closes the file
            return pageRankDict
    
##graph = {"a" : {"b", "c", "d", "e"}, "b": {"c", "d"}, "c": {"a"}, "d" : {"a", "c"}}
##print(pageRank(graph))

def main(*args):
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('graph' , help='a dictionary based graph that has keys as nodes and values as a set of the nodes it points to')
    args = parser.parse_args()
    print(pageRank(args.graph))
if __name__ == '__main__':
    main(*sys.argv)
