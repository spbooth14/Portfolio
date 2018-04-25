#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211f16_spbooth" 		#change username to yours!!!
password = "my+sql=i211f16_spbooth" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
##form = cgi.FieldStorage() #sets up the form
##robot1 = form.getfirst('robot1', '')
##robot2 = form.getfirst('robot2', '')
html = """<html>
<head><title>Item Shop!</title></head><body>
        {content}</body></html>"""

try:				#Always surround .execute with a try!
    SQL = """select Item, Cost from ShopItems;"""
    cursor.execute(SQL)
    db_con.commit()
    results = cursor.fetchall()
except Exception as e:		#Here we handle the error
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "Error:", e)
else:				#This runs if there was no error
    itemList = ""
    for row in results:
        tableRow = "<tr><td  align='center'>" + row[0] + "</td><td  align='center'>" + str(row[1]) + "</td><td  align='center'><input type='radio' name='choice' value=" + row[0] + "></tr>"
        itemList += tableRow
    form = """<H1><h1>Welcome to the Item Shop</h1>
	    <p>Please select your purchase.</p>
	    <form action='RegisterSale.cgi' method='Post'>
            <table border='1' width='60%'>
            <tr><th>Item</th><th>Cost</th><th>Selection</th></tr>
            {itemTable}
            </table>
	    <p>How many would you like to buy? <input type="text" name="quantity" Required></p>
	    <p><button type="submit">Buy</button></p>
            </form>"""
    form = form.format(itemTable = itemList)
    print(html.format(content = form))
