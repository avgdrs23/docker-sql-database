#!/usr/local/bin/python3
import mysql.connector
import  flask
 
#app = Flask.flask(__name__)
app = flask.Flask(__name__)

"""
mydb = mysql.connector.connect(user="root", password="secret",database="test", auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Numbers")
for x in mycursor:
  print(x[0])
mydb.close()
"""
@app.route("/")
#@app.route("/home")
def home():
   html='<html><body>'
   mydb = mysql.connector.connect(user="root", password="secret",database="test", auth_plugin='mysql_native_password')
   mycursor = mydb.cursor()
   mycursor.execute("SELECT * FROM Numbers")
   for x in mycursor:
      html = html + f"<br>{x[0]}</br>"
   mydb.close()
   html = html + "</body></html>"
   return html
app.run(port=8080, host="0.0.0.0")

