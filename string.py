#learn about string
#str()为eval()的反函数
print("零一二三四五六七八九十"[1:8:2])#<string>[m:n:k] m为起始，n为结束，k为步长
print("abc".upper())
print("ABC".lower())#字符串的大小写变更
print("ABC,BC,C".split(",",1))#str.split(str1,int)以str1为分隔符，将str分割int下，int为分割次数最大值
print("Aford is a little dog that owned by a boy".count("a"))#字符串中字符计数（貌似小写可以找到大写，大写找不到小写？）
print("Im a good boy".replace("o","0"))#替换字符串的字符
print("center".center(20,"="))#字符串剧中，参数为长度，填充符,填充符长度为1
print("www.baidu.com ".strip(" wcom."))#去除字符串两侧参数中的每个单个字符
print(",".join("garyxiong"))#将字符串插入到参数中
print("字符串的格式化输出，{}为槽，槽中填充{}中的{}".format("大括号","format方法","参数"))
print("字符串的格式化输出，{1}为槽，槽中填充{0}中的{2}".format("format方法","大括号","参数"))#通过在槽中填写序号来设定槽对应第n个参数
print("|{0:=<10}|{1:=^20}|{2:=>10}|".format("name","telephone","gender"))
print("|{: <10}|{: ^20}|{: >10}|".format("Gary","13279247931","male"))#在槽中的序号后跟":",之后进行格式化，参数为：<填充>（单一字符）、<对齐>（<^>代表左中右）、<宽度>（槽的输出宽度）
print("{:=,.2f}".format(14256.25234))#对于数字，参数如右：<,>（千位点）、<.精度>、<类型>
print("{:b},{:c},{:d},{:o},{:x},{:X}".format(425,425,425,425,425,425))#b:二进制，c:字符，d：十进制，o：八进制，x：16进制，X：大写16进制（这些都是整型）
print("{:e},{:E},{:f},{:%}".format(425.667,425.667,425.667,425.667))#e：科学记数法，E:大写科学记数法，f:通常浮点数，%：百分数形式表示（这些都是浮点数）
print("{:=^50,.2f}".format(14256.25234))#参数可以同时作用