#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

path = 'D:\\images'              # make sure to use '\\' in file directory string

main_folder = os.listdir(path)
dictionary = {}
subpath = []

for i in range(0, len(main_folder)):
    subpath.append(path+'\\'+main_folder[i])               # defines file paths for each folder
    dictionary[main_folder[i]] = os.listdir(subpath[i])   # assigns key and value pairs for dictionary using file paths

index = 0
subpath_files = []

arg = input('Delete all files in Camera folders? Type Y to proceed...')
if arg == 'Y':
    for i in range(0,len(subpath)):

        if len(os.listdir(subpath[i])) > 1:
            files = os.listdir(subpath[i])
            for j in range(0,len(files)):
                #print(subpath[i]+'//'+files[j])
                os.remove(subpath[i]+'//'+files[j])
                print('Removed '+ files[j]+' from '+subpath[i])
else:
    print('Files Not Deleted')
        
        


# In[ ]:




