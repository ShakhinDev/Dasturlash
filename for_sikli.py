#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


mehmonlar = ['Ali','Vali', 'Eshmat','Toshmat','Chori','Panji']


# In[3]:


for mehmon in mehmonlar:
    print(f"Assalom alekum hurmatli {mehmon}. Sizni 18 fevral kungi tug'ilgan kunimga lutfan taklif etaman")
    print("Xurmat bilan Shakhriddin Korakhanov")


# In[4]:


sonlar = list(range(1,11))
for x in sonlar:
    print(f"Ushbu {x} sonining kvadrati {x**2} ga teng")


# In[5]:


dustlar =[]
print(" 5 ta eng yaqin dustingiz kim ?")
for n in range(5):
    dustlar.append(input(f"{n+1}-dustingizni ismini kiriting "))
print(dustlar)    


# Praktika
# 

# In[18]:


ismlar = ["Xadicha","Sabina","Madina","Nozima", "Sitora"]
for love in ismlar:
    print(f"{love} men seni sevaman, gapimga ishon")
print(f"kod {len(ismlar)},marta takrorlandi")


# In[20]:


sonlar = list(range(11,100,2))
for son in sonlar:
    print(f"{son}ning kubi {son**3} ga teng bo'ladi")


# In[26]:


kino = []
print(" 5 ta eng Sevimli kinolaringiz bormi?")
for x in range(5):
    kino.append(input(f"{x+1}-kinoning nomini kiriting >> "))
print(kino)


# In[34]:


# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)


# In[ ]:




