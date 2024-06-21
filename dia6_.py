import random  # Importamos la biblioteca para generar números aleatorios

opciones = ['Piedra', 'Papel', 'Tijera']  # Definimos las posibles opciones del juego

# Pedimos al usuario que ingrese su elección
usuarioeleccion = input('Ingrese Piedra, Papel o Tijera: ')  

# La computadora elige aleatoriamente una opción
eleccioncompu = random.choice(opciones)  

# Determinamos el resultado del juego
if usuarioeleccion == eleccioncompu:
    resultado = 'Empate'  # Si las elecciones son iguales, es un empate
elif (usuarioeleccion == 'Piedra' and eleccioncompu == 'Tijera' or 
      usuarioeleccion == 'Papel' and eleccioncompu == 'Piedra' or
      usuarioeleccion == 'Tijera' and eleccioncompu == 'Papel'):
    resultado = 'Ganaste'  # Verificamos todas las combinaciones en las que el usuario gana
else:
    resultado = 'Computadora gana'  # Si no es empate ni gana el usuario, gana la computadora

# Mostramos el resultado del juego
print(f'La elección de la compu fue *{eleccioncompu}* entonces el {resultado}') 


