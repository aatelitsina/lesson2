# Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
def ask_user():
    while True:
        ans = input('Как дела? ')
        if ans.lower() == 'хорошо':
            break
# ask_user()