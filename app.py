# import the nessecary pieces from Flask
from flask import Flask,render_template,request,redirect, url_for, flash,jsonify, send_file
from flask_mysqldb import MySQL
import mcpras
import time, sys
from openpyxl import Workbook
import exxcel
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

                @app.route('/historicos')
                def Historicos():
                        return render_template('hist.html')
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
                                volt = float(vol)
                                R2 = 360*((volt/1.25)-1)
                                n = 256*(R2-3200-75)/10000
                                n = round(n)
                                n = int(n)
                                mcpras.set_value(n)
                                cur = mysql.connection.cursor()
                                cur.execute('INSERT INTO parametros (id, voltaje, corriente) VALUES (%s, %s, %s)', (0,vol,5))
                                mysql.connection.commit()
                                flash('Voltaje Ajustado')
                                return redirect(url_for('Index'))
                @app.route('/histor', methods = ['POST'])
                def Histor():
                        if request.method == 'POST':
                                inicio = request.form['inicio']
                                fin = request.form['final']
                                exxcel.main() 
                                print(inicio)
                                print(fin)
                                flash('Descargado')
                                time.sleep(1)
                                return send_file('datainfo.xlsx', attachment_filename='datainfo.xlsx')

                if __name__ == '__main__':
                        app.run(host ='0.0.0.0', port = self.port, debug = True)
                

p = server(3000)
p.myfunc()

