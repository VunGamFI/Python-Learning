dictionary = {
    'nile' : 'egypt',
    'chang jiang' : 'china',
    'amazon river' : 'brazil',
    }

for river, country in dictionary.items():
    print(f"The {river.title()} runs through {country.title()}.")