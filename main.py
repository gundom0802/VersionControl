# Encoder function
def encode():
    # Converts input string into list
    password = list(input("Please enter your password to encode: "))
    # Loops through length of password list
    for i in range(len(password)):
        # Changes index i of password and adds 3
        password[i] = str(int(password[i]) + 3)[-1]
    # Joins all elements of the list into a new string
    password = "".join(password)
    print("Your password has been encoded and stored!\n")


if __name__ == '__main__':
    # Looping until quit
    while True:
        # Displays menu
        sel = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        if sel == "1":
            encode()
        if sel == "2":
            pass # REPLACE "PASS" WITH DECODER FUNCTION CALL
        if sel == "3":
            break
