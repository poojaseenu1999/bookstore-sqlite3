import sqlite3

def create_table():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(id,title,author,year,isbn):
        conn=sqlite3.connect("book.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES(?,?,?,?,?)",(id,title,author,year,isbn))
        conn.commit()
        conn.close()

insert("5",'baby hoana','ammu',2020,1999)

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows



def delete(id):
        conn=sqlite3.connect("book.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()



def update(title,id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=? WHERE id=?",(title,id))
    conn.commit()
    conn.close()

update('hoana the super girl',5)
delete(0)

print(view())
