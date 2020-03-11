import requests
from lxml import etree  #解析XML字符串
import re
import time

#设计模式，面向对象编程
class Spider(object):
	#反反爬虫措施，加请求头部信息
	def __init__(self):
		self.headers={
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
		}

	def start_requests(self):
	#获取整体网页的数据requests
		for i in range(1,203):
			#print(i)
			print("===========正在抓取%s页========"% i)
			#print(i)
			response=requests.get("https://www.mzitu.com/page/"+str(i)+"/",header=self.header)
			html=etree.HTML(requests.content.decode())
			self.xpath_data(html)
			print(html)

	def xpath_data(self,html):
		#2,抽取想要的数据吗，标题，图片，xpath
		src_list=html.xpath('//ul[@id="pins"]/li/a/img/@data_original')
		alt_list=html.xpath('//ul[@id="pins"]/li/a/img/@alt')

		for src.alt in zip(src_list,alt_list):
			file_name=alt+".jpg"
			respons=requests.get(src,header=self.headers)
			print("正在抓取图片:"+file_name)
			#3.存储数据jpg  with open
			try:
				with open(file_name,"wb") as f:
					f.write(response.content)
			except:
				print("=========文件名有错误=======")
spider=Spider()
spider.start_requests()