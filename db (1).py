import sqlite3

conn = sqlite3.connect('spring.db')
cur = conn.cursor()
#create table
cur.execute("CREATE TABLE reg (name text,age integer,email text,mob integer,per integer,uname text primary key,pswd text)")
#INSERTION
#conn.commit()
#cur.execute("CREATE TABLE dest (name text,age integer,email text,mob integer,per integer,uname text,pswd text)")
#cur.execute("CREATE TABLE cities(id integer primary key, city text)")
#cur.execute("INSERT INTO cities VALUES(6,'Spiti')")
#cur.execute("CREATE TABLE details(uname text, date text)")
cur.execute("SELECT*FROM reg")


print(cur.fetchall())


conn.commit()
conn.close()