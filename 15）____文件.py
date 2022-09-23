### 读取文件时，默认读取的是字符串
### 读取整个文件
# with open ('测试文本.text') as ck:
#     a = ck.read()
#     print(a)
#     print(a.rstrip())         #利用 rstrip() 删除空白行

### 通过文件的路径去定位文件    (建议与Python文件放在同一个目录内减少读取错误）
# 文本位置 = 'D:\Python\PyCharm.txt'
# with open(文本位置) as ck:
#     a = ck.read()
#     print(a)

### 逐行读取文件
# with open ('测试文本.text') as ck:
#     for i in ck:
#         print(i.rstrip())

### 创建一个包含文件内容的列表
# with open ('测试文本.text') as ck:
#     cklb = ck.readlines()           # 从文件中读取每一行并储存到列表中
# for i in cklb:                      # 打印出列表内容
#     print(i.rstrip())

### 对文件内容进行运用
# with open ('测试文本.text') as ck:
#     cklb = ck.readlines()
# a =""
# for i in cklb:
#     a += i.strip()             # strip() 删除列表里的空格
# print(a)
# print(len(a))

### 测试文件内容是否包含某一项
# with open ('测试文本.text') as ck:
#     cklb = ck.readlines()
# a =""
# for i in cklb:
#     a += i.strip()
# b = input("输入一个数字，看是否在这个文档中：")
# if b in a :
#     print("你输入的数字在文档中")
# else:
#     print("你输入的数字不在文档中")

### 写入文件
# with open("测试写入文件.text","w") as ck:       #利用 write 的简写 w
#     ck.write("测试写入文件")

### 写入多行文件并利用 \n 换行
# with open("测试写入文件.text","w") as ck:
#     ck.write("测试写入文件\n")
#     ck.write("文件写入中\n")
#     ck.write("文件写入成功\n")

### 附加写入文件（可防止覆盖原文件内容）
# with open("测试写入文件.text","a") as ck:         #利用 append 的简写 a
#     ck.write("\n新添加第一行\n")
#     ck.write("新添加第二行\n")

### 测试用户输入添加
with open("测试写入文件.text","a") as ck:         #利用 append 的简写 a
    while True:
        a = input("输入你的信息并保存，退出请按N:\n")
        b = ck.write("\n"+a)
        if a == "N":
            break

