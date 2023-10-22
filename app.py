from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)  

@app.route("/")
def index():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$$Carmela0015",
        database="Clarku_Research"
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM research_projects")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
