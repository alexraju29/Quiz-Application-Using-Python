from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
score = 0
questions = 0


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        global score
        global questions
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_board = Label(text=f"Score: {score}/{questions}", fg="white", bg=THEME_COLOR)
        self.score_board.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        check_image = PhotoImage(file="images/true.png")
        cross_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=check_image, command=self.true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=cross_image, command=self.false)
        self.false_button.grid(row=2, column=1)
        if self.quiz.network_error():
            self.disable_switch()
        self.next_question()
        self.window.mainloop()

    def true(self):
        answer = self.quiz.check_answer("True")
        self.feedback(answer)

    def false(self):
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You' ve reached the end of the quiz\n"
                                                            f"Score={score}/{questions}")
            self.disable_switch()

    def feedback(self, answer):
        global score
        global questions
        if answer:
            score = score + 1
            questions = questions + 1
            self.score_board.config(text=f"Score: {score}/{questions}")
            self.canvas.config(bg="green")

        else:
            questions = questions + 1
            self.score_board.config(text=f"Score: {score}/{questions}")
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

    def disable_switch(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
