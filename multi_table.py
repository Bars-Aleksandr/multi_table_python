import random


# Функция для получения корректного ввода от пользователя
def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")


# создание пустого массива
multi_table = [[0] * 9 for _ in range(9)]


# Генерируем случайные числа для умножения
while True:
    # Генерируем случайные числа для умножения
    first_multiplier = random.randint(1, 9)
    second_multiplier = random.randint(1, 9)

    print(f"{first_multiplier} * {second_multiplier} = введите ответ")
    correct_answer = first_multiplier * second_multiplier

    # Количество попыток
    count_answer = 3

    while count_answer > 0:
        answer = get_user_input("Ваш ответ: ")

        if answer == correct_answer:
            print("Ты прав, молодец!")
            multi_table[first_multiplier - 1][second_multiplier - 1] += 1
            break  # Успех, выходим из цикла
        else:
            count_answer -= 1
            if count_answer > 0:
                print(
                    f"Ошибочка, но ничего страшного! У тебя осталось {count_answer} попыток."
                )
            else:
                print(f"Попытки закончились! Правильный ответ: {correct_answer}")

    # Вывод таблицы умножения

    # Спрашиваем, хочет ли пользователь продолжать
    continue_check = input("Хотите попробовать еще раз? (да-1/нет-0): ")
    if continue_check != "1":
        print("Спасибо за игру! До свидания!")
        for row in multi_table:
            print(" ".join(map(str, row)))
        break
