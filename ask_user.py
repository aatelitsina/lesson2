from get_answer import get_answer
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”


def ask_user():
    while True:
        qw = input()
        an = get_answer(qw.lower())
        print(an)
        if qw == 'пока':
            break

ask_user()
