
# coding: utf-8

# In[4]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

sentence_final = [(sub+" "+ vrb + " " + oj) for sub in subject for vrb in verb for oj in obj]
for sentence in sentence_final:
 print (sentence)

