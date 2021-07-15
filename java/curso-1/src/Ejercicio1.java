import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		System.out.print("Enter number to pow: ");
		Scanner input_scanner = new Scanner(System.in);

		double num = input_scanner.nextDouble();		
		input_scanner.close();

		double result = getPow(num, 2);
		System.out.println(String.format("The result is: %s", result));
	}
	
	private static double getPow(double num, int pow) {
		return Math.pow(num, pow);
	}
}
