n=int(input("enter the num of rows"))
c=n
for i in range(0,n):
    print(" "*(n-c),end="")
    c-=1
    for j in range(n,i,-1):
        print("*",end="")
    print()
