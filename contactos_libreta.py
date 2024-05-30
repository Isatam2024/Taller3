#Crea un programa que almacene la información de contactos en una libreta utilizando tuplas. Cada tupla debe contener
# el nombre y el número de teléfono de un contacto. Puedes implementar funciones para agregar nuevos contactos,
# buscar un contacto por nombre y listar todos los contactos.

# Inicializamos la libreta de contactos vacía
libreta = ()

# Función para agregar un nuevo contacto
def agregar_contacto(libreta, nombre, telefono):
    # Creamos una nueva tupla con el nombre y el número de teléfono
    nuevo_contacto = (nombre, telefono)
    # Agregamos el nuevo contacto a la libreta
    libreta += (nuevo_contacto,)
    return libreta

# Función para buscar un contacto por nombre
def buscar_contacto(libreta, nombre):
    # Recorremos la libreta de contactos
    for contacto in libreta:
        # Si el nombre del contacto coincide con el nombre buscado
        if contacto[0] == nombre:
            # Devolvemos el contacto encontrado
            return contacto
    # Si no se encuentra el contacto, devolvemos None
    return None

# Función para listar todos los contactos
def listar_contactos(libreta):
    # Recorremos la libreta de contactos
    for contacto in libreta:
        # Imprimimos el nombre y el número de teléfono del contacto
        print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

# Agregamos algunos contactos a la libreta
libreta = agregar_contacto(libreta, "Juan", "1234567890")
libreta = agregar_contacto(libreta, "María", "9876543210")
libreta = agregar_contacto(libreta, "Pedro", "5551234567")

# Listamos todos los contactos
print("Contactos:")
listar_contactos(libreta)

# Buscamos un contacto por nombre
contacto_busqueda = buscar_contacto(libreta, "Pedro")
if contacto_busqueda:
    print(f"Contacto encontrado: {contacto_busqueda[0]}, Teléfono: {contacto_busqueda[1]}")
else:
    print("Contacto no encontrado")