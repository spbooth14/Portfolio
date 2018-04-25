#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi

def totalCost(cursor, item, quantity):
    try:				#Always surround .execute with a try!
        SQL = "select Cost from ShopItems WHERE Item = '{}'".format(item)
        cursor.execute(SQL)
        db_con.commit()
        results = cursor.fetchall()
    except Exception as e:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
    else:				#This runs if there was no error
        itemCost = float(results[0][0])
        total = int(quantity) * itemCost
        return total
def updateRecord(cursor, item, quantity):
    try:				#Always surround .execute with a try!
        SQL = "UPDATE ShopItems SET Sold =+ {} WHERE Item = '{}'".format(quantity, item)
        cursor.execute(SQL)
        db_con.commit()
        results = cursor.fetchall()
    except Exception as e:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
    else:
        try:				#Always surround .execute with a try!
            SQL = """select Item, Sold from ShopItems;"""
            cursor.execute(SQL)
            db_con.commit()
            results = cursor.fetchall()
        except Exception as e:		#Here we handle the error
            print('<p>Something went wrong with the SQL!</p>')
            print(SQL, "Error:", e)
        else:				#This runs if there was no error
            itemTable = ""
            for row in results:
                tableRow = "<tr><td  align='center'>" + row[0] + "</td><td  align='center'>" + str(row[1]) + "</td></tr>"
                itemTable += tableRow
            return itemTable



string = "i211f16_spbooth" 		#change username to yours!!!
password = "my+sql=i211f16_spbooth" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage() #sets up the form
item = form.getfirst('choice', 'Key')
quantity = form.getfirst('quantity', '0')
html = """<html>
<head><title>Checkout!</title></head><body>
        {content}</body></html>"""

htmlUpdate = """<h1>Thank you</h1>
        <p>You purchased {quantityOfItem} {itemName} for a total of {totalPrice}.</p>
        <h2>Sales Record</h2>
        <table border='1' width='60%'>
        <tr><th>Item</th><th>Total Sold</th></tr>
        {soldItemTable}
        </table>"""
        
total = totalCost(cursor, item, quantity)
selectTable = updateRecord(cursor, item, quantity)
htmlUpdate = htmlUpdate.format(quantityOfItem= quantity, itemName = item, totalPrice = total, soldItemTable = selectTable)
print(html.format(content = htmlUpdate))

