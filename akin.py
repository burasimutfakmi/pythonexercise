def newgame():
    guesses = []
    correct_guesses = 0
    questions_num = 1
    for key in questions:
        print(key)
        for i in answers[questions_num - 1]:
            print(i)
        guess = input("enter (A, B, C, D):")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += answer(questions.get(key),guess)
        questions_num += 1

    display_score(correct_guesses,guesses)


def answer(answer, guess):
    if answer == guess:
        print("You are correct")
        return 1
    else:
        print("You are wrong.")
        return 0
def display_score(correct_guesses,guesses):
    print("RESULTS")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your final score is " + str(score)+ "%")

def playagain():
    response = input("Do you wish to play again? Yes or No:")
    response = response.lower()


    if response == "yes":
        return True
    elif response == "no":
        print("goodbye")
        return False
    else:
        print("Please say yes or no")
        playagain()
questions = {"Who created the best AI?": "A",
             "Who is the best player on the earth?": "B",
             "Who is the leader of the band of the hawk?":"D"}

answers = [["A. Jacob Tagg","B. Izumi19", "C. Bot himself","D. Muzphius" ],
           ["A. Muzphius", "B. Pritok himself", "C. ThatOneYugo", "D. Viperdx"],
            ["A. Guts", "B. Casca", "C.Corkus", "D. Griffith"]]

newgame()

while playagain():
    newgame()

