import os, shutil
path = r"C:/Users/Zuhan Shahria/OneDrive/Pictures/Testing/"

file_name = os.listdir(path)
folder_names = ['JPEG files', 'JPG files', 'WEBP files', 'PNG files']


for i in range(0,4):
    if not os.path.exists(path + folder_names[i]):
        print(os.path.exists(path + folder_names[i]))
        os.makedirs(path + folder_names[i])

for file in file_name:
    if ".jpeg" in file and not os.path.exists(path + 'JPEG files/' + file):
        shutil.move(path + file, path + 'JPEG files/' + file)

    elif ".jpg" in file and not os.path.exists(path + 'JPG files/' + file):
        shutil.move(path + file, path + 'JPG files/' + file)

    elif ".webp" in file and not os.path.exists(path + 'WEBP files/' + file):
        shutil.move(path + file, path + 'WEBP files/' + file)

    elif ".png" in file and not os.path.exists(path + 'PNG files/' + file):
        shutil.move(path + file, path + 'PNG files/' + file)
    
