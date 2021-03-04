import random

def Random_section():
    section=random.randint(1,254)
    return section

def Random_IP():
    IP = str(Random_section())+ '.' +str(Random_section())+ '.' +str(Random_section())+ '.' +str(Random_section())
    return IP
if __name__=='__main__':
    print(Random_IP())

