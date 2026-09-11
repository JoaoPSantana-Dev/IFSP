/*
Quantas vezes a função Fx é autochamada quando b=12 e e=8?
*/
#include <stdio.h>

int Fx(unsigned long int b, unsigned long int e){
    printf("Foi chamada!");
    if (e==0){
        return 1;
    }
    else{
        return b * Fx(b,e-1);
    }
}

int main(){
    int resultado = Fx(12,8);

    printf("%i",resultado);
}

//A função Fx foi autochamada 8 vezes