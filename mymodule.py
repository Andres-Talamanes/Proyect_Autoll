import xlrd
book = xlrd.open_workbook('/home/Andres18/mysite/Tienda1.xls')

def saludo():
    return("Hola te saludo")

def total_hoja():
    sheets = book.sheet_names()
    return len(sheets)

def total_columnas(sheet_index):
    sheet = book.sheet_by_index(sheet_index)
    return sheet.ncols

def total_filas(sheet_index):
    sheet = book.sheet_by_index(sheet_index)
    return sheet.nrows