# Matthew Dam
def encode(password):
   # Loops through length of password list
   for i in range(len(password)):
       # Changes index i of password and adds 3
       password[i] = str(int(password[i]) + 3)[-1]
   # Joins all elements of the list into a new string
   global encoded_password
   encoded_password = "".join(password)
   return password


def decode(password):
   for i in range(len(password)):
       password[i] = str(int(password[i]) - 3)
       if int(password[i]) < 0:
           password[i] = str(int(password[i] + 10))
   password = "".join(password)
   print(f"The encoded password is {encoded_password}, and the original password is {password}.")


def main():
   # declare initial password
   password = ""
   # Looping until quit
   while True:
       # Displays menu
       sel = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
       # Encodes password
       if sel == "1":
           password = encode(list(input("Please enter your password to encode: ")))
           print("Your password has been encoded and stored!\n")
       if sel == "2":
           decode(password)
       if sel == "3":
           break


if __name__ == '__main__':
   main()





if __name__ == '__main__':
   main()

