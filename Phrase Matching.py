#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
nlp = spacy.load('en_core_web_sm')


# In[2]:


from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)


# In[3]:


#SolarPower
#Solar-power
#Solar power
pattern1 = [{'LOWER':'solarpower'}]
pattern2 = [{'LOWER':'solar'}, {'IS_PUNCT':True}, {"LOWER":"power"}]
pattern3 = [{'LOWER':'solar'}, {'LOWER':'power'}]


# In[4]:


matcher.add("SolarPower", None, pattern1, pattern2, pattern3)


# In[5]:


doc = nlp(u"The Solar Power industry continues to grow as solar power increases. Solar-power is amazing.")


# In[6]:


found_matches = matcher(doc)
print(found_matches)


# In[7]:


for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)


# 

# In[ ]:




