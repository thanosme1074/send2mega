#!/bin/python
import os, sys

# Install megatools pkg if not found in /bin
if os.path.exists("/bin/megaput") == False:
    os.system('apt-get install megatools')



#### NON-INTERACTIVE ####
if len(sys.argv) > 1:
    file = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]
    os.system(f'megaput -u "{email}" -p "{password}" "{file}"')
    sys.exit()


#### INTERACTIVE ####

# List files in current dir
FILES = []
for file in os.listdir():
    if os.path.isfile(file) == True:
        FILES.append(file)
def show_files():
    os.system('clear')
    for i in range(len(FILES)):
        print(f'  \033[33;1m[\033[35;1m{i+1}\033[33;1m] \033[0m\033[32;1m{FILES[i]}\033[0m')

# Get mega credentials
email = input(f'\n\n  \033[34;1mEnter your Email    : \033[36;1m')
password = input(f'  \033[34;1mEnter your password : \033[36;1m')

# Upload files to mega drive
show_files()
index = input(f'\n\n  \033[34;1mSelect file-index to upload\n  \033[30;1m[1-{len(FILES)}] \033[36;1m\033[36;1m')
file = FILES[int(index)-1]
show_files()
ans = input(f'\n\n  \033[0m\033[35mAre you sure to upload \033[35;1m\033[35;4m{file}\033[0m\033[35m to Mega Drive?\n  \033[30;1m[y|n] \033[36;1m')
if ans.lower() == 'y':
    os.system(f'megaput -u "{email}" -p "{password}" "{file}"')
