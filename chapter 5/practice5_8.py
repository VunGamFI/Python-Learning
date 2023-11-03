users = ['admin', 'john', 'mike', 'jaden', 'lucy']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")