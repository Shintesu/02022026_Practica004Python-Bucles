# BUCLE V CONTINUE, PASS Y ELSE

for letra in "Python": # Recorremos la cadena

    if letra=="h": # Si la letra es h, saltamos a la siguiente iteración
        continue # Saltamos a la siguiente iteración

    print("Viendo la letra: " + letra) 


nombre="Wuthering Waves"
print(len(nombre)) # Imprimimos la longitud del nombre (incluyendo espacios)

contador=0

for i in nombre: # Recorremos el nombre
    if i==" ": # Si el carácter es un espacio, no hacemos nada
        continue # Saltamos a la siguiente iteración
    contador+=1 # Incrementamos el contador

print(contador) # Imprimimos el contador



# BUCLE V PASS (no las ejecutaré porque consumen recursos del CPU XD en bucle)

# while True: # Bucle infinito
#    pass # No hacemos nada, es un marcador de posición


# class MiClase: # Definimos una clase
#    pass # No hacemos nada, es un marcador de posición  


# BUCLE V ELSE

email=input("Ingrese su email: ")

for i in email: # Recorremos el email
    if i=="@":
        arroba=True # Si encontramos un arroba, establecemos la variable en True
        break # Salimos del bucle
else: # Si no se ha ejecutado el break, es decir, no se ha encontrado un arroba
    arroba=False # Establecemos la variable en False
print(arroba) # Imprimimos el valor de la variable
