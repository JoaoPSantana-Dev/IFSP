/* Bibliotecas */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* O vetor de alunos pagodeiros será de 20 alunos */
#define TAMANHO_VETOR_ALUNOS 20

/* Tipos de dados pré-definidos */
typedef struct{
	char pront 	[10];
	char nome	[50];
	char email	[80];
}
registro;

/* Protótipos de funções */
int main();
int buscaBin(registro *r, char n[10], int t);
void mostra(registro *r);
void bubble_sort(registro *r, int TAMANHO_VETOR);
void abastece (registro *r);

/* Funções */
void abastece (registro *r)
{   /* Cria-se um vetor local temporário com a inicialização literal 
	   e copia-se o seu conteúdo para o ponteiro de destino usando memcpy.*/
    registro dados[TAMANHO_VETOR_ALUNOS] = {
        {"SP3234967", "Belo", 					"belo@pagode.com.br"				},
        {"SP3134208", "Chande", 				"chande@pagode.com.br"				},
        {"SP3235202", "Chrigor", 				"chrigor@pagode.com.br"				},
        {"SP3240649", "Dilsinho", 				"dilsinho@pagode.com.br"			},
        {"SP3240321", "Ferrugem", 				"ferrugem@pagode.com.br"			},
        {"SP3233207", "Leandro Lehart", 		"leandro.lehart@pagode.com.br"		},
        {"SP3200200", "Leci Brandao", 			"leci.brandao@pagode.com.br"		},
        {"SP3240209", "Luiz Carlos", 			"luiz.carlos@pagode.com.br"			},
        {"SP3240206", "Marquinhos Sensacao", 	"marquinhos.sensacao@pagode.com.br"	},
        {"SP323309X", "Mumuzinho", 				"mumuzinho@pagode.com.br"			},
        {"SP3234203", "Netinho de Paula", 		"netinho.paula@pagode.com.br"		},
        {"SP3234681", "Pericles", 				"pericles@pagode.com.br"			},
        {"SP3134091", "Rodriguinho", 			"rodriguinho@pagode.com.br"			},
        {"SP3240204", "Salgadinho", 			"salgadinho@pagode.com.br"			},
        {"SP3240851", "Suel", 					"suel@pagode.com.br"				},
        {"SP3200175", "Thiaguinho", 			"thiaguinho@pagode.com.br"			},
        {"SP3234201", "Tiee", 					"tiee@pagode.com.br"				},
        {"SP3240205", "Vava", 					"vava@pagode.com.br"				},
        {"SP3240835", "Xande de Pilares", 		"xande.pilares@pagode.com.br"		},
        {"SP3235793", "Zeca Pagodinho", 		"zeca.pagodinho@pagode.com.br"		}
    };

    /* Copia todo o bloco de memória do vetor temporário para o destino */
    memcpy(r, dados, sizeof(dados));
}

void bubble_sort(registro *r, int TAMANHO_VETOR)
{
	int i, j; registro aux;
    for ( j = 0; j<TAMANHO_VETOR-1; j++) 
    {
       for ( i = 0; i<TAMANHO_VETOR-1-j; i++) 
       {
           if ( strcmp(r[i].pront , r[i+1].pront) > 0 )
           {
            aux   = r[i];
			r[i]  = r[i+1];
			r[i+1]= aux;
		   }
	   }
	}
}

void mostra(registro *r){
	int i;
	char tecla;
	printf ("\n---------------ALUNOS PAGODEIROS--------------");
	printf ("---------------PRONTUARIOS--------------");
	for (i=0; i<TAMANHO_VETOR_ALUNOS; i++)
		printf ("\n%-10s\t%-50s\t%-80s", r[i].pront, r[i].nome, r[i].email);
	printf ("\nPressione qualquer tecla para continuar -> ");
	scanf("%c", &tecla);
}

int buscaBin    (registro *r, char n[10], int t)
{    
  int ini=0, fim=t, meio;    
  while (ini<=fim)    
  {        
    meio=(ini+fim)/2; /* descobre qual � a posi��o do meio do vetor     */
    if (strcmp(r[meio].pront, n) == 0) /* se o elemento do meio do vetor for o buscado...*/            
     return meio;     /* ...retorna a posi��o onde o elemento est�      */   
    if (strcmp(r[meio].pront, n) > 0) /* se o elemento do meio do vetor for maior que o buscado...*/         
     fim=meio-1;      /* ...o que se busca est� ANTES do meio; logo o novo fim do vetor ser� uma posi��o antes do meio*/  
    else              /* sen�o o que se busca est� DEPOIS do meio...*/
     ini=meio+1;      /* ... logo o novo in�cio do vetor ser� uma posi��o depois do meio */  
   }    
   return -1; /* s� retorna -1 quando fez sucessivas divis�es do vetor e N�O ACHOU o que se busca */
}

/* Corpo do programa */
int main(){
	registro    rAlunos[TAMANHO_VETOR_ALUNOS];
	char 		pBusca[10];
	int 		result;
	char		opc;
	
	abastece(rAlunos);
	mostra (rAlunos);
	bubble_sort(rAlunos, TAMANHO_VETOR_ALUNOS);
	mostra (rAlunos);
	
    do {
		printf ("\nDigite prontuario para busca: "); 
		fflush(stdin); gets(pBusca);
		result=buscaBin (rAlunos, pBusca, TAMANHO_VETOR_ALUNOS);
		if ( result != -1 )
			printf ("\nAluno %s correspondente ao prontuario %s - INDICE = %i", 
			        rAlunos[result].nome, rAlunos[result].pront, result);
		else
			printf ("\nProntuario %s nao localizado", pBusca);
		printf ("\n\nNovo teste? [n/N=nao] --> ");
		fflush(stdin); scanf("%c", &opc);
	} while (opc!='n' && opc!='N');
	
	return 0;
}
