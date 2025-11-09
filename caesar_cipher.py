message ='first code in the new season'
shift = 5
alphabet = 'abcdefghijklmnopqrstuvwyxz'
def main():
    print(encrypt(message,shift))
    print(decrypt(cipher(message,shift),shift))

def cipher(message, shift, act = 1):
    result = ''
    for char in message.lower():
        if char == ' ':
            result += char
        else:
            index = alphabet.find(char)
            result+= alphabet[(index + shift * act) % len(alphabet)]
    return(result)

def encrypt(message,shift):
    return cipher(message, shift, 1)

def decrypt(message, shift):
    return cipher(message, shift, -1)
        
    
if __name__ == '__main__' :
    main()


