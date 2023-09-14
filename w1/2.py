k,t = map(int, input().split())
gate = k - t%k
if (t//k)%2 == 0:
    print(t%k)
else:
    print(gate)

