palabra= input('ingrese una palabra: ')
def invertir_caracteres(cadena_de_caracteres):
     if len(cadena_de_caracteres) == 0:
         return ""
     else:
         return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1]) #:-1 operacion slacing
    
resultado = invertir_caracteres(palabra)
print (resultado)