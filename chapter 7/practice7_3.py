num = input("请输入一个数：")
num = int(num)

if num % 10 == 0:
    print(f"{num}是10的整数倍。")
else:
    print(f"{num}不是10的整数倍。")