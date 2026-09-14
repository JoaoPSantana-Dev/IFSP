public class Livro {
    private String codigo;
    private String titulo;
    private String autor;

    public Livro(String codigo, String titulo, String autor){
        this.codigo = codigo;
        this.titulo = titulo;
        this.autor = autor;
    }

    public void mostrarCampos(){
        System.out.println(
                "\nCódigo: "+codigo +
                "\nTitulo: "+titulo+
                "\nAutor: "+autor);
    }

    public String getCodigo(){
        return this.codigo;
    }

    public String getTitulo(){
        return this.titulo;
    }

    public String getAutor(){
        return this.autor;
    }
}
