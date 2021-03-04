import pyperclip

def main():

    message="Common sense is not so common."
    key=8

    ciphertext=encryptMessage(key,message)

    print(ciphertext+'|')

    pyperclip.copy(ciphertext)

def encryptMessage(key,message):
    ciphertext=['']*key
 
    for column in range(key):
        currentIndex=column

        while currentIndex < len(message):
            ciphertext[column]+=message[currentIndex]

            currentIndex+=key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
