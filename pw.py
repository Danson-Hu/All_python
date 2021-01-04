#! /usr/bin/python3.5
import sys, pyperclip

PASSWORDS = {'email': 'querying',
             'blog': 'asdfghjkl',
             'youtube': 'zxcvbnm'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]  # 账户名
# sys.argv[]是用来获取命令行输入的参数的(参数和参数之间空格区分),sys.argv[0]表示代码本身文件路径（程序文件名）,所以从参数1开始,表示获取的参数了

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)

# print(pyperclip.paste())
