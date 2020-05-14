a, b, c = map(int, input().split())
if a > (b and c):
    print('A is greatest')
elif b > c:
    print('B is greatest')
else:
    print('C is graetest')
