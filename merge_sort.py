class Sorting(object):
    """
        This class contains all the sorting algorithms.
    """

    def __init__(self):
        pass
    def merge_sort(self,_arr,left,right):
        if left < right:
            mid = int(left+(right-left)/2)
            self.merge_sort(_arr,left,mid)
            self.merge_sort(_arr,mid+1,right)
            self.merge(_arr,left,mid,right)
    def merge(self,_arr,left,mid,right):
        # n1 and n2 used as condition check for the while iteration while merging
        n1 = mid-left+1
        n2 = right-mid

        # initialise the left and right array
        L = [0]*n1
        R = [0]*n2

        # copy the current array to the L and r array
        for i in range(n1):
            L[i] = _arr[left+i]
        for j in range(n2):
            R[j] = _arr[mid+1+j]

        # intiliase the i,j,k counter to 0
        i,j,k=0,0,0
        while i<n1 and j<n2:
            if L[i]<R[j]:
                _arr[k]=L[i]
                i+=1
            else:
                _arr[k]=R[j]
                j+=1
            k+=1
        # There will be conditons when one array will get empty
             #and others will have values so we need handle to that case also.
        # for left subarray
        while i<n1:
            _arr[k]=L[i]
            i+=1
            k+=1
        while i<n2:
            _arr[k] = R[j]
            j+=1
            k+=1

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print ("Given array is",arr)
    _sort = Sorting()
    _sort.merge_sort(arr,0,n-1)
    print ("\n\nSorted array is")
    for i in range(n):
        print ("%d" %arr[i])
