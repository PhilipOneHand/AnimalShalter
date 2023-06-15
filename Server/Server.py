from flask import Flask ,render_template, request, url_for, redirect
# from flask_mysqldb import MySQL
import mysql.connector
app = Flask(__name__,template_folder="../templates")
# mysql = MySQL()

db = mysql.connector.connect(
    host="localhost",       # MySQL host (container name or IP address)
    port=3307,              # MySQL port in my local pc
    user="root",            # MySQL username
    password="pass1234",    # MySQL password
    database="Animal_Shelter"   # MySQL database name
)
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/delete_cat/<int:cat_id>", methods=["POST"])
def delete_cat(cat_id):
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to delete the cat record
    cursor.execute("DELETE FROM Cats WHERE id=%s", (cat_id,))
    db.commit()

    # Close the cursor
    cursor.close()

    # Redirect back to the showcats page
    return redirect(url_for('showcats'))


@app.route("/Show_Cats_list", methods=['GET','POST'])
def showcats():
    # Connect to the database
    cursor = db.cursor()

    if request.method == 'POST':
        if 'cat_id' in request.form:
            # Get the cat ID entered in the form
            cat_id = request.form['cat_id']

            # Execute the SQL query to retrieve cat by ID
            cursor.execute("SELECT * FROM Cats WHERE id=%s", (cat_id,))
            data = cursor.fetchall()

        elif 'cat_breed' in request.form:
            # Get the cat breed entered in the form
            cat_breed = request.form['cat_breed']

            # Execute the SQL query to retrieve cat by breed
            cursor.execute("SELECT * FROM Cats WHERE breed LIKE %s", ('%' + cat_breed + '%',))
            data = cursor.fetchall()

    else:
        # Execute the SQL query to retrieve all cats
        cursor.execute("SELECT * FROM Cats")
        data = cursor.fetchall()

    # Close the database connection
    cursor.close()

    # Render the template with the cat data
    return render_template("Cats_list.html", data=data)

@app.route("/add_cat", methods=["GET", "POST"])
def add_cat():
    # Connect to the database
    cursor = db.cursor()

    if request.method == "POST":
        breed = request.form["breed"]
        color = request.form["color"]
        age = request.form["age"]
        vaccinated = request.form["vaccinated"]
        castrated = request.form["castrated"]

        # Insert the cat into the Cats table
        insert_query = "INSERT INTO Cats (breed, color, age, vaccinated, castrated) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (breed, color, age, vaccinated, castrated))
        db.commit()

        # Redirect to the Cats list page
        return redirect(url_for("showcats"))

    return render_template("add_cat.html")
if __name__ == "__main__":
    app.run(debug=True)


