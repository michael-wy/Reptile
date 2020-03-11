import requests
from lxml import etree
import re
import csv

class DoubanSpider:
	def __init__(self):
		self.url="https://movie.douban.com/review/best?start={}"
		self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

	def parse_url(self,start_url):
		response=requests.get(start_url,headers=self.headers)
		response_str=response.content.decode()
		return response_str

	def save_content_list(self,response_str):
		with open(r"C:\Users\wy\Desktop\sublime\豆瓣影评\yingping1.html","a",encoding="utf-8") as f:
			f.write(response_str)
			print("保存成功")
	def run(self):
		#1.构造url
		num=0
		while True:
			start_url=self.url.format(num)
			print(start_url)
			#2.发送请求，获取相应
			response_str=self.parse_url(start_url)
			print(response_str)
			#3.提取数据

			#4.保存
			self.save_content_list(response_str)
			if num>10:
				break
			num+=20

if __name__=="__main__":
	doubanspider=DoubanSpider()
	doubanspider.run()
