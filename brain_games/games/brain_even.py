from brain_games.cli import welcome_user
from random import randint

START = 1
END = 100
ROUNDS_TO_WIN = 3


def get_answer():
    number = randint(START, END)  # NOSONAR

    print(f"Question: {number}")
    player_answer = input("Your answer: ").lower().strip()
    correct_answer = "yes" if is_even(number) else "no"
    return player_answer, correct_answer


def is_even(number):
    return number % 2 == 0


def is_answer_correct(player_answer, correct_answer):
    return player_answer == correct_answer


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0

    while counter < ROUNDS_TO_WIN:
        player_answer, correct_answer = get_answer()

        if is_answer_correct(player_answer, correct_answer):
            print("Correct!")
            counter += 1
        else:
            print(
                f"'{player_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")
