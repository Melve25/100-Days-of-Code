class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} "
              f"(True/False)?: ")
        self.check_answer(answer, self.question_list[self.question_number])
        self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question):
        if user_answer.lower() == question.answer.lower():
            self.score += 1
            print(f"You got it right -> your score is {self.score} / {len(self.question_list)}")
        else:
            print(f"Wrong answer -> your score is {self.score} / {len(self.question_list)}")

