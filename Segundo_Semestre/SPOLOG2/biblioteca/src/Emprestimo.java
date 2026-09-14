public class Emprestimo {
    private Usuario usuario;
    private Livro livro;
    private String dataEmprestimo;
    private String nomeEmprestimo;


    public Emprestimo(Usuario usuario, Livro livro,String dataEmprestimo){
        this.usuario = usuario;
        this.livro = livro;
        this.dataEmprestimo = dataEmprestimo;
    }

    public void mostratDados(){
        System.out.println(
                "\nUsuário: "+usuario.getNome()+
                "\nLivro: "+livro.getTitulo()+
                "\nData de empréstimo: "+dataEmprestimo);
    }
}
