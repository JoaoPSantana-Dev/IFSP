public class Main{
    public static void main(String[] args){
        Livro livro1 = new Livro("001","Pequeno Principe", "Antoine de Saint-Exupéry",1943);
        Livro livro2 = new Livro("002","As Esganadas", "Jô Soares",2011);

        livro1.mostrarCampos();
        livro2.mostrarCampos();
    }
}