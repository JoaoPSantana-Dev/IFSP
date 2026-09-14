public class Main {
    public static void main(String[] args) {
        Livro livro1 = new Livro("001","Pequeno Príncipe","Julio Verne");
        Usuario usuario1 = new Usuario("001","Joao Paulo");

        Livro livro2 = new Livro("002","Eu robô","Isaac Asimov");
        Usuario usuario2 = new Usuario("002","Romário da Silva");


        Emprestimo emprestimo1 = new Emprestimo(usuario1,livro1,"14/09/2026");
        Emprestimo emprestimo2 = new Emprestimo(usuario2,livro2,"14/09/2026");
        Emprestimo emprestimo3 = new Emprestimo(usuario1,livro2,"14/09/2025");


        emprestimo1.mostratDados();
        emprestimo2.mostratDados();
        emprestimo3.mostratDados();
    }
}