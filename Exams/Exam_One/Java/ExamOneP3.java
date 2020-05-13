package Exams.Exam_One.Java;

import java.util.Map;
import java.util.HashMap;

public class ExamOneP3 {

    enum ECoin {
        Quarter(25),
        Dime(10),
        Nickel(5),
        Penny(1);

        final int value;

        ECoin(int value) {
            this.value = value;
        }
    }

    private static Map<ECoin, Integer> makeChange(int cents) {
        var change = new HashMap<ECoin, Integer>();

        for (var coin : ECoin.values()) {
            while (cents - coin.value >= 0) {
                change.put(coin, change.getOrDefault(coin, 0) + 1);
                cents -= coin.value;
            }
        }

        return change;

    }

    public static void main(String[] args) {
        Map<ECoin, Integer> solution = makeChange(99);
        System.out.println(solution);
    }
}