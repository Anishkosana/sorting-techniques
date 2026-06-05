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