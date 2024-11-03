# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, arg=','):
    set1 = set(group1.split(arg))
    list2 = group2.split(arg)
    both = list(set1.intersection(list2))
    both.sort()
    return both


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
divide = '|'

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, divide)
