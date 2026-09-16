public class Livro {
    private String codigo;
    private String titulo;
    private String autor;
    private int ano;

    public Livro(String codigo, String titulo, String autor, int ano){
        this.codigo = codigo;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }

    public void mostrarCampos(){
        System.out.println(
                "\nCódigo: "+codigo +
                "\nTitulo: "+titulo+
                "\nAutor: "+autor+
                "\nAno: "+ano);
    }
}
