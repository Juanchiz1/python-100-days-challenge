from dia17.QuizGame import quiz_brain
from question_model import Question
from data import question_data
from quiz_brain import  Quiz_Brain
q={}
question_bank=[]
for question in question_data :
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz=Quiz_Brain(question_bank)

while(quiz.still_has_question()):
    quiz.next_question()

print("You've completed the quiz!!!")
print(f"The final score was {quiz.score}/{len(question_bank)}")

