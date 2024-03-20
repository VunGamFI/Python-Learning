def make_sandwich(*toppings):
    """概述要在三明治中添加的食材"""
    print("添加以下食材：")
    for topping in toppings:
        print(f"\t- {topping}")


make_sandwich("热狗")
make_sandwich("热狗", "火腿", "鸡蛋")
make_sandwich("煎蛋", "火腿")