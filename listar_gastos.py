from datetime import datetime #se importan las librerias necesarias
import json
import os
from tabulate import tabulate

def listar ():# Define una función llamada "listar" que permite ver los gastos registrados con distintos filtros.
    while True:# Inicia un bucle infinito para mantener el menú activo hasta que el usuario elija regresar.
        print("=============================================")#Imprime el menú
        print("                Listar Gastos")
        print("=============================================")
        print("Seleccione una opción para filtrar los gastos:")
        print("")
        print("1. Ver todos los gastos")
        print("2. Filtrar por categoría")
        print("3. Filtrar por rango de fechas")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcion=int(input("Seleccione un categoria: "))
        if opcion == 1:
            try:# Intenta ejecutar el siguiente bloque; si hay errores, los atrapa.
                if os.path.exists("gastos.json"):# Verifica si el archivo "gastos.json" existe en la carpeta actual.
                    with open("gastos.json", "r", encoding="utf-8") as archivo:# Abre el archivo en modo lectura con codificación UTF-8.
                        busqueda=json.load(archivo)# Carga el contenido del archivo JSON como una lista de diccionarios.
                    tabulado=tabulate(busqueda, headers="keys", tablefmt="grid")# Convierte la lista en una tabla bonita usando la librería tabulate.
                print(tabulado)# Muestra la tabla formateada en la pantalla.
                input("ENTER PARA CONTINUAR .....")
            except FileNotFoundError:# Si el archivo no se encuentra aunque ya se verificó, por si acaso
                print("archivo no encontrado.")
            except json.JSONDecodeError:# Si el archivo existe pero no tiene un formato JSON válido
                print("Archivo no encontrado.")
            except Exception as e:
                print(f"Ocurrio un error inesperado: {e}")
        elif opcion == 2:
            try:
                if os.path.exists("gastos.json"):# Verifica si el archivo "gastos.json" existe.
                    with open("gastos.json", "r", encoding="utf-8") as archivo:# Abre el archivo en modo lectura.
                        busqueda2=json.load(archivo)  # Carga los datos del archivo como una lista.
                    cat=input("ingrese una categoria de las siguientes Comida, Transporte, Entretenimiento, Otros").strip().title() # Pide al usuario una categoría y la formatea (primera letra mayúscula, sin espacios).
                    total=0                      # Inicializa una variable para acumular el total gastado en esa categoría.
                    for c in busqueda2: # Recorre cada gasto en la lista cargada.
                        if c["categoria"] == cat:  # Si la categoría del gasto coincide con la ingresada ifc["Categoria"]          
                            print(c)# Muestra ese gasto (como diccionario)
                            total+= c["Monto"]# Suma el monto de ese gasto al total.
                print(f"Total gastado en {cat} {total}")# Muestra el total acumulado para esa categoría.
                input("ENTER PARA CONTINUAR .....")
            except FileNotFoundError:
                print("archivo no encontrado")
            except Exception as e:
                print(f"Ocurrio un error inesperado: {e}")
        elif opcion == 3:
            if os.path.exists("gastos.json"):# Verifica si el archivo "gastos.json" existe.
                with open("gastos.json", "r", encoding="utf-8") as archivo:# Abre el archivo en modo lectura.
                    fechas=json.load(archivo)# Carga los datos del archivo como una lista.
            print("ingrese las fechas en formato YYYY-MM-DD")
            inicio=input("Fecha de inicio: ").strip()#se esta capturando la fecha en formato texto
            input("ENTER PARA CONTINUAR .....")
            fin= input("Fecha de fin: ").strip()#se esta capturando la fecha en formato texto
            input("ENTER PARA CONTINUAR .....")
            try:
                formato="%Y-%m-%d"#se declara el formato fecha
                fecha_inicio=datetime.strptime(inicio,formato)# Convierte la cadena de texto "inicio" a un objeto de fecha.
                fecha_fin=datetime.strptime(fin,formato)# Convierte la cadena "fin" a un objeto de fecha.
                total=0 # Inicializa el total gastado en el rango.
                for c in fechas:# Recorre cada gasto en la lista.
                    fech=c["Fecha"]# Obtiene la fecha del gasto (como texto).
                    ffecha=datetime.strptime(fech,formato)# Convierte esa fecha a objeto datetime.
                    if ffecha >= fecha_inicio and ffecha<= fecha_fin:# Si la fecha del gasto está dentro del rango
                        print(c)# Muestra el gasto.
                        total+= c["Monto"]# Suma su monto al total.
                print(f"Total gastado entre {inicio} y {fin}: {total}")# Muestra el total del rango.
            except FileNotFoundError:
                print("archivo no encontrado")
            except Exception as e:
                print("Error inesperado", e)
        elif opcion ==4:# Si el usuario eligió la opción 4 (regresar)
            print("Gracias por usar el Simulador de Gasto Diario.")
            break
        else:
            print("No se registra esa opción dentro del menú")


