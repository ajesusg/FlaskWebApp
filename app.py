# import the nessecary pieces from Flask
from flask import Flask,render_template,request,redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
import mcpras
class server:
        def __init__(self, port):
                self.port = port
                
        def myfunc(self):
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

                @app.route('/datab', methods = ['POST'])
                def datab():
                        cur = mysql.connection.cursor()
                        cur.execute('SELECT voltaje, corriente FROM parametros ORDER BY id DESC LIMIT 1')
                        data = cur.fetchall()
                        for row in data:
                                vol = row[0]
                                co = row[1]
                                
                        cur.close()
                        return jsonify(str(vol)+":"+str(co))


                @app.route('/setvoltage', methods = ['POST'])
                def SetVoltage():
                        if request.method == 'POST':
                                vol = request.form['voltaje']
                                volt = int(vol)
                                mcpras.set_value(volt)
                                cur = mysql.connection.cursor()
                                cur.execute('INSERT INTO parametros (id, voltaje, corriente) VALUES (%s, %s, %s)', (0,vol,5))
                                mysql.connection.commit()
                                flash('Voltaje Ajustado')
                                return redirect(url_for('Index'))

                if __name__ == '__main__':
                        app.run(host ='0.0.0.0', port = self.port, debug = True)
                

p = server(3000)
p.myfunc()

