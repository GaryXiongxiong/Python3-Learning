def arrange(array):#全排列数组-通过递归
    output = []
    if len(array) == 1:
        return [array]#当数组只有一个元素时直接返回该数组
    else:#对于多个元素的数组，全排列相当于以不同的元素首，并将其余元素分全排列
        # 例如全排列[1,2,3]，相当于以1为头部排列[2,3]，以2为头部排列[1,3]，以3为头部排列[1,2]
        # 所以全排列为[1]+arrange([2,3]),[2]+arrange([1,3]),[3]+arrange([1,2])
        # 推广至n个元素的数列
        # arrange([x1,x2,...,xn])为[x1]+arrange([x2,x3,...,xn]),[x2]+arrange([x1,x3,...,xn]),...,[xn]+arrange([x1,x2,...,xn-1])
        for i in array:
            subArr = array.copy()
            subArr.remove(i)
            for j in arrange(subArr):
                newArr = [i]+j
                output.append(newArr)

    return output
strIn = input()
eleList = strIn.split(' ')
array = [eval(i) for i in eleList]
print(arrange(array))
