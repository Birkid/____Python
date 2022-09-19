### and 和 or 的具体应用。
wendu = int(input('今天外面的温度是多少？\n '))

if wendu >= 16 and wendu <= 30:
    print('天气真好，我们出去玩吧！ ')
elif wendu < 16 or wendu >30:
    print('天气那么糟糕，还是在家玩吧！ ')