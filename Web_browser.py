import webbrowser
import requests
"""下载文件"""
# webbrowser.open('http://baidu.com')
res = requests.get('http://gutenberg.org/cache/epub/1112/pg1112.txt')
# res = requests.get('https://github.com/majido/clipper/releases/download/v1.2.1/clipper.apk')
print(type(res))        # 返回一个Response对象
# 检查对网页的请求是否成功，如果该值等于requests.codes.ok，就成功(HTTP协议中'OK'的状态码是200)
# print(res.status_code == requests.codes.ok)
# 同样可以在Response对象上调用raise_for_status()方法检查
print(res.raise_for_status())
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):      # iter_content()方法在每次迭代中，返回一段内容，需要指定一段包含多少字节
    playFile.write(chunk)
playFile.close()