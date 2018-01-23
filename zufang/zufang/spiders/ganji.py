import scrapy

class Ganji(scrapy.Spider):
    name = "zufang"
    start_urls = ["http://bj.ganji.com/fang1/"]

    def parse(self, response):
        print(response)

        title_list = response.xpath('.//*[@id="f_mew_list"]/div[6]/div[1]/div[3]').extract()
        money_list = response.xpath('.//div[@class="price"]/dl/dd[5]/div[1]/span[1]/text').extract()


        for i,j in zip(title_list,money_list):
            print(i,";",j)



