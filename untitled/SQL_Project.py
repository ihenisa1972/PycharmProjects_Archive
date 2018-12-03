import sqlite3


# create a database
# add a table with a few columns.  One should be quantity
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("Create Table pizza2(topping_1 TEXT, topping_2 TEXT, quantity INT)")
    # add a row to the table
    c.execute("INSERT INTO pizza VALUES('pepperoni', 'mushrooms', 5)")
