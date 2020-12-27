#Problem Statement: You are given an array and its size. You need to create a new array where each element is a sum of its previous element, current element and next element in 
#                   the given array. If the element does not exist (a[-1] and a[n]) then consider it as 0. Return the new array.

a=[1,2,3,4,5]
n=5
def mutateArray(n,a):
    b=[]
    for i in range(n):
        if i==0:
            b.append(a[i]+a[i+1])
        elif i==n-1:
            b.append(a[i-1]+a[i])
        else:
            b.append(a[i-1]+a[i]+a[i+1])
    print(b)

mutateArray(n,a)
