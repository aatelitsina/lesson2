from get_answer import get_answer
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”


def ask_user():
    while True:
        try:
            qw = input()
            an = get_answer(qw.lower())
            print(an)
            if qw == 'пока':
                break
        except KeyboardInterrupt:
            print('прерывание ctrl+C')
            break

ask_user()