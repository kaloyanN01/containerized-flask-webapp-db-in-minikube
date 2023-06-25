from flask import Flask, render_template ,request, redirect, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_DB'] = 'votes'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
print(mysql)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/results')
def display_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM animals")
    data = cur.fetchall()
    return render_template('results.html', data=data)

#--------- above works
@app.route("/", methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor() #1
    if request.method == 'POST':
        if request.form.get('action1') == 'dogs':
            cur.execute("UPDATE animals SET dogs = dogs + 1")
            mysql.connection.commit()
        elif  request.form.get('action2') == 'cats':
            cur.execute("UPDATE animals SET cats = cats + 1")
            mysql.connection.commit()
    
    return redirect('/votes')

@app.route("/votes")
def display_percentages():
    cur = mysql.connection.cursor() #1
    # Execute the query
    cur.execute("SELECT dogs, cats, CONCAT(ROUND(dogs / (dogs + cats) * 100, 2), '% vs ', ROUND(cats / (dogs + cats) * 100, 2), '%') AS percentage FROM animals")
    #cur.execute("SELECT dogs, cats, CONCAT(ROUND(dogs / (dogs + cats) * 100), '% vs ', ROUND(cats / (dogs + cats) * 100), '%') AS percentage FROM animals")
    result = cur.fetchone()
    # Format the result as desired
    percentages = f"Dogs {result['percentage']} Cats"
    # Render the template with the percentages
    return render_template("percentages.html", percentages=percentages)

