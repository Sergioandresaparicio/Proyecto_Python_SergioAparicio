from datetime import datetime, timedelta #se llaman las librerias necesarias para ejecutar el modulo
import json
import os
formato="%Y-%m-%d" #se da el formato de fecha segun esta determinado en el diccionario  

def reporte ():
    while True:
        print("=============================================")
        print("          Calcular Total de Gastos")
        print("=============================================")
        print("Seleccione el periodo de cálculo:")
        print("")
        print("1. Calcular total diario")
        print("2. Calcular total semanal")
        print("3. Calcular total mensual")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcion= int(input("Ingrese una opcion: "))
        if opcion==1:    
            inicio_busqueda=input("Ingrese la fecha donde va a iniciar su busqueda en el siguiente formato YYYY-MM-DD: ") #Solicita la fecha en el formato establecido
            if os.path.exists("gastos.json"):# Verifica si el archivo "gastos.json" existe.
                with open("gastos.json","r",encoding="utf-8")as document:# Abre el archivo en modo lectura con codificación UTF-8.
                    report=json.load(document)# Carga los datos del archivo como una lista de diccionarios.
            precio=0# Inicializa una variable para acumular el total del día.
            for c in report:# Recorre cada gasto en la lista cargada.
                fech=c["Fecha"]# Obtiene la fecha del gasto actual.
                if fech == inicio_busqueda:# Si la fecha del gasto coincide exactamente con la fecha ingresada.
                    precio += c["Monto"]#suma su monto al total.
            print(precio)# Muestra el total gastado ese día.
            input("Presione enter para continuar.")
        elif opcion == 2:
            inicio_busqueda=input("Ingrese la fecha donde va a iniciar su busqueda en el siguiente formato YYYY-MM-DD")
            try:
                total=0# Inicializa el total semanal en 0.
                fecha_inicio = datetime.strptime(inicio_busqueda, formato)# Convierte la cadena de texto a un objeto de fecha.
                fecha_fin = fecha_inicio+timedelta(days=6)# Calcula la fecha final sumando 6 días (para cubrir 7 días en total).
                if os.path.exists("gastos.json"):# Verifica si el archivo existe.
                    with open("gastos.json","r",encoding="utf-8")as document:# Abre el archivo.
                        report=json.load(document)# Carga los gastos.
                for c in report:# Recorre cada gasto.
                    fech=c["Fecha"]# Obtiene la fecha del gasto (como texto).
                    ffecha = datetime.strptime(fech, formato)# Convierte esa fecha a objeto datetime.
                    if ffecha >= fecha_inicio and ffecha <= fecha_fin:# Si la fecha del gasto está dentro del rango semanal
                        total += c["Monto"]#suma su monto al total.
                print(f"El total de gastos en el periodo es: {total}")# Muestra el total semanal.
                input("ENTER PARA CONTINUAR .....")
            except ValueError:# Si la fecha ingresada no tiene el formato correcto
                print("Formato de fecha inválido. Use YYYY-MM-DD.")
                input("ENTER PARA CONTINUAR .....")
            except KeyError as e:# Si algún gasto no tiene la clave esperada (ej. "Fecha" o "Monto")
                print(f"Campo faltante en un gasto: {e}")
                input("ENTER PARA CONTINUAR .....")
        elif opcion == 3:
            inicio_busqueda=input("Ingrese la fecha donde va a iniciar su busqueda en el siguiente formato YYYY-MM-DD")
            try:
                total=0# Inicializa el total mensual.
                fecha_inicio = datetime.strptime(inicio_busqueda, formato)# Convierte la fecha de inicio a objeto datetime.
                fecha_fin = fecha_inicio+timedelta(days=30)# Suma 30 días para definir el rango mensual.
                if os.path.exists("gastos.json"):# Verifica existencia del archivo.
                    with open("gastos.json","r",encoding="utf-8")as document:# Abre el archivo.
                        report=json.load(document)# Carga los datos.
                for c in report: # Recorre cada gasto.
                    fech=c["Fecha"] # Obtiene la fecha del gasto.
                    ffecha = datetime.strptime(fech, formato)# Convierte a objeto datetime.
                    if ffecha >= fecha_inicio and ffecha <= fecha_fin:# Verifica existencia del archivo.
                        total += c["Monto"]#suma el monto.
                print(f"El total de gastos en el periodo es: {total}")# Muestra el total.
                input("ENTER PARA CONTINUAR .....")
            except ValueError:# Si el formato de fecha es incorrecto
                print("Formato de fecha inválido. Use YYYY-MM-DD.")
                input("ENTER PARA CONTINUAR .....")
            except KeyError as e:# Si falta una clave en algún gasto
                print(f"Campo faltante en un gasto: {e}")
                input("ENTER PARA CONTINUAR .....")
        elif opcion==4:
            print("Gracias por usar el Simulador de Gasto Diario.")
            break            
        else:
            print("No existe opcion para su solicitud.")

