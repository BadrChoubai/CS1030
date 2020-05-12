#!/bin/bash
for i in {1..3}
do 

    {
    echo "package Exams.Exam_Two.Java;\n"
    echo "public class ExamTwoP$i {"
    echo "\tpublic static void main(String[] args) {}"
    echo "}"
    } >> ExamTwoP$i.java
done