public class Pedido {
    private String numero;
    private double valor;

    public Pedido(String numero, double valor){
        this.numero = numero;
        this.valor = valor;
    }

    //getters
    public String getNumero() {
        return numero;
    }

    public double getValor() {
        return valor;
    }
}
