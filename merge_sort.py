def merge_sort(A,l,h):
    if l<h:
        mid=(l+h)//2
        merge_sort(A,l,mid)
        merge_sort(A,mid+1,h)
        merge(A,l,mid,h)
    
def merge(A,l,mid,h):
    i=l
    j=mid+1
    temp=[]
    while i<=mid and j<=h:
        if A[i]<A[j]:
            temp.append(A[i])
            i+=1
        else:
            temp.append(A[j])
            j+=1
    while i<=mid:
        temp.append(A[i])
        i+=1
    while j<=h:
        temp.append(A[j])
        j+=1
    A[l:h+1]=temp
A=[12,13,9,2,10,6,21]
merge_sort(A,0,len(A)-1)
print(A)
