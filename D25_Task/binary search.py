l = list(map(int,input().split()))
n = int(input())
low = 0
high = len(l) - 1
mid = 0
r=-1
while low <= high:
    mid = (high + low) // 2
    if l[mid] < n:
        low = mid + 1
    elif l[mid] > n:
        high = mid - 1
    else:
        r= mid
        break
print("Found at index "+str(r) if r != -1  else "Not found")