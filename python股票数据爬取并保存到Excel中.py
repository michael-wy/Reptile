import urllib.request
import re
import glob
import time

# 上海、深圳A/B股票，近期成交量前40支股票代码
allCodelist = [
    '601099', '601258', '600010', '600050', '601668', '601288', '600604', '600157', '601519', '600030',  # 上海A股
    '900902', '900941', '900948', '900938', '900947', '900932', '900907', '900906', '900903', '900919',  # 上海B股
    '000725', '300059', '002131', '300116', '002195', '002526', '002477', '000536', '300104', '000793',  # 深圳A股
    '200725', '200160', '200018', '200037', '200488', '200168', '200468', '200058', '200012', '200625'  # 深圳B股
]
for code in allCodelist:
    print('正在获取%s股票数据...' % code)
    if (code[0] == '6' or code[0] == '9'):  # A股
        url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
              '&start=20180101&end=20190228&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        print(url)
    else:  # B股
        url = 'http://quotes.money.163.com/service/chddata.html?code=1' + code + \
              '&start=20180101&end=20190228&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        print(url)
    urllib.request.urlretrieve(url,'H:\\python股票爬取数据\\' + code + '.csv')  # 需要提前新建好D盘的“股票”目录，将数据写入csv文件

csvx_list = glob.glob('d:\\股票\\*.csv')
print('总共发现%s个CSV文件' % len(csvx_list))
time.sleep(2)
print('正在处理............')
for i in csvx_list:
    fr = open(i, 'r').read()
    with open(r'H:\python股票爬取数据\csv_to_csv.csv', 'a') as f:  # 合并csv文件
        f.write(fr)
print('写入完毕！')