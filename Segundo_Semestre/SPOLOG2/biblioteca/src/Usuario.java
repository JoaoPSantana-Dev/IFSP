public class Usuario {
    private String matricula;
    private String nome;

    public Usuario(String matricula, String nome){
        this.matricula = matricula;
        this.nome = nome;
    }

    public void mostrarCampos(){
        System.out.println(
                "\nMatricula: "+matricula
                + "\nNome: "+nome
        );
    }

    public String getNome(){
        return this.nome;
    }

    public String getMatricula(){
        return this.matricula;
    }
}
