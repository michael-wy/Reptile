import requests
import json
import re
class DoubanSpider:
	def __init__(self):
		self.url="https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=20&page_start={}"
		self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
	def parse_url(self,start_url):
		response=requests.get(start_url,headers=self.headers)
		json_str=response.content.decode()
		return json_str
	def get_content_list(self,json_str):
		drict_str=json.loads(json_str)
		content_list=drict_str["subjects"]
		return content_list
	def save_content_list(self,content_list):
		with open(r"C:\Users\wy\Desktop\sublime\豆瓣爬取\data14.json","a",encoding="utf-8") as f:
			for content in content_list:
				f.write(json.dumps(content,ensure_ascii=False))
				f.write("\n")

	def run(self):
		#1.构造URL地址
		num=0
		while True:
			start_url=self.url.format(num)
			print(start_url)
			#2，发送请求，获取响应
			json_str=self.parse_url(start_url)
			#3，提取数据
			content_list=self.get_content_list(json_str)
			#4，保存
			self.save_content_list(content_list)
			num+=20
			if len(content_list)<19:
				break
if __name__=="__main__":
	doubanspider=DoubanSpider()
	doubanspider.run()