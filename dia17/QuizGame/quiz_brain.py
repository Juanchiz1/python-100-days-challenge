
class Quiz_Brain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score =0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print("Question number: ", self.question_number)
        print(current_question.text)
        answer = input("(True/False): ")
        self.check_answer(answer,current_question.answer)

    def check_answer(self,answer,correct_answer):
        if answer.upper() ==correct_answer.upper():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
