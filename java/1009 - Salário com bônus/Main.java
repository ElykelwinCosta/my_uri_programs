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
		String nome = leitor.nextLine();
		Double fixo = Double.parseDouble(leitor.nextLine());
		Double vendas = Double.parseDouble(leitor.nextLine());
		Double valorReceber = fixo + (vendas * 0.15);
		System.out.printf("TOTAL = R$ %.2f\n", valorReceber);
		leitor.close();
 
    }
 
}