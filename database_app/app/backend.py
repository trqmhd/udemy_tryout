import sqlite3

def connect():
     conn= sqlite3.connect("books.db")
     cur= conn.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS book(id integer primary key, title text, author text, year integer, isbn integer)")
     conn.commit()
     conn.close()



def insert(title,author,year,isbn):
     conn= sqlite3.connect("books.db")
     cur= conn.cursor()
     cur.execute("insert into book values(NULL,?,?,?,?)",(title,author,year,isbn))
     conn.commit()
     conn.close()



def search(title="",author="",year="",isbn=""):
     conn= sqlite3.connect("books.db")
     cur= conn.cursor()
     cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
     rows= cur.fetchall()
     conn.close()
     return rows



def delete(id):
     conn= sqlite3.connect("books.db")
     cur= conn.cursor()
     cur.execute("delete from book where id=?",(id,))
     conn.commit()
     conn.close()


def update(id,title, author,year,isbn):
     conn= sqlite3.connect("books.db")
     cur= conn.cursor()
     cur.execute("update book set title=?, author=?, year=?, isbn=? where id=?",(title, author, year, isbn,id,))
     conn.commit()
     conn.close()


def view():
     conn= sqlite3.connect("books.db")
     cur= conn.cursor()
     cur.execute("select * from book")
     rows= cur.fetchall()
     conn.close()
     return rows


connect()

#insert("Database Fundamental","John Cena",2011, 13481014)
#print(search(author="John Carrey"))
#delete(6)
#update(1,"Big Data Analysis","John Smith", 2013, 385294695349)
#print(view())
