
#   字符串切片   https://www.runoob.com/python/python-func-slice.html

# name = 'china'
# name1 = name[:3]        #截止到第三位
# name2 = name[:-1]       #截止到倒数第一位
# name3 = name[1:4:2]     #从1开始到4结束，间隔2个步长
# print(name3)

### slcie 切片

# web1 = 'http://baidu.com'
# web2 = 'http://bilibili.com'
# #方法 1
# print(web1[slice(7,-4)])
# #方法2
# bi = slice(7,-4)      #   相对方法 1 多创建了一个变量
# print(web2[bi])
# #方法3 给切片赋值
# web3 = list('baidu')
# web3[2:] = list('google')
# print(web3)

### 字符串的基本操作
    # 标准的序列操作（索引，切片，乘法，长度，最大最小值，成员资格检查）都适用于字符串
    # 字符串是不可变的，所有的元素赋值和切片赋值都会报错。
## 使用转换符 %s
# aa = "hello,%s,%s world haha"
# bb = ('你好','世界')
# print(aa % bb)
## 替换字符段名
# cc = "{one} {} {} {two}"
# print(cc.format(3,4,one = 1 , two = 2))
## center让字符串居中 具体看书内标签。
print("my wolrld is myself".center(18,"1"))