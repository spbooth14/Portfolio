#I211 Homework 6
#Skyler Payne Boooth
#Spbooth
#Group 54

import xml.etree.ElementTree as ET
import time
#Part 1

#Algorithm for Part 1:
        
    #Goal:  Write a function called display_book that prints the title, author, and price of the book with a certain id (passed as a parameter). 
    #Starting point: I210, Python Book, Computer with Python Installed, Library XML File

    #parse the xml
    #iterate over each book
    #check if the book id is the same as the user stated
    #if so: print the title, author, and price of the book
    #if none are found, retrun "none found"

def display_book(bookid):
    root = ET.parse("library.xml")
    books = root.iter("book")
    for book in books:
        if book.attrib["id"] == bookid:
            print("Title:", book.find("title").text)
            print("Author:", book.find("author").text)
            print("Price:", book.find("price").text)
            print()
            return True
    return "None Found"
#Part 2

#Algorithm for Part 2:
        
    #Goal: Display the title, author, and price of each Computer book released in December
    #Starting point: I210, Python Book, Computer with Python Installed, Library XML File

    #create a list to keep track of the books that are found
    #parse the xml
    #iterate over each book
    #change the books publish date to a date type using strptime
    #pick out what month it was published
    #check if the genre and release month are equal to what the user gave
    #if so: add the book id to the book list
    #print out all the books that are in the book list using display book

def findGenre(genre, releaseMonthNumber):
    bookList = []
    root = ET.parse("library.xml")
    books = root.iter("book")
    for book in books:
        bookReleaseDate = date = time.strptime(book.find("publish_date").text, "%Y-%m-%d")
        monthReleaseDate = time.strftime("%m", bookReleaseDate)
        if book.find("genre").text == genre.title() and int(monthReleaseDate) == int(releaseMonthNumber):
            bookID = book.attrib['id']
            bookList.append(bookID)
    month = time.strptime(str(releaseMonthNumber), "%m")
    print("The following books are catagorized under the", genre, "genre and were released in the month of", time.strftime("%B", month) + ":")
    print()
    for bookID in bookList:
        display_book(bookID)


#Part 3

#Algorithm for Part 3:
        
    #Goal: Print the unique genres in the file.
    #Starting point: I210, Python Book, Computer with Python Installed, Library XML File

    #create a list to keep track of the book genres
    #parse the xml
    #iterate over each book and add its genre to the genre list
    #print all the unique genres

def findUniqueGenres(xmlFile):
    genreList = []
    root = ET.parse(xmlFile)
    books = root.iter("book")
    genreList = [book.find("genre").text for book in books]
    print("The unique genres in the", xmlFile, "file are:")
    print()
    for genre in set(genreList):
        print(genre)

#TEST CODE
display_book("bk102")            
findGenre("Computer", 12)
findUniqueGenres("library.xml")
