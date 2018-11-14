# Created by S&D, 14-11-2018.
# All rights reserved.

"""
Этот скрипт сортирует файлы на рабочем столе, перемещая их в
несколько различных папок.
"""

import os

dir = os.getcwd() + '\\'

ext_dict = {
    'Photo&Video': ('jpeg', 'png', 'mp4', 'wmv', 'jpg'),
    'Docs': ('ppt', 'pptx', 'doc', 'docx', 'pdf', 'txt', 'py', 'cpp'),
    'URLs': ('url', 'lnk')
}

if not os.path.exists(dir + 'Photo&Video'):
    os.makedirs(dir + 'Photo&Video')
if not os.path.exists(dir + 'Docs'):
    os.makedirs(dir + 'Docs')
if not os.path.exists(dir + 'URLs'):
    os.makedirs(dir + 'URLs')
if not os.path.exists(dir + 'Other'):
    os.makedirs(dir + 'Other')
if not os.path.exists(dir + 'Dirs'):
    os.makedirs(dir + 'Dirs')

for file in os.listdir(dir):

    done = False

    if file == 'sort_files.py':
        continue

    for key in ext_dict:
        for ext in ext_dict[key]:

            if file.endswith(ext):
                try:
                    os.rename(file, key + '\\' + file)
                    print('Moving:', file, '--->', key + '\\' + file)
                    done = True

                except FileExistsError:
                    # If there are a file in new folder with similar name
                    i = 1
                    while True:
                        try:
                            os.rename(file, key + '\\' + '(' + str(i) + ') ' + file)
                            print('Moving:', file, ' ---> ', key + '\\' + '(' + str(i) + ') ' + file)
                            done = True
                            break
                        except FileExistsError:
                            i += 1

    if not done:
        if os.path.isdir(file):
            if file not in ('Docs', 'Other', 'Dirs', 'Photo&Video', 'URLs'):

                try:
                    os.rename(file, 'Dirs\\' + file)
                    print('Moving:', file, '---> Dirs\\' + file)

                except FileExistsError:
                    # If there are a file in new folder with similar name
                    i = 1
                    while True:
                        try:
                            os.rename(file, 'Dirs\\' + '(' + str(i) + ') ' + file)
                            print('Moving:', file, '--->', 'Dirs\\' + '(' + str(i) + ') ' + file)
                            break
                        except FileExistsError:
                            i += 1

        else:
            try:
                os.rename(file, 'Other\\' + file)
                print('Moving:', file, '---> Other\\' + file)

            except FileExistsError:
                # If there are a file in new folder with similar name
                i = 1
                while True:
                    try:
                        os.rename(file, 'Other\\' + '(' + str(i) + ') ' + file)
                        print('Moving:', file, '--->', 'Other\\' + '(' + str(i) + ') ' + file)
                        break
                    except FileExistsError:
                        i += 1

print("""       
        Done!
        Press Enter to exit.   
    """)
input()