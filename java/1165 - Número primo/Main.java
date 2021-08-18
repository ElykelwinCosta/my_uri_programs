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
    	int N = leitor.nextInt();
    	for (int k = 0; k < N; k++) {
    		int X = leitor.nextInt();
    		boolean ehPrimo = true;
    		for (int y = 2; y < X; y++) {
    			if (X % y == 0) {
    				ehPrimo = false;
    				break;
    			}
    		}
    		if (ehPrimo == true) {
    			System.out.println(X + " eh primo");
    		} else {
    			System.out.println(X + " nao eh primo");
    		}
    			
    	}
    	leitor.close();
    }
 
}