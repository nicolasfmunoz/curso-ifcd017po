import java.util.Scanner;

public class Ejercicio9 {

	public static void main(String[] args) {
		Scanner input_scanner = new Scanner(System.in);
		
		System.out.println("Ingresa el numero para calcular el factorial:\n");
		int num = input_scanner.nextInt();
		
		input_scanner.close();
		
		int factorial = 1;
		for (int n = factorial; n <= num; n++) {
			
			factorial *= n;
		}
		
		System.out.println(String.format("El factorial de %s es %s.", num, factorial));
	}
}
