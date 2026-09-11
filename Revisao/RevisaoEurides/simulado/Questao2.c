#include <stdio.h>
#include <locale.h>

int encontrarMinimo(int *vet, int tamanho) {
    // Caso base: se o vetor tiver tamanho 1, o único elemento é o mínimo
    if (tamanho == 1) {
        return vet[0];
    }
    
    // Passo recursivo: encontra o mínimo no restante do array (a partir do segundo elemento)
    int minResto = encontrarMinimo(vet + 1, tamanho - 1);
    
    // Compara o primeiro elemento com o menor do restante e retorna o menor deles
    if (vet[0] < minResto) {
        return vet[0];
    } else {
        return minResto;
    }
}

void mostraArray(int *vet, int tamanho) {
    int i;
    printf("\n[");
    for (i = 0; i < tamanho; i++)
        if (i < tamanho - 1)
            printf("%i,", vet[i]);
        else
            printf("%i]\n", vet[i]);
}

int main() {
    int arr[] = {3, 5, 75, 2, 8}, tamanho;
    setlocale(LC_ALL, "");
    tamanho = sizeof(arr) / sizeof(arr[0]);
    mostraArray(arr, tamanho);
    printf("\nO valor mínimo no array é: %d\n", encontrarMinimo(arr, tamanho));
    return 0;
}