def minMaxSelectionSort(A):
    i = 0
    limit = len(A)-1
 	limit2 = limit
    while(i < limit):
        min = arr[i]
        max = arr[i]
        min_i = i
        max_i = i
        for k in range(i, limit + 1, 1):
            if (arr[k] > max):
                max = arr[k]
                max_i = k
            elif (arr[k] < min):
                min = arr[k]
                min_i = k
          
        # shifting the min.
        temp = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = temp
  
        # Shifting the max. The equal condition
        # happens if we shifted the max to 
        # arr[min_i] in the previous swap.
        if (arr[min_i] == max):
            temp = arr[limit]
            arr[limit] = arr[min_i]
            arr[min_i] = temp
        else:
            temp = arr[limit]
            arr[limit] = arr[max_i]
            arr[max_i] = temp
  
        i += 1
        limit -= 1
  
    print("Sorted array:", end = " ")
    for i in range(limit2):
        print(arr[i], end = " ") 
  

arr = [23, 78, 45, 8, 32, 56, 1]

minMaxSelectionSort(arr)
