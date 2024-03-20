human_1 = {
    'first_name' : 'GamFI',
    'last_name' : 'Vun',
    'age' : 28,
    'city' : 'ShenZhen',
    }

human_2 = {
    'first_name' : 'Ming',
    'last_name' : 'Xiao',
    'age' : 25,
    'city' : 'ShanDong',
    }

human_3 = {
    'first_name' : 'Fei',
    'last_name' : 'Chen',
    'age' : 25,
    'city' : 'ZhanJiang',
}

people = [human_1, human_2, human_3]

for human in people:
    for info, m_info in human.items():
        print(f"{info}：{m_info}")
    print()