

Questions =[
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin","D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English","D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3","D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To kill a MockingBird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling","D. Ernest Heningway"],
        "answer": "A"
    }
]

def run_quiz(Questions):
    score = 0
    for Question in Questions:
        print(Question["prompt"])
        for option in Question["options"]:
            print(option)

        UserAnswer = input("Enter your answer ")
        print("\n")
        if Question["answer"] == UserAnswer :
           score =score + 1
           print("Correct")
           print("\n")
        else:
            print("Wrong")
            print("\n") #well done

    print(f"{score} out of {len(Questions)}")

run_quiz(Questions)





