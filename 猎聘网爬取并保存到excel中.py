from selenium import webdriver
import requests
import pandas as pd
import time
from lxml import etree
class Liepin_Spider():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.url='https://www.liepin.com/zhaopin/?init=-1&headckid=null&fromSearchBtn=2&dqs=010&ckid=09022f7f2e15711a&degradeFlag=0&key=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&siTag=bFGQTbwE_AAQSb-u11jrBw%7EF5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_unknown&d_ckId=61e0fb93b7abee6bc900207d3e12bb26&d_curPage=0&d_pageSize=40&d_headId=3e63e19d053765eb20984b109e44287d&curPage={}'

    def get_url(self,start_url):
        self.driver.get(start_url)
        source = self.driver.page_source
        return source

    def xpath_html(self,source):
        html = etree.HTML(source)
        self.xinzi = html.xpath("//div[@class='job-info']//p/span[@class='text-warning']")#薪资
        self.area=html.xpath("//div[@class='job-info']//p/span[@class='area']")#地点
        self.edu=html.xpath("//div[@class='job-info']//p/span[@class='edu']")#学历
        self.jingyan=html.xpath("//div[@class='job-info']//p/span[4]")#经验
        self.xpath_jingyan()
        self.xpath_edu()
        self.xpath_area()
        self.xpath_xinzi()
        self.dict_text()

    def xpath_xinzi(self):
        self.salary_text=[]#只能保存一次url请求
        for salary in self.xinzi:
            # print(salary.text)
            self.salary_text.append(salary.text)
        # print(salary_text)
    def xpath_area(self):
        self.didian_text=[]
        for didian in self.area:
            # print(didian.text)
            self.didian_text.append(didian.text)
        # print(didian_text)

    def xpath_edu(self):
        self.xueli_text=[]
        for xueli in self.edu:
            # print(xueli.text)
            self.xueli_text.append(xueli.text)
        # print(xueli_text)
    def xpath_jingyan(self):
        self.jy_text=[]
        for jy in self.jingyan:
            # print(jy.text)
            self.jy_text.append(jy.text)
        # print(jy_text)
    def dict_text(self):
        # dict_str={'xinzi':self.salary_text,'didian':self.didian_text,'xueli':self.xueli_text,'jy':self.jy_text}
        dict_str = {'xinzi': self.salary_text}
        df=pd.DataFrame(dict_str)
        # df.columns=['薪资','地点','学历','经验']
        df.columns = ['薪资']
        writer = pd.ExcelWriter(r'C:\Users\wy\Desktop\sublime\python数据分析爬取招聘网站\猎聘网.xlsx')
        df.to_excel(excel_writer=writer, index=False, encoding='utf-8', sheet_name='数据分析师')
        writer.save()
        writer.close()


        # for i in zhiwei:
        #     a = i.text
        #     print(a)


    def run(self):
        #构造url
        i=0
        while True:
            start_url=self.url.format(i)
            # self.driver.get(start_url)
            source=self.get_url(start_url)
            self.xpath_html(source)
            i+=1
            time.sleep(10)
            if i>5:
                break




if __name__=="__main__":
    liepin_spider=Liepin_Spider()
    liepin_spider.run()


