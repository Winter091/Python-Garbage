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
    'Docs':        ('ppt', 'pptx', 'doc', 'docx', 'pdf', 'txt', 'py', 'cpp'),
    'URLs':        ('url', 'lnk')
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


def move(file, folder):

    # User decide to move file or not
    while True:
        ans = input('Move {} to {}? (Y/N) >'.format(file, folder))
        if ans.lower() == 'y':
            break
        elif ans.lower() == 'n':
            return 0

    try:
        os.rename(file, folder + '\\' + file)
        print('Moving', file, 'to', key)

    except FileExistsError:
        # If there are a file in new folder with similar name
        i = 1
        while True:
            try:
                os.rename(file, folder + '\\' + '({}) '.format(str(i)) + file)
                print('Moving', file, 'to', folder)
                break
            except FileExistsError:
                i += 1

    finally:
        os.system('cls')


for file in os.listdir(dir):

    done = False

    if file == 'sort_files.py':
        continue

    for key in ext_dict:
        for ext in ext_dict[key]:

            if file.endswith(ext):
                move(file, key)
                done = True

    if not done:
        if os.path.isdir(file):
            if file not in ('Docs', 'Other', 'Dirs', 'Photo&Video', 'URLs'):
                move(file, 'Dirs')
        else:
            move(file, 'Other')

print("""       
        Done!
        Press Enter to exit.   
    """)
input()
