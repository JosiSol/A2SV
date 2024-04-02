import os
import sys

def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    return count

if __name__ == '__main__':
    
    if 'OUTPUT_PATH' not in os.environ:
        print("Error: OUTPUT_PATH environment variable is not defined")
        sys.exit(1)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

   
    result = countingSort(arr)

   
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
