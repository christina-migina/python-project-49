from brain_games.cli import welcome_user
from random import randint


def get_answer():
    number1, number2 = randint(1, 100), randint(1, 100)
    print(f"Question: {number1} {number2}")
    player_answer = input("Your answer: ")
    correct_answer = correct_answer = get_result(number1, number2)
    return player_answer, correct_answer


def get_result(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2


def is_answer_correct(player_answer, correct_answer):
    try:
        return int(player_answer) == correct_answer
    except ValueError:
        return False


def gcd_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
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
