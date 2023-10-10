def binary_search(arr,target,low,high):
    mid=(low+high)//2
    if mid==target:
        return mid
    elif mid>target:
        return binary_search(arr,target,mid+1,high)
    elif mid<target:
        return binary_search(arr,target,low,mid-1)
    return -1
    
high=int(input("Enter the elements in list: "))
bin=[]
for i in range(high):
    x=int(input(f"Enter the {i+1} element: "))
    bin.append(x)
print(bin)
target=int(input("Enter the target element"))
result= binary_search(bin,target,0,high)
if result==-1:
    print("The target is not present in the list")
else:
    print("The target is present in index ",str(result))