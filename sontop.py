#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#  sontopish
import random

def son(x=10):
    A=0
    input(f'Son topish o\'yini o\'ynaymizmi? Men 1 dan {x} gacha son oylayman siz toping :')
    N=random.randint(1,x)
    for i in range(1,x):
        S=int(input("Men o'ylagan son : "))
        A+=1
        if N==S:
            print(f"Siz {A} martada to'g'ri topdingiz")
            break
        elif S>N:
            print('Men o\'ylagan son bundan kichik')
        else:
            print("'Men o'ylagan son bundan katta")
        if i==10:
            print(f"Siz 10 ta urinishda ham topolmadingiz men {N} ni o'ylagan edim")
            break
    return A
def son_com(x=10):
    B=0
    input(f"Endi Siz ham 1 dan {x} gacha son o'ylang men topaman ")
    M=random.randint(1,x)
    for i in range(x):
        B+=1
        print(f"Siz o'ylagan son  : {M}  ")
        D=input("Agar to'g'ri bo'lsa '#' agar  siz o'yalgan son katta bundan bo'lsa '>' kichik bo'lsa '<' ni bosing : ")
        if D=="#":
            print(f"men {B} martada to'g'ri topdim")
            break
        if D==">":
            M+=1
        if D=="<":
            M-=1
    return B 
def OK(x=10):
    y=True
    while y:
        a=son(x)
        b=son_com(x)
        if a<b:
            print('Tabriklar!')
        elif a>b:
            print("game over")
        else:
            print("Durang")
        y=int(input('yana oynaysizmi ha(1) yoq(0)'))
print(OK())

