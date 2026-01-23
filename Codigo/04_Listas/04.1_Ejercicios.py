print("----------EJERCICIOS DE LISTAS----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea una lista con los nombres de tus amigos. Imprime el primer y el último nombre de la lista.")
nombres = ["luis","kathe","jonathan","angel","nicol","arian"]
print("El primer nombre de la lista es:",nombres[0])
print("El ultimo nombre de la lista es:",(nombres[5]))
print("-----FIN-----\n")

print("Ejercicio 2: Crea dos listas: una con frutas y otra con verduras. Concátenalas en una sola lista e imprime el resultado.")
frutas = ["Manzana","Banano","Fresa","Frambuesa","Coco"]
verduras = ["Berenjena","Pimenton","Zanahoria","Espinaca","Apio"]
print("Las Frutas y Verduras son:", frutas + verduras)
print("-----FIN-----\n")

print("Ejercicio 3: Crea una lista que contenga números repetidos. Usa count para determinar cuántas veces aparece un número específico.")
numeros = [1,2,345,67,89,3,2]
print("El numero", numeros[1] ,"esta repetido", numeros.count(2) , "veces")
print("-----FIN-----\n")

print("Ejercicio 4: Crea una lista y imprime la lista")
numeros = [12,23,123,32,1]
print("La lista de numeros es:", numeros)
print("-----FIN-----\n")

print("Ejercicio 5: Crea una lista de 4 colores cambia el segundo elemento o color y muestra el resultado")
colores = ["Rojo","Azul","Verde","Amarillo"]
print("Impresion sin el cambio", colores)
colores.insert(1,"Naranja")
colores.remove("Azul")
print("Impresion con el cambio", colores)
print("-----FIN-----\n")

print("Ejercicio 6: Crear una lista con animales y usa insert,append y remove para modificar la lista.")
animales = ["perro","gato","cocodrilo","caballo","cerdo"]
print("Impresion sin el cambio", animales)
animales.append("jirafa")
animales.insert(2,"tigre")
animales.remove("gato")
print("Impresion con el cambio", animales)
print("-----FIN-----\n")

print("Ejercicio 7: Dada una lista de elementos imprime cuantos elementos tiene la lista y cuantas veces se repite un elemento específico.")
nombres = ["luis","kathe","jonathan","angel","nicol","arian","kathe","kathe"]
print("La lista tiene:",len(nombres),"elementos")
print("El nombre kathe se repite:",nombres.count("kathe"),"veces")
print("-----FIN-----\n")

print("Ejercicio 8: Dada una lista de numeros usa el for para realizar la suma de los elementos que estan en la lista")
numeros = [12,23,34,45,56]
suma = 0
for numero in numeros:
      suma = suma + numero
print("La suma de los numeros es:",suma)
print("-----FIN-----\n")

print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Crea una lista con los números del 1 al 5.Usa append para agregar el número 6."
      "Luego usa remove para eliminar el número 3."
      "Finalmente, imprime la lista.")
numeros = [1,2,3,4,5]
print("Impresion sin el Append", numeros)
numeros.append(6)
print("Impresion con el Append",numeros)
numeros.remove(6)
print("Impresion sin el 6",numeros)
print("-----FIN-----\n")

print("Ejercicio 5: Crea una lista de números desordenados.Usa sort para ordenarlos de menor a mayor."
      "Luego, usa reverse para invertir el orden.")
numeros = [12,2,45,23,24,1,34]
numeros.sort()#El sort ordena los numero de manera automatica de menor a mayor
print("Impresion con el sort",numeros)
print("-----FIN-----\n")

print("Ejercicio 6: Crea una lista con cinco elementos.Haz una copia independiente de la lista usando copy."
      "Limpia la lista original usando clear y muestra ambas listas.")
elementos = ["Rodio","Plata","Oro","Estaño","Cobre"]
copia_elementos = elementos.copy()
elementos.clear()
print("Impresion de la lista original",copia_elementos)
print("-----FIN-----\n")

print("----------EJERCICIOS DIFICIL----------")
print("Ejercicio 7: Crea una lista con al menos 5 elementos." 
      "Escribe un programa que intercambie el primer elemento con el último y el segundo con el penúltimo.")
numeros = [1,2,3,4,5]
print("Impresion sin el intercambio", numeros)
intercambio = numeros[0],numeros[4] = numeros[4],numeros[0]
print("Impresion con el intercambio",intercambio)
print("-----FIN-----\n")

print("Ejercicio 8: Crea una lista de números entre 1 y 20." 
      "Escribe un programa que elimine todos los números pares de la lista sin usar un bucle explícito (for o while).")
numeros = list(range(1,21))#de esta manera utilizo una forma diferente de crear una lista
#y aparte utilizo una funcion range la cual me crea un listado de numero del 1 al 20
print("Impresion sin el remove", numeros)
#La siguiente linea elimina todos los numeros pares de la lista
numeros = list(filter(lambda x: x % 2 != 0, numeros))#de igual manera utilizo la forma especifica de crear la lista
#La función filter() en Python se utiliza para filtrar elementos de un iterable (como una lista o una tupla) 
#según una condición especificada en una función.
#La función lambda es una forma de definir funciones anónimas en una sola línea, lo que es útil cuando se usa con filter().
print("Lista sin números pares:", numeros)
print("-----FIN-----\n")

