#! /usr/bin/env python

import cgi

#Skyler Booth
#Spbooth
#Lab Practical 3
#Group 54

print('Content-type: text/html\n')

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Alphabet Practice</title></head>
    <body>
        <img src="{image}.jpg">
	<h2>{correctMessage}</h2>
	<form method="post" action="Spbooth_LP3.cgi">
            <p>The letter:
            <select name="letter">
                <option>a</option>
                <option>b</option>
                <option>c</option>
                <option>d</option>
                <option>e</option>
                <option>f</option>
                <option>g</option>
                <option>h</option>
                <option>i</option>
                <option>j</option>
                <option>k</option>
                <option>l</option>
                <option>m</option>
                <option>n</option>
                <option>o</option>
                <option>p</option>
                <option>q</option>
                <option>r</option>
                <option>s</option>
                <option>t</option>
                <option>u</option>
                <option>v</option>
                <option>w</option>
                <option>x</option>
                <option>y</option>
                <option>z</option>
            </select>
            </p>
            <p>Is for: <input type="text" name="guess"></p>
        <button type="submit">Submit</button>
</form> 

	
    </body>
</html>"""

form = cgi.FieldStorage()
letter = form.getfirst('letter', "a")
image = letter
guess = form.getfirst("guess", "ACKBAR")
letterDict = {
"a":"ACKBAR",
"b":"BOSSK",
"c":"CHEWIE AND C-3PO",
"d":"DASH RENDAR",
"e":"EWOKS",
"f":"FETT",
"g":"GREEDO",
"h":"HAN SOLO",
"i":"IG-88",
"j":"JABBA",
"k":"KYLE KATARN",
"l":"LUKE AND LEIA",
"m":"MARA JADE",
"n":"NIEN NUNB",
"o":"OBI-WAN",
"p":"PALPATINE",
"q":"QUINLAN VOS",
"r":"R2-D2",
"s":"STORM TROOPERS",
"t":"THRAWN",
"u":"ULIC QEL-DROMA",
"v":"VADER",
"w":"WEDGE",
"x":"XIZOR",
"y":"YODA",
"z":"ZUCKUSS"}

correctAnswer = letterDict.get(letter)

if guess.upper() == correctAnswer:
    print(html.format(image = image, correctMessage = "That's correct!"))
else:
    print(html.format(image = image,  correctMessage = "Sorry, the correct response was " + letterDict.get(letter).title()))
