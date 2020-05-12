package Exams.Exam_Two.Java;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ExamTwoP2 {
	public static void main(String[] args) {
		List<Integer> lotto = new ArrayList<Integer>(6);
		Random numberGenerator = new Random();

		for (int i = 0; i < 6; i++) {
			int randInt = numberGenerator.nextInt(49);
			while (lotto.contains(randInt)) {
				randInt = numberGenerator.nextInt(49 - 1 + 1) + 1; // https://stackoverflow.com/questions/20389890/generating-a-random-number-between-1-and-10-java
			}

			lotto.add(randInt);
		}
		System.out.println(lotto);
	}
}
