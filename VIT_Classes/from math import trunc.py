def MaxAbsDiff(arr,n):
    max_diff= abs(arr[1]-arr[0]);
    for i in range( 1, n ):
        if(abs(arr[i] - arr[i-1]) > max_diff):
            max_diff = abs(arr[i] - arr[i-1])
                
    return max_diff;


n = int(input('Enter number of elements in array: '))
print (f'enter {n} elements of array')
arr = input()   # takes the whole line of n numbers
l = list(map(int,arr.split(' ')))
    

print(f'maximum absolute difference in array is {MaxAbsDiff(l,n)}')