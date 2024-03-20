pet_1 = {
    '类型' : '狗',
    '主人' : '小明',
    }

pet_2 = {
    '类型' : '猫',
    '主人' : '小刚',
    }

pet_3 = {
    '类型' : '仓鼠',
    '主人' : '小红',
    }

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for info, m_info in pet.items():
        print(f"{info}：{m_info}")
    print()