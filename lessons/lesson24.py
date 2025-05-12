#db.browser
import sqlite3
db=sqlite3.connect("data1.db")
cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS jurnal(
tema TEXT,
podtem TEXT,
view TEXT,
avtor TEXT
)
""")
db.commit() 
# cursor.execute("INSERT INTO jurnal VALUES('Instagramm','Insta','10000','Aydos')")
# cursor.execute("INSERT INTO jurnal VALUES('Telegramm','tg','hehehehe','Abbaz')")
cursor.execute("DELETE FROM jurnal WHERE avtor ='Abbaz' ")
# cursor.execute("INSERT INTO jurnal VALUES('Instagrammqwdasd','ahs dhj ','10012300','Aydos')")
# cursor.execute("INSERT INTO jurnal VALUES('Insdsftagramm','Iasf23efnsta','10012312030','Aydds fsdfos')")
db.commit()



db.close()