#!/usr/bin/env python
# coding: utf-8

# In[ ]:


coffee={
    'Maximum' :  400,
    'zahira' : {
        'shakar': 3000,
        'shokolad': 3000,
        'sut': 5000,
        'suv': 5000
    },
    'Tangalar' : {
        '100' : 100,
        '50'  : 200,
        '10'  : 1000
    },
    'Qahvalar': {
        'Americano': 3000,
        'Latte' : 3000,
        'Cappucino' : 3000,
        'Espresso' : 4000,
    },
    'Americano':{
        'Americano': 30,
        'shakar': 10,
        'shokolad' : 30,
        'sut' : 30,
        'suv' : 150,
        'narxi' : 150
    },
    'Latte': {
        'Latte' : 30,
        'shakar': 10,
        'shokolad' : 50,
        'sut': 100,
        'suv' : 50,
        'narxi': 160
    },
    'Cappucino' :{
        'Cappucino' : 30,
        'shakar': 10,
        'shokolad' : 50,
        'sut': 100,
        'suv' : 50,
        'narxi': 180
    },
    'Espresso' :{
        'Espresso' : 40,
        'shakar': 15,
        'shokolad' : 50,
        'sut': 100,
        'suv' : 30,
        'narxi' : 200
    }  
}
def coffeeyn(coffename):
    if coffee["Qahvalar"][coffename]<coffee[coffename][coffename]:
        return False
    for i in coffee['zahira'].keys():
        if coffee['zahira'][i]<coffee[coffename][i]:
            return False
    return True
def sotildi(coffename):
    coffee["Qahvalar"][coffename]-=coffee[coffename][coffename]
    for i in coffee['zahira'].keys():
        coffee['zahira'][i]-=coffee[coffename][i]
def isqaytim(S):
    qayt=coffee['Tangalar'].copy()
    for i in qayt.keys():
        while S>=int(i) and qayt[i]>=1:
            qayt[i]-=1
            S-=int(i)
    return S
def pul(S,dicti,satr):
    qaytim=""
    while True:
        if S==coffee[satr]['narxi']:
            for i in coffee['Tangalar'].keys():
                coffee['Tangalar'][i]+=dicti[i]
            return 0
        if S>coffee[satr]['narxi']:
            S-=coffee[satr]['narxi']
            for i in coffee['Tangalar'].keys():
                coffee['Tangalar'][i]+=dicti[i]
            if isqaytim(S)>0:
                print(f"Bazada {S} So'm qaytim yetmayapti davom etasizmi?")
                A=int(input("1 ha 0 yo'q : "))
                if A==1:
                    pass
                if A==0:
                    for i in coffee['Tangalar'].keys():
                        coffee['Tangalar'][i]-=dicti[i]
                        qaytim+=str(dicti[i])+" ta "+i+"So'mlik qaytarildi"
                        print(qaytim)
                    return 1        
            for i in dicti.keys():
                sana=0
                while S>=int(i) and coffee['Tangalar'][i]>=1:
                    coffee['Tangalar'][i]-=1
                    sana+=1
                    S-=int(i)
                qaytim += str(sana) + " " + i + " so'mlik "
            return qaytim
        if S<coffee[satr]['narxi']:    
            print("Pulingiz yetarli emas")
            for i in coffee['Tangalar'].keys():
                if coffee[satr]['narxi']-S>=int(i):
                    qiy = int(input(f"{i} somlik"))
                    dicti[i] += qiy
                    S+=qiy*int(i)
while True:
    print(coffee)
    for j,i in zip(range(1,len(coffee['Qahvalar'].keys())+1),coffee['Qahvalar'].keys()):
        print(j,'-',i,coffee[i]['narxi'])
    t=int(input('tanlang : '))
    if t==10:
        break
    satr=list(coffee['Qahvalar'].keys())[t-1]
    if not coffeeyn(satr):
        print('Siz buyurtma bergan kofe mavjud emas')
        continue
    print(f"Siz {satr} buyurtma berdingiz Narxi:  {coffee[satr]['narxi']} so'm")
    print(f"Maximum summa: {coffee['Maximum']}")
    dicti = {}; S=0 ;
    for i in coffee['Tangalar'].keys():
        dicti[i] = int(input(f"{i} somlik : "))
        S+=dicti[i]*int(i)
        if S>coffee['Maximum']:
            print('Ko\'p pul kiritib yubordingiz')
            break
    qaytim = pul(S,dicti,satr)
    if qaytim==0:
        print(f'Sizning Kofengiz {satr}')
        sotildi(satr)
    elif qaytim==1:
        continue
    else:
        print('Sizning qaytimingiz : '+ qaytim)
        print(f'Sizning Kofengiz {satr}')
        sotildi(satr)

