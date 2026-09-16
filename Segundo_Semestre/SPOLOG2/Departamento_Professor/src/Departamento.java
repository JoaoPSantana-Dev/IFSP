import java.util.ArrayList;

public class Departamento {
    private String nome;
    private ArrayList<Professor> professores = new ArrayList<Professor>();

    public Departamento(String nome) {
        this.nome = nome;
    }

    public void adicionar_professor(Professor professor){
        this.professores.add(professor);
        System.out.println("Professor Adicionado\n");
    }

    public void listar_professores(){

        if(professores.isEmpty()){
            System.out.println("Esse departamento não possui professores\n");
            return;
        }

        System.out.println("Lista de Professores: ");

        for(Professor professor:professores){
            professor.mostrar_dados();
        }
    }
}
