import java.io.IOException;
import java.util.Scanner;

/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
    	Scanner leitor = new Scanner(System.in);
    	int N = Integer.parseInt(leitor.nextLine());
    	String X = leitor.nextLine();
    	String[] numeros = X.split(" ");
    	int valorMenor = 1000000000;
    	int posicao = 1000000000;
    	for (int k = 0; k < N; k++) {
    		int valor = Integer.parseInt(numeros[k]);
    		if (valor < valorMenor) {
    			valorMenor = valor;
    			posicao = k;
    		}
    	}
    	//Menor valor: -5
    	//Posicao: 4
    	System.out.println("Menor valor: " +valorMenor+ "\n"
    					+  "Posicao: " +posicao);
    	leitor.close();
    }
}