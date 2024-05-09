def selectionSort(arraylist):
    n = len(arraylist)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if arraylist[j] < arraylist[min_ind]:
                min_ind = j
            if min_ind != i:
                temp = arraylist[i]
                arraylist[i] = arraylist[min_ind]
                arraylist[min_ind] = temp
    return arraylist

a = [2, 5, 4, 1, 9, 3, 0,12,45]
print("The Sorted Array is : ",selectionSort(a))
