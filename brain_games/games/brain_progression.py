from brain_games.cli import welcome_user
from random import randint

START_NUM = 1
END_NUM = 100
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
ROUNDS_TO_WIN = 3


def get_answer():
    progression, correct_answer = get_progression()
    print(f"Question: {' '.join(progression)}")
    player_answer = input("Your answer: ")
    return player_answer, correct_answer


def get_progression():
    start = randint(START_NUM, END_NUM)  # NOSONAR
    length = randint(MIN_LENGTH, MAX_LENGTH)  # NOSONAR
    step = randint(MIN_STEP, MAX_STEP)  # NOSONAR

    progression = [str(start + i * step) for i in range(length)]
    missing_num_index = randint(0, length - 1)  # NOSONAR
    missing_num = progression[missing_num_index]
    progression[missing_num_index] = ".."
    return progression, missing_num


def is_answer_correct(player_answer, correct_answer):
    return player_answer == correct_answer


def progression_game():
    name = welcome_user()
    print("What number is missing in the progression?")
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
