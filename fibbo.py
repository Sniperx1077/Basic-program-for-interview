def fibb(n):
    x=0
    y=1
    z=0
    while(z<=n):
        print(z)
        x=y
        y=z
        z=x+y
fibb(int(input("Enter the number")))
