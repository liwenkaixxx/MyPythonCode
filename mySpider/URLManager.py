#coding:utf-8

class UrlManager(object):
    def __int__(self):
        self.new_urls = set()#未爬取的url集合
        self.old_urls = set()#已爬取的url集合

    def hes_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size() != 0
    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''

        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,url):
        '''
        添加新的url->未爬取的url集合中
        :param url: 单个url
        :return:
        '''

        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def new_url_size(self):
        '''
        获取未爬取url集合的大小
        :return:
        '''

        return len(self.new_urls)
    def old_url_size(self):
        '''
        获取已爬取url集合的大小
        :return:
        '''

        return len(self.old_urls)












