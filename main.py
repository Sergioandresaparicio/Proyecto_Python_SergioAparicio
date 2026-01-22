# Importamos los modulos para poder usar sus funciones más adelante.Debe existir en la misma carpeta y contener la funciones que se van a llamar.
import registro_nuevo_gasto
import listar_gastos
import reporte_gastos
import reporte_total
# Definimos la función principal del programa. Esta función se llama "main".
def main():
    while True: # Iniciamos un bucle infinito usando "while True". Esto significa que el menú se repetirá una y otra vez hasta que el usuario elija salir.
            print("=============================================")
            print("         Simulador de Gasto Diario")
            print("=============================================")
            print("Seleccione una opción:")
            print()
            print("1. Registrar nuevo gasto")
            print("2. Listar gastos")
            print("3. Calcular total de gastos")
            print("4. Generar reporte de gastos")
            print("5. Salir")
            print("=============================================")
            try:# Aquí intentamos leer lo que el usuario escribe, porque podrían ocurrir errores
                opcion = int(input("Ingrese una opción: ").strip())#Solicitamos el input que sera almacenado en la variable, se define como integrer
                #al elegir la opcion del menu se va a ejecutar alguna de las condiciones definidas en el if y elif
                if opcion == 1:
                    registro_nuevo_gasto.registrar_gasto()
                elif opcion == 2:
                    listar_gastos.listar()
                elif opcion == 3:
                    reporte_gastos.reporte()
                elif opcion == 4:
                    reporte_total.generar_reporte()
                elif opcion == 5:#Esta opcion lleva al break y a terminar la ejecucion del while
                    opcion=str(input("¿Desea salir del programa? (S/N): ").title().strip())
                    if opcion == "S":
                        print("Muchas gracias por usar nuestro sistema.")
                        break#el break termina la ejecucion del programa
                    elif opcion == "N":
                        continue
                else:# Mostramos un mensaje de error indicando que la opción no es válida.
                    print("Opción no válida. Por favor, seleccione una opción del menú.")                    
            except ValueError:# Si el usuario escribe algo que NO es un número (por ejemplo, "hola"), Python no puede convertirlo a "int", y lanza un error llamado "ValueError".Aquí lo capturamos y mostramos.
                print("Entrada inválida. Por favor, ingrese un número.")
            except Exception as e:# Este bloque atrapa cualquier otro error inesperado que no sea un ValueError.
                print(f"Ocurrió un error inesperado: {e}")# Guardamos el error en la variable "e" para mostrarlo al usuario.
            print()
if __name__ == "__main__":# Esta línea es una convención en Python. Significa: "Si este archivo se ejecuta directamente
    main()# (y no se importa desde otro archivo), entonces ejecuta la función main()".