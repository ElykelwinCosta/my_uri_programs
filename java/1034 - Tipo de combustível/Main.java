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
 
        /**
         * Escreva a sua solução aqui
         * Code your solution here
         * Escriba su solución aquí
         */
         
		    	Scanner leitor = new Scanner(System.in);
				int opcao = Integer.parseInt(leitor.nextLine());
				int alcool = 0;
				int gasolina = 0;
				int diesel = 0;
				while (opcao != 4) {
					if (opcao == 1) {
						alcool ++;
					} else if (opcao == 2) {
						gasolina ++;
					} else if (opcao == 3) {
						diesel ++;
					} 
					opcao = Integer.parseInt(leitor.nextLine());
				}
				System.out.println("MUITO OBRIGADO");
				System.out.println("Alcool: " +alcool);
				System.out.println("Gasolina: " +gasolina);
				System.out.println("Diesel: " +diesel);
				leitor.close();
 
    }
 
}