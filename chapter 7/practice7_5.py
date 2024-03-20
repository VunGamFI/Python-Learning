age = "\n请输入年龄"
age += "\n（输入“quit”退出） "

active = True

while active:
    price = input(age)

    if price == 'quit':
        active = False
    else:
        price = int(price)
        if price < 3:
            print("免费")
        elif price < 12:
            print("收费10美元")
        else:
            print("票价15美元")