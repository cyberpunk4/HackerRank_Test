package bignumber;

import java.math.BigInteger;
import java.util.Scanner;

public class PrimalityTest {
	private static final Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.println(new BigInteger(scanner.nextLine()).isProbablePrime(1000) ? "prime" : "not prime");
		scanner.close();
	}
}
