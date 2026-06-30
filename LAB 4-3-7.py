def is_prime(num):
    # Los números menores o iguales a 1 no son primos
    if num <= 1:
        return False
    
    # Verificamos divisibilidad desde 2 hasta la raíz cuadrada de num
    # Usamos num**0.5 para la raíz y int() para el límite superior del rango
    limit = int(num**0.5)
    
    for i in range(2, limit + 1):
        if num % i == 0:
            return False  # Se encontró un divisor, no es primo
            
    return True  # No se encontraron divisores, es primo

# --- Bloque de pruebas ---
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
