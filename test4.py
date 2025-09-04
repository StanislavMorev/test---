import re


def check_password(password):
    if len(password) < 10:
        print("Ненадежный пароль")
        return

    if not re.search("[A-Z]", password):
        print("Ненадежный пароль")
        return

    if len(re.findall("[0-9]", password)) < 3:
        print("Ненадежный пароль")
        return

    if not re.search("[!@#$%*]", password):
        print("Ненадежный пароль")
        return

    print("Хорош!!!")


password = input()
check_password(password)

