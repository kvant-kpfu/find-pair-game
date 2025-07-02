import os
current_dir=os.getcwd()
print(current_dir)
os.chdir("C:\\Users\\Insaf\\PycharmProjects\\PythonProject\\")
print(os.getcwd())

print(os.listdir('.'))

def recreate_file(fileName):
    with open(fileName, 'w',encoding='utf_8') as f:
        f.write("Привет!\n")
        f.write("Это приер текстового файла.\n")
'''for i in range(10000):
    recreate_file(f"{i}.txt")
for i in range(10000):
    os.remove(f"{i}.txt")'''
def walk_directory(directory):
    for root, dirs, files in os.walk(directory):
        print(f"\nТекущая директория:{root}")
        print("Поддеректория:dirs")
        print("Файлы:",files)
walk_directory("C:\\Users\\Insaf\\PycharmProjects")