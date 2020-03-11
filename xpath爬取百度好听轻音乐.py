import requests
from lxml import etree
import re
import time

headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}

songID=[]            #歌曲sid
songName=[]          #歌曲名字
songNamee=[]         #歌曲作者
for i in range(0,2):
	url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
	response=requests.get(url,headers=headers)
	#print(response)
	r=response.content.decode()
	#print(r)
	html=etree.HTML(response.content.decode())
	#print(html)
	#歌曲的名字
	namelist=html.xpath('//ul/li/span/a[@target="play"]/./@title')
	#歌曲的sid
	idlist=html.xpath('//ul/li/span/a[@target="play"]/./@sid')
	#歌曲作者的姓名
	nameelist=html.xpath('//ul[@id="musicList"]/li/span[@class="artistName"]/a[@target="_blank"]/./@title')

	#print(pat1)
	#print(pat2)
	#print(pat3)

	songID.extend(idlist)
	songName.extend(namelist)
	songNamee.extend(nameelist)
	#print(songID)
	#print(songName)
	#print(songNamee)



for i in range(0,len(songID)):
	songurl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/7"
	#print(songurl)
	songname=songName[i]
	songnamee=songNamee[i]
	musicc=requests.get(songurl).content
	print("正在抓取第",i+1,"首",songname)
	with open(r"C:\Users\wy\Desktop\sublime\百度好听轻音乐\music\{},{}.mp3".format(songnamee,songname),"wb") as f:
		f.write(musicc)
time.sleep(0.5)


#歌曲链接
		#http://f2.htqyy.com/play7/33/mp3/7
		#http://f2.htqyy.com/play7/62/mp3/7


#歌单首页  http://www.htqyy.com/top/hot
#歌单第一页http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
#歌单第二页http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#歌单第三页http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
