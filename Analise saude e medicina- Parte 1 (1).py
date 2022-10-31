#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas 

# In[7]:


import pandas as pd


# In[ ]:





# ## Primeira análise 

# In[8]:


dados_covid = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
dados_covid


# In[9]:


dados_covid.shape   # um dataset de 289 dados ao todo


# In[10]:


dados_covid["Province/State"].unique() #provincias afetas de maneiras unicas


# In[11]:


dados_covid.set_index("Province/State") #renomei o index para as provicias


# In[12]:


#Não vou considerar essa metrica e analise pois tem muitos campos vazios (muita disparidade)

dados_covid["Country/Region"].value_counts()


# In[16]:


#resolvi agrupar e somar para entender quanto de cada pais foi impactado

confirmados_por_pais = dados_covid.groupby("Country/Region").sum()
confirmados_por_pais.head()


# In[18]:


#dados confirmados China
confirmados_por_pais.loc["China"][2:].plot()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




