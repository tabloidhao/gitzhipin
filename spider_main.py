'''
    主函数
'''
from my_zhipin_spider import html_downloader
from my_zhipin_spider import html_output
from my_zhipin_spider import html_parser
import random
import time
import pymysql

class BOSS_Main(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.Html_parser()
        self.output = html_output.HtmlOutputer()


    def start(self, keyword, baseURL, page_count):
        for i in range(1,page_count+1):
            # 获取网页内容
            content = self.downloader.get_page(baseURL, i, keyword)
            # 解析数据
            com_results = self.parser.parser(content)
            print("正在抓取第 %d 页数据, 有 %d 条数据" % (i, len(com_results)))
            # for lists in com_results:
            #     print(lists)
            # name_list = [com_name, job, salary, job_require, com_desc]
            # 保存数据到列表
            self.output.output(com_results)
            #等待1~3秒
            time.sleep(random.uniform(1, 3))


if __name__=='__main__':
    keyword = input('请输入抓取的关键词：\n')
    page_counts = input("请输入抓取总页数：\n")
    baseURL = "http://www.zhipin.com/job_detail/"
    bosszp = BOSS_Main()
    bosszp.start(keyword, baseURL, int(page_counts))
    print('finsh')

