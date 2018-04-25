#! /usr/bin/env python
print("content-type: text/html\n")
#I211 Homework 7
#Skyler Payne Boooth
#Spbooth
#Group 54
import cgi
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
<body>
<h1>Robot Delivery System Confirmation</h1>
<p>You have selected to have a {message}. </p>
<p>Your total delivery fee comes to: ${cost} </p>
</body>
</html>"""
form = cgi.FieldStorage() #sets up the form
delivPackage = form.getfirst('delivery', 'Hippo') #gets the name of the package with a default to hippo
delivMethod = form.getfirst('delivery_method', 'Flying Drone') #gets the method of the delivery with a default to flying drone
addons1 = form.getvalue('addons1') #gets the value of add on 1 
addons2 = form.getvalue('addons2') #gets the value of add on 2 
addons3 = form.getvalue('addons3') #gets the value of add on 3

deliveryMethodPriceDict = {"Flying Drone" :10, "Self Driving Car" : 20, "Giant Robot": 1000} #sets a price dctionary
addonsPriceDict = {"with Express Delivery" : 30, "Mostly Not Broken": 20, "with a Smile" : 1}
total = deliveryMethodPriceDict.get(delivMethod) #starts the total as the amount for the delivery method selected
addons = [] #gets the add on list
if addons1: #checks if add on is empty or no
    addons.append(addons1) #if not its added to the list and the price is added to the total
    total += addonsPriceDict.get(addons1)
if addons2: #checks if add on is empty or no
    addons.append(addons2)#if not its added to the list and the price is added to the total
    total += addonsPriceDict.get(addons2)
if addons3: #checks if add on is empty or no
    addons.append(addons3)#if not its added to the list and the price is added to the total
    total += addonsPriceDict.get(addons3)

if len(addons) == 0: #This section just gets the number of add ons so it can correctly format the message
    message = delivPackage + " delivered by a " + delivMethod
elif len(addons) == 1:
    message = delivPackage + " delivered by a " + delivMethod + ", " + addons[0]
elif len(addons) == 2:
    message = delivPackage+ " delivered by a " + delivMethod + ", " + addons[0] + " and " + addons[1]
elif len(addons) == 3:
    message = delivPackage+ " delivered by a " + delivMethod + ", " + addons[0]+ ", " + addons[1]+ ", " + "and " + addons[2]

print(html.format(message = message, cost = total)) #adds the message and the total to the output html and then prints it


