#include <stdio.h>

int busca_binaria(float *vetor,int tamanhoVetor, float elementoBuscado){
    int esquerda=0,direita=tamanhoVetor-1,meio;

    while(esquerda<=direita){
        meio=(esquerda+direita)/2;

        if(vetor[meio]==elementoBuscado){
            return meio;
        }

        if(vetor[meio]>elementoBuscado){
            direita=meio-1;
        }
        else{
            esquerda=meio+1;
        }
    }

    return -1;
}

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
}



int main(){
    float notas[10]={8,9,3,2,5,4,3,8,9,10};
    int indice;

    bubble_sort(notas,10);
    indice = busca_binaria(notas,10,4);

    printf("\nO valor buscado se encontra na posição: %d\n",indice);


    return 0;
}