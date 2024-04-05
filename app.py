from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect



import base
import cryptage



app = Flask(__name__)

db = base.connecter()


@app.route('/')
def connection():
    return render_template('signin.html')




@app.route('/Sign', methods = ['POST'])
def Sign():
     if request.method == "POST":
        username = request.form['name']
        password = request.form['password']
        cur = db.cursor()
        cur.execute("INSERT INTO connection (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return redirect(url_for('Index'))
     
     
@app.route('/Index')
def Index():
        cur = db.cursor()
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()        
        cur.close()
        return render_template('index.html', students=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        id = request.form['id']
        id_crypted = cryptage.rsa(id,3457,17)           
        
        name = request.form['name']
        email = request.form['email']
        date = request.form['date_birth']
        
         
        cur = db.cursor()
        cur.execute("INSERT INTO students (id, name, email, datebirth) VALUES (%s, %s, %s, %s)", (id_crypted,name, email, date))
        db.commit()
        return redirect(url_for('Index'))
    

@app.route('/delete/<string:id_data>/', methods = ['GET'])
def delete(id_data):
    cur = db.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    db.commit()
    return redirect(url_for('Index'))


@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        date = request.form['date_birth']
        cur = db.cursor()
        cur.execute("""
        UPDATE students SET name=%s, email=%s, datebirth=%s
        WHERE id=%s
        """, (name, email, date, id_data))
        return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)
