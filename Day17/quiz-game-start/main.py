from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(text=question["text"], answer=question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You have done with the quiz, your score is {quiz.score} / {len(quiz.question_list)}")
