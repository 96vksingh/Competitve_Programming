def rowWiseSum(arr):
    li = []
    for i in arr:
        sum = 0
        for j in i:
            sum+=j
        li.append(sum)
    return li
def colWiseSum(arr):
    li = []
    m = len(arr[0])
    for j in range(m):
        sum = 0
        for ele in arr:
            sum+=ele[j]
        li.append(sum)
    return li
 
def largestRowCol(arr):
    rowSum = rowWiseSum(arr)
    colSum = colWiseSum(arr)
    print(colSum)
    largeNo = -1
    index = -1 
    largeWh = 'r'
    for i in range(len(rowSum)):
        if(largeNo<rowSum[i]):
            largeNo = rowSum[i]
            largeWh = 'r'
            index = i
        for j in range(len(colSum)):
            if(largeNo<colSum[j]):
                largeNo = colSum[j]
                index = j
                largeWh = 'c'
    if(largeWh == 'c'):
        ans = "column " + str(index) + " " + str(colSum[index])
    else:
        ans = "row " + str(index) +" "+ str(rowSum[index])
    print(ans)
    return ans

#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l=largestRowCol(arr)
print(*l)
