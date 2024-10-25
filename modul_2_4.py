numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len (numbers)): #перебираем числа списка
    for j in range(2, numbers[i]+1): #перебираем делители от 2 до самого числа
        is_prime = True
        #print(numbers[i], j)
        if numbers[i] % j == 0: # выставляем условие: число из списка делится без остатка
            is_prime = False # значит число из списка, возможно, не простое
            if numbers[i] != j and is_prime == False : # выставляем условие: число из списка и делитель не равны и оно делится на него без остатка
                not_primes.append(numbers[i]) # значит оно являет не простым и мы добавляем его в список не простых чисел
                break # прерываем цикл, начинаем проверку следующего числа из списка
            else:
                primes.append(numbers[i]) # в противном случае это постое число :)
# выводим на экран результат
print(primes)
print(not_primes)