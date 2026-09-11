#include <stdio.h>
#include <string.h> 


/*Declaro as pessoas aqui com o typedef e struct*/
typedef struct Pessoa {
    char nome[50];
    char dataNascimento[11];
    char cpf[15];
} Pessoa;
//No final tem q colocar o nome do struct

/*O segredo é trocar as datas e colocar os anos e mês primeiros para funcionar o string compare*/
Pessoa pessoas[] = {
    {"Freddie Mercury", "1946/09/05", "123.456.789-01"},
    {"Jimi Hendrix",    "1942/11/27", "234.567.890-12"},
    {"Janis Joplin",    "1943/01/19", "345.678.901-23"},
    {"John Lennon",     "1940/10/09", "456.789.012-34"},
    {"Elvis Presley",   "1935/01/08", "567.890.123-45"},
    {"David Bowie",     "1947/01/08", "678.901.234-56"},
    {"Kurt Cobain",     "1967/02/20", "789.012.345-67"},
    {"Robert Plant",    "1948/08/20", "890.123.456-78"},
    {"Mick Jagger",     "1943/07/26", "901.234.567-89"},
    {"Joan Jett",       "1958/09/22", "012.345.678-90"}
};



/*Tem q colocar o tipo de vetor com o tipo do Struct que no caso é Pessoa*/
void insertion_sort(Pessoa *vetor, int tamanhoVetor){
    Pessoa escolhido; //Deve-se declarar o tipo do escolhido
    int anterior,i;
    
    for(i=1;i<tamanhoVetor;i++){
        escolhido=vetor[i];
        anterior=i-1;
        
        while (anterior>=0 && (strcmp(vetor[anterior].dataNascimento,escolhido.dataNascimento))>0){
            vetor[anterior+1] = vetor[anterior]; //Aqui é a troca do vetor atual pelo vetor que vem antes dele
            anterior--;
    }
    
    //E aqui faz o vetor atual que mudou de lugar com o anterior se tornar o e que antes era o anterior
    vetor[anterior+1]=escolhido;
    
   }
}

int main()
{
    insertion_sort(pessoas,10);
    
    int i;
    for(i=0;i<10;i++){
         printf("Nome: %s | Data de nascimento: %s | CPF: %s\n",
               pessoas[i].nome,
               pessoas[i].dataNascimento,
               pessoas[i].cpf);
    }
    return 0;
}