package Projects.Project_One.Java;

import java.util.Scanner;

class ProjectOne01 {
    private static Scanner inputScanner = new Scanner(System.in);

    private static String getUserInput(String prompt) {
        System.out.printf("%s:\n> ", prompt);
        var input = inputScanner.nextLine();
        return input;
    }

    public static void main(String[] args) {
        String feetInput = getUserInput("Feet");
        String inchesInput = getUserInput("Inches");
        var heightString = String.format("%s'%s\"", feetInput, inchesInput);

        var feet = Integer.parseInt(feetInput);
        var inches = Integer.parseInt(inchesInput);

        var total = (feet * 12) + inches;

        if (total >= 95) {
            System.out.println("Wow! You're so tall");
        } else {
            var centimeters = total * 2.54;
            var meters = centimeters / 100;

            System.out.printf("Original height input %s, to meters: %.2fm", heightString, meters);
        }
    }
}
