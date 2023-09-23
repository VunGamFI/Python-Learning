place = ['us', 'jk', 'hk', 'en', 'hangzhou']

print(place)                            #原始列表
print(sorted(place))                    #按字母顺序排列
print(place)                            #验证原列表
print(sorted(place, reverse = True))    #按字母反序排列
print(place)                            #验证原列表
place.reverse()                         #反序列表
print(place)                            #验证列表
place.reverse()                         #反序列表
print(place)                            #验证列表
place.sort()                            #按字母顺序排列
print(place)
place.sort(reverse = True)              #按字母反序排列
print(place)