def reverse_caesar_shift(message, shift):
    secret = ""
    message = message.upper()
    for letter in message:
        if letter == ' ':
            secret += letter
        else:
            secret += chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))
    print(secret)