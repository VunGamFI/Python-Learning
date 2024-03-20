favorite_places = {
    'Ben' : ['China', 'US', 'Japan'],
    'Mike' : ['England'],
    'Marry' : ['China', 'Russia'],
    }

for name, places in favorite_places.items():
    print(f"\n{name}喜欢的地点有：")
    for place in places[:]:
        print(f"\t{place}")