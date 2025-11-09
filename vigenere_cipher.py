message = 'ino ok konam dg kheili khafanam'
key = 'kelid'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def main():
    print(vigenere(message,key))

def vigenere(message, key):
    result = ''
    result_index = ''
    number = 0
    new_key = int(len(message)/len(key)+ 1) * key
    for char in message:
        if char == ' ':
            result += ' '
            number += 1
        else :
            result_index = alphabet.find(char)+alphabet.find(f'{new_key[number]}')
            result += alphabet[result_index % len(alphabet)]
    return result

if __name__ == '__main__':
    main()