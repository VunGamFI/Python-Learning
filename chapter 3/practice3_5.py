human = ['ben', 'mike', 'john']

print(f"{human[1].title()}无法赴约")

human[1] = 'mark'
message = f"{human[0].title()}，{human[1].title()}，{human[2].title()}，请来跟我共进晚餐！"

print(message)