
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.question_number += 1
        current_question = self.question_list[self.question_number]
        user_answer = ""
        while user_answer.lower() !="true" and user_answer.lower() !="false":
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self): 
        if self.question_number == len(self.question_list):
            return False
        else:
            return True
        
    def check_answer(self,user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score+=1
            print("You got it right!")
        else:
            print(f"The correct answer was: {question_answer.lower()}")

        print(f"Your current score is {self.score}/{self.question_number}")
        