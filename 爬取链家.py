import requests
from lxml import etree
import csv
class LanjiaSpider:
    def __init__(self):
        self.url="https://bj.lianjia.com/ershoufang/pg{}rs北京/"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}

    def parse_url(self,start_url):
        response=requests.get(start_url,headers=self.headers)
        response_str=response.content.decode()
        html=etree.HTML(response_str)
        return html
    def get_content_list(self,html):
        self.houseInfo = html.xpath('//div[@class="houseInfo"]/text()')
        self.title = html.xpath('//div[@class="title"]/a/text()')
        self.positionInfo = html.xpath('//div[@class="positionInfo"]/a/text()')
        self.totalPrice = html.xpath('//div[@class="totalPrice"]/span/text()')
        self.unitPrice = html.xpath('//div[@class="unitPrice"]/span/text()')
        self.followInfo = html.xpath('//div[@class="followInfo"]/text()')
        self.tag = html.xpath('//div[@class="tag"]/span/text()')
        #return houseInfo, title, positionInfo, totalPrice, unitPrice, followInfo, tag


    def xpath_houseInfo(self):
        for i in range(len(self.houseInfo)):
            yield self.houseInfo[i]
            self.qingxi_data_houseInfo()
            self.qingxi()
    def xpath_title(self):
        for i in range(len(self.title)):
            yield self.title[i]
            self.qingxi_data_title()
            self.qingxi()
    def xpath_positionInfo(self):
        for i in range(len(self.positionInfo)):
            yield self.positionInfo[i]
            self.qingxi_data_positionInfo()
            self.qingxi()
    def xpath_totalPrice(self):
        for i in range(len(self.totalPrice)):
            yield self.totalPrice[i]
            self.qingxi_data_totalPrice()
            self.qingxi()
    def xpath_unitPrice(self):
        for i in range(len(self.unitPrice)):
            yield self.unitPrice[i]
            self.qingxi_data_unitPrice()
            self.qingxi()
    def xpath_followInfo(self):
        for i in range(len(self.followInfo)):
            yield self.followInfo[i]
            self.qingxi_data_followInfo()
            self.qingxi()
    def xpath_tag(self):
        for i in range(len(self.tag)):
            yield self.tag[i]
            self.qingxi_data_tag()
            self.qingxi()


    def qingxi_data_houseInfo(self):  # 清洗数据
        self.get_houseInfo = self.xpath_houseInfo()

    def qingxi_data_title(self):  # 清洗数据
        self.get_title = self.xpath_title()

    def qingxi_data_positionInfo(self):  # 清洗数据
        self.get_positionInfo = self.xpath_positionInfo()

    def qingxi_data_totalPrice(self):  # 清洗数据
        self.get_totalPrice = self.xpath_totalPrice()

    def qingxi_data_unitPrice(self):  # 清洗数据
        self.get_unitPrice = self.xpath_unitPrice()

    def qingxi_data_followInfo(self):  # 清洗数据
        self.get_followInfo = self.xpath_followInfo()

    def qingxi_data_tag(self):  # 清洗数据
        self.get_tag = self.xpath_tag()
    def qingxi(self):
        i = 1
        while True:
            self.data_houseInfo = next(self.get_houseInfo)
            self.data_title = next(self.get_title)
            self.data_positionInfo = next(self.get_positionInfo)
            self.data_totalPrice = next(self.get_totalPrice)
            self.data_unitPrice = next(self.get_unitPrice)
            self.data_followInfo = next(self.get_followInfo)
            self.data_tag = next(self.get_tag)
            i+=1
            if i>len(self.data_houseInfo):
                break
    def save_content_list(self):
        self.xpath_houseInfo()  # 提取到数据之后调用其函数，遍历数据，把每一个数据遍历出来，方便存储
        self.xpath_title()
        self.xpath_positionInfo()
        self.xpath_totalPrice()
        self.xpath_unitPrice()
        self.xpath_followInfo()
        self.xpath_tag()
        with open(r"C:\Users\wy\Desktop\sublime\链家\linajiaxin2.csv", "a", newline="", encoding="utf-8-sig") as f:
            fieldnames = ['houseInfo', 'title', 'positionInfo', 'totalPrice', 'unitPrice', 'followInfo', 'tag']
            writer = csv.DictWriter(f, fieldnames=fieldnames)  # 写入表头
            writer.writeheader()
            list_1=['houseInfo', 'title', 'positionInfo', 'totalPrice', 'unitPrice', 'followInfo', 'tag']
            list_2=[self.data_title,self.data_title,self.data_positionInfo,self.data_totalPrice,self.data_unitPrice,self.data_followInfo,self.data_tag]
            list_3 = dict(zip(list_1, list_2))
            writer.writerow(list_3)
    def run(self):#实现主要逻辑
        #1.构造url
        i=1
        while True:
            start_url=self.url.format(i)
            #print(start_url)
            #2.发送请求，获取数据
            html=self.parse_url(start_url)
            #3.数据提取
            self.get_content_list(html)
            #4.数据保存
            self.save_content_list()
            i+=1
            if i>10:
                break
if __name__=="__main__":
    lanjia=LanjiaSpider()
    lanjia.run()


