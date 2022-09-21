## 面向对象的编程

### 创建和使用类，示例（一）

# class 小狗():
#     "模拟尝试"
#     def __init__(self,name ,age):
#         "初始化名字和年龄"
#         self.name = name
#         self.age = age
#     def sit(self):                  #创建一个蹲下函数
#         print(self.name + "蹲下")
#     def stand(self):                #创建一个站起来函数
#         print(self.name + "站起来")
#
# dog = 小狗('旺财',6)
# dog2 = 小狗('笨笨',7)
# print("我的小狗叫"+ dog.name + "。它今年"+ str(dog.age)+"岁了")
# print("还有一条叫"+ dog2.name + "。它今年"+ str(dog2.age)+"岁了")
# dog.sit()
# dog2.sit()
# dog.stand()

### 示例（二）
class 诛仙():
    def __init__(self,门派,武器,坐骑,技能):
        self.门派 = 门派
        self.武器 = 武器
        self.坐骑 = 坐骑
        self.技能 = 技能
        self.速度= 0          #新增函数并赋值
    def 角色(self):
        角色信息 = self.门派 + self.坐骑 + self.武器 + self.技能
        print("创建角色成功."+ "\n你的人物门派是:"+self.门派+"\n坐骑是："+
              self.坐骑+"\n武器是:"+self.武器+"\n技能是:"+self.技能)
        return 角色信息

    # def 设定角色速度(self,角色速度):            #创建一个设定角色速度函数，太过麻烦，不如直接修改值方便
    #    self.速度 = 角色速度
    def 人物速度(self):
        print("人物移动速度是:"+ str(self.速度))

a = 诛仙("青云","剑","马","御剑诀")
b = 诛仙("鬼王","刀","驴","鬼斩")
print(a.角色())
# a.设定角色速度(22)
a.速度 = 44                   #直接修改值
a.人物速度()                   #

