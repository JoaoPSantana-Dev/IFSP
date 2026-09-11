#include <stdio.h>

void bubble_sort(float *vetor,int tamanhoVetor){
    int i, j;
    float aux;

    for(j =0;j<tamanhoVetor-1;j++){
        for(i=0;i<tamanhoVetor-1-j;i++){
            if(vetor[i] > vetor[i+1]){
                aux = vetor[i];

                vetor[i]=vetor[i+1];
                vetor[i+1]=aux;
            }
        }

    }

    
    for(int i =0;i<tamanhoVetor;i++){
        printf("\n%f",vetor[i]);
    }


}


int main(){
    float notas[10]={8,9,3,2,5,4,3,8,9,10};

    bubble_sort(notas, 10);

    return 0;
}