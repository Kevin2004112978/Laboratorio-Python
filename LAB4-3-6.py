def is_year_leap(year):
    if year < 1:
        return False
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None
    
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_year_leap(year):
        return 29
        
    return days_per_month[month - 1]

def day_of_year(year, month, day):

    if year < 1 or month < 1 or month > 12:
        return None
        

    max_days = days_in_month(year, month)
    if day < 1 or day > max_days:
        return None
        
    
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
        
    
    total_days += day
    return total_days


print("Año bisiesto completo (esperado 366):", day_of_year(2000, 12, 31))
print("Año común completo (esperado 365):", day_of_year(2021, 12, 31))
print("Primer día del año (esperado 1):", day_of_year(2023, 1, 1))
print("Fin de febrero bisiesto (esperado 60):", day_of_year(2024, 2, 29))
print("Fin de febrero común (esperado 59):", day_of_year(2023, 2, 28))


print("Día inválido en febrero común:", day_of_year(2023, 2, 29))
print("Mes inválido (13):", day_of_year(2023, 13, 10))
print("Día negativo:", day_of_year(2023, 5, -5))
print("Año inválido:", day_of_year(0, 1, 1))
