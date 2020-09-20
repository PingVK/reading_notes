import re
import os
import urllib

import requests


def get_page(keyword, page, n):
    """获取搜索页面"""
    page = page * n
    keyword = urllib.parse.quote(keyword, safe='/')
    url_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin + keyword + "&pn=" + str(page) + "&gsm=" + str(hex(page)) + "&ct=&ic=0&lm=-1&width=0&height=0"
    # print('URL:', url)
    return url


def get_picture(page_url):
    """获取图片链接"""
    try:
        html = requests.get(page_url).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls


def down_pic(pic_urls, word, download_path):
    """给出图片链接列表, 下载所有图片"""
    for i, pic_url in enumerate(pic_urls):
        if str(pic_url).split('.')[-1] not in ('jpg', 'jpeg'):  # 过滤一下图片格式
            continue
        try:
            pic = requests.get(pic_url, timeout=3)  # 连接超时设定的秒数
            save_path = os.path.join(download_path, word)  #  # 图片存储路径
            pic_name = str(i+1) + '.jpg'
            if not os.path.isdir(save_path):
                os.mkdir(save_path)
            with open(os.path.join(save_path, pic_name), 'wb') as f:
                f.write(pic.content)
                print('成功下载: %s' % os.path.join(save_path, pic_name))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue


def baidu_pictures(keyword, save_path, page_num=5):
    """
    下载百度图片
    :param keyword: 搜索关键字
    :param save_path: 保存路径
    :param page_num: 爬取的页数，一页对应60张图片
    :return: None
    """
    NUM = 60  # 1个page返回60张图
    all_pic_urls = []
    for page in range(page_num):
        url = get_page(keyword, page, NUM)
        pic_urls = get_picture(url)
        all_pic_urls.extend(pic_urls)
    down_pic(all_pic_urls, keyword, save_path)


if __name__ == '__main__':
    PATH = r'D:\picture'
    baidu_pictures('1080P壁纸', PATH, page_num=1)
