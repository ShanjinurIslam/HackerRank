import os
def diagonalDifference(arr):
    m = len(arr)
    
    sum_1 = 0
    sum_2 = 0
    
    for i in range(m):
        sum_1 += arr[i][i]
        sum_2 += arr[n-i-1][i]
        
    return abs(sum_1-sum_2)
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
