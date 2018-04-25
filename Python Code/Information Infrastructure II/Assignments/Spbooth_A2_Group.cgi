#! /usr/bin/env python3
print("content-type: text/html\n")
#I211 Group Homework 2
#Skyler Payne Boooth
#Spbooth
#Group 54
import cgi, urllib.request, re #
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Stock Compare</title>
</head>
<body>
{stuff}
<table border=1>
{tableStuff}
</table>
</body>
</html>"""
form = cgi.FieldStorage() #sets up the form
stocks = form.getfirst('symbols', "GOOG MSFT EBAY AMZN") #gets the stocks
stocks = stocks.strip().upper().split() #splits the stocks into a list and capitalizes all of them
stocksDict = {} #sets an empty dictionary
notFound = False #sets a variable for user error checking
for stock in stocks: #goes through each stock
    try: #trys to open each stocks url
        url = "https://finance.yahoo.com/quote/" + stock + "?p=" +stock
        stockPage = urllib.request.urlopen(url)
    except:
        notFound = True #this catches errors
    else:
        contents = stockPage.read().decode(errors="replace") #reads the stock page
        closing = re.findall('(?<=PREV_CLOSE.1">).+?(?=</td>)', contents) #searches for the openening price
        opening = re.findall('(?<=OPEN.1">).+?(?=</td>)', contents, re.DOTALL) #searches for the closing price
        pe = re.findall('(?<=PE_RATIO.1">).+?(?=</td>)', contents, re.DOTALL) #searches for the PE ration
        if closing and opening and pe: #if all are found it adds them to the stock dictionary
            stocksDict[stock] = [float(opening[0]), float(closing[0]), float(pe[0])]
        else: #this also catches errors
            notFound = True
        stockPage.close() #closes the stock page
if notFound is True: #if the notFound variable is true (which only happens for erros) it prints out to the user that they had an invalid stock name
    print(html.format(stuff = "One of stocks you entered does not exist", tableStuff = " "))
else: #if all are okay
    method = form.getfirst("comp", "opn") #it gets the method
    if method == "opn": #checks if the method is opn
        table ="" #creates a blank table string
        stockList = []  
        for stock in stocks: #goes through each of the stocks and gets the open value and adds the value and the stock name as a tuple to the stock list
            values = stocksDict.get(stock)
            openValue = values[0]
            stockList.append([openValue, stock])
        stockList = sorted(stockList) #sorts the list according to each of the open values
        stockList = stockList[::-1] #reverses it so its in descending order
        for stock in stockList: #adds each of the stock names and values in the table format to the table variable 
            table += "<tr><td>{stockName}</td><td>{value}</td>".format(stockName = stock[1], value = stock[0])
        print(html.format(tableStuff = table, stuff =" ")) #prints out the html page with the valid table using the opening value

    elif method == "close": #works the same was as open but uses the closing value
        table =""
        stockList = []
        for stock in stocks:
            values = stocksDict.get(stock)
            closeValue = values[1]
            stockList.append([closeValue, stock])
        stockList = sorted(stockList)
        stockList = stockList[::-1]
        for stock in stockList:
            table += "<tr><td>{stockName}</td><td>{value}</td>".format(stockName = stock[1], value = stock[0])
        print(html.format(tableStuff = table, stuff =" "))

    elif method == "peRatio": #works the same was as open but uses the pe ratio value
        table =""
        stockList = []
        for stock in stocks:
            values = stocksDict.get(stock)
            peValue = values[2]
            stockList.append([peValue, stock])
        stockList = sorted(stockList)
        stockList = stockList[::-1]
        for stock in stockList:
            table += "<tr><td>{stockName}</td><td>{value}</td>".format(stockName = stock[1], value = stock[0])
        print(html.format(tableStuff = table, stuff =" "))

#sort list and print#
#build in error checker#

