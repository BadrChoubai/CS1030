package Projects.Project_One.Java;

import java.util.Scanner;

class ProjectOne02 {
    private static Scanner inputScanner = new Scanner(System.in);

    private static String getUserInput(String prompt) {
        System.out.printf("%s:\n> ", prompt);
        var input = inputScanner.nextLine();
        return input;
    }

    public static void main(String[] args) {
        String milesInput = getUserInput("Miles travelled");
        String gallonsInput = getUserInput("Gallons of gas used");

        Integer miles = Integer.parseInt(milesInput);
        Integer gallons = Integer.parseInt(gallonsInput);

        var kilometers = (miles * 1.60934);
        var liters = (gallons * 3.7854);

        var milesPerGallon = (miles / gallons);
        var kilometersPerMile = (kilometers / miles);
        var gallonsPerLiter = (gallons / liters);
        var litersPerKilometer = 1 / (milesPerGallon * kilometersPerMile * gallonsPerLiter);

        System.out.printf("Miles per gallon: %d\nKilometers per liter: %.2f", milesPerGallon, litersPerKilometer);

    }
}
