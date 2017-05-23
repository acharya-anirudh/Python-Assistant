import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";
conn.execute('''CREATE TABLE FRIENDS
       (NAME          TEXT    NOT NULL,
       ADDRESS        CHAR(50),
       MOBILE         NUMERIC);''')

print "Table created successfully";

conn.execute("INSERT INTO FRIENDS (NAME,ADDRESS,MOBILE) \
      VALUES ('lucky', 'India', 9868615665)");
	  
conn.execute("INSERT INTO FRIENDS (NAME,ADDRESS,MOBILE) \
      VALUES ('luckey', 'India', 9868615665)");

conn.execute("INSERT INTO FRIENDS (NAME,ADDRESS,MOBILE) \
      VALUES ('david', 'India', 7678557569 )");
	  
conn.execute("INSERT INTO FRIENDS (NAME, ADDRESS, MOBILE) \
	  VALUES ('teacher', 'India', 9711786002)");
	  
conn.execute("INSERT INTO FRIENDS (NAME, ADDRESS, MOBILE) \
	  VALUES ('teachers', 'India', 9711786002)");

conn.commit()
print "Records created successfully";

#for testing purpose
#x=conn.execute("SELECT mobile FROM FRIENDS WHERE NAME ='David'")
#for i in x:
#	print i[0]
	
conn.close()