import os
import shutil

from_dir = "C:\\Users\\HP\\Downloads"
to_dir = "C:\\Users\\HP\\Desktop\\Document_Files"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name


        if os.path.exists(path2):
            print("Moving " + file_name + ".....")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2) 
            print("Moving" + file_name + "......")
            shutil.move(path1,path3)   
        


   # root,extension = os.path.splitext(list_of_files)
   # print("Root of the tha path: ", root)
 #    shutil.move(from_dir,to_dir)

#print(to_dir)
