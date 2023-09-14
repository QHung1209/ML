cnt = 0
n = str(input())
for i in n:
    if(i == '7' or i == '4'):
        cnt+=1
if cnt == 4 or cnt ==7:
    print("YES")
else:
    print("NO")
