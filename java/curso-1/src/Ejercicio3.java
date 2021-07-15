import java.util.Scanner;

public class Ejercicio3 {

	public static void main(String[] args) {
		Scanner input_scanner = new Scanner(System.in);
		
		System.out.print("Ingresa el primer numero a comparar: ");
		int num_1 = input_scanner.nextInt();

		System.out.print("Ingresa el segundo numero a comparar: ");
		int num_2 = input_scanner.nextInt();
		
		input_scanner.close();

		int num_mayor = 0;

		if (num_1 > num_2) {
			num_mayor = num_1;
		} else if (num_1 < num_2) {
			num_mayor = num_2;
		} else {
			System.out.println("Ambos números son iguales.");
			System.exit(0);
		}
		
		System.out.println(num_mayor + " es el número mayor.");
	}
}
