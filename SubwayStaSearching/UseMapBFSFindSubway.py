#UseMapBFSFindSubway
from Stations import *#导入编写的地铁站信息
from collections import deque#导入队列类
def search(station,dst):
    search_queue = deque()#创建搜索队列
    searched = []#创建列表记录已搜索的站点
    search_queue += stationMap[station]#将起始站点连接的站点导入队列尾
    while search_queue:#当队列不为空时，循环搜索
        curStation = search_queue.popleft()#从队列头取出一个站点
        if curStation not in searched:#判断站点是否为目的地站点
            if curStation.getName() == dst.getName():
                print(curStation.__dict__)
                return True
            else:#如果不是
                search_queue += stationMap[curStation]#把当前站点相连通的站点导入队列尾 
                searched.append(curStation)#把当前站点标记为已搜索
    print("NULL")
    return False
print(search(tongHM,daYT))
