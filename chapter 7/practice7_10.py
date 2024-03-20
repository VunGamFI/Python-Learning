vocations = {}

active = True

while active:
    name = input("\n姓名：")
    place = input("\n您梦想中的度假胜地是：")

    vocations[name] = place

    repeat = input("还想让其他人参与调查吗？（yes / no）")
    if repeat == 'no':
        active = False

print("\n--- 调查结果 ---")
for name, place in vocations.items():
    print(f"{name}梦想中的度假胜地为{place}")