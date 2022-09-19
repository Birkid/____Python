# if语句 = 如果条件为真（True）将会执行的语句 https://www.runoob.com/python3/python3-if-example.html

age = int(input('你今年多大年纪了？ \n'))            #字符串加 /n 换行

if age >= 1000:
    print('千年的王八万年的龟。 ')
elif age >= 18:
    print('你已经是个成年人了')
elif age <= 0:
    print('怎么？ 你还在娘胎里就会说话了吗？ ')
else:
    print('根据法律法规，未成年每天上网时间不能大于俩小时哟！ ')


