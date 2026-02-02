# BUCLES FOR III

for i in range(5,10,3):  # el tercer parámetro es el "step" o paso, es decir, de cuánto en cuánto va aumentando
    print(f"valor de la variable {i}") # al poner f antes de las comillas, se puede usar {} para incluir variables dentro del string
print("Fin del bucle")




valido=False

email=input("Ingrese su email: ")

for i in range(len(email)): # len() devuelve la cantidad de caracteres en el string
    if  email[i]=="@":
        valido=True

if valido:
    print("Email válido")
else:   
    print("Email inválido") 





# ejemplo_len.py
# Demuestra usos comunes de len()

def validar_email(email):
    # comprobamos que tenga al menos 6 caracteres y contenga '@'
    if len(email) < 6:
        return False, "El email es demasiado corto"
    if "@" not in email:
        return False, "Falta el caracter '@'"
    return True, "Email válido"

def main():
    emails = ["a@b.c", "usuario@example.com", ""]
    for e in emails:
        ok, mensaje = validar_email(e)
        print(f"'{e}': {mensaje} (longitud: {len(e)})")

    lista = [10, 20, 30]
    print("\nEjemplo con lista")
    print("longitud de lista:", len(lista))
    if len(lista) > 0:
        print("La lista no está vacía. Primer elemento:", lista[0])

    texto = "Hola\nMundo"
    print("\nEjemplo con string (len cuenta caracteres):")
    print(f"texto: {repr(texto)} -> len = {len(texto)}")

    dic = {"a": 1, "b": 2}
    print("\nEjemplo con diccionario (len cuenta claves):", len(dic))

    # Usar len() con range para índices (menos idiomático que enumerate)
    print("\nIterar por índices usando len():")
    for i in range(len(lista)):
        print(f"índice {i} -> valor {lista[i]}")

    # Caso con generador: len() no funciona, hay que contar manualmente
    gen = (x for x in range(5))
    try:
        print("\nIntentando len(gen):", len(gen))
    except TypeError as err:
        print("len(gen) falla porque los generadores no tienen __len__():", err)
        # contar sin consumir en bucle (consumirá el generador)
        contador = sum(1 for _ in gen)
        print("Contados con sum(1 for _ in gen):", contador)

if __name__ == "__main__":
    main()