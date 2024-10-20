money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0

total_capital = money_capital + salary  # Капитал на месяц(зарплата 1 числа)
while total_capital > spend:
    total_capital = total_capital - spend + salary  # Капитал след. месяца
    spend *= 1 + increase
    month += 1
else:
    print("Количество месяцев, которое можно протянуть без долгов:", month)
