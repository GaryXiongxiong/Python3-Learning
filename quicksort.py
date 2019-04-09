#quicksort.py 利用递归写出快速排序算法
def QuickSort(arrayIn):
    if len(arrayIn) < 2:
        return arrayIn
    else:
        pivot = arrayIn.pop(len(arrayIn)//2)
        subArr1= []
        subArr2= []
        for i in arrayIn:
            if i <= pivot:
                subArr1.append(i)
            else:
                subArr2.append(i)
        return QuickSort(subArr1)+[pivot]+QuickSort(subArr2)
print(QuickSort([2,5,11,6,2,13]))