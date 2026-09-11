#include <stdio.h>

int fatorial(int numero){

    if(numero==1){
        return 1;
    }

    return (numero * fatorial(numero-1));
}

int main(){
    int resultado;
    int numero;

    printf("\nDigite um número positivo para achar o fatorial: ");
    scanf("%i",&numero);

    resultado = fatorial(numero);

    printf("O fatorial do número %i é %i \n",numero,resultado);

    return 0;
}