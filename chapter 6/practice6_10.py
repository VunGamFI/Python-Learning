favorite_nums = {
    'Mike' : ['2', '15', '21'],
    'Bob' : ['15', '99', '999', '100'],
    'Marry' : ['23', '19'],
    'Jack' : ['9', '21', '14'],
    'Tim' : ['0', '119', '991', '56', '95'],
    }

for name, nums in favorite_nums.items():
    print(f"\n{name}'s favorite numbers: ")
    for num in nums:
        print(f"\t{num}")