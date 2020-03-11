from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import re
import time
from lxml import etree
class Lagouspider:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.url="https://www.lagou.com/jobs/list_python%E5%BC%80%E5%8F%91/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput="#拉钩python开发工程师总url
        self.positions=[]
        #self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
    def run(self):
        self.driver.get(self.url)#打开浏览器，输入总的url地址
        while True:
            source=self.driver.page_source#获取总url获取的网页源码
            WebDriverWait(driver=self.driver,timeout=10).until(
                EC.presence_of_all_elements_located((By.XPATH,'//div[@class="pager_container"]/span[last()]'))
            )#timeout=10和EC的意思是显示等待，显示等待是表明某个条件成立之后才会执行获取元素的操作。反之如果没有出现想的要元素，最大等待时间为10S。until的意思是直到某某元素出现
            #print(source)
            #self.parse_url(source)  # 把网页源码带入到，下一页新的请求中，用于解析页面，获取小的url
            #return source
            try:
                next_page=self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')#用XPATH查询下一页的位置
                #a="pager_next_disabled"
                #for i in range(30):
                if "pager_next_disabled" in next_page.__getattribute__("class"):#看看下一页在这个class列表中与否，如果在就返回上一层，如果不在就执行next_page.click()
                    #if i ==29:
                    break
                else:
                    next_page.click()#点击下一页
            except:
                print(source)  #输入最后一页的源码
                time.sleep(0)#延迟1秒

    def parse_url(self,source):#获取小的url函数
        #source_str=self.run()
        html=etree.HTML(source)#用XPAth解析页面，获取小的url
        links=html.xpath('//div/a[@class="position_link"]/@href')#获取小的url为列表类型
        for link in links:#遍历网页内部的url
            print(link)#打印每一个遍历成功的小的 url
            self.requests_page(link)#调用函数，发送请求，调用内部url
            time.sleep(0)#延迟0.5秒
    def requests_page(self,link):#用于请求小的url网页的函数
        self.driver.get(link)#打开浏览器，放人小的url
        WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_all_elements_located((By.XPATH,'//span[@class="name"]/text()'))
        )#职位的发布者
        source=self.driver.page_source#获取网页源码
        self.parse_page(source)#放入函数中
    def parse_page(self,source):
        html=etree.HTML(source)
        position_name=html.xpath('//div/h1[@class="name"]/text()')
        jobs_request_spans=html.xpath("//div/dd[@class='job_request']//span")
        salary=jobs_request_spans[0].xpath('.//text()')[0].strip()
        city = jobs_request_spans[1].xpath(".//text()")[0].strip()
        city = re.sub(r"[\s/]", "", city)
        work_years=jobs_request_spans[2].xpath(".//text()")[0].strip()
        work_years=re.sub(r"[\s/]", "",work_years)
        education = jobs_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r"[\s/]", "", education)
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        # print(desc)
        position = {
            'name': position_name,
            'salary': salary,
            'city': city,
            'work_years': education,
            'desc': desc
        }
        self.positions.append(position)
        #print(position)
        print('=' * 40)
        with open(r"C:\Users\wy\Desktop\sublime\selenium\拉钩\拉钩文件\data.txt","a",encoding="utf-8") as f:
            f.write(position)
            print("成功写入！！！")
if __name__=="__main__":
    lagouspider=Lagouspider()
    lagouspider.run()
    lagouspider.parse_url()

