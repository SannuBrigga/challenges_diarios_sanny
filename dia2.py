numero = int(input('ingrese un numero: ')) # le pido al usuario que ingrese un numero entero

for i in range (1,11): #utilizo un bucle for que recorra un rango del 1 al 10
    resultado= i * numero # creo la variable resultado y su valor es el indice * el numero ingresado
    print(f"{numero} x {i} = {resultado}") # se imprime el resultado
    
    
