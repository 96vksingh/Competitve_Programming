def wavePrint(arr):
    n = len(arr[0])
    m = len(arr)
    li = []
    for j in range(n): # 0 1 2 3
        k= []
        for ele in arr: 
            if(j%2==0):
                li.append(ele[j])
            else:
                k.append(ele[j])
        k = k[-1::-1]
        li.extend(k)
    for i in li:
        print(i,"",end='')

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
wavePrint(arr)
