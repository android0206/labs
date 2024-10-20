salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_spend = 0  # Общие траты за 10 месяцев
total_salary = salary * months  # Зарплата за 10 месяцев

for month in range(0, months):
    total_spend += spend
    spend *= 1 + increase
money_capital = int(total_spend - total_salary)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
