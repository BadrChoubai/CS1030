package Exams.Exam_Two.Java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class ExamTwoP3 {
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File("ZipAndCity.txt");
		System.out.printf("File Exists: %s\n", file.exists());
		Scanner scan = new Scanner(file);
		Map<String, String> zipCodes = new HashMap<>();

		while (scan.hasNextLine()) {
			String line = scan.nextLine();
			int delineatorChar = line.indexOf(',');
			zipCodes.put((line.substring(0, delineatorChar - 1)),
					line.substring(delineatorChar + 1, line.length() - 1));
		}

		scan.close();
		System.out.println(zipCodes);
	}
}
