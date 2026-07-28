mascotas = []
allowed_types = ["gato","perro","puerco espín","búho","hámster"]


#Esta funcion pide el numero de telefono del dueno de la mascota, sino pone letras le pide que lo haga de nuevo 
def phone_number():
    while True:
        cellphone = input("Ingrese su numero de telefono para emergencias: \n")
        if cellphone.isdigit():
            return cellphone
        else:
            print("Error: El telefono solo puede tener numeros. Intentelo de nuevo. \n")
            

#Esta funcion obliga a elegir solo los tipos de mascotas permitidos            
def choosing_type():
    while True:
        print("Tipos de mascotas permitidos:\n")
        for type in allowed_types:
            print("-", type)
        
        type = input("Ingrese el tipo de mascota: ").lower().strip()
        
        if type in allowed_types:
            return type
        else:
            print("Este tipo de mascota no esta permitido. Intentelo otra vez.\n")
            

#Crea una nueva mascota y la guarda en una lista
def create_pet():
    print("---Crear una mascota---")
    
    name = input("Ingrese el nombre de la mascota: \n")
    type = choosing_type()
    
    pet = {
        "nombre": name,
        "tipo": type,
        "color": "",
        "apodo": "",
        "propietario": "",
        "telefono": ""
    }
    
    mascotas.append(pet)
    print("Macota creada correctamente.\n")
    

#Muestra la lista de mascotas
def show_pets():
    print("---Lista de mascotas---\n")
    
    if len(mascotas) == 0:
        print("No hay mascotas registradas.\n")
        return
    
    for i, pet in enumerate(mascotas):
        print(f"{i+1}.{pet['nombre']} - {pet['tipo']}")
        

#Permite editar los datos de una mascota
def edit_pet():
    print("---Editar mascotas---\n")
    
    if len(mascotas) == 0:
        print("No hay mascotas para editar.\n")
        return
    
    show_pets()
    
    try:
        numero = int(input("Elige el numero de la mascota que quieres editar: \n"))
        indice = numero - 1
        
        if indice < 0 or indice >= len(mascotas):
            print("Numero invalido.\n")
            return
        
    except ValueError:
        print("Debes escribir un numero.")
        return
    
    pet = mascotas[indice]
    
    print(f"Editando a {pet['nombre']}")
    
    nuevo_nombre = input("Nuevo nombre de la mascota, o presiona Enter para dejarlo igual: \n")
    
    if nuevo_nombre.strip() != "":
        pet["nombre"] = nuevo_nombre
        
    color = input("Ingrese el color de la masocta: \n")
    pet["color"] = color
    
    apodo = input("Ingrese el apodo de la mascota: \n")
    pet["apodo"] = apodo
    
    propietario = input("Ingrese el nombre del propietario: \n")
    pet["propietario"] = propietario
    
    telefono = phone_number()
    pet["telefono"] = telefono
    
    print("Mascota editada correctamente\n")
    
    print("Así quedó la mascota: \n")
    print(f"Nombre: {pet['nombre']}")
    print(f"Tipo: {pet['tipo']}")
    print(f"Color: {pet['color']}")
    print(f"Apodo: {pet['apodo']}")
    print(f"Propietario: {pet['propietario']}")
    print(f"Teléfono: {pet['telefono']}")


#Elimina una mascota de la lista    
def delete_pet():
    print("---Elimina una mascota de la lista---")
    if len(mascotas) == 0:
        print("No hay mascotas para eliminar.\n")
        return
    
    show_pets()
    
    try:
        numero = int(input("Elige el numero de la mascota que quieres eliminar: \n"))
        indice = numero - 1
        
        if indice < 0 or indice >= len(mascotas):
            print("Numero invalido.\n")
            return
        
    except ValueError:
        print("Debes escribir un numero. \n")
        return
    
    mascota_eliminada = mascotas.pop(indice)
    print(f"La mascota {mascota_eliminada['nombre']} fue eliminada correctamente.\n")
    
    
#Menu principal del programa
def menu():
    while True:
        print("==========Guraderia de mascotas==========\n")
        print("1. Crear mascota")
        print("2. Editar mascota")
        print("3. Eliminar mascota")
        print("4. Ver mascotas")
        print("5. Salir")
        
        opcion = int(input("Elige una opcion:\n"))
        
        if opcion == 1:
            create_pet()
        elif opcion == 2:
            edit_pet()
        elif opcion == 3:
            delete_pet()
        elif opcion == 4:
            show_pets()
        elif opcion == 5:
            print("Saliendo del porgrama...\n")
            break
        else:
            print("Opcion incorrecta. Intentalo otra vez...\n")
            
menu()