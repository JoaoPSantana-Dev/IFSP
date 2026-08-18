import java.util.List;
import java.util.ArrayList;

public class Alunos {
    private String nome;
    private String prontuario;
    private String curso;
    private String disciplina;
    private String professor;
    private ArrayList<Float> notas = new ArrayList<>();

    //Construtores
    public Alunos(String nome, String prontuario,String curso, String disciplina, String professor, float nota1, float nota2){
        this.nome = nome;
        this.prontuario = prontuario;
        this.curso = curso;
        this.disciplina = disciplina;
        this.professor = professor;
        this.notas.add(0,nota1);
        this.notas.add(1,nota2);
    }

    //Getters
    public String getNome(){
        return this.nome;
    }

    public String getProntuario(){
        return this.prontuario;
    }

    public float getNota(int index){
        return notas.get(index);
    }

    //Métodos
    public float calcula_media(){
        float soma = 0;
        float numeroNotas = notas.size();

        for(float nota:notas){
            soma+=nota;
        }
        return  soma/numeroNotas;
    }

    public String verificar_sitaucao(){
        float media = calcula_media();

        if(media>=6){
            return "APROVADO";
        }

        return "REPROVADO";
    }

    public void alterar_notas(float nota1,float nota2){
        notas.set(0,nota1);
        notas.set(1,nota1);
    }

    public void displayDados(){
        System.out.println("\n"+"=".repeat(60));
        System.out.println("DADOS DO ALUNO");
        System.out.println("=".repeat(60));

        System.out.println("Nome: "+nome);
        System.out.println("Prontuario: "+prontuario);
        System.out.println("Curso: "+curso);
        System.out.println("Disciplina: "+disciplina);
        System.out.println("Professor: "+professor);
        System.out.printf("Nota1: %.2f\n",getNota(0));
        System.out.printf("Nota2: %.2f\n",getNota(1));
        System.out.printf("Media: %.2f\n",calcula_media());
        System.out.println("Situação: "+verificar_sitaucao());
    }

}
