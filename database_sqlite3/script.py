import sqlite3


def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE if not exixt store(item text, quantity integer, price real)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("insert into store values (?,?,?)", (item, quantity, price))
    connection.commit()
    connection.close()

#insert("Snacks",7, 35.5)


def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("delete from store where item=?",(item,))
    connection.commit()
    connection.close()


#delete("Snacks")

def update(quantity,price,item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("update store set quantity=?, price=? where item=?", (quantity,price,item))
    connection.commit()
    connection.close()

update(23,345.5,"Snacks")


def views():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("select * from store")
    rows= cursor.fetchall()
    connection.close()
    return rows

print (views())
