public class ContaBancaria {
    private int numero;
    private String titular;
    private double saldo;

    public ContaBancaria(int numero, String titular, double saldoInicial) {
        this.numero = numero;
        this.titular = titular;
        if (saldoInicial >= 0) {
            this.saldo = saldoInicial;
        } else {
            this.saldo = 0;
        }
    }
    public void depositar(double valor) {
        if (valor > 0) {
            saldo = saldo + valor;
            System.out.println("Depósito realizado com sucesso.");
        } else {
            System.out.println("Erro: o valor do depósito deve ser maior que zero.");
        }
    }

    public boolean sacar(double valor) {
        if (valor <= 0) {
            System.out.println("Erro: o valor do saque deve ser maior que zero.");
            return false;
        }
        if (valor > saldo) {
            System.out.println("Erro: saldo insuficiente.");
            return false;
        }
        saldo = saldo - valor;
        System.out.println("Saque realizado com sucesso.");
        return true;
    }
    public double consultarSaldo() {
        return saldo;
    }
    public void exibirDados() {
        System.out.println("-----------------------------");
        System.out.println("Número da conta: " + numero);
        System.out.println("Titular: " + titular);
        System.out.printf("Saldo: R$ %.2f%n", saldo);
        System.out.println("-----------------------------");
    }
    public int getNumero() {
        return numero;
    }
    public String getTitular() {
        return titular;
    }
}

