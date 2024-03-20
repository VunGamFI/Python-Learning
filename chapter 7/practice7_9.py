sandwich_orders = [
    "肉松三明治",
    "五香烟熏牛肉",
    "酱牛肉番茄三明治",
    "五香烟熏牛肉",
    "五香烟熏牛肉",
    "金枪鱼三明治",
    "煎起司三明治",
    "五香烟熏牛肉",
    ]
finished_sandwich = []

print("本店的五香烟熏牛肉已售罄")

while "五香烟熏牛肉" in sandwich_orders:
    sandwich_orders.remove("五香烟熏牛肉")

while sandwich_orders:
    finish = sandwich_orders.pop()
    print(f"{finish}做好了！")

    finished_sandwich.append(finish)

print()

for sandwich in finished_sandwich:
    print(sandwich)