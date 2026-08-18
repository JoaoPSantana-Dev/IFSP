import  java.util.ArrayList;
import java.util.Scanner;

public class Controles {

    public Alunos buscar_aluno_por_prontuario(ArrayList<Alunos> alunos,String prontuario){

        for(Alunos aluno: alunos){
            if (prontuario.equals(aluno.getProntuario())){
                return  aluno;
            }
        }
        return null;
    }
}
