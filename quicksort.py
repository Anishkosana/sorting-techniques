# quicksort function

def quicksort(l,h,nums):
    if l<h:
        j=partitioning(l,h,nums)
        quicksort(l,j,nums)
        quicksort(j+1,h,nums)

# partioning algorithm
def partitioning(l,h,nums):
    if not nums:
        return None
    pivot=nums[l]
    i,j=l,h
    # j=h
    while i<j:
        while nums[i]<=pivot:
            i+=1
        while nums[j]>pivot:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[l],nums[j]=nums[j],nums[l]
    return j

# hoarse partitioning algorithm 
def hoarse_partitioning(l,h,nums):
    if not nums:
        return None
    mid=(l+h)//2
    pivot=nums[mid]
    i=l
    j=h
    while True:
        while nums[i]<pivot:
            i+=1
        while nums[j]>pivot:
            j-=1
        if i>=j:
            return j
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1