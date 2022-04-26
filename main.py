import os
import zipfile
filelist = []
progress=0
path = input()
for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root,file))
for files in filelist:
    newfiledir=files.replace(path, path + " Zipped")
    while newfiledir[len(newfiledir) - 1] != "\\":
        newfiledir = newfiledir[:-1]
    newfiledir = newfiledir[:-1]
    os.makedirs(newfiledir,exist_ok=True)
    archive = zipfile.ZipFile(files.replace(path, path + " Zipped"), mode='w')
    print(files)
    archmame=files.replace(path, "")
    while "\\" in archmame:
        archmame=archmame[1:]
    archive.write(files, arcname=archmame,compress_type=zipfile.ZIP_DEFLATED )
    archive.close()
    progress=progress+1
    print(f"progress {progress}/{len(filelist)}")
