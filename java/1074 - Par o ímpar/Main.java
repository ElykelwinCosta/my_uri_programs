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
		for ( int k = 0; k < N; k++) {
			int numero = Integer.parseInt(leitor.nextLine());
			if (numero == 0) {
				System.out.println("NULL");
			} else if (numero % 2 == 0 && numero > 0) {
				System.out.println("EVEN POSITIVE");
			} else if (numero % 2 != 0 && numero > 0) {
				System.out.println("ODD POSITIVE");
			} else if (numero % 2 == 0 && numero < 0) {
				System.out.println("EVEN NEGATIVE");
			} else if (numero % 2 != 0 && numero < 0) {
				System.out.println("ODD NEGATIVE");
			}
		}
		leitor.close();
 
    }
 
}