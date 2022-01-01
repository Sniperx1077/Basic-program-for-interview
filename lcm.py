def lcm(a,b):
    if a>b:
        higher=a
    else:
        higher=b
    value=higher
    while True:
        if higher%a==0 and higher%b==0:
            print("lcm is",higher)
            break
        else:
            higher=higher+value
lcm(72,36)
