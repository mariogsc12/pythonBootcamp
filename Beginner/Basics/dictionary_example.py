"""
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 
Write a program that converts their scores to grades.

By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 

The final version of the student_grades dictionary will be checked. 

This is the scoring criteria: 
- Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable" 
- Scores 70 or lower: Grade = "Fail" 
"""

def calculate_grade(score):
    if score>100:
        print("ERROR - Invalid score")
    elif score>=91 and score<=100:
        return "Outstanding"
    elif score>=81 and score<=90:
        return "Exceeds Expectations"
    elif score>=71 and score<=80:
        return "Acceptable"
    elif score<=70:
        return "Fail"

def create_grade_dictionary(student_scores):
    student_grades = {}
    for student in student_scores:
        student_grades[student]=calculate_grade(student_scores[student])
        
    return student_grades

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = create_grade_dictionary(student_scores)
print(student_grades)