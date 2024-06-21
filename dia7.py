import random
import string

def generar_contraseña(longitud):
    # Definir los conjuntos de caracteres
    caracteres_mayusculas = string.ascii_uppercase
    caracteres_minusculas = string.ascii_lowercase
    caracteres_numeros = string.digits
    caracteres_simbolos = string.punctuation  # Símbolos de puntuación
    
    # Validar que la longitud esté entre 8 y 16 caracteres
    if longitud < 8 or longitud > 16:
        print("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")
        return None
    
    # Inicializar una lista para la contraseña
    lista_contraseña = []
    
    # Añadir al menos un carácter de cada tipo a la lista
    lista_contraseña.append(random.choice(caracteres_mayusculas))
    lista_contraseña.append(random.choice(caracteres_minusculas))
    lista_contraseña.append(random.choice(caracteres_numeros))
    lista_contraseña.append(random.choice(caracteres_simbolos))
    
    # Completar el resto de la contraseña con caracteres aleatorios
    while len(lista_contraseña) < longitud:
        # Seleccionar un carácter aleatorio de la combinación de todos los conjuntos de caracteres
        caracter_aleatorio = random.choice(caracteres_mayusculas + caracteres_minusculas + caracteres_numeros + caracteres_simbolos)
        lista_contraseña.append(caracter_aleatorio)
    
    # Mezclar aleatoriamente los caracteres en la lista de contraseña
    random.shuffle(lista_contraseña)
    
    # Convertir la lista de caracteres a una cadena de texto
    contraseña = ''.join(lista_contraseña)
    
    return contraseña

# Ejemplo de uso: generar una contraseña de longitud 12
longitud_contraseña = 12
nueva_contraseña = generar_contraseña(longitud_contraseña)
print("Contraseña generada:", nueva_contraseña)
