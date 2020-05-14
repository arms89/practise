n = 50000

preval, curval = 0, 1
print(preval, curval, sep='\n')
for i in range(1, n+1):
    preval, curval = curval, curval + preval

print(curval)
