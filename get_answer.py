
def get_answer(question,ans=[
                            {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"},
                            {"что задали": "Не знаю", "кто знает": "Рома", "спасибо": "Пжл"}]):
    if ans[0].get(question) is not None:
        res = ans[0].get(question)
    else:
        res = ans[1].get(question)
    return res

# print(get_answer('Кто Знает').lower())