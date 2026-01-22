from datetime import datetime, timedelta
import json
import os
formato="%Y-%m-%d"
def calcular_gasto_por_categoria(gastos):
    """
    Recibe una lista de gastos (diccionarios) y devuelve un diccionario
    con el total gastado por cada categoría.
    """
    acumulado = {}                                 # Crea un diccionario vacío para ir guardando la suma de gastos por categoría.
    for c in gastos:                           # Recorre cada gasto (diccionario) en la lista "gastos".
        cat = c["categoria"]                   # Extrae el valor de la clave "categoria" del gasto actual.
        monto = c["Monto"]                     # Extrae el valor de la clave "Monto" del gasto actual.
        if cat in acumulado:                       # Si la categoría ya existe en el diccionario "acumulado"...
            acumulado[cat] += monto                # ...suma el monto actual al total ya guardado para esa categoría.
        else:                                      # Si la categoría NO está en el diccionario...
            acumulado[cat] = monto                 # ...la agrega con el monto actual como primer valor.
    return acumulado                               # Devuelve el diccionario con los totales por categoría.

def generar_reporte():                          # Define una función llamada "generar_reporte" que crea un resumen de gastos.
    if not os.path.exists("gastos.json"):       # Verifica si el archivo "gastos.json" NO existe.
        print("No hay datos de gastos para generar un reporte.")  # Muestra mensaje si no hay datos.
        input("ENTER PARA CONTINUAR .....")     # Pausa el programa hasta que el usuario presione Enter.
        return                                  # Termina la función aquí, sin hacer nada más.

    with open("gastos.json", "r", encoding="utf-8") as archivo:  # Abre el archivo "gastos.json" en modo lectura con codificación UTF-8.
        gastos = json.load(archivo)             # Carga todos los gastos del archivo como una lista de diccionarios.

    print("=============================================")  # Línea decorativa.
    print("           Generar Reporte de Gastos")         # Título de la sección.
    print("=============================================")  # Línea decorativa.
    print("1. Reporte diario")                  # Opción 1: reporte de un solo día.
    print("2. Reporte semanal")                 # Opción 2: reporte de los últimos 7 días.
    print("3. Reporte mensual")                 # Opción 3: reporte de los últimos 30 días.
    print("4. Regresar")                        # Opción 4: salir sin generar reporte.
    print("=============================================")  # Línea decorativa final.

    try:                                        # Intenta ejecutar lo siguiente; si hay error de conversión, lo atrapa.
        opcion = int(input("Seleccione el opcion de reporte: "))  # Pide al usuario que ingrese un número y lo convierte a entero.
    except ValueError:                          # Si el usuario escribe algo que no es un número...
        print("Opción inválida.")               # Muestra mensaje de error.
        input("ENTER PARA CONTINUAR .....")     # Pausa.
        return                                  # Sale de la función.

    print("Ingrese la fecha de referencia en formato YYYY-MM-DD")  # Indica el formato esperado para la fecha.
    fecha1 = input("Fecha: ").strip()           # Pide la fecha y elimina espacios innecesarios.

    try:                                        # Intenta convertir la fecha ingresada a un objeto datetime.
        fecha_ref = datetime.strptime(fecha1, formato)  # Convierte la cadena de texto a fecha usando el formato definido (ej. "%Y-%m-%d").
    except ValueError:                          # Si el formato es incorrecto...
        print("Formato de fecha inválido. Use YYYY-MM-DD.")  # Muestra mensaje de error.
        input("ENTER PARA CONTINUAR .....")     # Pausa.
        return                                  # Sale de la función.

    gastos_filtrados = []                       # Crea una lista vacía para guardar los gastos que coincidan con el período.
    total_general = 0                           # Inicializa el total general en 0.

    for gasto in gastos:                        # Recorre cada gasto en la lista cargada del archivo.
        try:                                    # Intenta procesar la fecha de este gasto.
            fecha_gasto = datetime.strptime(gasto["Fecha"], formato)  # Convierte la fecha del gasto a objeto datetime.
        except ValueError:                      # Si la fecha del gasto está mal formateada...
            continue                            # Salta este gasto y pasa al siguiente (no lo incluye en el reporte).

        if opcion == 1:                         # Si el usuario eligió reporte diario...
            if fecha_gasto.date() == fecha_ref.date():  # Compara solo las fechas (sin hora).
                gastos_filtrados.append(gasto)  # Agrega el gasto a la lista filtrada.
                total_general += gasto["Monto"] # Suma su monto al total.

        elif opcion == 2:                       # Si eligió reporte semanal...
            inicio_semana = fecha_ref - timedelta(days=6)  # Calcula la fecha de inicio de la semana (6 días antes).
            if inicio_semana.date() <= fecha_gasto.date() <= fecha_ref.date():  # Si la fecha del gasto está en ese rango...
                gastos_filtrados.append(gasto)  # Lo agrega a la lista.
                total_general += gasto["Monto"] # Suma su monto.

        elif opcion == 3:                       # Si eligió reporte mensual (30 días)...
            inicio_mes = fecha_ref - timedelta(days=29)  # Calcula el inicio del período (29 días antes, para cubrir 30 días).
            if inicio_mes.date() <= fecha_gasto.date() <= fecha_ref.date():  # Si el gasto está en ese rango...
                gastos_filtrados.append(gasto)  # Lo agrega.
                total_general += gasto["Monto"] # Suma su monto.

        elif opcion == 4:                       # Si eligió la opción 4 (regresar)...
            print("Gracias por usar el Simulador de Gasto Diario.")  # Muestra mensaje de despedida.
            break                               # Sale del bucle "for" (aunque esto no tiene mucho efecto aquí, ya que no hay más iteraciones después).

        else:                                   # Si la opción no es 1, 2, 3 ni 4...
            print("Opción no válida.")          # Muestra mensaje de error.
            input("ENTER PARA CONTINUAR .....") # Pausa.
            return                              # Sale de la función.

    if not gastos_filtrados:                    # Si no se encontró ningún gasto en el período seleccionado...
        print("No se encontraron gastos en el período seleccionado.")  # Muestra mensaje.
        input("ENTER PARA CONTINUAR .....")     # Pausa.
        return                                  # Sale de la función.

    gasto_por_categoria = calcular_gasto_por_categoria(gastos_filtrados)  # Llama a la función que suma gastos por categoría.

    reporte_texto = (f"REPORTE DE GASTOS\n")    # Inicia el texto del reporte con un título.

    if opcion == 1:                             # Si es reporte diario...
        reporte_texto += (f"Período: Día {fecha1}\n")  # Agrega la fecha específica.
    elif opcion == 2:                           # Si es semanal...
        inicio_sem = (fecha_ref - timedelta(days=6)).strftime(formato)  # Calcula y formatea la fecha de inicio.
        reporte_texto += f"Período: Semana del {inicio_sem} al {fecha1}\n"  # Agrega el rango semanal.
    elif opcion == 3:                           # Si es mensual...
        inicio_mes = (fecha_ref - timedelta(days=29)).strftime(formato)  # Calcula y formatea la fecha de inicio del mes.
        reporte_texto += (f"Período: Mes del {inicio_mes} al {fecha1}\n")  # Agrega el rango mensual.

    reporte_texto += f"Total general: {total_general}\n"  # Agrega el total gastado en el período.
    reporte_texto += "\nGastos por categoría:\n"  # Agrega un subtítulo.
    for cat, total in gasto_por_categoria.items():  # Recorre cada categoría y su total.
        reporte_texto += f"- {cat}: {total}\n"   # Agrega una línea por categoría.

    # Preguntar al usuario cómo quiere el reporte
    print("¿Cómo desea ver el reporte?")        # Pregunta al usuario cómo prefiere recibir el reporte.
    print("1. Mostrar en pantalla")             # Opción 1: imprimir en consola.
    print("2. Guardar en archivo JSON")         # Opción 2: guardar en un archivo.

    try:                                        # Intenta leer la opción del usuario.
        salida = int(input("Seleccione una opción: "))  # Convierte la entrada a entero.
    except ValueError:                          # Si el usuario no ingresa un número...
        salida = 1                              # Por defecto, muestra en pantalla.

    if salida == 1:                             # Si eligió mostrar en pantalla...
        print("\n" + "="*50)                   # Imprime una línea decorativa.
        print(reporte_texto)                    # Muestra el reporte completo.
        print("="*50)                          # Línea decorativa final.
        input("ENTER PARA CONTINUAR .....")     # Pausa.

    elif salida == 2:                           # Si eligió guardar en archivo...
        nombre_archivo = f"reporte_gastos_{fecha1}.json"  # Define el nombre del archivo usando la fecha.
        reporte_json = {                        # Crea un diccionario con la estructura del reporte en formato JSON.
            "periodo": "",                      # Campo vacío que se llenará según la opción.
            "total_general": total_general,     # Total gastado.
            "gastos_por_categoria": gasto_por_categoria,  # Diccionario con totales por categoría.
            "detalle_gastos": gastos_filtrados  # Lista completa de los gastos incluidos.
        }
        if opcion == 1:                         # Si es diario...
            reporte_json["periodo"] = f"Diario - {fecha1}"  # Define el período.
        elif opcion == 2:                       # Si es semanal...
            inicio_sem = (fecha_ref - timedelta(days=6)).strftime(formato)
            reporte_json["periodo"] = f"Semanal - {inicio_sem} a {fecha1}"
        elif opcion == 3:                       # Si es mensual...
            inicio_mes = (fecha_ref - timedelta(days=29)).strftime(formato)
            reporte_json["periodo"] = f"Mensual - {inicio_mes} a {fecha1}"

        with open(nombre_archivo, "w", encoding="utf-8") as f:  # Abre un nuevo archivo en modo escritura.
            json.dump(reporte_json, f, ensure_ascii=False, indent=4)  # Guarda el diccionario como JSON bonito y legible.
        print(f"Reporte guardado en: {nombre_archivo}")  # Confirma dónde se guardó.
        input("ENTER PARA CONTINUAR .....")     # Pausa.

    else:                                       # Si elige una opción distinta de 1 o 2...
        print("Opción no válida. Mostrando en pantalla...")  # Asume que quiere verlo en pantalla.
        print("\n" + "="*50)                   # Línea decorativa.
        print(reporte_texto)                    # Muestra el reporte.
        print("="*50)                          # Línea decorativa final.