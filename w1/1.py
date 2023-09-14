
n = int(input())
k = 1
for i in range(2,n,1):
    if n % i == 0:
        k+=i
print(k)