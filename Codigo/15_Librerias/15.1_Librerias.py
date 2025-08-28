#Las librerias en python son un conjunto de modulos que nos permiten realizar tareas especificas
#Libreria OS
import os#Sirve para interactuar con el sistema operativo, permitiendo realizar operaciones como manipular archivos y directorios,
#obtener informacion del sistema, ejecutar comandos del sistema, etc.

#Variable cwd = Currect Working Directory
cwd = os.getcwd()
print("El directorio actual es: ", cwd)

#Listar los archivos .txt
txt_files = [f for f in os.listdir(cwd) if f.endswith('.txt')]# el metodo os.listdir() devuelve una lista de los archivos y directorios en el directorio actual
#El metodo endswith() devuelve True si la cadena termina con el sufijo especificado,
print("Los archivos .txt en el directorio actual son: ", txt_files)

# #Renombrar un archivo
# os.rename('Cuento_Caperucita.txt', 'Caperucita.txt') #El metodo os.rename() renombra un archivo o directorio
# print("El archivo 'archivo.txt' ha sido renombrado a 'nuevo_archivo.txt'")

# #Eliminar un archivo
# #os.remove('nuevo_archivo.txt') #El metodo os.remove() elimina un archivo

# #Listar los archivos .txt renombrados
# txt_files = [f for f in os.listdir(cwd) if f.endswith('.txt')]# el metodo os.listdir() devuelve una lista de los archivos y directorios en el directorio actual
# #El metodo endswith() devuelve True si la cadena termina con el sufijo especificado,
# print("Los archivos .txt en el directorio actual son: ", txt_files)
print("------------------------------------------------------------\n")
#Libreria Math
import math#Sirve para realizar operaciones matematicas avanzadas, como trigonometria, logaritmos, potencias, etc.

#Halalr el area y perimetro de un circulo
radio = 5
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El area del circulo de radio {radio} es: {area:.3f}")
print(f"El perimetro del circulo de radio {radio} es: {perimetro:.3f}")

#Calcular la raiz cuadrada de un numero
numero = 16
raiz_cuadrada = math.sqrt(numero)  # El metodo math.sqrt() devuelve la raiz cuadrada de un numero
print(f"La raiz cuadrada de {numero} es: {raiz_cuadrada:.3f}")

#Calcular el valor absoluto de un numero
numero_negativo = -10
valor_absoluto = abs(numero_negativo)  # El metodo abs() devuelve el valor absoluto de un numero
print(f"El valor absoluto de {numero_negativo} es: {valor_absoluto}")
print("------------------------------------------------------------\n")
#Libreria Random
import random#Sirve para generar numeros aleatorios, elegir elementos aleatorios de una lista, barajar listas, etc.

#Generar un numero aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)#El metodo random.randint(a, b) devuelve un numero entero aleatorio entre a y b, 
#incluyendo ambos extremos
print(f"El numero aleatorio entre 1 y 10 es: {numero_aleatorio}")

#Elegir colores aleatorios de una lista
colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja']
color_aleatorio = random.choice(colores)  # El metodo random.choice(lista) devuelve un elemento aleatorio de la lista
print(f"El color aleatorio elegido es: {color_aleatorio}")

#Barajar una lista de cartas
cartas = ['As de corazones', '2 de corazones', '3 de corazones', '4 de corazones', '5 de corazones']
random.shuffle(cartas)  # El metodo random.shuffle(lista) baraja o desordena los elementos de la lista en su lugar
print("Las cartas barajadas son: ", cartas)
print("------------------------------------------------------------\n")
#Libreria Datetime
import datetime#Sirve para trabajar con fechas y horas en Python, permitiendo realizar operaciones como obtener 
#la fecha y hora actual, formatear fechas, calcular diferencias entre fechas, etc.

#Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()  # El metodo datetime.datetime.now() devuelve la fecha y hora actual
print("La fecha y hora actual es: ", fecha_hora_actual)

#Formatear la fecha y hora
fecha_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")  # El metodo strftime() formatea la fecha y hora en una cadena
print("La fecha y hora actual formateada es: ", fecha_formateada)

#Calcular la diferencia entre dos fechas
fecha_inicio = datetime.datetime(2023, 1, 1)
fecha_fin = datetime.datetime(2023, 12, 31)
diferencia = fecha_fin - fecha_inicio  # La resta de dos objetos datetime devuelve un objeto timedelta
print(f"La diferencia entre {fecha_inicio.date()} y {fecha_fin.date()} es: {diferencia.days} dias")

#Obtener el dia de la semana
dia_semana = fecha_hora_actual.strftime("%A")  # El metodo strftime() devuelve el dia de la semana en formato de texto
print(f"Hoy es: {dia_semana}")
print("------------------------------------------------------------\n")
#Libreria JSON
import json#Sirve para trabajar con datos en formato JSON (JavaScript Object Notation), que es un formato 
#ligero de intercambio de datos
#Crear un diccionario
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "C++"]
}
#Convertir el diccionario a una cadena JSON
datos_json = json.dumps(datos, indent=4)  # El metodo json.dumps() convierte un objeto Python a una cadena JSON
print("Datos en formato JSON: \n", datos_json)

#Guardar los datos en un archivo JSON
with open('datos.json', 'w') as archivo_json:
    json.dump(datos, archivo_json, indent=4)  # El metodo json.dump() guarda un objeto Python en un archivo en formato JSON
    
print("------------------------------------------------------------\n")
#Libreria collections
from collections import Counter#Sirve para contar la frecuencia de elementos en un iterable, como una lista o una cadena

#Contar la frecuencia de palabras en un texto
texto = "Python es un lenguaje de programacion. Python es facil de aprender. Python es divertido."
palabras = texto.lower().split()  # El metodo lower() convierte el texto a minusculas y el metodo split() divide el texto en palabras
#El metodo split() divide una cadena en una lista de palabras, usando espacios como separador
frecuencia_palabras = Counter(palabras)  # El metodo Counter() cuenta la frecuencia de los elementos en un iterable
print("Frecuencia de palabras: ", frecuencia_palabras)

#Obtener los 3 elementos mas comunes
elementos_comunes = frecuencia_palabras.most_common(3)  # El metodo most_common(n) devuelve una lista de los n elementos mas 
#comunes y sus frecuencias
print("Los 3 elementos mas comunes son: ", elementos_comunes)
print("------------------------------------------------------------\n")
#Libreria statistics
import statistics#Sirve para realizar operaciones estadisticas, como calcular la media, mediana, moda, desviacion estandar, etc.

#Calcular la media de una lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = statistics.mean(numeros)  # El metodo statistics.mean() calcula la media de una lista de numeros
print(f"La media de los numeros es: {media:.3f}")

#Calcular la mediana de una lista de numeros
mediana = statistics.median(numeros)  # El metodo statistics.median() calcula la mediana de una lista de numeros
print(f"La mediana de los numeros es: {mediana:.3f}")

#Calcular la moda de una lista de numeros
moda = statistics.mode(numeros)  # El metodo statistics.mode() calcula la moda de una lista de numeros
print(f"La moda de los numeros es: {moda:.3f}")

#Calcular la desviacion estandar de una lista de numeros
desviacion_estandar = statistics.stdev(numeros)  # El metodo statistics.stdev() calcula la desviacion estandar de una lista de numeros
print(f"La desviacion estandar de los numeros es: {desviacion_estandar:.3f}")