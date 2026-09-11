#include <stdio.h>


int somaNumeros(int numeroFinal){
    if (numeroFinal==1){
        return 1;
    }

    return (numeroFinal + somaNumeros(numeroFinal-1));
}

int main(){
    int resultado, numero;

    printf("\nDigite o número para saber a soma de 0 até ele: ");
    scanf("%i", &numero);

    resultado = somaNumeros(numero);

    printf("A soma dos n primeiros números até o digitado é: %i \n",resultado);

    return 0;
}