import java.util.Scanner;

public class Ejercicio2 {

	public static void main(String[] args) {
		System.out.print("Ingresa el número a evaluar si es par o impar: ");
		Scanner input_scanner = new Scanner(System.in);

		int num = input_scanner.nextInt();		
		
		input_scanner.close();

		if (num % 2 == 0) {
			System.out.println(num + " es par");
		} else {
			System.out.println(num + " es impar");
		}
	}
}
