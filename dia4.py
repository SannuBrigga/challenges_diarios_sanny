datos= input('ingrese una serie de numeros ENTRE espacios:')

numeros=datos.split() #hace que el dato ingresado separe uno del otro

numeros=[int(num)for num in numeros]# se conviertee en entero el dato, y se recorre

numeros.sort() #ordena los numeros

print(numeros) #imprime los numeros