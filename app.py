from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdfwerqewgfgzvzxc'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createuser', methods=['POST', 'GET'])
def createuser():
    if request.method == 'GET':
        return render_template('createuser.html')
    conn = sqlite3.connect('test.db')
    name = request.form['name']
    email = request.form['email']
    conn.execute("INSERT INTO USERS (EMAIL,NAME) VALUES (?,?)",(email, name));
    conn.commit()
    conn.close()
    return "User Created", 200

@app.route('/getUser/', methods=['GET'])
def getUser():
    requestData = request.args
    id = requestData['id']
    conn = sqlite3.connect('test.db')
    cursor = conn.execute("SELECT * from USERS WHERE ID = ?", id)
    user = {
      'id': "",
      'name': "",
      'email': ""
    }
    for row in cursor:
      user['id'] = row[0]
      user['email'] = row[2]
      user['name'] = row[3]
    conn.close()
    response = jsonify(user)
    
    return response, 200

if __name__ == "__main__":
    app.run(debug=True)