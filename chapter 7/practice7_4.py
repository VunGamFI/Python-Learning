requested_topping = "\n请输入需要加的配料"
requested_topping += "\n（输入“quit”结束加料） "

active = True

while active:
    topping = input(requested_topping)

    if topping == 'quit':
        active = False
    else:
        print(f"要在披萨里添加{topping}")