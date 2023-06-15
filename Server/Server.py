#########################################################################
# Writers: Nicole Gurevich, Philip Shpigel
# Description: Animal shelter server section for our final project
# Date: 15.06.2023
#########################################################################

from flask import Flask ,render_template, request, url_for, redirect
import mysql.connector
app = Flask(__name__,template_folder="../templates")


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

################ Cats Section ##############################

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

        elif 'cat_color' in request.form:
            # Get the cat breed entered in the form
            cat_color = request.form['cat_color']

            # Execute the SQL query to retrieve cat by breed
            cursor.execute("SELECT * FROM Cats WHERE color LIKE %s", ('%' + cat_color + '%',))
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

################ Dogs Section ###############################

@app.route("/delete_dog/<int:dog_id>", methods=["POST"])
def delete_dog(dog_id):
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to delete the dog record
    cursor.execute("DELETE FROM Dogs WHERE id=%s", (dog_id,))
    db.commit()

    # Close the cursor
    cursor.close()

    # Redirect back to the showdogs page
    return redirect(url_for('showdogs'))


@app.route("/Show_Dogs_list", methods=['GET','POST'])
def showdogs():
    # Connect to the database
    cursor = db.cursor()

    if request.method == 'POST':
        if 'dog_id' in request.form:
            # Get the dog ID entered in the form
            dog_id = request.form['dog_id']

            # Execute the SQL query to retrieve dog by ID
            cursor.execute("SELECT * FROM Dogs WHERE id=%s", (dog_id,))
            data = cursor.fetchall()

        elif 'dog_breed' in request.form:
            # Get the dog breed entered in the form
            dog_breed = request.form['dog_breed']

            # Execute the SQL query to retrieve dog by breed
            cursor.execute("SELECT * FROM Dogs WHERE breed LIKE %s", ('%' + dog_breed + '%',))
            data = cursor.fetchall()

        elif 'dog_color' in request.form:
            # Get the dog breed entered in the form
            dog_color = request.form['dog_color']

            # Execute the SQL query to retrieve dog by breed
            cursor.execute("SELECT * FROM Dogs WHERE color LIKE %s", ('%' + dog_color + '%',))
            data = cursor.fetchall()

    else:
        # Execute the SQL query to retrieve all cats
        cursor.execute("SELECT * FROM Dogs")
        data = cursor.fetchall()

    # Close the database connection
    cursor.close()

    # Render the template with the dog data
    return render_template("Dogs_list.html", data=data)

@app.route("/add_dog", methods=["GET", "POST"])
def add_dog():
    # Connect to the database
    cursor = db.cursor()

    if request.method == "POST":
        breed = request.form["breed"]
        color = request.form["color"]
        age = request.form["age"]
        vaccinated = request.form["vaccinated"]
        castrated = request.form["castrated"]

        # Insert the cat into the Dogs table
        insert_query = "INSERT INTO Dogs (breed, color, age, vaccinated, castrated) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (breed, color, age, vaccinated, castrated))
        db.commit()

        # Redirect to the Dogs list page
        return redirect(url_for("showdogs"))

    return render_template("add_dog.html")


if __name__ == "__main__":
    app.run(debug=True)


