import webbrowser
import requests
import bs4
import sys
"""必应搜索输入的内容并打开4个网页"""


def BingSearch(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    linkElems = soup.select('h2 > a')       # 解析网页找到所有直接在<h2>元素之内的<a>元素，中间没有其他元素
    # print(linkElems)
    print(len(linkElems))
    numOpen = min(4, len(linkElems))        # 返回传入的整型或浮点型参数最小的一个，此处确保有4个；max()方法返回传入参数中最大的一个
    for i in range(numOpen):
        webbrowser.open(linkElems[i].get('href'))


if __name__ == '__main__':
    url = 'https://cn.bing.com/search?q=' + ' '.join(sys.argv[1:])
    webbrowser.open(url)
    BingSearch(url)