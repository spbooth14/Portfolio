#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, random, cgi
        
string = "i211f16_spbooth" 		#change username to yours!!!
password = "my+sql=i211f16_spbooth" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage() #sets up the form
student = form.getfirst('student', '')
html = """<html>
<head><title>Group Homework 3</title></head><body>
{content}</body></html>"""

try:				#Always surround .execute with a try!
    SQL = """select Name from Addresses;"""
    cursor.execute(SQL)
    db_con.commit()
    results = cursor.fetchall()
except Exception as e:		#Here we handle the error
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "Error:", e)
else:				#This runs if there was no error
    studentList = ""
    for row in results:
        option = "<option>" + row[0] + "</option>"
        studentList += option
    form = """<H1>Choose a name!</H1><hr />
        <FORM method="post" action="Spbooth_A3_Group_Parts-4-5.cgi">
        <H3>Please select a name:</H3>
        <p> <select name="student">{selectStuff}</student></p>
	</FORM>
	<br />
	<br />
	<input type="submit" value="Submit Name!" />"""
    form = form.format(selectStuff = studentList)
    if not student:
        print(html.format(content = form))
    else:
        htmltable = """<table style="width:100%">
        <tr>
          <th>Name</th>
          <th>Address</th> 
        </tr>
        {tableRows}"""
        try:				#Always surround .execute with a try!
            SQL = "select Name, Address1, Address2, City, State, Zip from Addresses where Name = '{}';".format(student)
            cursor.execute(SQL)
            db_con.commit()
            results = cursor.fetchall()
        except Exception as e:		#Here we handle the error
            print('<p>Something went wrong with the SQL!</p>')
            print(SQL, "Error:", e)
        else:				#This runs if there was no error
            students = ""
            for row in results:
                tableRow = "<tr><td>" + row[0] + "</td><td>" + row[1] + row[2] + row[3] + row[4] + row[5] + "</td></tr>"
                studens += tableRow
            htmladd = htmltable.format(tableRows=students)
            print(html.format(contents = htmladd))
