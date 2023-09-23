human = ['ben', 'mike', 'john']

human.insert(0, 'mark') #开头插入数据
human.insert(2, 'marry') #中间插入数据
human.append('sam')

pop_human = human.pop()
print(f"抱歉，{pop_human.title()}，因座位不够无法邀请你")

pop_human = human.pop()
print(f"抱歉，{pop_human.title()}，因座位不够无法邀请你")

pop_human = human.pop()
print(f"抱歉，{pop_human.title()}，因座位不够无法邀请你")

pop_human = human.pop()
print(f"抱歉，{pop_human.title()}，因座位不够无法邀请你")

message = f"{human[0].title()}，请来跟我共进晚餐！"

print(message)

message = f"{human[1].title()}，请来跟我共进晚餐！"

print(message)

del human[0]
del human[0]

print(human)