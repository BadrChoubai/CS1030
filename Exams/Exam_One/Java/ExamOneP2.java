package Exams.Exam_One.Java;

public class ExamOneP2 {

    private static int mutationMath(int number) {
        var result = 0;
        var numberString = Integer.toString(number);

        for (int i = 1; i <= 3; i++) {
            result += Integer.parseInt(numberString);
            numberString += Integer.toString(number);
        }

        return result;
    }
    public static void main(String[] args) {
        /*
         * Write a function that takes a number and return a math equation mutating the
         * number Ex. number = 1; return 1 + 11 + 111 -> 123
         */

        mutationMath(1);
    }
}