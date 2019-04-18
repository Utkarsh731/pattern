n=int(input("enter the number of rows"))
c=n-1
for i in range(1,n+1):
    print(" "*c,end="")
    c-=1
    for j in range(0,i):
        print("*",end="")
    print()
