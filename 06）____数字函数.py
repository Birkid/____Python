
#具体应用参考  https://www.runoob.com/python/python-numbers.html

import math
pi = 3.1415
x = 1
y = 2
z = 3

print(round(pi))            #四舍五入
print(math.ceil(pi))        #返回数字类型的上入整数，例如 math.ceil(4.1) 会返回5
print(math.floor(pi))       #返回数字类型的下舍整数，例如 math.ceil(4.9) 会返回4
print(abs(pi))              #绝对值 负数返回正数
print(pow(pi,2))            #开平方
print(math.sqrt(36))        #解平方
print(max(x, y , z))        #比较最大
print(min(x, y, z))         #比较最小