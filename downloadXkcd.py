import urllib.request
import requests
import bs4
import os
import re


def download(url):
    for time in range(1, 3):
        print('开始第 %s 次爬取...' % time)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="lxml")
        elem_url = soup.select('#comic img')

        if not elem_url:
            print('未找到任何图片网址！')
        else:
            picUrl = elem_url[0].get('src')
            picRes = requests.get('http:' + picUrl)
            picRes = picRes.url     # 得到图片文件的网址
            print('要爬取图片的网址为', picRes)
            picName = re.findall(r'/.*/(.*)', picUrl)       # 使用正则表达式提取图片名称
            print('爬取中...')
            urllib.request.urlretrieve(picRes, 'xkcd/' + picName[0], callback)
            print('爬取完成！\n')

        prevLink = soup.select('a[rel=prev]')[0]        # 获取上一张图片信息
        url = 'http://xkcd.com' + prevLink.get('href')      # 修改url信息，开始新的爬取


def callback(a1, a2, a3):
    """
        @a1:目前为此传递的数据块数量
        @a2:每个数据块的大小，单位是byte,字节
        @a3:远程文件的大小
    """
    download_pg = 100.0 * a1 * a2 / a3
    if download_pg > 100:
        download_pg = 100

    print("\t%.2f%%" % download_pg)


if __name__ == '__main__':
    setUrl = 'https://c.xkcd.com/random/comic/'        # 改为随机
    os.makedirs('xkcd', exist_ok=True)
    download(setUrl)