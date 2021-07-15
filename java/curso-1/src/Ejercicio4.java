import java.util.Scanner;

public class Ejercicio4 {

	public static void main(String[] args) {
		Scanner input_scanner = new Scanner(System.in);
		
		System.out.print("Ingresa el numero a verificar: ");
		int num = input_scanner.nextInt();
		
		input_scanner.close();
		
		String numString = Integer.toString(num, 0);
		
		if (numString.endsWith("1") && (1 <= num && num <= 1000)) {
			System.out.println("El número termina en 1 y está entre 1 y 1000.");
		} else {
			System.out.println("El número ingresado no cumple con las condiciones.");
		}
	}
}
