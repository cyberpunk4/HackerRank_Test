// Problem: https://www.hackerrank.com/challenges/java-bigdecimal
// Difficulty: Medium
// Score: 20

import java.math.BigDecimal;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String[] s = new String[n + 2];
		for (int i = 0; i < n; i++) {
			s[i] = sc.next();
		}
		sc.close();
		Arrays.sort(s, 0, n, new Comparator<String>() {

			@Override
			public int compare(String s1, String s2) {
				// this is for the ascending order
				// return new BigDecimal(s1).compareTo(new BigDecimal(s2));
				// this is for the descending order
				return new BigDecimal(s2).compareTo(new BigDecimal(s1));
			}
		});
		for (int i = 0; i < n; i++) {
			System.out.println(s[i]);
		}
	}
}
