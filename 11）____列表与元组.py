# 列表、元组、字符串都属于python的序列

###检查用户名和pin
# data = [
#     ['a','001'],
#     ['b','002'],
#     ['c','003']
# ]
# username = input('username:')
# pin = input('pin:')
# if [username,pin] in data:
#     print('ok')
# else:
#     print('NO')

# 基本的列表操作
### 修改列表，给列表赋值
# x = [1,1,1]
# x[1] = 2
# print(x)
### 删除元素
# del x[2]
# print(x)

### 高级排序，key和reverse
# x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
# x.sort()         #根据顺序排序
# print(x)
# x.sort(key=len)
# print(x)         #根据长度排序

## 指定reverse为True 或者False 进行相反的排序
# y = [4, 6, 2, 1, 7, 9]
# y.sort(reverse = True)
# print(y)

###  元组是不可修改的列表   元组是（） 列表是[]
## 函数 tuple 的工作原理与 list 很像： 将一个序列作为参数，并转换为元组，如果对象已经是元组就原封不动的返回他。
## 与list一样，tuple实际上也不函数，而是一个类型。
a = tuple([1,2,3])
print(a)
b = tuple('abc')
print(b)
c = tuple((1,2,3))
print(c)
