#!/usr/bin/env python
# coding: utf-8

# In[58]:


import os

path = 'C:\\Users\\admin1\\Desktop\\resources\\Python\\Ameredev\\AVO VIDEOS'              # make sure to use '\\' in file directory string

main_folder = os.listdir(path)
dictionary = {}
subpath = []

for i in range(0, len(main_folder)):
    subpath.append(path+'\\'+main_folder[i])               # defines file paths for each folder
    dictionary[main_folder[i]] = os.listdir(subpath[i])   # assigns key and value pairs for dictionary using file paths


index = 0

for i in dictionary:                            # dictionary[i] is each subfolder; a list of video files
                                               
        
    if len(dictionary[i]) > 1:                  # protects against empty folders
        print('In '+ i + ' folder:')
        
        old_first_file_path = subpath[index]+'\\'+dictionary[i][0]
        new_first_file_path = subpath[index]+'\\'+'As Found.mp4' 

        if 'As Found.mp4' not in dictionary[i]:
            os.rename(old_first_file_path,new_first_file_path)   # renames file given new file path name
            old_first_file_name =  dictionary[i][0]
            print('Renamed '+ old_first_file_name + ' to ' + 'As Found.mp4')
            dictionary[i][0] = 'As Found.mp4'       # changes name value in dictionary of the first file to 'As Found'

        else:
            print('Already have As Found')
#---------------------

        old_last_file_path = subpath[index]+'\\'+dictionary[i][-1]
        new_last_file_path =  subpath[index]+'\\'+'As Left.mp4'
        
        if 'As Left.mp4' not in dictionary[i]:
            os.rename(old_last_file_path,new_last_file_path)    # renames file given new file path name
            old_last_file_name =  dictionary[i][-1] 
            print('Renamed '+ old_last_file_name + ' to ' + 'As Left.mp4')
            dictionary[i][-1] = 'As Left.mp4'        # changes name value in dictionary of the last file to 'As Left'       

        else:
            print('Already have As Left')
            
        
#----------------------
    if len(dictionary[i]) > 2:                  # if number of video files is more than 2, a leak was recorded
        
        leaks = dictionary[i].copy()
        leaks.remove('As Found.mp4')
        leaks.remove('As Left.mp4')

        for l in range(0,len(leaks)):
            old_leak_file_path = subpath[index]+'\\'+leaks[l]
            new_leak_file_name = input('Leak detected in '+ i + ' folder...Rename '+ leaks[l] +' as: ')+'.mp4'
            new_leak_file_path = subpath[index]+'\\'+new_leak_file_name
            os.rename(old_leak_file_path,new_leak_file_path)
            leak_index = dictionary[i].index(leaks[l])
            dictionary[i][leak_index] = new_leak_file_name   #renames leaks within deictionary
            
    if len(dictionary[i])>0:
        print(i+' Files: '+str(dictionary[i]))
        print()
            
    index += 1  


# In[ ]:





# In[ ]:





# In[ ]:




