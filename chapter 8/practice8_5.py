def describe_city(city = "深圳", country = '中国'):
    """描述城市所属国家"""
    print(f"{city}在{country}\n")


describe_city("梅州")
describe_city("广州")
describe_city(country = '美国', city = '纽约')