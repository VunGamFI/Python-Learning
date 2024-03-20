def show_message(messages):
    """打印信息"""
    for message in messages:
        print(f"{message}")


def send_message(b_message, copy_messages):
    """转移信息"""
    while b_message:
        change = b_message.pop()
        copy_messages.append(change)


message = [
    "test_1",
    "test_2",
    "test_3",
    ]
copy_message = []

send_message(message[:], copy_message)
print()
show_message(message)
print()
show_message(copy_message)