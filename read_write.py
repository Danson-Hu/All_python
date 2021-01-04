import shelve
import os

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
# shelfFile.close()
print(type(shelfFile))
print(shelfFile['cats'])    # 保存为字典形式
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

print(os.getcwd())      # 获取当前工作目录
os.chdir(r'C:\Users\H1827\Desktop')     # 更改当前工作目录
print(os.getcwd())
print(os.listdir())     # 返回一个当前工作目录下所有文件夹和文件的列表


path = os.getcwd() + '\备注.txt'
# print(path)
print(os.path.split(path))      # 获取一个目录的目录名称和基本名称，生成至一个元祖
print(os.path.dirname(path))       # 获取目录名称
print(os.path.basename(path))       # 获取基本名称
print('该文件大小为：', os.path.getsize(path), '字节')        # 获取文件的字节数

pathfile = open(path)
print(pathfile.read())      # read()方法，以一个大字符串形式返回
pathfile.close()

pathfile1 = open(path)
print(pathfile1.readlines())        # readlines()方法，以字符串列表形式返回
pathfile1.close()
