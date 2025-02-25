# Algoritmo de Karatsuba

## Descrição do Projeto
O **algoritmo de Karatsuba** é um método eficiente para multiplicação de dois números inteiros grandes. Ele reduz o número de multiplicações necessárias em comparação ao método tradicional, utilizando a técnica de **divisão e conquista**.

### Lógica de Implementação
1. **Caso Base**: Se um dos números for menor que 10, realizamos a multiplicação diretamente.
2. **Divisão dos Números**: Os números são divididos em duas partes, separando a parte alta e baixa.
3. **Recursão**: Calculamos três multiplicações recursivas:
   - `z0 = karatsuba(low_x, low_y)`: Multiplicação das partes baixas.
   - `z1 = karatsuba((low_x + high_x), (low_y + high_y))`: Multiplicação da soma das partes.
   - `z2 = karatsuba(high_x, high_y)`: Multiplicação das partes altas.
4. **Combinação dos Resultados**: A multiplicação final é obtida pela fórmula:
   ```
   resultado = (z2 * 10^(2*m)) + ((z1 - z2 - z0) * 10^m) + z0
   ```

### Código-Fonte
```python
def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y
    
    # Determina o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Divide os números em duas partes
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)
    
    # Calcula as três multiplicações recursivas
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)
    
    # Combina os resultados
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# Exemplo de uso
num1 = 12345678
num2 = 87654321
resultado = karatsuba(num1, num2)
print(f"Resultado de {num1} * {num2} = {resultado}")
```

## Como Executar o Projeto
1. Instale o **Python 3** em sua máquina, caso não tenha.
2. Copie o código-fonte para um arquivo `main.py`.
3. Execute o script com o comando:
   ```sh
   python main.py
   ```

## Relatório Técnico
### Complexidade do Algoritmo

| Complexidade | Melhor Caso | Caso Médio | Pior Caso |
|--------------|-------------|------------|-----------|
| Temporal     | O(n)        | O(n)       | O(n)      |
| Espacial     | O(n)        | O(n)       | O(n)      |

### Vantagens
- **Menos operações de multiplicação** comparado ao método tradicional.
- **Melhor desempenho** para números grandes.
- **Utilização do paradigma de divisão e conquista**, tornando-o escalável.

### Desvantagens
- **Maior número de operações de soma e subtração**.
- **Requer mais memória** devido à recursão.

## Exemplo de Entrada e Saída

### Entrada
```python
num1 = 12345678
num2 = 87654321
```

### Saída
```
Resultado de 12345678 * 87654321 = 1082152022374638
```



## Referências
- Karatsuba, A. (1960). Multiplication of Multidigit Numbers on Automata.
- [Wikipedia - Karatsuba Algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm)

