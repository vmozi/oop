from datetime import date

# Отримати поточну дату
today = date.today()
year = today.year
month = today.month

# Визначення пори року за місяцем
if month in [12, 1, 2]:
    season = "Зима"
elif month in [3, 4, 5]:
    season = "Весна"
elif month in [6, 7, 8]:
    season = "Літо"
else:
    season = "Осінь"

# Перевірка, чи рік високосний
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Вивід результатів
print(f"Місяць: {today.strftime('%B')}, Пора року: {season}, Рік: {year}, Високосний рік: {'Так' if is_leap_year else 'Ні'}")
