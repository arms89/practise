
a = [6, 2, 5, 4, 5, 1, 6]
for i in range(0, len(a)):
    for j in range(i+1, len(a)+1):
        print(min(a[i:j]) * (j-i))




#
# n = int(input())
# result = []
# for case in range(0, n):
#     areas = []
#     m = int(input())
#     values = list(map(int, input().split()))
#     for i in range(0, m):
#         # val = values[i:]
#         for j in range(0, len(values[i:])):
#             areas.append(min(values[i:j + 1]) * (len(values[i:j + 1])))
#     print(max(areas))

