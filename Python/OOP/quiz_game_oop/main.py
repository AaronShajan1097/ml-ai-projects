from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
#[<question_model.Question object at 0x000001B966796A50>, <question_model.Question object at 0x000001B966A14A50>, <question_model.Question object at 0x000001B966A14B90>, <question_model.Question object at 0x000001B966809E00>, <question_model.Question object at 0x000001B96680A8B0>, <question_model.Question object at 0x000001B9667C7890>, <question_model.Question object at 0x000001B9667EFDF0>, <question_model.Question object at 0x000001B966A0C160>, <question_model.Question object at 0x000001B9669EC850>, <question_model.Question object at 0x000001B9669EC650>, <question_model.Question object at 0x000001B9667FBB60>, <question_model.Question object at 0x000001B9667FBD40>]
]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    if not quiz.next_question():
        break

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")