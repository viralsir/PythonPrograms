'''
   Datastructure - store temp.
   1.File :-
            unorgnised
            organaised
               sequance
               deletion

   Database : store data in tabular
   database : collection of tables
   table : collection of rows and cols

   IBM  sequeal  :- sql
   sql :- command or query

   dbms : database managment system
   oracle,mysql,sqlserver,ms access,db2,----

   Dr. e.f.codd
   12 rules
   rdbms : relational database managment system

'''

# create a table in database

import cx_Oracle
try:                        #username/password@localhost:1521/xe
    con = cx_Oracle.connect('system/1234@localhost:1521/xe')
    print("Connected")
    cursor = con.cursor()
    #cursor.execute("CREATE TABLE hr.student_shubham(username varchar(10),name varchar(30))")
    #cursor.execute("insert into hr.student_shubham  values('viren','virenpatel')")
    #cursor.execute("insert into hr.student_shubham (username) values('vimal')")

    #cursor.execute("update hr.student_shubham set name='vimalshah' where username='vimal'")
    #cursor.execute("delete from hr.student_shubham where username='viren'")

    cursor.execute("Select * from hr.student_shubham")

    for row in cursor:
        for data in row:
            print(data)

    #con.commit()
    #print("Table Created Successfully!")
    print("record is inserted")
    cursor.close()
    con.close()
except Exception as e:
    print("Error: ", str(e))

