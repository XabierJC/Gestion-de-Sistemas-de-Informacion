import sqlite3 
from flask import Flask, render_template
import json
from json2html import *
import sys

if len(sys.argv) < 2:
	print("No se ha detectado ningun parametro de entrada")
	db = input("Por favor introduzca el nombre de la base de datos que desea usar (terminado en db) :")
else:
	db = sys.argv[1]

print("Trabajamos con al base {}".format(db))  

app = Flask(__name__)

@app.route("/")
def home():
	return("Xabier Jimenez Cuesta     Practica 3: bases de datos en flask")

@app.route("/tablas/")
def mostrar_tablas():
	conn = sqlite3.connect("ejemplo.db")
	c = conn.cursor()
	ejecutable =  "SELECT name FROM sqlite_master where TYPE='table';"
	c.execute(ejecutable)
	out=c.fetchall()
	jsonfile = json.dumps(out)
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nom_tabla>")
def mostrar_registro(nom_tabla):
	conn = sqlite3.connect("ejemplo.db")
	c = conn.cursor() 
	ejecutable = "SELECT * FROM "+ str(nom_tabla)
	c.execute(ejecutable)
	out=c.fetchall()
	jsonfile = json.dumps(out)
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nom_tabla>/info")
def mostrar_informacion(nom_tabla):
	conn = sqlite3.connect("ejemplo.db")
	c = conn.cursor() 
	ejecutable = "PRAGMA TABLE_INFO({})".format(nom_tabla)
	c.execute(ejecutable)
	out=c.fetchall()
	nom_column = "Los nombres de las columnas son:    "
	for i in range(1,len(out)):
		nom_column = nom_column + out[i][1] + ", " 

	ejecutable = "SELECT * FROM "+ str(nom_tabla)
	c.execute(ejecutable)
	out=c.fetchall()
	num_reg = len(out)

	salida = nom_column + " y el numero de registros es " + str(num_reg)

	jsonfile = json.dumps(salida)
	return json2html.convert(json = jsonfile)

if __name__ == "__main__":
	app.run()
