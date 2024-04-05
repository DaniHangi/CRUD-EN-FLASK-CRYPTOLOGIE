from contextlib import nullcontext
import math as m



def rsa(plainText,n,e):

    print('=========plainText======>', plainText)

    print('========n=======>', n)
    print('=========e======>', e)
    
    CipherText= []
    codechart = "abcdefghijklmnopqrstuvwxyz"
    chaine = ""

    for key in codechart:
        for i in plainText:
            if key == i:
                char = codechart.index(key)
                # print(char)
                c = int(m.pow(char,e) % n)
                CipherText.append(c)
                print('_________ciphertext_______', CipherText, '__________________________')

                truechaine = chaine.join([str(item) for item in CipherText])

                # print('________________', chaine, '__________________________')
    print('======',truechaine)           
    return truechaine 


      

def dech_rsa(cryptedText,d,n):
    plainText = ""
    codechart = "abcdefghijklmnopqrstuvwxyz"
    char = nullcontext
    for i in cryptedText:
        char = m.pow(i,d) % n
        for i in range (len(codechart)):
            if i == char:
                plainText == codechart[i]
    return plainText

