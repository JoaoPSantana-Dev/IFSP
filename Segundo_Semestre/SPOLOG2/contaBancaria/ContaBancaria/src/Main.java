import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ContaBancaria conta1 =
                new ContaBancaria(1001, "Ana", 1000);
        ContaBancaria conta2 =
                new ContaBancaria(1002, "Carlos", 2500);
        ContaBancaria conta3 =
                new ContaBancaria(1003, "Maria", 5000);
        ContaBancaria[] contas = {
                conta1,
                conta2,
                conta3
        };
        int opcao;
        do {
            System.out.println();
            System.out.println("=================================");
            System.out.println(" SISTEMA DE CONTAS BANCÁRIAS");
            System.out.println("=================================");
            System.out.println("1 - Listar contas");
            System.out.println("2 - Consultar conta");
            System.out.println("3 - Depositar");
            System.out.println("4 - Sacar");
            System.out.println("5 - Consultar saldo");
            System.out.println("0 - Sair");
            System.out.println("=================================");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            switch (opcao) {
                case 1:
                    listarContas(contas);
                    break;
                case 2:
                    System.out.print("Digite o número da conta: ");
                    int numeroConsulta = scanner.nextInt();
                    ContaBancaria contaConsulta =
                            buscarConta(contas, numeroConsulta);
                    if (contaConsulta != null) {
                        contaConsulta.exibirDados();
                    } else {
                        System.out.println("Conta não encontrada.");
                    }
                    break;
                case 3:
                    System.out.print("Digite o número da conta: ");
                    int numeroDeposito = scanner.nextInt();
                    ContaBancaria contaDeposito =
                            buscarConta(contas, numeroDeposito);
                    if (contaDeposito != null) {
                        System.out.print("Digite o valor do depósito: R$ ");
                        double valorDeposito = scanner.nextDouble();
                        contaDeposito.depositar(valorDeposito);
                        System.out.printf(
                                "Novo saldo: R$ %.2f%n",
                                contaDeposito.consultarSaldo()
                        );
                    } else {
                        System.out.println("Conta não encontrada.");
                    }
                    break;
                case 4:
                    System.out.print("Digite o número da conta: ");
                    int numeroSaque = scanner.nextInt();
                    ContaBancaria contaSaque =
                            buscarConta(contas, numeroSaque);
                    if (contaSaque != null) {
                        System.out.print("Digite o valor do saque: R$ ");
                        double valorSaque = scanner.nextDouble();
                        contaSaque.sacar(valorSaque);
                        System.out.printf(
                                "Saldo atual: R$ %.2f%n",
                                contaSaque.consultarSaldo()
                        );
                    } else {
                        System.out.println("Conta não encontrada.");
                    }
                    break;
                case 5:
                    System.out.print("Digite o número da conta: ");
                    int numeroSaldo = scanner.nextInt();
                    ContaBancaria contaSaldo =
                            buscarConta(contas, numeroSaldo);
                    if (contaSaldo != null) {
                        System.out.printf(
                                "Saldo da conta %d: R$ %.2f%n",
                                contaSaldo.getNumero(),
                                contaSaldo.consultarSaldo()
                        );
                    } else {
                        System.out.println("Conta não encontrada.");
                    }
                    break;
                case 0:
                    System.out.println("Sistema encerrado.");
                    break;
                default:
                    System.out.println("Opção inválida.");
            }
        } while (opcao != 0);
        scanner.close();
    }

    public static ContaBancaria buscarConta(
            ContaBancaria[] contas,
            int numero) {
        for (ContaBancaria conta : contas) {
            if (conta.getNumero() == numero) {
                return conta;
            }
        }
        return null;
    }
    public static void listarContas(ContaBancaria[] contas) {
        System.out.println();
        System.out.println("CONTAS CADASTRADAS");
        for (ContaBancaria conta : contas) {
            conta.exibirDados();
        }
    }


}





