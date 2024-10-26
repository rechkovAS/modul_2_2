n = int(input('Введите число, которое видите на камнях (от 3 до 20): '))
result = ''
for a in range(1, n):
    for b in range(a, n):
        if n % (a + b) == 0 and a != b:
            result = result + str(a) + str(b)
print(result)
