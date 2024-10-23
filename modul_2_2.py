first = int(input("Первое чисто: "))
second = int(input("Второе чисто: "))
third = int(input("Третье чисто: "))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)




