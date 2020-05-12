package Exams.Exam_One.Java;

import java.util.Map;
import java.util.HashMap;

public class ExamOneP3 {

    private static class Coin {
        public String name;
        public int value;

        Coin(String name, int value) {
            this.name = name;
            this.value = value;
        }
    }

    static Coin quarter = new Coin("quarter", 25);
    static Coin dime = new Coin("dime", 10);
    static Coin nickel = new Coin("nickel", 5);
    static Coin penny = new Coin("penny", 1);
    static Coin[] coins = { quarter, dime, nickel, penny };

    private static Map<String, Integer> makeChange(int cents) {
        Map<String, Integer> counter = new HashMap<>();
        for (Coin coin : coins) {
            counter.put(coin.name, 0);
        }

        for (Coin coin : coins) {
            while (cents - coin.value >= 0) {
                counter.put(coin.name, counter.get(coin.name) + 1);
                cents -= coin.value;
            }
        }

        return counter;
    }

    public static void main(String[] args) {
        Map<String, Integer> solution = makeChange(99);
        System.out.println(solution);
    }
}