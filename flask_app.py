from flask import Flask, jsonify
import xlrd
#import datetime """Libreria para tomar fecha (manera de imprimir date(year,month,day)) """
#import time """ Libreria para tomar el tiempo  """
import mymodule

app = Flask(__name__ 
book = xlrd.open_workbook('/home/Andres18/mysite/Tienda1.xls')

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/excel/columna1')
def columna():
    return 'columna 1 data'

@app.route('/modulo')
def modulo():
    return (mymodule.saludo())

"""Moudulos de tarea sobre la aplicacion de una API-XLS"""

"""Funcion para contal el numero de paginas que hay """
@app.route('/totalhojas')
def sheets_num():
    return jsonify({"Numero de páginas": mymodule.total_hoja()})

"""Funcion para las columnas y filas"""
@app.route('/totalcolumnas/<int:sheet>')
def columns_numer(sheet):
   return jsonify({"Índice de hoja": sheet, "Numero de columnas": mymodule.total_columnas(sheet)})

@app.route('/totalfilas/<int:sheet>')
def rows_numer(sheet):
    return jsonify({"Índice de hoja": sheet, "Numero de filas": mymodule.total_filas(sheet)})

"""Funcion que regresa el contendio de una celda en una hoja especifica """
@app.route('/excel/columna/<int:col_num>/<int:hoja_num>')
def columna_hoja(col_num, hoja_num):
    sheet = book.sheet_by_index(hoja_num)
    data = []
    for row_idx in range(sheet.nrows):
        cell_value = sheet.cell_value(row_idx, col_num)
        data.append(cell_value)
    return jsonify(data)

"""Funcion que revisa la cabecera de la columna "para validar el nombre de la columna" """
@app.route('/excel/validar_columna/<int:hoja_num>/<int:col_num>/<string:column_name>')
def validar_columna(hoja_num, col_num, column_name):
    if mymodule.is_valid_column_name(hoja_num, col_num, column_name):
        message = f"La columna {column_name} es válida."
    else:
        message = f"La columna {column_name} no es válida."
    return jsonify({"mensaje": message})

"""Funcion que regresa el contenido de N columnas en la hoja X, dame_columnas([2,4,5],hoja2)"""
@app.route('/excel/columnas')
def get_columns():
    columnas = [2, 4, 5] # Índices de las columnas a obtener
    hoja = 'hoja2' # Nombre de la hoja a obtener
    data = mymodule.dame_columnas(columnas, hoja)
    return jsonify(data)

"""Funcion que regresa toda la hoja en una matriz"""
@app.route('/excel/hoja/<int:hoja_num>')
def hoja(hoja_num):
    sheet = book.sheet_by_index(hoja_num)
    data = []
    for row_idx in range(sheet.nrows):
        row_data = []
        for col_idx in range(sheet.ncols):
            cell_value = sheet.cell_value(row_idx, col_idx)
            row_data.append(cell_value)
        data.append(row_data)
    return jsonify(data)
""""""

if __name__== '__main__':
    print("Main saludo")
    app.run(host="0.0.0.0")