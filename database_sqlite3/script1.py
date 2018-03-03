import psycopg2


def create_table():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='trqmhd' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE if not exists store(item text, quantity integer, price real)")
    connection.commit()
    connection.close()

#create_table()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='trqmhd' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("insert into store values (%s,%s,%s)",(item, quantity, price))
    connection.commit()
    connection.close()

#insert("Book",11, 34.5)


def delete(item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='trqmhd' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("delete from store where item=%s" ,(item,))
    connection.commit()
    connection.close()


#delete("Books")

def update(quantity,price,item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='trqmhd' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("update store set quantity=%s, price=%s where item=%s",(quantity,price,item))
    connection.commit()
    connection.close()

update(23,345.5,"Snacks")


def views():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='trqmhd' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("select * from store")
    rows= cursor.fetchall()
    connection.close()
    return rows

print (views())
