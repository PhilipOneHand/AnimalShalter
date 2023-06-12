from flask import Flask ,render_template, request, url_for, redirect
# from flask_mysqldb import MySQL
import mysql.connector
app = Flask(__name__,template_folder="../templates")
# mysql = MySQL()

db = mysql.connector.connect(
    host="localhost",       # MySQL host (container name or IP address)
    port=3307,              #port
    user="root",            # MySQL username
    password="pass1234",    # MySQL password
    database="Animal_Shelter"   # MySQL database name
)
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Dogs")
    result = cursor.fetchall()
    cursor.close()
    return str(result)

if __name__ == "__main__":
    app.run()


