n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 1
b = 0
c = 0
summa = 0

for i in range(1, n+1):
    c = b
    b = a
    a = summa
    summa = (a+b+c)
    print(summa)

    