#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int id_produto;
    char descritivo[100];
    char unidade_medida[20];
    int quantidade_por_cesta;
    char validade_dias[20];
} Produto;

/* Efetua as trocas necess?rias */
void troca (Produto *A, Produto *B){
	Produto aux = *A;
	*A = *B;
	*B = aux;
}

int particiona (Produto *vetor, int ini, int pivo){
	int i;
	int p_maior = ini; /* a posi??o do maior ? a do in?cio do vetor */
	
	for ( i=ini; i<pivo; i++ ) /* percorre o vetor da posi??o ini at? a do piv? */{ /*se o elemento da posi??o atual for menor que o piv?...*/
		if (atoi(vetor[i].validade_dias)<atoi(vetor[pivo].validade_dias)){
			troca( &vetor[i], &vetor[p_maior] ); /*...troca o atual com o maior */
			p_maior++; /* o maior avan?a uma posi??o */
		}
			
	}
	/* percorrido o vetor, o piv? troca de posi??o com a do maior elemento... */
	troca( &vetor[p_maior], &vetor[pivo] );
	return p_maior; /* ... e o maior elemento passa a ser o novo piv? */
}




void quick_sort (Produto * vetor, int ini, int fim){
	int pivo;
	if ( ini<fim ) /* Caso base */{
	pivo = particiona ( vetor, ini, fim ); 
	
	quick_sort( vetor, ini, pivo-1 ); /* Ordena do in?cio do vetor at? antes do piv? */
	quick_sort( vetor, pivo+1, fim); /* Ordena desde ap?s o piv? at? o fim do vetor */
	}
}


void separarVetores(Produto *vetorBase, int tamanhoVetorBase){
	int i;
	int j=0;
	int k=0;
	
	Produto vetorAuxiliarString[tamanhoVetorBase];
	Produto vetorAuxiliarInteiro[tamanhoVetorBase];
	
	
	for(i=0;i<tamanhoVetorBase;i++){
		
		if(strcmp(vetorBase[i].validade_dias,"indeterminada")==0){
			vetorAuxiliarString[j]=vetorBase[i];
			
			j++;
		}
		else{
			vetorAuxiliarInteiro[k]=vetorBase[i];
			k++;
		}
	}
	
	if(k>1){
			quick_sort(vetorAuxiliarInteiro,0,k-1);
	}
		
	
	for(i=0;i<k;i++){
				vetorBase[i]=vetorAuxiliarInteiro[i];
	};
			
	for(i=0;i<j;i++){
		vetorBase[k+i]=vetorAuxiliarString[i];
	}

		
};	



void mostrar_tabela(Produto *vetor, int tamanhoArray){
	int i;
	
	for(i=0;i<tamanhoArray;i++){
		printf("ID: %d\n", vetor[i].id_produto);
        printf("Descricao: %s\n", vetor[i].descritivo);
        printf("Unidade: %s\n", vetor[i].unidade_medida);
        printf("Quantidade por cesta: %d\n",vetor[i].quantidade_por_cesta);
        printf("Validade (dias): %s\n\n",vetor[i].validade_dias);
	}
}

int main(){
	
	Produto produtos[] = {
    { 1,  "Leite em po integral para bebida", "400 g",   2,  "1095" },
    { 2,  "Arroz agulhinha",                 "5 Kg",    1,  "indeterminada" },
    { 3,  "Feijao carioquinha",               "1 Kg",    1,  "indeterminada" },
    { 4,  "Farinha de mandioca branca",       "500 g",   1,  "2190" },
    { 5,  "Acucar refinado",                  "1 Kg",    1,  "indeterminada" },
    { 6,  "Oleo de soja",                     "900 ml",  1,  "400" },
    { 7,  "Sal",                              "1 kg",    1,  "indeterminada" },
    { 8,  "Macarrao tipo espaguete",          "1 pacote",1,  "indeterminada" },
    { 9,  "Polpa ou pure de tomate",           "caixa",   1,  "300" },
    { 10, "Sardinha em oleo comestivel",      "lata",    2,  "1825" },
    { 11, "Racao animal",                     "1 Kg",    1,  "180" },
    { 12, "Sabonete de corpo",                "barra",   1,  "1095" },
    { 13, "Escova dental",                    "peca",    1,  "indeterminada" },
    { 14, "Creme dental",                     "bisnaga", 1,  "700" },
    { 15, "Absorvente higienico",             "pacote",  1,  "1825" },
    { 16, "Papel higienico",                  "pacote",  1,  "indeterminada" },
    { 17, "Agua sanitaria",                   "1 L",     1,  "2190" },
    { 18, "Detergente em po",                 "1 Kg",    1,  "1825" },
    { 19, "Desinfetante",                     "500 ml",  1,  "730" },
    { 20, "Esponja multiuso",                 "peca",    1,  "indeterminada" }
	};
	
	
	separarVetores(produtos,20);
	
	mostrar_tabela(produtos,20);
	
	return 0;
}
