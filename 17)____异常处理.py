### 利用 try-except 对报错进行处理

### 示例（一）
            #先复制报错内容，并利用except进行说明
# try:
#     print(aa)
# except SyntaxError:
#     print("语法错误")
# except NameError:
#     print("重新输入")

### 示例（二）
            #让用户避免输入错误
# print("输入两个数字相除")
# print("输入”N“退出")
# while True:
#     first_number = input("\n输入第一个数字：")
#     if first_number == "N":
#         break
#     second_number = input("输入第二个数字：")
#     # answer = int(first_number) / int(second_number)
#     # print(answer)
# # 再如下执行try except 语句，添加else语句使程序无论输入什么都能正常运行下去。
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("输入有误，结果不能为0")
#     except ValueError:
#         print("输入有效字符")
#     else:
#         print(answer)

### 示例（三）
            #处理文件异常
try:
    with open ("不存在的文件.text") as ck:
        ck.read()
except FileNotFoundError:           #当文件不存在时出现报错，并打印下列语句。
    pass                            #当报错出现，并不需要打印的时候，用pass空语句跳过
    # print("这个文件不存在。")
