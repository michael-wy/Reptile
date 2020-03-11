import requests
import pandas as pd
class Spider_People():
    def __init__(self):
        self.url="http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds={}"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
        # 人口数量excel文件保存路径
        self.POPULATION_EXCEL_PATH = r'C:\Users\wy\Desktop\新建文件夹\population.xlsx'
    def requests_people_spider(self):
        """爬取人口数据"""
        #请求参数sj（时间）,zb（指标）
        #LAST70 表示 近70年
        #A0301 表示 总人口
        #A0302 表示 增长率
        #A0303 表示 结构
        #总人口
        self.dfwds1='[{"wdcode":"sj","valuecode":"LAST70"},{"wdcode":"zb","valuecode":"A0301"}]'
        #增长率
        self.dfwds2='[{"wdcode":"sj","valuecode":"LAST70"},{"wdcode":"zb","valuecode":"A0302"}]'
        #人口结构
        self.dfwds3='[{"wdcode":"sj","valuecode":"LAST70"},{"wdcode":"zb","valuecode":"A0303"}]'
        response1=requests.get(self.url.format(self.dfwds1),headers=self.headers)
        response2=requests.get(self.url.format(self.dfwds2),headers=self.headers)
        response3=requests.get(self.url.format(self.dfwds3),headers=self.headers)
        #将所有数据放在这里，年份为key,值为各个指标值组成
        #因为2019年数据还没有列入到年度数据表里，所以根据统计局2019年经济报告中给出的人口数据计算得出
        #数据顺序为历年数据
        population_dict={'2019':[2019,140005,71527,68478,84843,55162,10.48,7.14,3.34,140005,25061,97341,17603,43.82942439,25.74557483,18.08384956]}
        self.get_population_info(population_dict,response1.json())
        self.get_population_info(population_dict,response2.json())
        self.get_population_info(population_dict,response3.json())
        self.save_excel(population_dict)
        #return self.population_dict
        #print(response1.json())
        #print(response2.json())
        #print(response3.json())
    def get_population_info(self,population_dict,json_obj):

        print(json_obj)
        """提取人口数量信息"""
        datanodes=json_obj['returndata']['datanodes']
        for node in datanodes:
            #获取年份
            year=node['code'][-4:]
            # 数据数值
            data = node['data']['data']
            if year in population_dict.keys():
                population_dict[year].append(data)
            else:
                population_dict[year]=[int(year),data]
        return population_dict
    def save_excel(self,population_dict):
        """人口数据生成excel文件
        ：param population_dict :人口数据
        ：:return"""
        #.T是行列转换
        df = pd.DataFrame(population_dict).T[::-1]
        df.columns = ['年份', '年末总人口(万人)', '男性人口(万人)', '女性人口(万人)', '城镇人口(万人)', '乡村人口(万人)', '人口出生率(‰)', '人口死亡率(‰)',
                      '人口自然增长率(‰)', '年末总人口(万人)', '0-14岁人口(万人)', '15-64岁人口(万人)', '65岁及以上人口(万人)', '总抚养比(%)',
                      '少儿抚养比(%)', '老年抚养比(%)']
        writer = pd.ExcelWriter(self.POPULATION_EXCEL_PATH)
        # columns参数用于指定生成的excel中列的顺序
        df.to_excel(excel_writer=writer,index=False,encoding='utf-8',sheet_name='中国70年人口数据')
        writer.save()
        writer.close()
    def run(self):
        self.requests_people_spider()
        #self.get_population_info()
        #self.save_excel()
if __name__=="__main__":
    spider_popleo=Spider_People()
    spider_popleo.run()