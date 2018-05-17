# Оценки
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
         {'school_class': '4b', 'scores': [1,1,1,1,1]},
         {'school_class': '4c', 'scores': [5,5,5,5,5]}
         ]
sum_score = 0
count = len(school)
for cl in school:
    all_sch = str(sum(cl['scores'])/len(cl['scores']))
    for i in cl['scores']:
        sum_score += i
    avg_sch = sum_score/count
    print('средний балл по каждому классу ',cl['school_class'], sum(cl['scores']) / len(cl['scores']))
print('средний балл по всей школе  = ', avg_sch)

