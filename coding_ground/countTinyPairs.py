#Problem Statement: You are given two arrays and a value k to compare. You need to join the first element of the first array and last element of the second array and compare it 
#                   with k. Give count of all values smaller than k. For first array the elements will increase for second array the elements will decrease.

a=[37,22,19,37,40,9,35,9,7,37]
b=[30,40,40,29,13,23,0,0,16,8]
k=1822
def countTinyPairs(a,b,k):
    b=b[::-1]
    count=0
    for i in range(len(a)):
        if k>a[i]*10+b[i]:
            count+=1
    print(count)

def countTinyPairs2(a,b,k):
    b=b[::-1]
    count=0
    for i in range(len(a)):
        val=int(str(a[i])+str(b[i]))
        if k>val:
            count+=1
    print(count)
countTinyPairs(a,b,k)
countTinyPairs2(a,b,k)
