favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
    }

human = ['jen', 'mike', 'sarah', 'jack', 'ben', 'edward', 'phil']

for name in human:
    print(f"Hi {name.title()}.")

    if name in favorite_languages.keys():
        print("Thanks for your poll!")
    else:
        print("Please take our poll!")