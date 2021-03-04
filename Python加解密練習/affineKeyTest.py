import affineCiper,Cryptomath

message='Make things as simple as possible,but not simpler.'

for keyA in range(2,80):
    key=keyA*len(affineCiper.SYMBOLS)+1

    if Cryptomath.gcd(keyA,len(affineCiper.SYMBOLS))==1:
        print(keyA,affineCiper.encryptMessage(key,message))