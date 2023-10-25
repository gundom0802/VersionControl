# Matthew Dam
def encode (password):
   encoded_password = ""
   for number in password:
       added_number = str((int(number) + 3) % 10)  # add each number by 3
       encoded_password += added_number
   return encoded_password


def decode (encoded_password):
   password = ""
   for number in encoded_password:
       subtracted_number = str((int(number) - 3) % 10)  # subtract each number by 3
       password += subtracted_number
   return password
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")


        elif choice == "2":
            print(
                f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            print("")
        elif choice == "3":
            break



if __name__ == '__main__':
   main()

