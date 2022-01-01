import sys
sys.setrecursionlimit(5000)
def fact(num):
    while num>=0:
        if num==1 or num==0:
            return 1
        else:
            return num*(fact(num-1))
fact(int(input("enter the positive number")))
