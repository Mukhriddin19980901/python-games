#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Avtomobil 
class Avto:
    def __init__(self,model, rang, korobka, narx,mator,yoqilgi,salon):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.mator=mator
        self.yoqilgi=yoqilgi
        self.salon=salon
        self.yurgani=0
    def get_model(self):
        return self.model
    def get_rang(self):
        return self.rang
    def get_korobka(self):
        return self.korobka
    def get_narx(self):
        return str(self.narx)
    def get_mator(self):
        return self.mator
    def get_yoqilgi(self):
        return self.yoqilgi
    def get_salon(self):
        return self.salon
    def get_yurgani(self):
        return self.yurgani
    def set_yurgani(self,yurgani):
        self.yurgani=str(yurgani)
    def update_yurgani(self):
        self.yurgani+=10
    def update_narx(self):
        self.narx+=1000
    def set_narx(self,narx):
        self.narx=yangi_narx
    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}  Karobka: {self.korobka} , Narxi: {self.narx} $, Yoqilg'isi: {self.yoqilgi} , Saloni : {self.salon} , Yurgani : {self.yurgani} km"
Avto_1=Avto('I20',"qizil","avtomat",35000,"3.6 N 250km/s","electromobile","elegant",)
Avto_2=Avto('KIA 5',"qora","mexanika",50000,"2.4 N 340km/s","benzin","super",)
Avto_3=Avto('Genesis',"oq","avtomat",70000,"2.4 N 450km/s","dizel","elegant",)
Avto_4=Avto('Ionique',"oq","avtomat",40000,"1.8 N 200km/s","electromobile","simple",)
Avto_2.update_narx()
Avto_1.update_narx()
Avto_2.update_yurgani()
Avto_3.set_yurgani(100)
Avto_2.get_info()


# In[6]:


# Avtosalon
class Avtosalon:
    def __init__(self,nomi,manzil,telefon,email):
        self.nomi=nomi
        self.manzil=manzil
        self.telefon=telefon
        self.email=email
        self.soni=0
        self.mashinalar=[]
    def add_avto(self,avto):
        self.mashinalar.append(avto)
        self.soni+=1
    def get_avto_num(self):
        return self.soni
    def get_nomi(self):
        return self.nomi
    def get_manzil(self):
        return self.manzil
    def get_telefon(self):
        return self.telefon
    def get_email(self):
        return self.email
    def set_telefon(self,telefon):
        self.telefon=yangi_raqam
    def set_email(self,email):
        self.email=yangi_email
    def get_avto(self):
        return [avto.get_info() for avto in self.mashinalar]
    def get_info(self):
        return f"Salon Nomi : {self.nomi} , Manzil : {self.manzil.get_info()} , Telefon : {self.telefon}, E-mail : {self.email}"
    
class Adres:
    def __init__(self, davlat,shahar_tuman,kocha_uy,):
        self.davlat=davlat
        self.shahar_tuman=shahar_tuman
        self.kocha_uy=kocha_uy
    def get_info(self):
        return f" Davlati : {self.davlat},shahar/tuman : {self.shahar_tuman},uy manzili: {self.kocha_uy} "
A_1_manzil=Adres("Koreya","Daegu","Petuelring 130 D-80809")
Avtosalon_X=Avtosalon("Hyundai",A_1_manzil,"+8210 5975 2662","hyundaiteam@email.com")
Avtosalon_X.add_avto(Avto_1)
Avtosalon_X.add_avto(Avto_2)
Avtosalon_X.add_avto(Avto_3)
Avtosalon_X.get_info()


# In[3]:


print(dir(Adres))


# In[114]:


print(dir(Avto))


# In[11]:


# faqat biz kiritgan methodlarni chiqaradi
def get_methods(clas):
    return [metod for metod in dir(clas) if  metod.endswith("__") is False]
print(get_methods(Avto),"\n",get_realmethods(Avto))


# In[17]:


# faqat o'zidagi mavjud metodlarni qaytaradi""""""
def get_realmethods(clas):
    return [metod for metod in dir(clas) if  metod.endswith("__") ]
get_realmethods(Avtosalon)
get_methods(Avtosalon)


# In[ ]:




