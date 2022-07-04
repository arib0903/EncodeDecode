import art

print(art.logo)

st = ""  # Using these as a storing variable to be used by the caeser function
message = ""
shift = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z']


def starter(st, message, shift):
    st1 = input("Type 'e' to start encrypting or Type 'd' to start decrypting: ").lower()
    st += st1
    if st != 'd' and st != 'e':
        print(st1)
        print("Invalid input, running again")
        starter(st='', message='', shift=0)
    message1 = input("Enter your message: ").lower()
    message += message1
    shift1 = int(input("Enter a shift number: "))
    shift += shift1
    caeser(message, shift, st)


def retry(result):
    if result == "no":
        print("Goodbye!, Thank You For Using The Cipher Program")
    else:
        starter(st='', message='', shift=0)


def caeser(message, shift, st):
    str = ""
    if st == 'd':
        shift *= -1
    for char in message:

        if char in alphabet:
            position = alphabet.index(char)  # Gets the current index of the letter in the user's inputted word
            newPosition = position + shift  # The new index of each letter with the shift applied
            if newPosition > 25:  # Checking if the updated index is above the available 0-25
                newPosition = newPosition % 26  # The out of range index is updated again with the remainder when dividing by 26.
                newLetter = alphabet[newPosition]  # Gets the new letter with the updated index from lis1
                str += newLetter
            else:
                newLetter = alphabet[newPosition]
                str += newLetter
        else:
            str += char
    print(str)
    result = input("Would You Like To Go Again?: \n")  # This happens after everything has been executed
    retry(result)


# def caeser(message, shift, st):
#     shouldCont = True
#     while shouldCont:

#         str = ""
#         if st == 'e':
#
#             for char in message:
#
#                 if char in alphabet:
#                     position = alphabet.index(char)  # Gets the current index of the letter in the user's inputted word
#                     newPosition = position + shift  # The new index of each letter with the shift applied
#                     if newPosition > 25:  # Checking if the updated index is above the available 0-25
#                         newPosition = newPosition % 26  # The out of range index is updated again with the remainder when dividing by 26.
#                         newLetter = alphabet[newPosition]  # Gets the new letter with the updated index from lis1
#                         str += newLetter
#                     else:
#                         newLetter = alphabet[newPosition]
#                         str += newLetter
#                 else:
#                     str += char
#             print(str)
#
#         else:
#             for char in message:
#                 if char in alphabet:
#                     currentPosition = alphabet.index(char)
#                     newPosition = currentPosition - shift
#                     newLetter = alphabet[newPosition]
#                     if newPosition > 25:
#                         newPosition = newPosition % 26
#                         str += newLetter
#                     else:
#                         str += newLetter
#                 else:
#                     str += char  # If there is a anything other than a letter, it will still add it on the new message
#
#             print(str)
#         result = input("Would You Like To Go Again?:  \n") #This happens after everything has been executed
#         if result == "no":
#             shouldCont = False
#             print("Goodbye!, Thank You For Using The Cipher Program")
#         #Else, the while loop continues to execute until 'result' = no

# def encode(store, shift):

#     str = ""
#     # for x in store:
#     #     for y in range(len(lis1)):
#     #         z = lis1[y]
#     #         if x == z:
#     #             # print(acc)
#     #             sm = y + shift
#     #             if sm > 25:
#     #                 sm = y%26
#     #                 str += lis#     1[sm]
#     #             else:
#     #                 str += lis1[sm]
#     # print(str)
#     for x in store:
#         position = lis1.index(x)  # Gets the current index of the letter in the user's inputted word
#         newPosition = position + shift  # The new index of each letter with the shift applied
#         if newPosition > 25:  # Checking if the updated index is above the available 0-25
#             newPosition = newPosition % 26  # The out of range index is updated again with the remainder when dividing by 26.
#             newLetter = lis1[newPosition]  # Gets the new letter with the updated index from lis1
#             str += newLetter
#         else:
#             newLetter = lis1[newPosition]
#             str += newLetter
#     print(str)
#
#
# def decode(store, shift):
#     str = ""
#     for x in store:
#         currentPosition = lis1.index(x)
#         newPosition = currentPosition - shift
#         newLetter = lis1[newPosition]
#         if newPosition > 25:
#             newPosition = newPosition % 26
#             str += newLetter
#         else:
#             str += newLetter
#     print(str)

# shouldCont = True
# while  shouldCont:
#     st = input("Type 'e' to start encrypting or Type 'd' to start decrypting: ").lower()
#
#     message = input("Enter your message: ").lower()
#     shift = int(input("Enter a shift number: "))
#     caeser(message, shift, st)
#     result = input("Would You Like To Go Again?:  \n")
#     if result == "no":
#         shouldCont = False
#         print("Goodbye!, Thank You For Using The Cipher Program")


starter(st, message, shift)
