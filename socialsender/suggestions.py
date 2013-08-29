import cgi, os sys
import sqlite3 as db

conn = db.connect('suggestions.db')
cursor = conn.cursor()
conn.row_factory = db.Row
cursor.execute("select * from suggestions")
rows = cursor.fetchall()

sys.stdout.write("Content-type: text/html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body>")
# will change this so that it represents actual links and checkboxes to select them
for row in rows:
	sys.stdout.write("<p>Article:&nbsp;%<br />" % (row[0]))
	sys.stdout.write("Link:&nbsp;%s<br />" % (row[1]))
	sys.stdout.write("Picture:&nbsp;%s<br />" % (row[2]))
	sys.stdout.write("<p>")
sys.stdout.write("</body></html>")