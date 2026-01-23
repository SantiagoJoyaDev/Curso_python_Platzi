print("----------EJERCICIOS DE TUPLAS----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea una tupla con los nombres de tus amigos. Imprime el primer y el último nombre de la tupla.")
my_friends_tuple = ("Santiago","Joya","Juan","Pedro","Pablo")
print(my_friends_tuple[0])
print(my_friends_tuple[4])    
print("-----FIN-----\n")

print("Ejercicio 2: Crea dos tuplas: una con frutas y otra con verduras. Concátenalas en una sola tupla e imprime el resultado.")  
my_fruits_tuple = ("Manzana","Pera","Naranja")
my_vegetables_tuple = ("Zanahoria","Lechuga","Tomate")
my_fruits_and_vegetables_tuple = my_fruits_tuple + my_vegetables_tuple
print(my_fruits_and_vegetables_tuple) #Se imprimen las tuplas concatenadas en una
print("-----FIN-----\n")

print("Ejercicio 3: Crea una tupla con números repetidos. Usa count para determinar cuántas veces aparece un número específico.")
my_repeated_numbers_tuple = (1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,3,4,5,3,3,6,7,78)
print("El numero 3 se repite:",my_repeated_numbers_tuple.count(3), "Veces")  
print("-----FIN-----\n")

print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Crea una lista de números. Convierte la lista en una tupla usando tuple(). Luego, convierte la tupla de vuelta a una lista usando list() y añade un nuevo número.")
my_numbers_list = [1,2,3,4,5,8,23,5,7,8,9,0]
my_numbers_list = tuple(my_numbers_list)
print("Impresion de los numeros como tupla -->", my_numbers_list)
my_numbers_tuple = list(my_numbers_list)
my_numbers_tuple.append(100)
print("Impresion de los numeros como lista y agregandole el valor (100)-->", my_numbers_tuple)
print("-----FIN-----\n")

print("Ejercicio 5: Crea una tupla con tres elementos: tu nombre, tu edad y tu ciudad. Usa el desempaquetado para asignar cada elemento a una variable e imprime esas variables.")  
my_personal_data_tuple = ("Santiago",22,"Bucaramanga")
name, age, city = my_personal_data_tuple
print("Nombre:",name)
print("Edad:",age)
print("Ciudad:",city)
print("-----FIN-----\n")

print("Ejercicio 6: Crea una tupla con diferentes nombres. Usa el método index para encontrar la posición de un nombre específico en la tupla.")  
my_names_tuple = ("Santiago","Joya","Juan","Pedro","Pablo")
my_names_tuple.index("Santiago")
print("La posicion de Santiago en la tupla es:",my_names_tuple.index("Juan"))
print("-----FIN-----\n")

print("----------EJERCICIOS DIFICL----------")
print("Ejercicio 7: Crea una tupla con dos números. Escribe un programa que intercambie sus valores sin usar una variable temporal adicional. Ejemplo: (a, b) = (b, a).")
mytwo_numbers_tuple = (1,2)
print("Valores iniciales:",mytwo_numbers_tuple)
mytwo_numbers_tuple = (mytwo_numbers_tuple[1],mytwo_numbers_tuple[0])
print("Valores intercambiados:",mytwo_numbers_tuple)  
print("-----FIN-----\n")

print("Ejercicio 8: Dada una tupla con los números del 1 al 4, crea una nueva tupla que contenga solo los números pares. Usa índices para acceder a los elementos específicos.")
my_numbers_tuple = (1,2,3,4)
my_even_numbers_tuple = (my_numbers_tuple[1],my_numbers_tuple[3])
print("-----FIN-----\n")

print("Ejercicio 9: Crea una tupla que contenga tres sub-tuplas: una con frutas, otra con verduras y otra con lácteos. Usa índices para acceder a cada sub-tupla y a un elemento específico dentro de ellas.")
my_food_tuple = (("Manzana","Pera","Naranja"),("Zanahoria","Lechuga","Tomate"),("Leche","Queso","Yogurt"))
print("Frutas:",my_food_tuple[2])
print("Verduras:",my_food_tuple[1])
print("Lacteos:",my_food_tuple[2])
print("-----FIN-----\n")

