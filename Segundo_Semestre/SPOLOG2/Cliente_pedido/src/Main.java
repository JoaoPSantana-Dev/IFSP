public class Main{
    public static void main(String[] args){
        Cliente Joao = new Cliente("Joao","123");
        Pedido pedido1 = new Pedido("001",45.59);
        Pedido pedido2 = new Pedido("002",60.00);
        Pedido pedido3 = new Pedido("003",600.00);

        Joao.adicionar_pedido(pedido1);
        Joao.adicionar_pedido(pedido2);
        Joao.adicionar_pedido(pedido3);

        Joao.mostrar_pedidos();

    }

}