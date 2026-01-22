import json
import os

def ingreso_gastos (gasto):
    try:
        gastos_json=[]
        if os.path.exists("gastos.json"):
            with open("gastos.json","r",encoding="utf-8") as document:
                gastos_json=json.load(document)
        gastos_json.append(gasto)
        with open("gastos.json","w",encoding="utf-8") as document:
            json.dump(gastos_json,document,indent=4)
            print("Datos Ingresados exitosamente.")
    except FileNotFoundError:
        print("El archivo no existe.")
    except json.JSONDecodeError:
        print("Ya existe un archivo con ese nombre.")
    except Exception as e:
        print("Ocurrio un error inesperado:, {e}")