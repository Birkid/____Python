
### 调用模块 json 储存数据

# json.dump() 接受两个实参，要储存的数据以及储存数据据的文件对象。
# import json
# numbers = [1,2,3,4,5,6,7,8,9,10]
# 文件名称 = "测试存储.json"
# with open(文件名称,"w") as ck:
#     json.dump(numbers,ck)

# json.load() 读取文件对象内容
# import json
# with open("测试存储.json") as ck:
#     numbers = json.load(ck)
# print(numbers)

### 保存读取用户生成的数据
# import json
# 用户名 = input("输入你要保存的数据：")
# with open("测试存储.json","w") as ck:
#     json.dump(用户名,ck)
#     print("即将保存你输入的："+ 用户名)
# with open("测试存储.json","r" ) as ckk:
#     json.load(ckk)
#     print("你保存的数据是"+ 用户名)

#当文件不存在时，尝试输入避免报错
# import json
# try:
#     with open("测试存储.json") as ck:
#         用户名 = json.load(ck)
# except FileNotFoundError:           #当文件不存在时出现报错，并打印下列语句。
#     pass
#     用户名 = input("输入你要保存的数据：")
#     with open("测试存储.json", "w") as ckk:
#         json.dump(用户名,ckk)
#         print("即将你保存的数据是" + 用户名)
# else:
#     print("保存的用户数据是"  +  用户名)

### 重构
        #把代码分为一系列具体的函数
#示例
import json
def 查询数据():
    try:
        with open("测试存储.json") as ck:
            用户名 = json.load(ck)
    except FileNotFoundError:
        pass
    else:
        return 用户名
def 新增数据():
    用户名 = input("输入你要保存的数据：")
    with open("测试存储.json", "w") as ckk:
        json.dump(用户名, ckk)
    return 用户名

def 保存数据():
    保存 = 查询数据()
    if 保存:
        print("你保存的数据是：")
    else:
        保存 = 新增数据()
        print("即将保存你的数据：")
保存数据()

