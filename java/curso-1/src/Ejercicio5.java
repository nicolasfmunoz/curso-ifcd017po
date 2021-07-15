import java.util.Scanner;

public class Ejercicio5 {

	public static void main(String[] args) {
		Scanner input_scanner = new Scanner(System.in);
		
		System.out.print("Ingresa el dia de la semana para ver la programacion de TV:\n");
		String dia = input_scanner.next();
		
		input_scanner.close();
		
		String programa_tv = "";
		switch (dia.toLowerCase()) {
		case "lunes":
			programa_tv = "Midnight dinner";
			break;
		case "martes":
			programa_tv = "Lupin";
			break;
		case "miercoles", "miércoles":
			programa_tv = "Breaking Bad";
			break;
		case "jueves":
			programa_tv = "Death Note";
			break;
		case "viernes":
			programa_tv = "Old Boy";
			break;
		case "sabado", "sábado":
			programa_tv = "Contacto";
			break;
		case "domingo":
			programa_tv = "Dragon Ball Z";
			break;

		default:
			System.err.println("Ha itroducido un día de semana inválido");
			System.exit(1);
		}
		
		String mensaje = String.format("El programa para el día %s es: %s", dia, programa_tv);
		System.out.println(mensaje);
	}
}
