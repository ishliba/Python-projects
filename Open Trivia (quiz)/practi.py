s = "abcabc"
string = ((s+s)[1:-1])
print(string)
print(string.find(s))


class Question():

    def __init__(self,q_text,q_answer):
        self.text = q_text
        self.answer = q_answer

question_bank = []

for item in question_data:
    question = html.unescape(item['question'])
    answer = item['correct_answer']
    next_question = Question(question,answer)
    question_bank.append(next_question)


class Quiz_brain():

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = self.current_question.text
        return f" {self.question_number}:{q_text} TRUE/FALSE"
