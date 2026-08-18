import java.util.ArrayList;

public class Main {
    public static void main(String[] args){
        ArrayList<Alunos>alunos= new ArrayList<>();

        Alunos aluno1 = new Alunos("João Paulo","SP3295893","TADS","Quebrar Códigos","Celso",9,8);
        Alunos aluno2 = new Alunos("Henrique","SP3295958","RH","Incompentência 1","Carlinho",4,5);

        alunos.add(aluno1);
        alunos.add(aluno2);

        for(Alunos aluno: alunos){
            aluno.displayDados();
        }


    }
}