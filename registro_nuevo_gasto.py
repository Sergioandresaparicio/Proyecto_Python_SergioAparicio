from datetime import date
import carga_datos
def registrar_gasto ():
    while True:
        try:
            try:
                print("=============================================")#Imprime todas las lineas de menú
                print("            Registrar Nuevo Gasto")
                print("=============================================")
                print("Ingrese la información del gasto:")
                print()
                print("- Monto del gasto:")
                print("- Categoría (ej. comida, transporte, entretenimiento, otros):")
                print("- Descripción (opcional):")
                print()
                print("Ingrese 'S' para guardar o 'C' para cancelar.")
                print("=============================================")
                opcion=str(input().title().strip())# Lee lo que el usuario escribe, elimina espacios al inicio/final, convierte la primera letra a mayúscula y lo guarda como texto.
                if opcion == "S":# Si el usuario escribió "S" (guardar)...
                    while True:
                        try:
                            monto = float(input("Ingrese el monto gastado: "))#Solicita el monto al usuario
                            if monto < 0:
                                print("El monto no puede ser negativo. Intente de nuevo.")
                                continue # Regresa al inicio del ciclo while
                            break # Sale del ciclo si el monto es válido
                        except ValueError:
                            print("Entrada no válida. Ingrese un número.")
                    print("=============================================")
                    print(" Registrar Nueva categoria")
                    print("=============================================")
                    print("Seleccione la categoria del gasto:")
                    print("1. Comida")
                    print("2. Transporte")
                    print("3. Entretenimiento")
                    print("4. Otros")
                    print("=============================================")
                    opcion2=int(input())# Lee la opción numérica que el usuario ingresa y la convierte a entero.
                    if opcion2==1: #De aca en adelante se agregan las categorias por asignaciones predefinidas
                        categoria="Comida"
                        print("Selecciono la categoria de Comida")
                    elif opcion2==2:
                        categoria="Transporte"
                        print("Selecciono la categoria de Transporte")
                    elif opcion2==3:
                        categoria="Entretenimiento"
                        print("Selecciono la categoria de Entretenimiento")
                    elif opcion2==4:
                        categoria="Otros"
                        print("Selecciono la categoria de Otros")
                    else:
                        print("no existe la categoria")
                    print("=============================================")#en este punto se le pregunta al usuario si desea agregar una descripcion del monto gastado
                    print("            Registrar Descripción")
                    print("=============================================")
                    print("Desea ingresar una descripción:")
                    print("Ingrese 'S' para guardar o 'C' para cancelar.")
                    print("=============================================")
                    opcion3=str(input().title().strip())#se formatea la respuesta del usuario para que la entrada sea aceptada por los condicionale
                    if opcion3=="S":
                        comentario=str(input("Ingrese la descripción: ").title().strip())#Se solicita la descripcion al usuario
                    if opcion3=="C":
                        comentario="N/A"
                        print("Procesando datos.")                    
                    ingreso={"Fecha": str(date.today()),
                        "Monto": monto,
                        "categoria": categoria,
                        "Descripcion": comentario}
                    print(f"Sus datos se ingresaron correctamente : {ingreso}") #Definimos la estructura del diccionario capturando la fecha del sistema
                    carga_datos.ingreso_gastos(ingreso)
                    break#rompe el ciclo y regresa al modulo inicial
                elif opcion =="C":
                    print("muchas gracias por usar nuestra aplicación")          
                    break#rompe el ciclo y regresa al modulo inicial
                else:#una opcion fuera de rango da el mensaje prederterminado en el print
                    print("Opción no reconocida. Intente nuevamente.")
            except ValueError:# Si ocurre un error al convertir texto a número por ejemplo, escribir letras donde se espera un número
                print("Error al ingresar opciones.")
            except KeyboardInterrupt:# Captura el error que ocurre si el usuario interrumpe el programa por ejemplo, presionando Ctrl+C
                print("error al ingresar datos.")
        except Exception as e:# Si ocurre cualquier otro error inesperado no relacionado con ValueError
            print(f"Error inesperado: {e}")

