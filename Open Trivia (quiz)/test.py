import requests
import html
from requests import *

parameter = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()

questions = response.json()

question_list = questions["results"]

print(question_list)  #question #correct_answer



class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer



class Quizbrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        if self.question_number < len(question_list):
            return True

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False)"

    def check_answer(self,user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score +=1
            return True
        else:
            False


q_list = []
for q in question_list:
    question_text = q['question']
    question_answer = q['correct_answer']
    question = Question(question_text,question_answer)
    q_list.append(question)

quiz = Quizbrain(q_list)
