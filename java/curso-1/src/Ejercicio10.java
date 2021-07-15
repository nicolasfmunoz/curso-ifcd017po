import java.util.Scanner;

public class Ejercicio10 {

	public static void main(String[] args) {
		Scanner input_scanner = new Scanner(System.in);
		
		System.out.println("Ingresa los numeros a sumar, separados por espacio:\n");
		String numeros = input_scanner.next();
		
		String[] array = numeros.split(" ");
		
		input_scanner.close();
		
		int suma = 0;
		for (String n : array) {
			
			suma += Integer.parseInt(n);
		}
		
		System.out.println(String.format("La suma de los numeros es %s.", suma));
	}
}
