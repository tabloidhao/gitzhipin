'''
    requests 获得网页内容
'''
import requests

class HtmlDownloader(object):
    #通过 url+页数+关键字 获取数据
    def get_page(self, baseUrl, page_num, keyword):
        param = {'query':keyword, 'scity':'101110100', 'page':page_num}
        #模拟浏览器
        header = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Referer': r'http://www.zhipin.com/job_detail/',
            'Connection': 'keep-alive'
        }
        r = requests.get(baseUrl, params=param, headers=header)
        if r.status_code is 200:
            # print(r.text)
            return r.text
        else:
            print('downloader error')