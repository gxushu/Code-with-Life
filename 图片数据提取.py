
# coding=utf-8
'''
#该脚本的功能爬去数据库的图片数据
    1、载入数据地址
    2、修改Host
    3、修改存储文件路径
'''


import urllib.request
import urllib3
from time import strftime, sleep
import requests
import json
import time

from bs4 import BeautifulSoup

#分析页面
def getUrl(urls):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'Cookie': 'JSESSIONID=F56829C344F5270ABE238F9EBF6DB62A',
               'Host': '121.201.83.194:8040',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
               }

    # cookies = {
    # }
    resultPage = requests.get(urls, headers=headers)  # 在请求中设定头，cookie
    soup = BeautifulSoup(resultPage.text)  # 实例化一个BeautifulSoup对象
    scrr = soup.findAll('p')
    lst = scrr[0].text[1:][:-1].split(",{")
    imgLst = []
    for tab in lst:
        print(tab)
        if not str(tab).startswith("{"):

            tab = "{"+tab
        d1 = eval(tab)
        if d1["cameraNo"] == 1:
           # print(d1["imgUrl"])
            imgLst.append(d1["imgUrl"])
    for img in imgLst:
        print(img)
        try:
            urllib.request.urlretrieve(img, 'E:/code with life/Head Calculation/3/%s.jpg' % int(round(time.time() * 1000)))  #图片存入路径
        except urllib.error.HTTPError:
            continue
    print("over")

num =180
listpagNum = []
for i in range(1,1000):
    print(i)
    num = num + 30
    try :#,200019,200041,200085,200091,200095,200096,200102,200105,200107,200109,200163wu,200210
        #urls ="http://121.201.83.194:8040/ops-web//report/historyPic/queryPicListByVehicleIdForMore.html?vehicleId=88043&startTime=2018-10-01%2000:00:00&endTime=2018-10-31%2009:58:21&dbKey=dbGzky&pageSize="+str(num)
        #爬取数据的地址
        urls ="http://121.201.83.194:8040/ops-web//report/historyPic/queryPicListByVehicleIdForMore.html?vehicleId=75497&startTime=2019-03-01%2000:00:00&endTime=2019-03-25%2016:46:04&dbKey=dbGzky&pageSize="+str(num)
              #http://121.201.83.194:8040/ops-web//report/historyPic/queryPicListByVehicleIdForMore.html?vehicleId=75497&startTime=2019-01-01%2000:00:00&endTime=2019-01-21%2016:46:04&pageSize=140&dbKey=dbGzky
        print (urls);
        sleep(1)
        getUrl(urls)
    except SyntaxError:
        listpagNum.append(i)
        continue
        # print("replice")
        # urls = "http://hbky.e-trans.com.cn:15068/gps-web//report/historyPic/queryPicListByVehicleIdForMore.html?vehicleId=93112,102393,102394,102395,102396,102397,102398,102399,102401,102402,102404,102405,102407,102408,102409,102410,102411,102412,102413,102415,102416,102418,102420,102421,102424,102425,102426,102427,102428&startTime=2018-07-01%2000:00:00&endTime=2018-07-19%2010:03:30&pageSize="+str(num)
        # print(urls);
        # sleep(1)
        # getUrl(urls)
    print(num)
print(listpagNum)







