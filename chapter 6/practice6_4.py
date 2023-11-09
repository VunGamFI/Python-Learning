dictionary = {
    'method' : '方法，是Python可对数据执行的操作',
    'comment' : '注释',
    'append' : '追加',
    'pop' : '弹出',
    'list comprehension' : '列表推导式',
    }

for dictionary_0, define in dictionary.items():
    print(dictionary_0)
    print(f"\t{define}")

dictionary['slice'] = '切片'
dictionary['set'] = '集合'
dictionary['tab'] = '制表符'
dictionary['tuple'] = '元组'
dictionary['float'] = '浮点数'

print()

for dictionary_0, define in dictionary.items():
    print(dictionary_0)
    print(f"\t{define}")