from brain_games.cli import welcome_user
from random import randint, choice


def get_answer():
    progression, correct_answer = get_progression()
    print(f"Question: {' '.join(progression)}")
    player_answer = input("Your answer: ")
    return player_answer, correct_answer


def get_progression():
    start, quantity, step = randint(1, 100), randint(5, 10), randint(1, 10)
    progression = [str(start + i * step) for i in range(quantity)]
    missing_num_index = randint(0, quantity - 1)
    missing_num = progression[missing_num_index]
    progression[missing_num_index] = ".."
    return progression, missing_num


def is_answer_correct(player_answer, correct_answer):
    return player_answer == correct_answer


def progression_game():
    name = welcome_user()
    print("What number is missing in the progression?")
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
