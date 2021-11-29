from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for datum in question_data:
    question_bank.append(Question(datum["text"], datum["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{len(quiz.questions_list)}")
