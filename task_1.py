import random

"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
    Программа должна подсказывать “больше” или “меньше” после каждой попытки"""

class NumberGuesser:
    def __init__(self):
        self.target_number = random.randint(0, 1000)
        self.attempts_left = 10

    def guess_number(self, user_guess):
        if self.attempts_left == 0:
            return "У вас закончились попытки. Загаданное число: " + str(self.target_number)

        self.attempts_left -= 1

        if user_guess == self.target_number:
            return "Вы угадали число " + str(self.target_number) + " с " + str(10 - self.attempts_left) + " попытки!"
        elif user_guess < self.target_number:
            return "Загаданное число больше вашего."
        else:
            return "Загаданное число меньше вашего."

guesser = NumberGuesser()

print(guesser.guess_number(500))
print(guesser.guess_number(750))
print(guesser.guess_number(600))