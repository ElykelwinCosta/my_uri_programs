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
    	int[] vetores = new int[10];
    	for (int k = 0; k < 10; k++) {
    		int i = Integer.parseInt(leitor.nextLine());
    		if (i <= 0) {
    			vetores[k] = 1;
    		} else {
    			vetores[k] = i;
    		}
    	}
    	for (int z = 0; z < vetores.length; z++) {
    		System.out.println("X["+z+"] = " +vetores[z]  );
    	}
    	leitor.close();
    }
 
}