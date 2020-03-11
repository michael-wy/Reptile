import re
import json
import requests
from urllib.parse import urlencode
import csv

class ZhilianSpider:
	def __init__(self):
		self.parameters={
		"pageSize":"90",
		"cityId":"530",
		"salary":"0,0",
		"workExperience":"-1",
		"education":"-1",
		"companyType":"-1",
		"employmentType":"-1",
		"jobWelfareTag":"-1",
		"kw":"数据分析师",
		"kt":"3",
		"at":"cb99c6d2181047e58d9b748e8a4a10f1",
		"rt":"916748eb964b4238b409d5b6f699af5a",
		"_v":"0.06510870",
		"userCode":"1023061592",
		"x-zp-page-request-id":"abed0baebab24a7c9bd4924e6d4e5d11-1563612701418-118361",
		"x-zp-client-id":"e6b7e554-cb9f-4c63-866d-ca091c1d12b5"
		}

		self.url="https://fe-api.zhaopin.com/c/i/sou?start={}&"

		self.headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
		}

	def parase_url(self,start_url):
		response=requests.get(start_url,headers=self.headers)
		#print(response)
		return response.content.decode()


	def get_content_list(self,json_str):
		dict_ret=json.loads(json_str)
		#print(dict_ret)
		content_list=dict_ret["data"]
		#print(type(content_list))
		content_list2=content_list["results"]
		#print(content_list2)
		#print(type(content_list2))
		for num in range(0,90):
			#print(num)
			shuju_str=content_list2[num]
			#print(type(shuju_str))
			#print(shuju_str)
			#print("\n")
			company=shuju_str['company']#g公司简要信息
			#print(company)
			#print("\n")
			job_str=shuju_str['jobName']#工作职称
			#print(job_str)
			#print("\n")
			company_str=shuju_str['company']['name']#公司名称
			#print(company_str)
			#print("\n")
			type_str=shuju_str['company']['type']['name']#公司类型
			#print(type_str)
			#print("\n")
			size_str=shuju_str['company']['size']['name']#公司人数
			#print(size_str)
			#print("\n")
			url_str=shuju_str['company']['url']#公司在智联上招聘的职位的详细网址
			#print(url_str)
			#print("\n")
			city=shuju_str['city']#城市
			#print(city)
			city_str=shuju_str['city']['display']#公司地点
			#print(city_str)
			salary_str=shuju_str['salary']#员工薪资
			#print(salary_str)
			welfare_str=shuju_str['welfare']#公司员工福利
			#print(welfare_str,salary_str)
			zongcontent_list=(job_str,company_str,type_str,size_str,url_str,city_str,salary_str,welfare_str)
			#print(zongcontent_list)
			#print(type(zongcontent_list))
			zongcontent_list1=list(zongcontent_list)
			#print(type(zongcontent_list1))
			#print(zongcontent_list1)
			list1=['工作职称','公司名称','公司类型','公司人数','公司招聘网址','公司地点','薪资','公司员工福利']
			list2=[job_str,company_str,type_str,size_str,url_str,city_str,salary_str,welfare_str]
			list3=dict(zip(list1,list2))
			#print(list3)
			print(list3['公司名称'])
			#print(type(list3))			
			with open(r"C:\Users\wy\Desktop\sublime\智联招聘爬取\datass9.csv","a",newline="",encoding="utf-8-sig") as f:
			#writer=csv.writer(filee)
			#writer.writerow(['工作职称','公司名称','公司类型','公司人数','公司招聘网址','公司地点','薪资'])
			#writer.writerow([list3])
				#fieldnames=['工作职称','公司名称','公司类型','公司人数','公司招聘网址','公司地点','薪资','公司员工福利']
				#writer=csv.DictWriter(f,fieldnames=fieldnames)
				#writer.writeheader()
				#writer.writerow(list3)


	def save_content_list(self,list3):

		with open(r"C:\Users\wy\Desktop\sublime\智联招聘爬取\datass21.csv","a",newline="",encoding="utf-8-sig") as f:
			#writer=csv.writer(filee)
			#writer.writerow(['工作职称','公司名称','公司类型','公司人数','公司招聘网址','公司地点','薪资'])
			#writer.writerow([list3])
			fieldnames=['工作职称','公司名称','公司类型','公司人数','公司招聘网址','公司地点','薪资']
			writer=csv.DictWriter(f,fieldnames=fieldnames)
			writer.writeheader()
			print(type(list3))
			print(list3['公司名称'])
			writer.writer(list3)

			print("保存成功！")

	def run(self):#实现主要逻辑
		#1.构造Url
		for i in range(0,10):
			start_url=self.url.format(i*90)+urlencode(self.parameters)
			print(start_url)
			#print("\n")
			#2.发送请求，获取响应
			json_str=self.parase_url(start_url)
			#3.提取数据
			list3=self.get_content_list(json_str)
			#4.保存
			self.save_content_list


if __name__=="__main__":
	zhilianspider=ZhilianSpider()
	zhilianspider.run()