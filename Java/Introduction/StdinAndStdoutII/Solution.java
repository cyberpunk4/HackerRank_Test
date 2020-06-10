package introduction;

import java.util.Scanner;

public class StdinAndStdoutII {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int i = scan.nextInt();
		double d = scan.nextDouble();
		scan.nextLine();
		String s = scan.nextLine();
		scan.close();
		System.out.println("String: " + s + "\nDouble: " + d + "\nInt: " + i);
	}
}
