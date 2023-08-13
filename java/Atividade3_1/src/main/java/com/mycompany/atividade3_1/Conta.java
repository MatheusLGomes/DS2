package com.mycompany.atividade3_1;

public class Conta {

    private int numero;
    private String titutar;
    protected double saldo;

    public Conta(int numero, String titutar, double saldo) {
        this.numero = numero;
        this.titutar = titutar;
        this.saldo = 0.0;
    }

    public void deposito(double montante) {
        saldo += montante;
    }

    public void saque(double montante) {
        if (montante <= saldo) {
            saldo -= montante;
        } else {
            System.out.println("Saldo insuficiente");
        }

    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getTitutar() {
        return titutar;
    }

    public void setTitutar(String titutar) {
        this.titutar = titutar;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

}


