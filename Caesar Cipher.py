
logo = """
 _____                              _____ _       _
  / ____|                            / ____(_)     | |
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|
                                             | |
                                             |_|
"""
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#ENCRYPTION CODE
def encrypt(Plain_text, Shift_amount):
    Cipher_text = ""
    for letter in Plain_text:
        Position = alphabet.index(letter)
        New_Position = Position + Shift_amount
        New_Letter = alphabet[New_Position]
        Cipher_text+=New_Letter
    print(f"The encoded text is {Cipher_text}")


#DECRYPTION CODE
def decrypt(Cipher_text, Shift_amount):
    Plain_text = ""
    for letter in Cipher_text:
        Position = alphabet.index(letter)
        New_positin = Position - Shift_amount
        Plain_text+=alphabet[New_positin]
    print(f"The decoded text is {Plain_text}")

if direction == "encode":
    encrypt(Plain_text=text, Shift_amount=shift)
elif direction == "decode":
    decrypt(Cipher_text=text, Shift_amount=shift)
else:
    print("Error")