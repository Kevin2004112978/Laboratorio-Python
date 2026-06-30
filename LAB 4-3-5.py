def is_year_leap(year):
    # Lógica del LAB 4.3.1.6: Año bisiesto si es divisible por 4,
    # excepto si es divisible por 100 pero no por 400.
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    # Validar que el mes esté en el rango correcto y que el año sea válido
    if month < 1 or month > 12 or year < 1:
        return None
    
    # Lista de días por mes (índice 0 es un placeholder para que febrero sea el índice 2)
    # Febrero (índice 2) se ajusta dinámicamente si es bisiesto.
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year) and month == 2:
        return 29
    
    return days[month]

# --- Casos de prueba ---
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

