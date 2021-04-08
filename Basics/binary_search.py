def bin_search(list,size,n):
    low=0
    high=size-1
    while low<=high:
        mid=(low+high)//2
        if  list[mid]==n:
            position=mid
            print(f"{n} found at position {position+1}\n")
            quit()
        else:
            if list[mid]>n:
                high=mid-1
            else:
                low=mid+1
    print("not found\n")

list=[12,45,8,14,15,16,27]
list.sort()
print("sorted list: ",list,"\n")
position=0;
size=len(list)
n=8
bin_search(list,size,n)


