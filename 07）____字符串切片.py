
#   字符串切片   https://www.runoob.com/python/python-func-slice.html

name = 'china'
name1 = name[:3]        #截止到第三位
name2 = name[:-1]       #截止到倒数第一位
name3 = name[1:4:2]     #从1开始到4结束，间隔2个步长
print(name3)

# slcie 切片

web1 = 'http://baidu.com'
web2 = 'http://bilibili.com'
#方法 1
print(web1[slice(7,-4)])
#方法2
bi = slice(7,-4)      #   相对方法 1 多创建了一个变量
print(web2[bi])
#方法3 给切片赋值
web3 = list('baidu')
web3[2:] = list('google')
print(web3)