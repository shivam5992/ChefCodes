def findlis(A):

    n = len(A)
    LIS = [1]*n
    #Base Case
    for k in range(0,n):
        LIS[k] = 1

    for i in range(1,n):
        for j in range(0,i):
            if A[i] > A[j] and LIS[i] < LIS[j] + 1 :
                LIS[i] = LIS[j] + 1;

    return max(LIS)    





A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print (findlis(A))
    
