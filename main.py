from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for key in question_data:
    question_text = key["question"]
    question_answer = key["correct_answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quizbrain = QuizBrain(question_bank)

quizbrain.next_question()

while quizbrain.still_has_questions():
    quizbrain.next_question()

print("You have completed the quiz")
print(f"Your final score is: {quizbrain.score}/{quizbrain.question_number} ")
