public class Professor {
    private String nome;
    private String codigo;

    public Professor(String nome, String codigo) {
        this.nome = nome;
        this.codigo = codigo;
    }

    public void mostrar_dados(){
        System.out.println(
                "\nNome: "+nome+
                "\nCodigo: "+codigo
        );
    }
}
