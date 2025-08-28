from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# Example DB config — update with your actual info
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yassin2011',
    'database': 'therapy'
}


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("base.html")

@app.route("/booking")
def book():
    return render_template("booking.html")

@app.route("/submit", methods=["POST"])
def submit():
    firstname = request.form['f-name']
    lastname = request.form['l-name']
    email = request.form['email']
    password = request.form['pass']  # Matches input name="pass"
    
    conn = None

    try:
        conn = pymysql.connect(**db_config)
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (first_name, last_name, email, pass) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (firstname, lastname, email, password))
            conn.commit()
    except Exception as e:
        print("Add to db error:", e)
    finally:
        if conn:
            conn.close()

    return render_template("base.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
