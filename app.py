from flask import Flask , jsonify
from flask_cors import CORS, cross_origin   
import mysql.connector
app = Flask(__name__)
CORS(app)
@app.route('/')
def fet():
    #conexão com o DB
    con = mysql.connector.connect(host='kaligor.com.br',database='u201025653_graph',user='u201025653_root',password='eV*I6*L9/')
    cursor=con.cursor()
    if con.is_connected():
        cursor.execute("SELECT * FROM portifolio")
        selt=cursor.fetchall()
        return jsonify(selt)



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
    