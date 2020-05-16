package Exams.Exam_Two.Java;

import java.util.Scanner;
import java.util.ArrayList;

public class ExamTwoP1 {
	private static Scanner inputScanner = new Scanner(System.in);

	public static void main(String[] args) {
		var numbers = new ArrayList<Double>();
		boolean using = true;
		double sum = 0;
		double average = 0;

		do {
			System.out.println("Give me a number: ");
			double numberInput = inputScanner.nextDouble();

			if (numberInput != 0.0) {
				numbers.add(numberInput);
			} else {
				sum = numbers.stream().reduce(0.0, Double::sum); // Method Reference
				average = sum / numbers.size();
				using = false;
			}
		} while (using);

		System.out.printf("Sum of all numbers: %.2f\n", sum);
		System.out.printf("Calculated average: %.2f\n", average);
	}
}
