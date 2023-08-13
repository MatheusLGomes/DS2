package com.mycompany.atividade3_1;

public class Conta_Empresa extends Conta {

    private double limiteEmprestimo;

    public Conta_Empresa(double limiteEmprestimo, int numero, String titular, double saldo) {
        super(numero, titular, saldo);
        this.limiteEmprestimo = limiteEmprestimo;
    }

    public void realizarEmprestimo(double valor) {
        if (valor <= limiteEmprestimo) {
            saldo += valor;
            limiteEmprestimo -= valor;
        } else {
            System.out.println("Limite de empréstimo excedido.");
        }
    }
}
