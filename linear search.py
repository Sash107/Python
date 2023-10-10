def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
mylist=[1,2,3,4,5,6,7]
target= 4
result= linear_search(mylist,target)
if result==-1:
    print("The target is not present in the list")
else:
    print(f"The target is present in index {result+1}")