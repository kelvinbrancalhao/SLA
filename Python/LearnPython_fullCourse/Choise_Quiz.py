from questions import Question

questions_prompt = [
    "What color are apples?\n (a) Red\n (b) Purple\n (c) Yellow\n\n",
    "What color are Bananas?\n (a) Red\n (b) Purple\n (c) Yellow\n\n",
    "What color are Blueberrys?\n (a) Red\n (b) Blue\n (c) Yellow\n\n"
]

questions_array = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "c")
]

def run_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.resposta:
            score = score+1

    print("Você acertou " + str(score) + "/" + str(len(questions)) + " Parabéns ")


run_questions(questions_array)
