lst_nm = ["Вася", "Маша", "Петя","Валера", "Саша", "Даша"]
i = 0
while i < len(lst_nm):
    print(i)
    print(lst_nm[i])
    if lst_nm[i] != "Валера":
        lst_nm.pop(i)
        continue

    print("Валера нашелся")
    break


