import java.util.Scanner;

public class Ejercicio7 {

	public static void main(String[] args) {
		Scanner input_scanner = new Scanner(System.in);
		
		System.out.println("Ingresa el texto:");
		String texto = input_scanner.nextLine();
		
		input_scanner.close();
		
		System.out.println("\nUsando while");
		int limite = texto.length();
		int contador = 0;
		while (contador < limite) {
			System.out.println(texto.charAt(contador));
			contador++;
		}
		
		System.out.println("\nUsando for");
		for (int i = 0; i < texto.length(); i++) {
			System.out.println(texto.charAt(i));
		}

		System.out.println("\nUsando for-each");
		for (char letra : texto.toCharArray()) {
			System.out.println(letra);
		}
	}
}
