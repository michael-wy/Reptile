import requests
import json#将字典 列表 转换为字符串
from lxml import etree 
def getOnePage(n):
	#字符串的格式化
	url = f'https://maoyan.com/board/4?offset={n*10}'
	#告诉服务器  我们是浏览器  字典
	header= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
	#.调用
	r = requests.get(url,headers=header)
	return r.text
def parse(text):
	#初始化 标准化
	html = etree.HTML(text)
	#提取我们想要的信息  需要xpath语法
	#names是列表  xpath返回一定是列表
	names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
	releasetimes = html.xpath('//p[@class="releasetime"]/text()')
	#zip函数是拉链函数
	#字典
	item = {}#dict
	for names,releasetimes in zip(names,releasetimes):
		
		item['names']= names
		item['releasetimes']=releasetimes
		#生成器  循环迭代
		yield item
#保存数据
def save2File(data):
	with open('movie.json','a',encoding='utf-8') as f:
		#把字典  列表  转化成字符串
		data=json.dumps(data,ensure_ascii=False)+'\n'
		f.write(data)
def run():
	for n in range(0,10):
		text = getOnePage(n)
		items = parse(text)
		for item in items:
			save2File(item)
if __name__=='__main__':
	run()