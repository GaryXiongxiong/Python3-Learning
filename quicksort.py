#quicksort.py 利用递归写出快速排序算法
def QuickSort(arrayIn):
    if len(arrayIn) < 2:
        return arrayIn#如果只有一个元素，直接返回列表
    else:
        pivot = arrayIn.pop(len(arrayIn)//2)#选取中间数作为排序的支点
        subArr1= []
        subArr2= []
        for i in arrayIn:
            if i <= pivot:
                subArr1.append(i)#小于支点放在子列表1
            else:
                subArr2.append(i)#大于支点放在子列表2
        return QuickSort(subArr1)+[pivot]+QuickSort(subArr2)#对子列表1与子列表2分别进行快速排序，并放在支点两侧
print(QuickSort([2,5,11,6,2,13]))