def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y

    # Determina o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide os números em duas partes
    high_x, low_x = divmod(x, 10 ** m)
    high_y, low_y = divmod(y, 10 ** m)

    # Calcula as três multiplicações recursivas
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    # Combina os resultados
    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0


# Exemplo de uso
num1 = 12345678
num2 = 87654321
resultado = karatsuba(num1, num2)
print(f"Resultado de {num1} * {num2} = {resultado}")