import random

questions= [{'question': "Which planet in our solar system is the absolute hottest?", 'answer': 'venus'}, 
            {'question': 'What was the very first commercial item ever scanned with a barcode in a store?','answer': 'wrigley gum'},
            {'question': 'Historical records show that frozen milk and rice mixtures were first invented as early as 200 BC in which country?', 'answer': 'china'},
            {'question':"which author wrote the book 'Metamorphosis'?", 'answer': "franz kafka"},
            {'question':"Who is the main character of the show 'Mentalist?'", 'answer':"patrick jane"}]

def quiz():
    num= int(input("enter the number of questions you want to give from 1-5: "))
    if num<1 or num> len(questions):
        print("invalid input! please try again")
        return
    selected_questions = random.sample(questions, num)

    for q in selected_questions:
        print("\n" + q['question'])
        answer = input("Your answer: ").strip().lower()

        if answer == q['answer']:
            print("Correct!")
        else:
            print("Incorrect!")
            print("Correct answer:", q['answer'])


while True:
    print("WELCOME TO THE QUIZ SESSION!")
    print("1. start the quiz")
    print("2. exit the quiz")

    try:
        user= int(input("enter the option you want to do: "))

    except ValueError:
        print("try again dear! it is an invalid input")
        continue
    
    if user == 1:
        quiz()
    elif user == 2:
        break
    else:
        print("invalid input, try again dear!")