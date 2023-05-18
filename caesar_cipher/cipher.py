import string


def encrypt(text, shift):
    """
    Encrypts a message depending on the number of shifted values
    :param text: A message
    :param shift: An int
    :return: An encrypted message
    """
    # creates a list of the alphabet
    alphabet = list(string.ascii_lowercase)
    # creates a list of the shifted alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    secret_message = ""

    for char in text:
        if char.lower() in alphabet:
            if char.isupper():
                index = alphabet.index(char.lower())
                secret_message += shifted_alphabet[index].upper()
            else:
                index = alphabet.index(char)
                secret_message += shifted_alphabet[index]
        else:
            secret_message += char
    return secret_message


def decrypt(text, shift):
    return encrypt(text, -shift)


# worked with Brenden Moore to solve
def crack(text):
    for shift in range(26):
        cracked = encrypt(text, -shift)
        if "the" in cracked.lower() and "of" in cracked.lower():
            return cracked
    return ""


if __name__ == "__main__":
    # crack("Hello")
    pass
