package Projects.Project_One.Java;

import java.util.Scanner;

class ProjectOne03 {
    private static String getUserInput(String prompt) {
       Scanner inputScanner = new Scanner(System.in);
       System.out.printf("%s:\n> ", prompt);
       return inputScanner.nextLine();
    }

    static void printIntro() {
        System.out.println("Welcome, to checkerboard color guesser!");
        System.out.println("\nEnter a checkerboard coordinate and we'll tell you what color it is.");
        System.out.println("\nEnter a letter in range a(-h)");
        System.out.println("Enter a number in range 1(-8)");
        System.out.println("Coordinate a8 would be white");
    }

    static boolean inRange(char[] coordinate) {
        char letter = coordinate[0];
        char number = coordinate[1];

        var letterRange = "abcdefgh";
        var numberRange = "12345678";

        return letterRange.indexOf(letter) > -1 && numberRange.indexOf(number) > -1;
    }

    public static void main(String[] args) {
        printIntro();

        var coordinateInput = getUserInput("Input a coordinate value");
        char[] coordinate = coordinateInput.toCharArray();

        if (inRange(coordinate)) {
            String color = ((int) coordinate[0] + coordinate[1]) % 2 == 0 ? "Black" : "White";
            System.out.printf("You entered coordinate: %s\n", coordinateInput);
            System.out.printf("It's color on the checkboard is %s", color);
        } else {
            System.out.println("Invalid Coordinate Input.");
        }

    }
}
