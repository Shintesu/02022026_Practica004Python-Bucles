# Bucles con range y notación especial con print

for i in ["Leisberth", "Cedeño", 3]:
    print("Hola", end=" ")  # Notación especial para que no haga salto de línea

for i in "leisberth_an24@hotmail.com":
    print(i, end=" ")  # Notación especial para que no haga salto de línea



email=False # Variable para verificar si el email es correcto, se inicializa en False

for i in "leisberth_an24@hotmail.com":
    if (i=="@"): # Si encuentra @ en el email, entonces es correcto
        email=True 
if email==True:
    print("\nEmail correcto") #n para salto de línea
else:
    print("\nEmail incorrecto")




email=False # Variable para verificar si el email es correcto, se inicializa en False
mi_email=input("Ingrese su email: ") 
for i in mi_email:
    if (i=="@"): # Si encuentra @ en el email, entonces es correcto
        email=True 
if email==True:
    print("\nEmail correcto") #n para salto de línea
else:
    print("\nEmail incorrecto")


contador=0 # Variable para contar la cantidad de caracteres válidos en el email
mi_email=input("Ingrese su email: ") 
for i in mi_email:
    if (i=="@" or i=="."): # si encuentra @ o . se sumará 1 al contador
        contador=contador+1 

if contador==2:
    print("\nEmail correcto") #n para salto de línea
else:
    print("\nEmail incorrecto")
