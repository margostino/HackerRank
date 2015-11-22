package Algorithms;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Diwali_Lights {
	private static BufferedReader in = new BufferedReader(
			new InputStreamReader(System.in));
	
	public static void main(String[] args) throws NumberFormatException,
	Exception {
		int T = Integer.parseInt(in.readLine());

		while (T-- > 0) {
			long noOfBulbs = Long.parseLong(in.readLine());
			System.out.println(ExponentBySquare(2, noOfBulbs).toString());
		}

		in.close();
	}

	private static BigInteger ExponentBySquare(long x, long n) {
		BigInteger big = BigInteger.valueOf(x).pow((int) n)
				.subtract(BigInteger.ONE).mod(new BigInteger("100000"));

		return big;
	}
}
