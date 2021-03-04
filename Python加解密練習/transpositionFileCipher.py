import time, os, sys, transpositionEncrypt, transpoitionDecrypt

def main():
    inputFilename='frankenstein.encrypted.txt'

    outputFilename='frankenstein.dectypt.txt'

    mykey=10
    mymode='dectypt'

    if not os.path.exists(inputFilename):
        print('This file %s does not exits.Quitting...' %(inputFilename))
        sys.exit()
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (c)ontinue or (Q)uit?' %(outputFilename))
        response=input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj=open(inputFilename)
    conten=fileObj.read()
    fileObj.close()
    print('%sing...' %(mymode.title()))

    startTime=time.time()
    if mymode=='encrypt':
        translated=transpositionEncrypt.encryptMessage(mykey,conten)
    elif mymode=='dectypt':
        translated=transpoitionDecrypt.dectryptMessage(mykey,conten)

    totalTime=round(time.time()-startTime,2)
    print('%sion time: %s seconds' %(mymode.title(),totalTime))

    outFileObj=open(outputFilename,'w')
    outFileObj.write(translated)
    outFileObj.close()

    print('Done %sing %s (%s character).' %(mymode,inputFilename,len(conten)))
    print('%sed file is %s.' %(mymode.title(),outputFilename))

if __name__=='__main__':
    main()