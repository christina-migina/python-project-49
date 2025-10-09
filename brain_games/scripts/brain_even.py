from brain_games.cli import welcome_user
from random import randint


# функция для генерация числа, вопроса и ответа, проверки числа на четность функцией
def ask_question():
    number = randint(1, 100)
    print(f"Question: {number}")
    return input("Your answer: "), is_even(number)


# функция для проверки числа на четность
def is_even(number):
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer


# функция для проверки верности ответа
def check_answer(player_answer, correct_answer):
    return player_answer == correct_answer


# игра
def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0

    while counter < 3:
        player_answer, correct_answer = ask_question()
        if check_answer(player_answer, correct_answer):
            print("Correct!")
            counter += 1
        else:
            print(
                f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            counter = 0

    print(f"Congratulations, {name}!")
