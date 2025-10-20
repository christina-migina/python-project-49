from brain_games.cli import welcome_user
from random import randint


def get_answer():
    number = randint(1, 100)
    print(f"Question: {number}")
    player_answer = input("Your answer: ").lower().strip()
    correct_answer = "yes" if is_prime(number) else "no"
    return player_answer, correct_answer


def is_prime(number):
    if number <= 2:
        return True
    for num in range(2, number // 2 + 1):
        if number % num == 0:
            return False
    return True


def is_answer_correct(player_answer, correct_answer):
    return player_answer == correct_answer


def prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
