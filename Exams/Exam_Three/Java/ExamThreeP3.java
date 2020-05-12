package Exams.Exam_Three.Java;

import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;

public class ExamThreeP3 {
    private static Scanner inputScanner = new Scanner(System.in);
    private static Map<Character, Integer> charactersInInput = new HashMap<Character, Integer>();

    public static void main(String[] args) {
        System.out.println("Give me a word or phrase: ");
        String string = inputScanner.nextLine();

        for (char character : string.toCharArray()) {
            if (Character.isLetter(character)) {
                if (charactersInInput.containsKey(character)) {
                    int currentValue = charactersInInput.get(character);
                    charactersInInput.put(character, currentValue + 1);
                } else {
                    charactersInInput.put(character, 1);
                }
            }
        }

        System.out.printf("Unique Characters in input: %d\n", charactersInInput.keySet().size());
        System.out.println("Character Dictionary\n" + charactersInInput);
    }
}