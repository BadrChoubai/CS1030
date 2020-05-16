package Exams.Exam_Three.Java;

import java.util.Arrays;
import java.util.Scanner;

public class ExamThreeP1 {
    private static Scanner inputScanner = new Scanner(System.in);
    private static String[] months = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"};
    private static String[] days = {"31", "28 or 29 days", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"};

    public static void main(String[] args) {

        System.out.println("Enter a month of the year:");
        var monthInput = inputScanner.nextLine();
        var searchIndex = Arrays.asList(months).indexOf(monthInput);

        System.out.printf("There are %s days in %s", days[searchIndex], monthInput);
    }
}