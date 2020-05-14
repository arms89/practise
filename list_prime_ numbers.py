from math import sqrt

n = 9
if n >= 2:
    print("2 is a prime number")
for i in range(3, n+1, 2):
    for j in range(3, int(sqrt(i)+1)):
        if i % j == 0:
            break
    else:
        print(f'{i} is a prime number')
