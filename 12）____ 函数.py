
##  函数就是带名字的代码块，可以反复调用。
###示例（一）
# def 函数():
#     print("最简单的函数！")
# 函数()

### 示例（二）： 向函数传递信息
# def 函数(a):
#     print("最简单的函数"+ a + "!")
# 函数('随便写')

### 示例（三） ： 位置实参（定义的是形参，后面自己填写的实参）
# def china(省,市,县):
#     print("\n我在"+ 省 + ".")
#     print(省+"的"+ 市 + 县)
# china("安徽","亳州","蒙城")
# china("湖北","武汉","枣庄")

### 示例（四） ： 关键字形参（就是把形参和实参相关联）
# def china(省,市,县):
#     print("\n我在"+ 省 + ".")
#     print(省+"的"+ 市 + 县)
# china("安徽","亳州","蒙城")
# china(县="湖北",省="武汉",市="枣庄")

### 示例（五） ：  默认值形参（就是实参没定义的时候用形参代替，定义默认形参的后面要跟着默认形参）
# def china(省,市="上海",县="奉贤"):
#     print("\n我在"+ 省 + ".")
#     print(省+"的"+ 市 + 县)
# china("安徽","亳州","蒙城")
# china(省="武汉")

## 返回值（简化程序）
### 示例（一） ：  返回简单值
# def 姓名(姓,名):
#     完整的名字 = 姓 + 名
#     return 完整的名字
# 结果 = 姓名("王","小二")
# print(结果)

### 示例（二） ：  让实参变得可选
# def china(省,市,县):
#     全称 = 省+市+县
#     return 全称
# print(china('安徽', '合肥','肥东'))
# print(china('安徽','','肥东'))

### 返回字典
# def china(a,b,c=''):                #定义一个可选形参
#     全称 = {'省':a,'市' :b}
#     if c:                           #如果包含这个值，将会被打印
#         全称['县']=c
#     return 全称
# print(china('安徽', '合肥','肥东'))
# print(china('安徽','','肥东'))

### 函数与while循环
# def china(省,市,县):
#     全称 = 省+市+县
#     return 全称
# while True:
#     print("\n 输入你送在的地域名称，输入'x'退出！")
#     a1 = input("你在哪个省？\n")
#     if a1 == 'x':
#          break
#     a2 = input("你在哪个市？\n")
#     a3 = input("你在哪个县？\n")
#     A = china(a1,a2,a3)
#     print("\n你在"+A)

## 函数与列表
### 传递列表
# def user_name(names):
#     for name in names:
#         msg = "你大爷的 " + name +'!'
#         print(msg)
# # users = ['aa','bb','cc','dd']
# # user_name(users)
# user_name(['aa','vv','ff'])

### 修改列表
# def 修改(kaishi,jieshu):
#     while kaishi:
#         xiugai = kaishi.pop()
#         print("待修改的数值有"+xiugai)
#         jieshu.append(xiugai)
# def 修改后(jieshu):
#     print("已修改完成")
#     for i in jieshu:
#         print(i)
# kaishi = ['aa','bb','cc','dd']
# jieshu = []
# 修改(kaishi[:4],jieshu)           #切片修改副本
# 修改后(jieshu)

### 传递任意数量的实参（利用 * 创建一个空的元组来填充）
# def china_shengfen(*shengfen):
#     print("\n中国的省份包含有：")
#     for i in shengfen:
#         print(i)
# china_shengfen('安徽','湖南','湖北','河北')
# china_shengfen('河南','陕西')

### 位置实参和任意数量实参
# def china_shengfen(renkou,*shengfen):
#     print("\n中国的省份人口" + str(renkou)+"的包含有：")
#     for i in shengfen:
#         print(i)
# china_shengfen(60,'安徽','湖南','湖北','河北')
# china_shengfen(88,'河南','陕西')

### 传递任意数量的关键字实参（利用 ** 创建一个空字典填充）
def user_msg(first,next,**end):
    msg = {}
    msg['姓名'] = first
    msg['爱好'] = next
    for i , u  in end.items():
        msg[i] = u
    return msg
a = user_msg('狗蛋','打游戏',生日 = 2022,学习 = '很差')
for k,v in a.items():
    print(k,v)
print(a)