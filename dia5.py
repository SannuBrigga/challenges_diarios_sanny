clave=['Goku','Veggeta','Gohan','Frezzer']#se completa en la variable clave utilizando listas los nombres de los personajes.
valor=['El mas fuerte de todos los ssj','Principe orgulloso del Planeta Veggeta,','El hijo de Goku le derroto a cell','El Villano destruye planetas'] #se completa en la variable valor utilizando listas las descripciones de los personajes
diccionariodbz={}#creo un diccionario vacio

for i in range(len(clave)):#recorre lo que es la lista clave
    diccionariodbz[clave[i]] = valor[i]# asigna el valor i a la clave i dentro del diccionaroio diccionariodbz.
print(diccionariodbz) #imprime el diccionario