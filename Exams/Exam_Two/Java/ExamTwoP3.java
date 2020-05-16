package Exams.Exam_Two.Java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.HashMap;

public class ExamTwoP3 {
	public static void main(String[] args) throws FileNotFoundException {
		var file = new File("ZipAndCity.txt");
		var inputScanner = new Scanner(file);
		var zipCodes = new HashMap<String, String>();

		while (inputScanner.hasNextLine()) {
			String line = inputScanner.nextLine();
			int delineatorIndex = line.indexOf(',');
			zipCodes.put((line.substring(0, delineatorIndex - 1)),
					line.substring(delineatorIndex + 1, line.length() - 1));
		}

		inputScanner.close();
		System.out.println(zipCodes);
	}
}
