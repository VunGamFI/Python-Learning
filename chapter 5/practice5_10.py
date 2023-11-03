current_users = ['admin', 'john', 'mike', 'jaden', 'lucy']
new_users = ['mike', 'john', 'marry', 'Joden', 'start']

copy_new_users = []

for temp in new_users:
    copy_new_users.append(temp.lower())

for new_user in copy_new_users:
    if new_user in current_users:
        print("该用户名已存在，请输入新的用户名！")
    else:
        print("该用户名未被使用")