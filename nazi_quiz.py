import random
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class NaziGermanyQuiz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nazi Germany Test")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #222222;")

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

        self.title = QLabel("⚠️ Nazi Germany Historical Quiz ⚠️")
        self.title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.title.setStyleSheet("color: #DDDDDD;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)

        self.flag = QLabel("卍")
        self.flag.setFont(QFont("Arial", 64))
        self.flag.setStyleSheet("color: #DDDDDD;")
        self.flag.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.flag)

        self.prompt = QLabel("Do you want to be part of Nazi Germany? (yes/no)")
        self.prompt.setFont(QFont("Arial", 12))
        self.prompt.setStyleSheet("color: #DDDDDD;")
        self.layout.addWidget(self.prompt)

        self.answer_input = QLineEdit()
        self.answer_input.setFont(QFont("Arial", 12))
        self.answer_input.setStyleSheet("background-color: #444444; color: #DDDDDD;")
        self.layout.addWidget(self.answer_input)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.submit_btn.setStyleSheet("background-color: #DDDDDD; color: #222222; padding: 8px;")
        self.submit_btn.clicked.connect(self.handle_join_response)
        self.layout.addWidget(self.submit_btn)

        self.stage = "join"
        self.name = ""
        self.age = 0
        self.quiz_index = 0
        self.score = 0

        self.q_and_a = [
            ("What year did Hitler become Chancellor?\n(a) 1933\n(b) 1941\n(c) 1929", ["a", "1933"]),
            ("What book did Hitler write?\n(a) Mein Kampf\n(b) Das Kapital\n(c) The Art of War", ["a", "mein kampf"]),
            ("Was Nazi Germany a democracy? (yes/no)", ["no"]),
            ("What was the name of the Nazi secret police?\n(a) Gestapo\n(b) KGB\n(c) OSS", ["a", "gestapo"]),
            ("Which symbol did the Nazi Party use?\n(a) Swastika\n(b) Hammer and Sickle\n(c) Eagle", ["a", "swastika"]),
            ("What started WWII?\n(a) Invasion of Poland\n(b) Attack on Pearl Harbor\n(c) Fall of France", ["a", "invasion of poland"]),
            ("Which group was targeted in the Holocaust?\n(a) Jews\n(b) Soviets\n(c) Americans", ["a", "jews"]),
            ("Who led Nazi propaganda?\n(a) Joseph Goebbels\n(b) Heinrich Himmler\n(c) Hermann Göring", ["a", "joseph goebbels", "goebbels"]),
            ("Where was Hitler born?\n(a) Austria\n(b) Germany\n(c) Switzerland", ["a", "austria"]),
            ("What was the Third Reich?\n(a) Nazi Germany\n(b) Holy Roman Empire\n(c) British Empire", ["a", "nazi germany"])
        ]
        random.shuffle(self.q_and_a)

        self.setLayout(self.layout)

    def handle_join_response(self):
        answer = self.answer_input.text().strip().lower()
        if self.stage == "join":
            if answer == "yes":
                self.show_message("Ok lil bro!!! Welcome to Nazi Germany historical zone!")
                self.stage = "info_name"
                self.prompt.setText("Whats ur name lil dude?:")
                self.answer_input.clear()
            elif answer == "no":
                self.show_message("You dont wanna join? ok bye!")
                self.close()
            else:
                self.show_message("say 'yes' or 'no' only bro!")
                self.answer_input.clear()

        elif self.stage == "info_name":
            if answer.isalpha():
                self.name = answer.title()
                self.show_message(f"yo {self.name}! u in now")
                self.stage = "info_age"
                self.prompt.setText(f"how old u is, {self.name}?")
                self.answer_input.clear()
            else:
                self.show_message("ur name should be letters only, bruv")

        elif self.stage == "info_age":
            if answer.isdigit():
                self.age = int(answer)
                if self.age > 70:
                    self.show_message(f"bro u too old for this")
                    self.close()
                elif self.age < 17:
                    self.show_message("nah bro u too smol")
                    self.close()
                else:
                    self.show_message(f"aight {self.name}, now take da history quiz")
                    self.stage = "quiz"
                    self.quiz_index = 0
                    self.score = 0
                    self.show_next_question()
            else:
                self.show_message("yo type numbers only")

        elif self.stage == "quiz":
            self.check_answer(answer)

    def show_next_question(self):
        if self.quiz_index < len(self.q_and_a):
            question, _ = self.q_and_a[self.quiz_index]
            self.prompt.setText(f"Question {self.quiz_index + 1}:\n{question}")
            self.answer_input.clear()
        else:
            self.finish_quiz()

    def check_answer(self, answer):
        _, correct_answers = self.q_and_a[self.quiz_index]
        if answer in correct_answers:
            self.score += 1
            self.show_message("yooo that's right!")
        else:
            self.show_message("nopeeee wrong bro")
        self.quiz_index += 1
        self.show_next_question()

    def finish_quiz(self):
        min_pass = 6
        self.answer_input.setDisabled(True)
        self.submit_btn.setDisabled(True)
        self.prompt.setText(f"{self.name}, u scored {self.score} outta {len(self.q_and_a)}.")

        if self.score >= min_pass:
            self.show_message("gratz lil bro u passed history class!")
        else:
            self.show_message("nahhh failed, go study more")

        self.show_message("Updates comin soon... stay tuned for da next history lesson.")

    def show_message(self, text):
        msg = QMessageBox(self)
        msg.setWindowTitle("Nazi Germany History Test")
        msg.setText(text)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NaziGermanyQuiz()
    window.show()
    sys.exit(app.exec())
