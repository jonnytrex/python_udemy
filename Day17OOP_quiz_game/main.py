from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# write a for loop to iterate over the question_data
# create a Question object from each entry in question_data
# append each Question object to the question_bank


question_bank = [

]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print(f"Your final score is {quiz.current_score}/{quiz.question_number}")


