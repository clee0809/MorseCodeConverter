MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----',  ".": "·-·-·-", ",": "--··--",
                    "?": "··--··", "!": "-·-·--", "=": "-···-",
                    ":": "---···", ";": "-·-·-·", "'": "·----·",
                    "/": "-··-·", "-": "-····-", "_": "··--·-",
                    '"': "·-··-·", "(": "-·--·", ")": "-·--·-",
                    "$": "···-··-", "&": "·-···", "@": "·--·-·",
                    "+": "·-·-·"}

def encrypt(message):
    encrypted_msg = ''
    for c in message:
        if c == ' ':
            encrypted_msg += ' '
        else:
            try:
                encrypted_msg += MORSE_CODE_DICT[c.upper()]
            except KeyError:
                pass
            encrypted_msg += ' '
    return encrypted_msg

def decrypt(morse_code):
    decrypted_msg = ''
    word_list = morse_code.split('  ')
    for word in word_list:
        letter_list = word.split(' ')
        for letter in letter_list:
            try:
                char = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)]
            except:
                char=''
            decrypted_msg += char
        decrypted_msg += ' '
    return decrypted_msg

def main():
    msg = input("Enter your message: ")
    print(encrypt(msg))

    morse_msg = input("Enter morse code: ")
    print(decrypt(morse_msg))

if __name__ == '__main__':
    main()

