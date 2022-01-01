arr=[]
n=int(input("enter number of elements: "))
for i in range(0,n):
    x=int(input())
    arr.append(x)
print("your elements are",arr)
num=int(input("enter the element you want to find"))
for i in range(len(arr)):
    if(arr[i])==num:
        print("Key element found",i)
        break
else:
    print("not found")
