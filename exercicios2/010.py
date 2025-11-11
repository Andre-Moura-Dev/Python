numero_fibonacci = int(input("Informe um número: "))
a, b = 0, 1

for i in range(numero_fibonacci):
    print(a)
    a, b = b, a + b