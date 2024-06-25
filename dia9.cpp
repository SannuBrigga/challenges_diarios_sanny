#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// Comienza el programa principal
int main() {
    // Se crea el vector y se declara que tipo de vector es, en este caso es "int"
    // La variable vector se llama "numeros" y luego se le asignan los valores
    vector<int> numeros = {5, 2, 8, 1, 3, 7};

    // Se usa "sort", función de "algorithm" para poder ordenar los números enteros dentro del vector
    sort(numeros.begin(), numeros.end());

    
    cout << "\n" << "\n";

    // se imprime los numeros
    cout << "Los números ordenados son: ";
    
    // Se itera "numero" dentro de los elementos del vector "numeros" ya ordenado 
    for(int numero : numeros) {
        // Cada "numero" se imprime con un espacio " " para que sea más legible
        cout << numero << " ";
    }
    
    // Imprimir salto de línea 
    cout << endl;

    return 0;
}
