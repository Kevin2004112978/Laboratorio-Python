def is_year_leap(year):

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    
    if month < 1 or month > 12 or year < 1:
        return None
    
    
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year) and month == 2:
        return 29
    
    return days[month]


test_years = [1900, 2000, 2016, 1987, 2026]
test_months = [2, 2, 1, 11, 13]
test_results = [28, 29, 31, 30, None]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(f"Año: {yr}, Mes: {mo} -> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print(f"OK (Resultado: {result})")
    else:
        print(f"Fallido (Esperado: {test_results[i]}, Obtenido: {result})")

