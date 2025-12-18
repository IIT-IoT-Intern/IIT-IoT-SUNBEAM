#Math Modules
import math
print(math.sqrt(25))
print(math.pow(2,3))
print(math.sin(0.785398))
print(math.log(1))
print(math.factorial(4))
print(math.ceil(4.9))
print(math.floor(4.9))

#OS Modules
import os

# 1. Get current working directory
print("Current Working Directory:")
print(os.getcwd())

# 2. List files and folders in current directory
print("\nFiles and folders in current directory:")
print(os.listdir())

# 3. Create a new directory
dir_name = "demo_folder"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"\nDirectory '{dir_name}' created")
else:
    print(f"\nDirectory '{dir_name}' already exists")

# 4. Change directory
os.chdir(dir_name)
print("\nChanged Directory:")
print(os.getcwd())

# 5. Create a file inside the directory
file = open("sample.txt", "w")
file.write("This file is created using os module")
file.close()
print("\nFile 'sample.txt' created")

# 6. Go back to parent directory
os.chdir("..")

# 7. Remove file and directory
os.remove("demo_folder/sample.txt")
os.rmdir("demo_folder")
print("\nFile and directory removed successfully")
