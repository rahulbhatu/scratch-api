from flask import Flask
from flask import request, jsonify, render_template
from flask_mysqldb import MySQL
from db.mysql import fetchone, query_exec, fetchall

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'myuser'
app.config['MYSQL_PASSWORD'] = 'mypass'
app.config['MYSQL_DB'] = 'userdata'


#from mysql connections
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/users', methods=['GET', 'POST'])
def api_all():
    if request.method == 'GET':
        users = fetchall(mysql, "SELECT * FROM userdata.users")
        dict_vars = []
        for i, n in users:
            num = {"id": i, "name": n}
            dict_vars.append(num)
        return jsonify(dict_vars)
    if request.method == 'POST':
        ids = request.json['id']
        name = request.json['name']
        query = "INSERT INTO userdata.users(id, name) VALUES ({0}, '{1}')".format(ids, name)
        print(query)
        new_user = query_exec(mysql, query)
        return jsonify(
                {"Msg": "User Added successfully"}), 200, {'ContentType':'application/json'}

@app.route('/api/v1/users/<userid>', methods=['GET'])
def data(userid):
    assert userid == request.view_args['userid']
    dict_vars_s = []
    query = "SELECT * FROM userdata.users WHERE id = {}".format(userid)
    user = fetchone(mysql, query)
    dict_vars = {
            "id" : user[0],
            "name": user[1]
            }
    return jsonify(dict_vars)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)

