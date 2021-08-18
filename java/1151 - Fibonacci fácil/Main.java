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
    	String sequence = "";
    	if (N == 0) {
    		System.out.println("0");
    	} else if (N == 1) {
    		System.out.println("0 1");
    	} else {
    		int penultimo = 0;
    		int ultimo = 1;
    		System.out.printf("0 1 ");
    		for (int k = 2; k < N; k++) {
    			int atual = penultimo + ultimo;
    			if (k == (N - 1)) {
    				sequence += atual;	
    			} else {
    				sequence += atual + " ";
    			}
    			penultimo = ultimo;
    			ultimo = atual;
    		}
    
    	}
    	System.out.println(sequence);
    	leitor.close();
    }
 
}