print("----------BUCLES----------")
print("----------WHILE----------")
#En Python existen dos tipos de bucles: while y for los cuales se utilizan para repetir un bloque de código varias veces.
#estos sirven para ejecutar un bloque de código varias veces.

#Bucle while
#El bucle while se ejecuta mientras una condición sea verdadera.

my_condition = 0
while my_condition < 11:
    print("El valor de la condición es:", my_condition)
    my_condition += 1#Incrementa en 1 el valor de la variable my_condition esto se llama contador
    #my_condition = my_condition + 1#Otra forma de incrementar el valor de la variable my_condition

print("Mensaje fuera del bucle while")

my_condition = 0 #lo tengo que volver a inicializar para que no me tome el valor anterior
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("El valor de la condición es:", my_condition)
        
my_condition = 0 #lo tengo que volver a inicializar para que no me tome el valor anterior
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("El valor de la condición es:", my_condition)
        break

my_condition = 0 #lo tengo que volver a inicializar para que no me tome el valor anterior
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("El valor de la condición es:", my_condition)
        continue
    
print("----------FOR----------")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in my_list: #Recorre la lista y asigna el valor a la variable number el number es una variable temporal que se crea en el bucle para 
    #almacenar el valor de la lista en cada iteración pero puede tener cualquier nombre como x, y, z, i, etc.
    print(number)
    
print("\n")
for i in range(10):
    print("Numeros:", i)
    
frutas = ["Banana","Fresa","Melon","Uva","Melocoton"]

for i in frutas:
    if i == "Melon":
        print("\nLa fruta es:", i)
        break
    
frutas = ["Banana","Fresa","Melon","Uva","Melocoton"]
for i in frutas:
    if i == "Melon":
        print("\nLa fruta es:", i)
        continue
    print("Fruta:", i)
    
animales = ["Perro","Gato","Conejo","Tortuga","Hamster"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for animales, numeros in zip(animales, numeros): #zip une dos listas en una tupla
    print("Animal:", animales, "Numero:", numeros)
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Imprimiendo la lista pero por su indiice

for num in enumerate(numeros): #enumerate devuelve una tupla con el indice y el valor de la lista
    print(num)
    
colores = {1: "Rojo", 
           2: "Verde", 
           3: "Azul"}

for key, value in colores.items(): #items devuelve una tupla con el indice y el valor del diccionario
    print("Key:", key, "Value:", value)

print("----------ITERADOARES----------")    
#El iterador es una variable que se utiliza para recorrer una secuencia como una lista

my_list = [1, 2, 3, 4, 5, 6]
my_iterador = iter(my_list) #crea un iterador para la lista
print(my_iterador.__next__()) #obtiene el primer elemento de la lista
#.__next__() es un método especial que pertenece a los iteradores. Se usa para obtener el siguiente elemento de un iterador y 
# es equivalente a usar la función
print(my_iterador.__next__())
print(my_iterador.__next__())
print(my_iterador.__next__())
print(my_iterador.__next__()) 
print(my_iterador.__next__(),"\n")

text = "Hola"
text_itedaror = iter(text)

for i in text_itedaror:
    print(i)

print("\n")
    
limit = 10

ood_iter = iter(range(1,limit+1,2))
for num in ood_iter:
    print(num)
    
print("----------GENERADORES----------")
#Los generadores son funciones que devuelven un iterador. Son muy útiles para crear secuencias de datos grandes o infinitas sin necesidad de almacenarlas en memoria.

def my_generator():
    yield 1#Aqui le decimos lo que va a imprimir llamando al yield
    yield 2
    yield 3

for i in my_generator():
    print(i)
    
print("\n")

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b#Aqui se realiza la operacion fibonacci 
    
for i in fibonacci(21):
    print(i)
        
print("\n") 

def NumerosPares():
    my_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    for num in my_numeros:
        if num % 2 == 0:  # Verificamos si el número es par
            yield num  # Usamos yield para devolverlo como un iterador

# Usamos un bucle for para iterar sobre los valores generados
for i in NumerosPares():
    print("Numeros pares -->", i)

print("\n")
    
def NumerosImpares():
    my_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    for num in my_numeros:
        if num % 2 != 0:  # Verificamos si el número es par
            yield num  # Usamos yield para devolverlo como un iterador

# Usamos un bucle for para iterar sobre los valores generados
for i in NumerosImpares():
    print("Numeros Impares -->", i)
