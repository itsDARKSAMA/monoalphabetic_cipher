letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
keys = [
    'q', 'w', 'e', 'c', 't', 'y', 'g', 'i', 'o', 'p', 'f', 's', 'd',
    'm', 'u', 'h', 'j', 'k', 'l', 'z', 'x', 'r', 'v', 'b', 'n', 'a'
]

letters_list = []


def encrypt():
    plain_text = str(input("Enter you Text >> ")).lower()

    for l in plain_text:
        key_number = letters.index(l)
        new_letter = keys[key_number]
        letters_list.append(new_letter)

    encrypt_text = ''.join(letters_list)
    letters_list.clear()
    print(encrypt_text)


def decrypt():
    cipher_text = str(input("Enter you Cipher >> ")).lower()
    for l in cipher_text:
        letter_number = keys.index(l)
        new_letter = letters[letter_number]
        letters_list.append(new_letter)

    plain_text = ''.join(letters_list)
    letters_list.clear()
    print(plain_text)


def about():
    header()
    print('Ucas Gaza')
    print('Ucas ID : 120190071')


def header():
    print("************ MonoAlphabet-Cipher ************")
    print("     created By Abdelrahman Almajayda        ")
    print("*********************************************\n")


if __name__ == "__main__":
    header()
    while (True):
        print('1- Encrypt / 2- Decrypt / 3- About / 0- exit')
        try:
            op = int(input('input : '))
            if (op == 1):
                encrypt()
            elif (op == 2):
                decrypt()
            elif (op == 3):
                about()
            elif (op == 0):
                break
        except:
            print('please enter an intger number')