print("Ejercicio 10: Dada una tupla con las edades de un grupo de personas, encuentra la edad máxima, mínima y crea una nueva tupla con las edades ordenadas manualmente (sin usar sort ni ciclos).")
my_ages_tuple = (12,23,45,67,89,100,1,2,3,4,5,6,7,8,9,10)
print("El valor mayor de la tupla es: ",max(my_ages_tuple))
print("El valor mayor de la tupla es: ",min(my_ages_tuple))
sorted_ages = sorted(my_ages_tuple)
print("La tupla ordenada es:",sorted_ages)
print("-----FIN-----\n")

print("Ejercicio 11: Dada una lista de almenos 8 numeros imprime los primero 3, los ultimos 3 y imprime los elementos del indice del 2 al 5")

my_numbers = (12,2,345,678,9,97,96,7,5,3)

for num in my_numbers: #impresion de los primero 3 numeros
    if my_numbers.index(num) < 3: #Esto me toma el indice del numero y si es menor a 3 lo imprime
        print(num)
print("-----") 
for num in my_numbers: #impresion de los ultimos 3 numeros
    if my_numbers.index(num) >= len(my_numbers)-3:
        print(num)
print("-----")
for num in my_numbers: #impresion de los numeros del indice 2 al 5
    if my_numbers.index(num) >=2 and my_numbers.index(num) <=5:
        print(num)
print("-----FIN-----\n")

print("Ejercicio 12: Dadas dos tuplas una vacia y una con varios elementos verifica cual tupla es la vacia e imprime un mensaje")
my_empty_tuple = ()
my_full_tuple = (1,2,3,4,5)

if len(my_empty_tuple) == 0:
    print("La tupla vacía es la primera.",my_empty_tuple)
elif len(my_full_tuple) == 0:
    print("La tupla vacía es la segunda.")
else:
    print("Ambas tuplas tienen elementos.")
print("-----FIN-----\n")

print("Ejercicio 13: Dada una tupla general con subtuplas con datos como nombre, edad y ciudad de varias personas, imprime cada valor de cada subtupla en lineas separadas")

my_general_tuple = (("Santiago",22,"Bucaramanga"),("Juan",25,"Medellin"),("Pedro",30,"Cali"),("Maria",28,"Bogota"),("Ana",24,"Cartagena"))

for persons in my_general_tuple:
    print(persons[0])  #Imprime el nombre
    print(persons[1])  #Imprime la edad
    print(persons[2])  #Imprime la ciudad
    print("-----")
print("-----FIN-----\n")

print("Ejercicio 14: Dada dos tuplas del mismo tamano realiza la comparacion de ambas tuplas usando operadore (==, >, <, >=, <=, !=) e imprime el resultado de cada comparacion")

my_tuple1 = (1,2,3,4,5)
my_tuple2 = (1,2,3,4,6)

if my_tuple1 == my_tuple2:
    print("Las tuplas son iguales.")
elif my_tuple1 != my_tuple2:
    print("Las tuplas son diferentes.")
elif my_tuple1 > my_tuple2:
    print("La primera tupla es mayor que la segunda.")
elif my_tuple1 < my_tuple2:
    print("La primera tupla es menor que la segunda.")
elif my_tuple1 >= my_tuple2:
    print("La primera tupla es mayor o igual que la segunda.")
elif my_tuple1 <= my_tuple2:
    print("La primera tupla es menor o igual que la segunda.")
print("-----FIN-----\n")

print("Ejercicio 15: Dada una tupla con N elementos usa el operador * para crear una nueva tupla que repita los elementos de la tupla original M veces e imprime el resultado")

my_original_tuple = (1,2,3)
my_repeated_tuple = my_original_tuple * 3
print("Tupla original:",my_original_tuple)
print("Tupla repetida:",my_repeated_tuple)

print("-----FIN-----\n")

print("Ejercicio 16: Dada una tupla con N elementos elimina un elemento de la tupla creando una nueva tupla sin ese elemento e imprime el resultado")

my_original_tuple = (1,2,3,4,5)
my_new_tuple = my_original_tuple[:2] + my_original_tuple[3:] #Se crea una nueva tupla sin el elemento en el indice 2
# con los [:2] se toman los elementos desde el inicio hasta el indice 2 (sin incluir el 2)
print("Tupla original:",my_original_tuple)
print("Tupla sin el elemento en el índice 2:",my_new_tuple)

print("-----FIN-----\n")