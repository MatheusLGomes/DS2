package aplicacao;

import entidades.Produto;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        Produto produto = new Produto();
        
        System.out.println("Informe os dados do produto: ");
        System.out.print("Nome: ");
        produto.setNome(scanner.nextLine());
        
        System.out.print("Preço: ");
        produto.setPreco(scanner.nextDouble());
        
        System.out.print("Quantidade de Estoque: ");
        produto.setQuantidade(scanner.nextInt());
        
        // Mostrar informações iniciais do produto
        System.out.println("\nDados do Produto:");
        mostrarDadosProduto(produto);
        
        // Realizar entrada no estoque
        System.out.print("\nInforme a quantidade de entrada no estoque: ");
        int entrada = scanner.nextInt();
        produto.addProduto(entrada);
        System.out.println("Entrada realizada no estoque.");
        mostrarDadosProduto(produto);
        
        // Realizar saída no estoque
        System.out.print("\nInforme a quantidade de saída no estoque: ");
        int saida = scanner.nextInt();
        produto.removerProduto(saida);
        System.out.println("Saída realizada no estoque.");
        mostrarDadosProduto(produto);
        
        scanner.close();
    }
    
    // Método para mostrar os dados do produto
    public static void mostrarDadosProduto(Produto produto) {
        System.out.println("Nome: " + produto.getNome());
        System.out.println("Preço: " + produto.getPreco());
        System.out.println("Quantidade em estoque: " + produto.getQuantidade());
        System.out.println("Valor total em estoque: " + produto.totalEstoque());
    }
}