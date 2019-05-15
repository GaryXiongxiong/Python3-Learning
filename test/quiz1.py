import sys
# 反转矩阵
def swing(array2):
    n = len(array2)
    arrOut = [[0]*n for i in range(n)]
    # 生成新的全零矩阵已接受数据
    for row in range(n):
        for col in range(n):
            # 逐行逐列进行数据转换
            arrOut[row][n-1-col] = array2[col][row]
    return arrOut

if __name__ == "__main__":
    array2 = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        inputLine = sys.stdin.readline().strip().split(" ")
        inputLine = [int(str) for str in inputLine]
        assert len(inputLine) == n , "参数数量错误"
        array2.append(inputLine)
    times = int(sys.stdin.readline().strip())
    for i in range(times):
        array2 = swing(array2)
    for y in range(n):
        for x in range(n):
            print(array2[y][x],end=' ')
        print()
