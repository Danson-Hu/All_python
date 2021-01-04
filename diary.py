# 需求：新建月份文件夹，在里面新建该月所有日期的markdown文件和对应日期的文件夹，用于存放一些图片以便于预览
import calendar
import datetime
import os
import subprocess


# 新建月份文件夹（1到12个数字或者英文月份），再在对应文件夹下新建markdown文件（如20201102.md）和对应日期的文件夹（如20201102）
#
# Months = \
#     ["January",
#      "February",
#      "March",
#      "April",
#      "May",
#      "June",
#      "July",
#      "August",
#      "September",
#      "October",
#      "November",
#      "December"]
#
# for M in Months:
#     dirName = "C:\\Users\\H1827\\Desktop\\手账\\{}".format(M)
#     try:
#         if not os.path.exists(dirName):
#             os.makedirs(dirName)
#             print("Create", dirName, "folder")
#     except Exception as e:
#         print("Failed:", e)

# 获取今天年份
year = datetime.datetime.now().year
# 获取今天月份(数字)
monthNumber = datetime.datetime.now().month
# 转换为对应英文月份
month = calendar.month_name[monthNumber]
# 获取当天日期
date = datetime.datetime.now().strftime('%Y-%m-%d')
# 要新建的文件夹名称
folderName = "C:\\Users\\H1827\\Desktop\\Diary\\{}\\{}\\{}".format(year, month, date)
# 要新建的markdown文件
fileName = "C:\\Users\\H1827\\Desktop\\Diary\\{}\\{}\\{}.md".format(year, month, date)

try:
    if not os.path.exists(folderName):
        os.makedirs(folderName)
        print("Create", folderName, "folder")
except Exception as e:
    print("Failed:", e)

with open(fileName, 'a+') as fp:
    print("Create", fileName, "file")

subprocess.Popen(r"F:\MarkdownPad.2.4.2\MarkdownPad2.exe {}".format(fileName))




