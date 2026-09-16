import java.util.ArrayList;

public class Cliente {
    private String nome;
    private String cpf;
    ArrayList<Pedido> pedidos = new ArrayList<Pedido>();

    public Cliente(String nome, String cpf){
        this.nome=nome;
        this.cpf=cpf;
    }

   public void adicionar_pedido(Pedido pedido){
       this.pedidos.add(pedido);
   }

   public void mostrar_pedidos(){

       if(this.pedidos.isEmpty()){
           System.out.println("O cliente "+nome+" não possui pedidos");
           return;
       }

       System.out.print("Os pedidos do cliente são: ");
       for(int i=0;i<pedidos.size();i++){
           System.out.printf("\n\n%dº Pedido:",i+1);
           System.out.printf("\nNumero: %s",pedidos.get(i).getNumero());
           System.out.printf("\nValor: %.2f",pedidos.get(i).getValor());
       }
   }
}
