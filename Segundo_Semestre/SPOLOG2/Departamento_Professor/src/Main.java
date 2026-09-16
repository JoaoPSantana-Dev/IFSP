public class Main{
    public static void main(String[] args){
        Departamento departamentoMatematica = new Departamento("Matemática");

        Professor professor1 = new Professor("Jorge","001");
        Professor professor2 = new Professor("Carlos","002");

        departamentoMatematica.listar_professores();

        departamentoMatematica.adicionar_professor(professor1);
        departamentoMatematica.adicionar_professor(professor2);

        departamentoMatematica.listar_professores();
    }
}