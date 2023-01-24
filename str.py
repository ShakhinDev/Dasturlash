#!/usr/bin/env python
# coding: utf-8

# In[16]:


name= "shakhriddin"
lname= "korakhanov"
year= 25
land= "Uzbekiston"


# In[17]:


print(f"Mening ismim {name} , familiyam {lname}  va men {year} yoshdaman. Men {land}likman")


# In[18]:


# String method matn.method() usulida ishlaydi, .upper() barcha harflarni KATTA qilib beradi
name.upper()


# In[19]:


#name.upper() qilib saqlaymiz 
x=name.upper()
print(x.lower()) # .lower() metodi harflarni kichik qilib beradi


# In[21]:


#.title() har bitta so'zdagi birinchi harfni katta qilib beradi
vname= f"{name} {lname}"
print(vname.title())


# In[24]:


#.capitalize() metodi faqat birinchi so'zning birinchi harfini katta qilib beradi
print(vname.capitalize())


# In[36]:


meva = "               olma                      "
print("Men "+meva.strip()+ " yaxshi ko'raman")


# In[39]:


name = input("What your name ?\n ")
print("Assalom alekum, "+ name.title())


# In[ ]:




