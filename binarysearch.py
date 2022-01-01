arr=[] #first we take a empty array
num=int(input("enter number of elements: ")) #now ask how many element you want in that array
for i in range(0,num): #now we take a loop from 0 to the number of element we want
    x=int(input()) #the the value which you want to put in that array
    arr.sort() # in binary search we should first short the element 
    arr.append(x) #then append that value into the empty array
n= int(input("enter the value you want to search :=")) #take the key value you want to search
low=0 #take lower value of array
high=len(arr)-1 #take higher vaue of array
found=False #initially assingn the found value to false
while low<=high and not found:
    mid=(high+low)//2 #take the middle value of array
    if n==arr[mid]: #we compare key element to mid element of array
        found=True #if mid element is equal to the key element then found became true and condition matched
    elif n>arr[mid]:#if above condition is not true then we compare mid element to given key if it is grater then
        low=mid+1 #we set lower value at mid+1
    else:
        high=mid-1 #new high will become mid-1
    if found==True:
        print("n is found")
        break
else:
    print("number is not found")
    



