class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_q = self.questions_list[self.question_number]
        self.check_answer(input(f"Q.{self.question_number + 1}: {current_q.text} (True/False)?"), current_q.answer)
        self.question_number += 1

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}.\n")
