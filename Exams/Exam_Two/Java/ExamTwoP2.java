package Exams.Exam_Two.Java;

import java.util.ArrayList;
import java.util.Random;

public class ExamTwoP2 {
	public static void main(String[] args) {
		var lottoNums = new ArrayList<>(6);
		var numberGenerator = new Random();

		for (int i = 0; i < 6; i++) {
			var randInt = numberGenerator.nextInt(49);
			while (lottoNums.contains(randInt)) {
				randInt = numberGenerator.nextInt(49 - 1 + 1) + 1; // https://stackoverflow.com/questions/20389890/generating-a-random-number-between-1-and-10-java
			}

			lottoNums.add(randInt);
		}
		System.out.println(lottoNums);
	}
}
