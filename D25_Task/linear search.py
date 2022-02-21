l=list(map(int,input().split()))
n=int(input())
f=False
ind=0
for i in l:
    if n==i:
        f=True
        break
    ind+=1
print("Found at index "+str(ind) if f else "Not found")