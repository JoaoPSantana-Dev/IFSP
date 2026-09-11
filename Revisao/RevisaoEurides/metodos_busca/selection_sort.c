#include <stdio.h>

void selection_sort(float *vetor, int tamanhoVetor){
    int pos_min, i,j;
    float aux;

    for(i=0;i<tamanhoVetor;i++){
        pos_min=i;

        for(j=i+1;j<tamanhoVetor;j++){
            if(vetor[j]<vetor[pos_min]){
                pos_min=j;
            }
        }

        if(pos_min !=i){
            aux = vetor[i];
            vetor[i] = vetor[pos_min];
            vetor[pos_min]=aux;
        }
    }

    for(i=0;i<tamanhoVetor;i++){
        printf("\n%f",vetor[i]);
    }
}

int main(){
    float notas[10]={8,9,3,2,5,4,3,8,9,10};

    selection_sort(notas, 10);

    return 0;
}