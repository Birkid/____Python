### 示例（一）
# name = input('你的名字叫什么?: ')
# age = int(input('你今年多大了？: '))        #根据需求，设定名字为整数位
# height = float(input('你的身高是多少？: '))      #根据需求，身高可以延申到小数点。
#
# print('你好'+ name +' 欢迎光临！')
# print('你的年龄是'+ str(age)+ '!')
# print('你的身高是'+ str(height) + '!')

### 增加提示信息获取输入！ +=
# shuru = "如果你告诉我你是谁，我将给你发信息"
# shuru += "\n如果你不告诉我你是谁，就算了！"
# shuru += "\n现在在下方输入你的名字吧:\n"
# name = input(shuru)
# print("\n你好"+name+"!")

### 求模运算符示例（一）
# number = int(input("输入一个数字，我能告诉你能不能被2整除:\n"))
# if number % 2 == 0:
#     print("你输入的数字能被2整除")
# else:
#     print("你输入的数字不能被2整除")

### 选择终止运行（whiel循环）
# shuru = "如果你告诉我你是谁，我将给你发信息"
# shuru += "\n如果你不告诉我你是谁，就说“是”！"
# shuru += "\n现在在下方输入你的名字吧:\n"
# name = ""
# while name != "是":
#     name = input(shuru)
#     if name != "是":
#         print("\n你好" + name + "!")
#     elif name == "是":
#         print("再见")

### 选择终止运行（true 和 false  break终止）
# shuru = "如果你告诉我你是谁，我将给你发信息"
# shuru += "\n如果你不告诉我你是谁，就说“是”！"
# shuru += "\n现在在下方输入你的名字吧:\n"
# name = True         #可直接简写成为while True  循环为真会一直循环，到后面跳到break停止。
# while name:
#     name = input(shuru)
#     if name == "是":
#         break           #选项1
#        # name = False    #选项2
#        # print("\n你好" + name + "再见!")       布尔类型的值不能打印
#     else:
#         print("\n你好" + name + "!")

### cotinue 返回循环开头
# number = 0
# while number < 10:
#     number += 1
#     if number % 2 == 0:
#         continue
#     print(number)

### while 循环在列表中的使用
# 未验证用户 = ['王二','狗蛋','铁锤','钢镚']
# 验证用户 = []
# while 未验证用户:
#     待增加用户 =  未验证用户.pop()
#     print("用户增加："+待增加用户)
#     验证用户.append(待增加用户)
# print("\n所有用户验证完毕：")
# for i in 验证用户:
#     print(i)

### while 循环删除列表中的特定值
# china = ['安徽','安徽','北京','南京','上海','广州']
# china.pop(5)             #方法一： pop 删除列表值所在的排序
# china.remove('上海')      #方法二： remove 删除列表中包含的值的名称
# print(china)
# while '安徽' in china:    #通过while 删除所有所给值
#     china.remove('安徽')
# print(china)

### while 循环，获取不断的输入填充字典
调查 = {}
问题= True
while 问题:
    名字 = input("\n你的名字叫什么？\n: ")
    爱好 = input("\n你的爱好是什么？\n: ")
    调查[名字]=爱好           #可以解释为 字典[第几页] = 里面有什么
    询问 = input("\n还有别的需要回答吗？是或者不\n:")
    if 询问 == '不':
        问题 = False
for 名字 , 爱好 in 调查.items():
    print(名字 + "你喜欢"+ 爱好)


