def сумма_обратных(N):
    сумма = 0.0
    for i in range(1, N + 1):
        сумма += 1 / i
    return сумма

N = int(input("Введите целое число N (> 0): "))

if N <= 0:
    print("Ошибка: N должно быть больше 0.")
else:
    print("Сумма 1 + 1/2 + 1/3 + ... + 1/{} равна: {:.2f}".format(N, сумма_обратных(N)))