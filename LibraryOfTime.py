#time库的使用
#   时间获取：time(),ctime(),gmtime()
#   时间格式化：strftime(),strptime()
#   程序计时：sleep(),perf_counter()
import time
start=time.perf_counter()
print(time.time())#返回当前时间戳，float格式
print(time.ctime())#返回可读性强的时间，字符串格式
print(time.gmtime())#返回对象：time.struct_time,其中包含tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))#strftime格式化时间输出，第一个参数为格式模板，第二个参数为时间，类型为time.struct_time
#time库中格式化字符串：
#   %Y 年份 0000-9999
#   %m 月份 01-12
#   %B 月份名称 January~December
#   %b 月份缩写 Jan~Dec
#   %d 日期 01-31
#   %A 星期 Monday~Sunday
#   %a 星期缩写 Mon~Sun
#   %H 24小时制的时 00-23
#   %I 12小时制的时 01-12
#   %M 分钟 00-59
#   %S 秒 00-59
print(time.strptime("2019-04-02 04:53:08","%Y-%m-%d %H:%M:%S"))#将字符串转换回time.struct_time
time.sleep(1)#程序休眠1秒
end=time.perf_counter()#调用起止两个时间点的准确时间戳，从而确定程序运行时间
print(end-start)