print("Ejercicio 9: Crea una lista de números del 1 al 10." 
      "Escribe un programa que divida esta lista en dos sublistas: una con los números pares y otra con los números impares.")

numeros = list(range(1, 11))
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 != 0, numeros))

# Mostrar resultados
print("Números pares:", pares)
print("Números impares:", impares)
print("-----FIN-----\n")

print("Ejercicio 10: Dada una lista con las edades de un grupo de personas, escribe un programa que:"
      "Encuentre la edad máxima y mínima usando las funciones max y min.Calcule el promedio de las edades."
      "Ordene la lista en orden ascendente.")
edades = [12,34,65,76,53,49,23]
promedio = sum(edades) / len(edades)

print("la edad maxina es:",max(edades))
print("la edad minima es:",min(edades))
print("El promedio de las edades es",promedio)
edades.sort()
print("El orden de la lista de forma ascendente es",edades)

print("-----FIN-----\n")

print("Ejercicio 11: Dada una lista de numeros, crea ua nueva lista sin repetir elementos pero manteniendo el orden original de los elementos.")

lista_original = [1,2,33,4,5,6,7,77,7,7,7,8,9,90,10,1,2,3,4,5]
lista_sin_repetidos = []
for numero in lista_original:
    if numero not in lista_sin_repetidos:
        lista_sin_repetidos.append(numero)

print("Impresion lista original",lista_original)
print("Impresion sin repetidos",lista_sin_repetidos)

print("-----FIN-----\n")

print("Ejercicio 12: Dada una lista de numeros enteros, regresa el segundo numero mayor sin que se use la funcion sort.")

lista_original = [10, 34, 23, 67, 89, 90]
maximo = float('-inf') #Asigna el valor mas bajo posible
segundo_maximo = float('-inf') #Aqui tambien asigna el valor mas bajo posible

for numero in lista_original:
      if numero > maximo:
            segundo_maximo = maximo
            maximo = numero
      elif numero > segundo_maximo and numero != maximo:
            segundo_maximo = numero

print("El segundo numero mayor es:", segundo_maximo)

print("-----FIN-----\n")

print("Ejercicio 13: Dada una lista de letras repetidas cuanta de cada letra cuanas veces aparece y muestra el resultado.")

lista_letras_repetidas = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'e', 'c', 'b']
lista_letras_repetidas.count('a')
lista_letras_repetidas.count('b')
lista_letras_repetidas.count('c')

print("La letra 'a' aparece:", lista_letras_repetidas.count('a'), "veces.")
print("La letra 'b' aparece:", lista_letras_repetidas.count('b'), "veces.")
print("La letra 'c' aparece:", lista_letras_repetidas.count('c'), "veces.")

print("-----FIN-----\n")

print("Ejercicio 14: Dada una lista de numero el ultimo numero muevelo al inicio de la lista")

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ultimo_numero = lista_de_numeros.pop()  # Elimina y obtiene el último número
lista_de_numeros.insert(0, 10)  # Inserta el último número al inicio de la lista

print("Lista con el ultimo numero al inicio:", lista_de_numeros)

print("-----FIN-----\n")

print("Ejercicio 15: Dada una lista de frutas pregunta al usuario por una fruta y si la fruta existe muestrala. Si no existe, agrégala a la lista.")

frutas = ["manzana", "banana", "cereza", "durazno"]
fruta_usuario = input("Ingresa el nombre de una fruta: ")
if fruta_usuario in frutas:
      print("La fruta es:", fruta_usuario)
else:
      frutas.append(fruta_usuario)
      print("Fruta agregada a la lista:", fruta_usuario)
      print("La lista de frutas actualizada es:", frutas)

print("-----FIN-----\n")

print("Ejercicio 16: Dada una lista de números imprime cada elemento con index y valor.")

numeros = [10, 20, 30, 40, 50]
for index, valor in enumerate(numeros):#La función enumerate() agrega un contador a un iterable y lo devuelve en forma de objeto enumerado.
      print(f"Índice: {index}, Valor: {valor}")

print("-----FIN-----\n")

print("----------EJERCICIOS DE COMPREHENSION(LISTAS)----------")
print("Ejercicio 1: Dada una lista de números [1, 2, 3, 4, 5]," 
      "crea una nueva lista que contenga el doble de cada número usando una List Comprehension.")
numeros = [1, 2, 3, 4, 5]
operacion = [x**2 for x in numeros]
print("El doble de los numeros es:", operacion)

print("-----FIN-----\n")

print("Ejercicio 2: Tienes una lista de palabras ['sol', 'mar', 'montaña', 'rio', 'estrella'] y" 
      "quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.")
palabras = ["sol", "mar", "montaña", "rio", "estrella"]
conversion = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print("Las palabras filtradas y en mayusculas son:", conversion)

print("-----FIN-----\n")

print("Ejercicio 3: Tienes dos listas, una de claves ['nombre', 'edad', 'ocupación'] y otra de valores ['Juan', 30, 'Ingeniero']." 
      "Crea un diccionario combinando ambas listas usando una List Comprehension.")
claves = ['nombre', 'edad', 'ocupación']
valores = ['Juan', 30, 'Ingeniero']

combinacion_dict = {claves[i]:valores[i] for i in range(len(claves))}
print("Los valores del diccionario son:", combinacion_dict)

print("-----FIN-----\n")