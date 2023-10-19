quiz = {
    "question1": {
        "question" : "What is Capital of France?",
        "answer": "Paris"
    },
     "question2": {
        "question" : "What is Capital of Germany?",
        "answer": "Berlin"
    },
     "question3": {
        "question" : "What is Capital of Iran?",
        "answer": "Tehran"
    },
     "question4": {
        "question" : "What is Capital of Italy?",
        "answer": "Rome"
    },
     "question5": {
        "question" : "What is Capital of Spain?",
        "answer": "Madrid"
    },
}

score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input("Please Write Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score = score + 1
        print("Your Score is " + str(score))

    else:
        print('Wrong!')
        print("The Correct Answer is " + value['answer'])
        print("Your Score is " + str(score))
        print("")
        print("")


print("You got" + str(score) + " Out of 5 questions correctly")
print(" Your Percantage is " + str(score / 5 * 100) + "%")