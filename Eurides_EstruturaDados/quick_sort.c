#include <stdio.h>

typedef struct {
	int id_produto;
	char descritivo[100];
	char unidade_medida[20];
	int quantidade_por_cesta;
	int validade_em_dias;
} Donativo;


void print_donativo(Donativo *vetor, int tamanho_vetor){
	int i;
	printf("\n\n ------ Tabela de Donativos ------ \n\n");
    for(i=0;i<tamanho_vetor;i++){
    	printf("ID:%02i |%-52s| %-10s| %i| %4i\n",
		vetor[i].id_produto,
		vetor[i].descritivo,
		vetor[i].unidade_medida,
		vetor[i].quantidade_por_cesta,
		vetor[i].validade_em_dias
		);
	}
	
}

/* Efetua as trocas necessárias */
void troca (Donativo *A, Donativo *B){
	Donativo aux = *A;
	*A = *B;
	*B = aux;
}

int particiona (Donativo *vetor, int ini, int pivo){
	int i;
	int p_maior = ini; /* a posição do maior é a do início do vetor */
	
	for ( i=ini; i<pivo; i++ ) /* percorre o vetor da posição ini até a do pivô */{ /*se o elemento da posição atual for menor que o pivô...*/
		if ( vetor[i].validade_em_dias < vetor[pivo].validade_em_dias ){
			troca( &vetor[i], &vetor[p_maior] ); /*...troca o atual com o maior */
			p_maior++; /* o maior avança uma posição */
		}
			
	}
	/* percorrido o vetor, o pivô troca de posição com a do maior elemento... */
	troca( &vetor[p_maior], &vetor[pivo] );
	return p_maior; /* ... e o maior elemento passa a ser o novo pivô */
}




void quick_sort (Donativo * vetor, int ini, int fim){
	int pivo;
	if ( ini<fim ) /* Caso base */{
	pivo = particiona ( vetor, ini, fim ); 
	
	if(ini==0 && fim==11){
		print_donativo(vetor,12);/* Particiona o vetor*/
	
	}

	quick_sort( vetor, ini, pivo-1 ); /* Ordena do início do vetor até antes do pivô */
	quick_sort( vetor, pivo+1, fim); /* Ordena desde após o pivô até o fim do vetor */
	}
}



int main(){
	
	Donativo donativos[12] = {
        {1,  "Leite em po integral para bebida", "400 g",   2, 1095},
        {2,  "Farinha de mandioca branca",       "500 g",   1, 2190},
        {3,  "Oleo de soja",                     "900 ml",  1, 400},
        {4,  "Polpa ou pure de tomate",          "caixa",   1, 300},
        {5,  "Sardinha em oleo comestivel",      "lata",    2, 1825},
        {6,  "Racao animal",                     "1 Kg",    1, 180},
        {7,  "Sabonete de corpo",                "barra",   1, 1095},
        {8,  "Creme dental",                     "bisnaga", 1, 700},
        {9,  "Absorvente higienico",             "pacote",  1, 1825},
        {10, "Agua sanitaria",                   "1 L",     1, 2190},
        {11, "Detergente em po",                 "1 Kg",    1, 1825},
        {12, "Desinfetante",                     "500 ml",  1, 730}
    };
    
	print_donativo(donativos,12);
	
	quick_sort(donativos,0,11);
	
	print_donativo(donativos,12);
	
	return 0;
    
}
