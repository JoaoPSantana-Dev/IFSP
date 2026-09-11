#include <stdio.h>

void insertion_sort(float *vetor, int tamanhoVetor){
   float escolhido;
   int anterior, i;
   
   for (i = 1;i<tamanhoVetor;i++){
    escolhido=vetor[i];
    anterior = i-1;

    while (anterior>=0 && (vetor[anterior]>escolhido)){
        vetor[anterior+1] = vetor[anterior];
        anterior--;
    }
    
    vetor[anterior+1]=escolhido;
   }

    for(i=0;i<tamanhoVetor;i++){
        printf("\n%f",vetor[i]);
    }
}

int main(){
    float notas[10]={8,9,3,2,5,4,3,8,9,10};

    insertion_sort(notas, 10);

    return 0;
}