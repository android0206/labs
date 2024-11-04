# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, arg=','):
    set_for_intersection = set(group1.split(arg))
    # Используем set для метода intersection,
    # разделяем строку по разделителю и записываем в список, затем во множество
    list_of_group2 = group2.split(arg)
    # Разделяем строку по разделителю и записываем в список
    both_participants = list(set_for_intersection.intersection(list_of_group2))
    # Находим общих участников
    both_participants.sort()
    # Алфавитный порядок
    return both_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, arg='|'))
