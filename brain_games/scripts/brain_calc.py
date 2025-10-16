from brain_games.cli import welcome_user
from random import randint, choice


def get_answer():
    number1, number2 = randint(1, 100), randint(1, 100)
    sign = choice(["-", "+", "*"])
    print(f"Question: {number1} {sign} {number2}")
    player_answer = input("Your answer: ")
    correct_answer = get_result(number1, number2, sign)
    return player_answer, correct_answer


def get_result(number1, number2, sign):
    if sign == "+":
        return number1 + number2
    if sign == "-":
        return number1 - number2
    if sign == "*":
        return number1 * number2


def is_answer_correct(player_answer, correct_answer):
    try:
        return int(player_answer) == correct_answer
    except ValueError:
        return False


def calc_game():
    name = welcome_user()
    print("What is the result of the expression?")
    counter = 0

    while counter < 3:
        player_answer, correct_answer = get_answer()

        if is_answer_correct(player_answer, correct_answer):
            print("Correct!")
            counter += 1
        else:
            print(
                f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")
