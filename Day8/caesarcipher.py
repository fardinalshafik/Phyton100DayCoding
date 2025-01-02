alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

choice = 1;

while choice == 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26

    # def encrypt(ttext, tshift):
    #     ciphertext = ""
    #     for i in ttext :
    #         position = alphabet.index(i)
    #         newposition = position + tshift
    #         letter = alphabet[newposition]
    #         ciphertext += letter
    #     print(f"The encoded text is {ciphertext}")

    # def decrypt(ttext, tshift):
    #     ciphertext = ""
    #     for i in ttext :
    #         position = alphabet.index(i)
    #         newposition = position - tshift
    #         letter = alphabet[newposition]
    #         ciphertext += letter
    #     print(f"The decoded text is {ciphertext}")

    # if direction == "decode":
    #     decrypt(ttext = text,tshift = shift)

    # elif direction == "encode":
    #     encrypt(ttext = text,tshift = shift)  

    def caesar(ttext, tshift, direction):
        ciphertext = ""
        for i in ttext :
            if i >= 'a' and i <= 'z':
                position = alphabet.index(i)
                if direction == "encode":
                    newposition = (position + tshift) %26
                else:
                    newposition = (position - tshift) %26
                letter = alphabet[newposition]
            else:
                letter = i
            ciphertext += letter
        print(f"The text is {ciphertext}")

    caesar(text, shift, direction)

    choice = int(input("Do you want to continue? Type 1 for yes and 0 for no:\n"))