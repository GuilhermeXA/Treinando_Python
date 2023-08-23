# Função para verificar se um ano é bissexto
def is_bissexto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Função para calcular a diferença em dias entre duas datas
def days_between_dates(date1, date2):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = date2[0] - date1[0] + 1
    for m in range(date1[1], date2[1]):
        days += days_in_month[m]
        if m == 2 and is_bissexto(date1[2]):
            days += 1
    if is_bissexto(date2[2]) and date2[1] > 2:
        days += 1
    return days


# Processamento dos casos de teste
while True:
    n = int(input())
    if n == 0:
        break

    total_days = 0
    total_consumption = 0
    last_date = None

    for _ in range(n):
        day, month, year, consumption = map(int, input().split())
        current_date = (day, month, year)

        if last_date is not None:
            days = days_between_dates(last_date, current_date) - 1
            total_days += days
            total_consumption += days * (last_consumption + consumption) // 2

        last_date = current_date
        last_consumption = consumption

    print(total_days, total_consumption)
