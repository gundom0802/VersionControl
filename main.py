def encode():
    password = list(input("Please enter your password to encode: "))
    for i in range(len(password)):
        password[i] = str(int(password[i]) + 3)[-1]
    password = "".join(password)
    print(password)
    print("Your password has been encoded and stored!\n")


if __name__ == '__main__':
    while True:
        sel = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        if sel == "1":
            encode()
        if sel == "2":
            pass
        if sel == "3":
            break
