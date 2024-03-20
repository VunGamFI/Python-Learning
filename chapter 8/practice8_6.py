def city_country(city, country):
    """描述城市所属国家"""
    city_count = f"{city.title()}，{country.title()}\n"
    return city_count


city_1 = city_country("深圳", "中国")
city_2 = city_country("纽约", "美国")
city_3 = city_country("东京", "日本")

print(city_1)
print(city_2)
print(city_3)