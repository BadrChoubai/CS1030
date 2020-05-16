package Exams.Exam_Three.Java;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class ExamThreeP2 {
    private static Scanner inputScanner = new Scanner(System.in);

    public static void main(String[] args) {
        var items = new ArrayList<String>();
        var item = "";
        do {
            System.out.println("Input a Word: ");
            item = inputScanner.nextLine();

            if (item.isEmpty()) {
                break;
            }

            items.add(item);

            if (items.size() == 1) {
                System.out.println(items.get(0));
            } else {
                List<String> segmentedList = items.subList(0, items.size() - 1);
                System.out.printf("%s and %s",
                        segmentedList.toString().replace("[", "").replace("]", ""),
                        items.get(items.size() - 1));
            }
        } while (!item.isEmpty());
        inputScanner.close();
    }
}