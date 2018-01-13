#coding:utf-8

from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from URLManager import UrlManager
from HtmlParser import HtmlParser

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = DataOutput()
        self.output = DataOutput()

    def crawl(self,root_url):
        #添加入口
        self.manager.add_new_url(root_url)
        #判断url管理管理器中是否有新的url，同时判断抓取了多少个url
        while(self.manager.hes_new_url() and self.manager.old_url_size() < 100):
            try:
                #从url管理器中获取新的url
                new_url = self.manager.get_new_url()
                #html解释器抽取网页数据
                html = self.downloader.download(new_url)
                #将抽取的url添加到url管理器中
                self.manager.add_new_url(new_url)
                #将数据存储到文件
                self.output.stor_data(data)
                print("已经抓取%个链接"%self.manager.old_url_size())
            except Exception,e:
                print("crawl failed")
        #数据存储器将文件输出成指定格式
        self.output.output_html()



if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%88%AC%E8%99%AB&oq=attribute&rsv_pq=8192f6d20001bedd&rsv_t=a987xxo5NB23zS23wVXK59MdGyz3UuE2xnFfVmH%2Bt4I1QmcjicJWoKbaGug&rqlang=cn&rsv_enter=1&inputT=507&rsv_sug3=7&rsv_sug1=6&rsv_sug7=100&bs=attribute")



