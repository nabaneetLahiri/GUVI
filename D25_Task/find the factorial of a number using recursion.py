def fact(n):
    if n<0:
        return -1
    elif n==0 or n==1 or n==2:
        return 1
    else:
        return n*fact(n-1)
r=fact(int(input()))
print(r if r>0 else "Invalid")