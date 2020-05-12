package Exams.Exam_Three.Java;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ExamThreeP2 {
    private static Scanner inputScanner = new Scanner(System.in);
    private static List<String> items = new ArrayList<String>();
    public static void main(String[] args) {
        String item = "";
        do {
            System.out.println("Enter an item: ");
            item = inputScanner.nextLine();
            
            if (item.isEmpty()) {
                break;
            } 
            
            items.add(item);

            if (items.size() == 1) {
                System.out.println(items.get(0));
            } else {
                List<String> segmentedList = items.subList(0, items.size() - 1);
                System.out.printf("%s and %s\n", segmentedList, items.get(items.size() - 1));
            }

        } while (!item.isEmpty());
        inputScanner.close();
    } 
}