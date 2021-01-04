import os

print(os.getcwd())  # 显示当前工作目录
print(os.chdir('path'))     # 改变当前工作目录为path
print(os.listdir('dirName'))    # 返回dirName目录下所有文件和目录名
print(os.makedirs('folderName'))    # 新建文件夹，可指定绝对路径
print(os.rmdir('dirName'))  # 删除单级目录、文件夹
print(os.remove('fileName'))    # 删除一个文件
print(os.rename('oldName', 'newName'))  # 重命名文件
print(os.stat(''))  # 获取文件或目录信息
print(os.system('command'))     # 在终端窗口运行command
print(os.environ)   # 获取系统环境变量

print(os.path.dirname('path'))  # 返回该路径的父目录
print(os.path.basename('path'))     # 返回该路径的最后一个目录或文件，即基本名称
print(os.path.split('path'))    # 将path分割成路径名和文件名
print(os.path.getsize('fileName'))  # 获取文件大小，以字节为单位
print(os.path.abspath('path'))  # 返回参数的绝对路径字符串，这是将相对路径转为绝对路径的简便方法
print(os.path.exists('path'))   # 如果参数所指的文件或文件夹存在，就返回True，否则返回False
print(os.path.isabs('path'))    # 如果参数是一个绝对路径，就返回True，如果是一个相对路径则返回False
print(os.path.isfile('path'))   # 如果参数是一个文件，就返回True
print(os.path.isdir('path'))    # 如果参数是一个目录，就返回True
print(os.path.join('path', 'name'))     # 连接目录与文件名或者连接目录与目录，格式为path/name

