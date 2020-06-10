package bignumber;

import java.math.BigInteger;
import java.util.Scanner;

public class BigIntegerDemo {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		BigInteger n1 = new BigInteger(s.nextLine());
		BigInteger n2 = new BigInteger(s.nextLine());
		System.out.println(n1.add(n2));
		System.out.println(n1.multiply(n2));
		s.close();
	}
}
