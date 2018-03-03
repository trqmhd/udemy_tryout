import sqlite3

class Database:
    def __init__(self):
         self.conn= sqlite3.connect("books.db")
         self.cur= self.conn.cursor()
         self.cur.execute("CREATE TABLE IF NOT EXISTS book(id integer primary key, title text, author text, year integer, isbn integer)")
         self.conn.commit()


    def insert(self,title,author,year,isbn):
         self.cur.execute("insert into book values(NULL,?,?,?,?)",(title,author,year,isbn))
         self.conn.commit()
         #conn.close()



    def search(self,title="",author="",year="",isbn=""):
         self.cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
         rows= self.cur.fetchall()
         #conn.close()
         return rows



    def delete(self,id):

         self.cur.execute("delete from book where id=?",(id,))
         self.conn.commit()
         #conn.close()


    def update(self,id,title, author,year,isbn):

         self.cur.execute("update book set title=?, author=?, year=?, isbn=? where id=?",(title, author, year, isbn,id,))
         self.conn.commit()
         #conn.close()


    def view(self):

         self.cur.execute("select * from book")
         rows= self.cur.fetchall()
         #conn.close()
         return rows

    def __del__(self):
        self.conn.close()
#connect()

#insert("database Fundamental","John Cena",2011, 13481014)
#print(search(author="John Carrey"))
#delete(6)
#update(1,"Big Data Analysis","John Smith", 2013, 385294695349)
#print(view())
