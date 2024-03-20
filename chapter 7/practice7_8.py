sandwich_orders = ["肉松三明治", "酱牛肉番茄三明治", "金枪鱼三明治", "煎起司三明治"]
finished_sandwich = []

while sandwich_orders:
    finish = sandwich_orders.pop()
    print(f"{finish}做好了！")

    finished_sandwich.append(finish)

print()

for sandwich in finished_sandwich:
    print(sandwich)