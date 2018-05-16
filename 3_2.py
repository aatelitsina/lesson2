def find_person(name):
    lst_nm = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    i = 0
    while i < len(lst_nm):
        if lst_nm[i] == name:
            print("нашелся ", name)
            break
        i+=1

find_person('Валера')