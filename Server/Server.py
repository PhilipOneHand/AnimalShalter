#########################################################################
# Writers: Nicole Gurevich, Philip Shpigel
# Description: Animal shelter server section for our final project
# Date: 15.06.2023
#########################################################################

from flask import Flask ,render_template, request, url_for, redirect
import mysql.connector
import time
import os
app = Flask(__name__,template_folder="../templates")


# db = mysql.connector.connect(
#     # host="localhost",       # MySQL host (container name or IP address)
#     # port=3307,              # MySQL port in my local pc
#     # user="root",            # MySQL username
#     # password="pass1234",    # MySQL password
#     # database="Animal_Shelter"   # MySQL database name
#     host=os.environ.get("MYSQL_HOST"),
#     port=os.environ.get("MYSQL_PORT"),
#     user=os.environ.get("MYSQL_USER"),
#     password=os.environ.get("MYSQL_PASSWORD"),
#     database=os.environ.get("MYSQL_DATABASE")
# )
max_retries = 10
retry_delay = 5

# Retry connecting to the database
for retry in range(max_retries):
    try:
        # Attempt to connect to the MySQL container
        db = mysql.connector.connect(
            host="db",
            port=3306,
            user="root",
            password="pass1234",
            database="Animal_Shelter"
        )

        # Connection successful, break out of the retry loop
        break
    except mysql.connector.Error as err:
        print(f"Failed to connect to the database (retry {retry + 1}/{max_retries}): {err}")
        # Wait for some time before retrying
        time.sleep(retry_delay)
else:
    # All retries failed, handle the error appropriately
    print("Could not establish a connection to the database.")
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

@app.route("/edit_cat/<int:cat_id>", methods=['GET', 'POST'])
def edit_cat(cat_id):
    if request.method == 'POST':
        # Retrieve the updated cat information from the form
        breed = request.form['breed']
        color = request.form['color']
        age = request.form['age']
        vaccinated = request.form['vaccinated']
        castrated = request.form['castrated']

        # Create a cursor object from the database connection
        cursor = db.cursor()

        # Update the cat record in the database
        cursor.execute("UPDATE Cats SET breed=%s, color=%s, age=%s, vaccinated=%s, castrated=%s WHERE id=%s",
                       (breed, color, age, vaccinated, castrated, cat_id))
        db.commit()

        # Retrieve the updated cat record from the database
        cursor.execute("SELECT * FROM Cats WHERE id=%s", (cat_id,))
        cat = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Render the template for cat list with the updated cat data
        return render_template("Cats_list.html", data=[cat])

    else:
        # Create a cursor object from the database connection
        cursor = db.cursor()

        # Retrieve the cat record from the database based on the cat_id
        cursor.execute("SELECT * FROM Cats WHERE id=%s", (cat_id,))
        cat = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Render the template for cat editing
        return render_template("editCat.html", cat=cat)



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

@app.route("/edit_dog/<int:dog_id>", methods=['GET', 'POST'])
def edit_dog(dog_id):
    if request.method == 'POST':
        # Retrieve the updated dog information from the form
        breed = request.form['breed']
        color = request.form['color']
        age = request.form['age']
        vaccinated = request.form['vaccinated']
        castrated = request.form['castrated']

        # Create a cursor object from the database connection
        cursor = db.cursor()

        # Update the dog record in the database
        cursor.execute("UPDATE Dogs SET breed=%s, color=%s, age=%s, vaccinated=%s, castrated=%s WHERE id=%s",
                       (breed, color, age, vaccinated, castrated, dog_id))
        db.commit()

        # Retrieve the updated dog record from the database
        cursor.execute("SELECT * FROM Dogs WHERE id=%s", (dog_id,))
        dog = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Render the template for dog list with the updated dog data
        return render_template("Dogs_list.html", data=[dog])

    else:
        # Create a cursor object from the database connection
        cursor = db.cursor()

        # Retrieve the dog record from the database based on the dog_id
        cursor.execute("SELECT * FROM Dogs WHERE id=%s", (dog_id,))
        dog = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Render the template for dog editing
        return render_template("editDog.html", dog=dog)

######################### Other Section###########################################
@app.route("/delete_other/<int:other_id>", methods=["POST"])
def delete_other(other_id):
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to delete the other record
    cursor.execute("DELETE FROM Other WHERE id=%s", (other_id,))
    db.commit()

    # Close the cursor
    cursor.close()

    # Redirect back to the showother page
    return redirect(url_for('showother'))


@app.route("/Show_Other_list", methods=['GET','POST'])
def showother():
    # Connect to the database
    cursor = db.cursor()

    if request.method == 'POST':
        if 'other_id' in request.form:
            # Get the other ID entered in the form
            other_id = request.form['other_id']

            # Execute the SQL query to retrieve dog by ID
            cursor.execute("SELECT * FROM Other WHERE id=%s", (other_id,))
            data = cursor.fetchall()

        elif 'animal' in request.form:
            # Get the animal entered in the form
            animal = request.form['animal']

            # Execute the SQL query to retrieve other by animal
            cursor.execute("SELECT * FROM Dogs WHERE breed LIKE %s", ('%' + animal + '%',))
            data = cursor.fetchall()


    else:
        # Execute the SQL query to retrieve all other
        cursor.execute("SELECT * FROM Other")
        data = cursor.fetchall()

    # Close the database connection
    cursor.close()

    # Render the template with the other data
    return render_template("Other_list.html", data=data)

@app.route("/add_other", methods=["GET", "POST"])
def add_other():
    # Connect to the database
    cursor = db.cursor()

    if request.method == "POST":
        animal = request.form["animal"]
        age = request.form["age"]
        vaccinated = request.form["vaccinated"]


        # Insert the cat into the Dogs table
        insert_query = "INSERT INTO Other ( animal, age, vaccinate) VALUES ( %s, %s, %s, %s)"
        cursor.execute(insert_query, ( animal, age, vaccinated))
        db.commit()

        # Redirect to the Dogs list page
        return redirect(url_for("showother"))

    return render_template("add_other.html")

@app.route("/edit_other/<int:other_id>", methods=['GET', 'POST'])
def edit_other(other_id):
    if request.method == 'POST':
        # Retrieve the updated dog information from the form
        animal = request.form["animal"]
        age = request.form["age"]
        vaccinated = request.form["vaccinated"]

        # Create a cursor object from the database connection
        cursor = db.cursor()

        # Update the dog record in the database
        cursor.execute("UPDATE Other SET animal=%s,age=%s, vaccinated=%s WHERE id=%s",
                       (animal, age, vaccinated, other_id))
        db.commit()

        # Retrieve the updated other record from the database
        cursor.execute("SELECT * FROM Other WHERE id=%s", (other_id,))
        other = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Render the template for other list with the updated other data
        return render_template("Other_list.html", data=[other])

    else:
        # Create a cursor object from the database connection
        cursor = db.cursor()

        # Retrieve the other record from the database based on the dog_id
        cursor.execute("SELECT * FROM Other WHERE id=%s", (other_id,))
        other = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Render the template for dog editing
        return render_template("editOther.html", other=other)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


