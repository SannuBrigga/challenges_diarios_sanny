#include <iostream>
#include <string>
#include <cctype> // Para tolower

using namespace std;

// Función para comprobar si una cadena es un palíndromo
bool esPalindromo(const string& cadena) {
    int inicio = 0;
    int fin = cadena.length() - 1;

    while (inicio < fin) {
        // Convertir ambos caracteres a minúsculas antes de compararlos
        char charInicio = tolower(cadena[inicio]);
        char charFin = tolower(cadena[fin]);

        // Ignorar caracteres que no son letras
        if (!isalpha(charInicio)) {
            inicio++;
            continue;
        }
        if (!isalpha(charFin)) {
            fin--;
            continue;
        }

        // Comparar los caracteres
        if (charInicio != charFin) {
            return false; // No es un palíndromo
        }

        inicio++;
        fin--;
    }

    return true; // Es un palíndromo
}

int main() {
    string texto;
    cout << "Introduce una palabra: ";
    cin >> texto;

    if (esPalindromo(texto)) {
        cout << texto << " SI es un palíndromo." << endl;
    } else {
        cout << texto << " no es un palíndromo." << endl;
    }

    return 0;
}
