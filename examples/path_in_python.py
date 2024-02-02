import os
import shutil

# full path to the file
print(os.path.abspath(__file__))
print(os.path.abspath('homework.py'))

# full path to the directory
print(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
print(PROJECT_ROOT_PATH)
print('The current directory is: ', os.getcwd()) # show current directory
os.chdir("../tmp") # Change current directory
print('The current directory is: ', os.getcwd()) # show current directory
os.chdir("../..")
print(os.listdir()) #list of directories


# work with path
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp"))
shutil.rmtree("../tmp")  # rm -rf todo быть осторожными с этой командой
print('The directory exist:', os.path.isdir("../tmp"))
os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp"))
print('The directory exist:', os.path.isdir("../tmp"))
#os.makedirs("nested1/nested2/nested3") #create several folders
#shutil.rmtree("nested1/nested2/nested3")  # rm -rf todo быть осторожными с этой командой

print('The information about :', os.stat("homework.py"))
# st_size — размер файла в байтах
# st_atime — время последнего доступа в секундах (временная метка)
# st_mtime — время последнего изменения
# st_ctime — в Windows это время создания файла, а в Linux — последнего изменения метаданных
