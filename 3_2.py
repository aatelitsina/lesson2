def find_person(name):
    lst_nm = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    # print(lst_nm[name])
     while name in lst_nm:
        print(name,' нашелся')

print(find_person('Валера'))