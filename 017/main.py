#######################################
# CLASS PROJECT
# The Trivia Game OOP
#######################################

# Day 17 - The Trivia Game OOP  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp


from question_model import Question
from quiz_brain import QuizBrain
from lib import logo, clear
import requests, html

clear()
logo()

url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"
question_data = requests.get(url).json()
question_bank = []
for item in question_data["results"]:
    question_bank.append(
        Question(html.unescape(item["question"]), item["correct_answer"])
    )

quiz_brain = QuizBrain(question_bank)


while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the Quiz.")
print(f"Your final score was: {quiz_brain.score} / {quiz_brain.question_number}.")
