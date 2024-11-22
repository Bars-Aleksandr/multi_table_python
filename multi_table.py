import random
import os
import time

# Инициализируем таблицу умножения
multi_table = [[0] * 9 for _ in range(9)]


# метод очистки экрана
def screen_clear():
    os.system("cls" if os.name == "nt" else "clear")


# Функция для получения корректного ввода от пользователя
def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")


def table_result_answer():
    print("\nТаблица участвовавших чисел:")
    for row in multi_table:
        print(" ".join(map(str, row)))


screen_clear()
print("Добро пожаловать в тренировку по таблице умножения!")
# print("Для выхода из программы необходимо нажать Ctrl + C.\n")

correct_answers_count = 0  # Счетчик правильных ответов

try:
    while True:
        # Генерируем случайные числа для умножения
        first_multiplier = random.randint(1, 9)
        second_multiplier = random.randint(1, 9)
        print("Для выхода из программы необходимо нажать Ctrl + C.\n")
        print(f"{first_multiplier} * {second_multiplier} = введите ответ")
        correct_answer = first_multiplier * second_multiplier

        # Количество попыток
        count_answer = 3

        while count_answer > 0:

            answer = get_user_input("Ваш ответ: ")

            if answer == correct_answer:
                print("Ты прав, молодец!")
                multi_table[first_multiplier - 1][second_multiplier - 1] += 1
                correct_answers_count += 1
                time.sleep(1)
                screen_clear()
                break  # Успех, выходим из цикла
            else:
                count_answer -= 1
                if count_answer > 0:
                    print(
                        f"Ошибочка, но ничего страшного! У тебя осталось {count_answer} попыток."
                    )
                else:
                    print(f"Попытки закончились! Правильный ответ: {correct_answer}")

        # Каждые 5 правильных ответов сообщаем о выходе
        if correct_answers_count > 0 and correct_answers_count % 10 == 0:
            print(
                f"У тебя {correct_answers_count} правильных ответов! Для выхода нажмите Ctrl + C."
            )
except KeyboardInterrupt:
    print("\nВы выходите из тренировки. Спасибо за участие!")
    # Вывод таблицы результатов
    table_result_answer()
