# import detectEnglish
# detectEnglish.isEnglish('Is this sentence English text?')

UPPERLETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS_AND_SPACE=UPPERLETTERS+UPPERLETTERS.lower()+' \t\n'

def loadDictionary():
    dictionaryFile=open('dictionary.txt')
    englishWords={}

    for word in dictionaryFile.read().split('\n'):
        englishWords[word]=None

    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS=loadDictionary()

def getEnglishCount(message):
    message=message.upper()
    message=removeNonLetters(message)
    possibleWord=message.split()

    if possibleWord==[]:
        return 0.0

    matches=0
    for word in possibleWord:
        if word in ENGLISH_WORDS:
            matches+=1
    
    return float(matches)/len(possibleWord)


def removeNonLetters(message):
    lettersOnly=[]

    for symble in message:
        if symble in LETTERS_AND_SPACE:
            lettersOnly.append(symble)

    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
    woedsMatch=getEnglishCount(message)*100>=wordPercentage
    numLetters=len(removeNonLetters(message))
    messageLettersPercentage=float(numLetters)/len(message)*100
    letteresMatch=messageLettersPercentage>=letterPercentage
    return woedsMatch and letteresMatch