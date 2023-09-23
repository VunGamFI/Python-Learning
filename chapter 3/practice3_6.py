human = ['ben', 'mike', 'john']

print(f"{human[1].title()}无法赴约")

human[1] = 'mark'

human.insert(0, 'marry')
human.insert(2, 'jack')
human.append('lucy')

message = f"{human[0].title()}，{human[1].title()}，{human[2].title()}，{human[3].title()}，{human[4].title()}，{human[5].title()}，请来跟我共进晚餐！"
print(message)