def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def verifica_fibonacci(num):
    fib_sequence = fibonacci(num)
    if num in fib_sequence:
        print(f"O número {num} pertence a sequencia de fibonacci.")
    else:
        print(f"O número {num} não pertence a sequencia de fibonacci.")

numero_informado = int(input("Informe um número: "))
verifica_fibonacci(numero_informado)