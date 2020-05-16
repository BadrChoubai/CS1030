package Exams.Exam_One.Java;

import java.util.Scanner;

public class ExamOneP1 {
    public static void main(String[] args) {
        /*
         * Ask a user for two numbers Calculate the Average, Product, and Sum of the two
         * numbers
         */
        Scanner inputScanner = new Scanner(System.in);

        System.out.println("Give me a number: ");
        int numOne = inputScanner.nextInt();
        System.out.println("Give me another number: ");
        int numTwo = inputScanner.nextInt();

        inputScanner.close();

        int average = (numOne + numTwo) / 2;
        int product = numOne / numTwo;
        int sum = numOne + numTwo;

        System.out.printf("Average: %d\n", average);
        System.out.printf("Product: %d\n", product);
        System.out.printf("Sum: %d\n", sum);
    }
}