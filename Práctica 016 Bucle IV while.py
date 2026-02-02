# BUCLE WHILE

# while condicion:
    # bloque de código  
    # se repite mientras la condición sea True

i=1

while i<=10:   # mientras i sea menor o igual a 10
    print("Ejecución " + str(i)) # muestra el valor de i en cada vuelta
    i=i+1  # incrementa i en 1 (i+=1)

print("Termino la ejecución del bucle")





edad=int(input("Ingrese su edad: "))
while edad<0: # bucle que se repite mientras la edad sea negativa
    print("Edad negativa no válida, ingrese un valor positivo")
    edad=int(input("Ingrese su edad: "))
    print(f"Edad ingresada: {edad} años") # solo se muestra si el usuario ingresa una edad negativa
print(f"Edad del usuario: {edad} años") # se muestra siempre, al final, la edad válida ingresada






edad=int(input("Ingrese su edad: "))
while edad<3 or edad>120: # bucle que se repite mientras la edad sea menor a 3 o mayor a 120
    print("Edad no válida, ingrese un valor entre 3 y 120")
    edad=int(input("Ingrese su edad: "))
    print(f"Edad ingresada: {edad} años") # solo se muestra si el usuario ingresa una edad negativa
print(f"Edad del usuario: {edad} años") # se muestra siempre, al final, la edad válida ingresada






import math # importa la librería math para usar funciones matemáticas

print("Programa de cálculo  de raíz cuadrada")
numero=int(input("Ingrese un número por favor: "))

intentos=0 # contador de intentos
while numero<0: # bucle que se repite mientras el número sea negativo
    print("No se puede calcular la raíz cuadrada de un número negativo")
    
    if intentos==2: # si ya hubo 2 intentos fallidos
        print("Ha agotado el número de intentos, el programa ha finalizado")
        break  # termina el bucle while

    numero=int(input("Ingrese un número por favor: "))
    if numero<0:
        intentos=intentos+1 # incrementa el contador de intentos

if intentos < 2:  # si no se agotaron los intentos
    solucion=math.sqrt(numero) # calcula la raíz cuadrada
    print(f"La raíz cuadrada de {numero} es {solucion}")
    print("Gracias por usar el programa de cálculo de raíz cuadrada")
