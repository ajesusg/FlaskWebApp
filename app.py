# import the nessecary pieces from Flask
from flask import Flask,render_template,request,redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'datos2019'
app.config['MYSQL_PASSWORD'] = '123452019'
app.config['MYSQL_DB'] = 'panelpf'
mysql = MySQL(app)

#settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT voltaje, corriente FROM parametros ORDER BY id DESC LIMIT 1')
    data = cur.fetchall()
    return render_template('index.html', parametro = data)

@app.route('/setvoltage', methods = ['POST'])
def SetVoltage():
    if request.method == 'POST':
        vol = request.form['voltaje']
        print(vol)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO parametros (id, voltaje, corriente) VALUES (%s, %s, %s)', (0,vol,5))
        mysql.connection.commit()
        flash('Voltaje Ajustado')
        return redirect(url_for('Index'))
@app.route('/operation')
def Operation():
    return render_template('operation.html')
#When run from command line, start the server
if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = True)
