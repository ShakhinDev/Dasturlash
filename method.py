#!/usr/bin/env python
# coding: utf-8

# In[1]:


"Salom Dunyo"


# In[6]:


x = "Salom dunyo"
x.upper() # upper metodi hamma harflarni katta qilib beradi


# In[7]:


x.lower() # hamma harflarni kichkina qilib beradi


# In[8]:


x.split() # x da berilgan malumotni alohida alohida qilib beradi


# In[12]:


x = " Dunyo sening tog'ang emas"
x.split('g') # agar qavsni ichiga kerakli harfni yozsak split metodi tashb ketadi


# In[13]:


a = 'z'#
a*25


# In[17]:


print('Bu qator boldi {0}'.format('dobavlena')) # bu metod  dobavlina sozini joylashtirishga xizmat qiladi


# In[28]:


print('Kerak emas {0} {1} {2}'.format('osmondagi', 'oy', 'Jonim')) # bu metod  dobavlina sozini joylashtirishga xizmat qiladi



# In[32]:


xisob = 55/56


# In[33]:


print(xisob)


# In[34]:


xisob


# In[37]:


print('Togri javob:{x:1.3f}'.format(x=xisob))


# 

# In[38]:


name =  "Shahriddin"


# In[39]:


print(f'Ism :{name}')


# In[42]:


my_list=['Shahriddin', 1234567 , 56.56]


# In[43]:


my_list


# In[45]:


len(my_list) # len funksiyasi list malumotlarining nechta elementdan tashkil topganini korsatadi


# my_list[0]

# In[46]:


my_list[0]


# In[48]:


my_list[1:] # ikkinchi qatordan ohirigacha korsatadi


# In[49]:


new_list = ['Kecha men dokonga bordim' , '1 kg gosht oldim', 'sabzi', 'piyoz']


# In[50]:


ikkita_list = my_list + new_list


# In[51]:


print(ikkita_list)


# In[52]:


ikkita_list


# In[53]:


type(ikkita_list)


# In[57]:


ikkita_list[0] = "Korakhanov Shakhriddin"


# In[58]:


ikkita_list


# In[59]:


number_list = [1, 3, 2, 5, 4 ,7 ,6 ,9]


# In[60]:


number_list.sort()


# In[61]:


print(number_list.sort())


# In[62]:


number_list


# In[65]:


number_list.reverse() # teskari sanoqqa qaytaradi


# In[64]:


number_list


# In[68]:


Ist = [0,1,2]


# In[69]:


Ist.pop()


# In[ ]:




