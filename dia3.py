lista_vocales = ['a', 'e', 'i', 'o', 'u'] # creo una lista con las vocales

palabra = input("Ingrese una palabra: ") #pido que se meta una palabra

contador_vocales = 0 #declaro la variable del contador en cero

for caracter in palabra: #bucle que recorre letra por letra la palabra
    if caracter in lista_vocales:# si hay una vocal  en la lista vocales
        contador_vocales += 1 # se suma +1

# Imprimir el total de vocales
print("El número total de vocales en la palabra es:", contador_vocales)
