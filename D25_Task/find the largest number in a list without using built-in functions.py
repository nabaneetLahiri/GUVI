l=list(map(int,input().split()))
r=l[0]
for i in l[1:]:
    if r<i:
        r=i
print(r)