package com.mycompany.atividade3_1;

import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Informe os dados da conta empresa: ");
        System.out.print("Número da conta: ");
        int numeroConta = sc.nextInt();
        sc.nextLine();
        System.out.print("Nome do Titular: ");
        String nomeTitular = sc.nextLine();
        System.out.print("Saldo Inicial: ");
        double saldoInicial = sc.nextDouble();
        System.out.print("Limite de Empréstimo: ");
        double limiteEmprestimo = sc.nextDouble();

        Conta_Empresa contaEmpresa = new Conta_Empresa(limiteEmprestimo, numeroConta, nomeTitular, saldoInicial);

        // Agora você pode usar os métodos da classe Conta_Empresa
        sc.close();
    }
}
