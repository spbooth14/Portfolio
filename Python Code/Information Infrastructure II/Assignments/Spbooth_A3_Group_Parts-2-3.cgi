#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, random, cgi

def addEntry(cursor, name, line1, line2, City, state, zipc):
        try:
                SQL = "INSERT INTO Addresses(Name, Address1, Address2, City, State, Zip) VALUES('{}', '{}', '{}', '{}',  '{}', '{}');".format(name, line1, line2, City, state, zipc)
                cursor.execute(SQL)
                db_con.commit()
        except Exception as e:		#Here we handle the error
                print('<p>Something went wrong with the SQL!</p>')
                print(SQL, "Error:", e)
                raise IOError
        else:
                pass
        
string = "i211f16_spbooth" 		#change username to yours!!!
password = "my+sql=i211f16_spbooth" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage() #sets up the form
aname = form.getfirst('name', '')
aline1 = form.getfirst('address1', '')
aline2 = form.getfirst('address2', '')
astate = form.getfirst('state', '')
acity = form.getfirst('city', '')
azip = form.getfirst('zip', '')
html = """<html>
<head><title>Group Homework 3</title></head><body>
{content}</body></html>"""


form = """<form action="Spbooth_A3_Group_Parts-2-3.cgi" method="post">
<h1>Enter a new address</h1> <br /> 
<p>
Name: <input type="text" name="name" maxlength=100 size=50 required><br /><br />
Address Line 1: <input type="text" name="address1" maxlength=100 size=50 required><br /><br />
Address Line 2: <input type="text" name="address2" maxlength=100 size=50><br /><br />
City: <input type="text" name="city" maxlength=100 size=50 required><br /><br />
State (2 Letter Code): <input type="text" name="state" maxlength=2 size=5 required><br /><br />
ZIP: <input type="text" name="zip" maxlength=5 size=10 required><br /><br />
</p>
<br /><input type="submit" value="Submit Address" />
</form>"""

if not aname:
        print(html.format(content = form))
else:
        try:
                addEntry(cursor, aname, aline1, aline2, acity, astate, azip)
        except:
                pass
        else:
                htmladd = """<p>Entry added!</p>"""
                print(html.format(content = htmladd))

