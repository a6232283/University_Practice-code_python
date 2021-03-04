import detectEnglish,vigenereCipher,pyperclip

def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage=hackVigenerdDictionary(ciphertext)

    if hackedMessage!= None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackVigenerdDictionary(ciphertext):
    fo=open('dictionary.txt')
    words=fo.readlines()
    fo.close()

    for word in words:
        word=word.strip()
        decrypedText=vigenereCipher.decryptMessage(word,ciphertext)

        if detectEnglish.isEnglish(decrypedText,wordPercentage=40):
            print()
            print('Possible encryption break:')
            print('Key'+str(word)+": "+decrypedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response=input('> ')

            if response.upper().startswith('D'):
                return decrypedText
if __name__=="__main__":
    main()
