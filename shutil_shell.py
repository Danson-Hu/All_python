import shutil
import os
import send2trash
"""
    shutil模块包含一些函数，可以在python程序中复制、移动、删除、重命名文件，
    相当于Windows的copy、move、remove、rename命令
    使用os和shutil模块都将永久性删除文件夹或文件夹，保险起见可以使用send2trash模块把文件放入回收站
"""
# shutil.copytree()   # 可复制整个目录树
# shutil.rmtree(path)     # 删除path处的文件夹，包含该路径下的所有文件夹和文件
# send2trash.send2trash(file)      # 将file放入计算机的垃圾箱或回收站
