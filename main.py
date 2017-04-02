#-encoding:utf-8
from 当当网图书爬取 import 获取数据信息 as bookInfo
from 当当网图书爬取 import KindLinks as kls
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import http.cookiejar
import re
import xlwt
import xlrd

def getCorrectUrl(url,page):
    if page==0:  return url
    url=url.replace("m/","m/pg"+str(page)+"-")
    return url


#url,当当网所有商品网页
url="http://category.dangdang.com/?ref=www-0-C"
#创建实例化对象
Cookie=http.cookiejar.CookieJar()
#创建处理器
CookieHandle=urllib.request.HTTPCookieProcessor(Cookie)
#创建opener
opener=urllib.request.build_opener(CookieHandle)
#模拟浏览器登录
header=\
    {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
head=[]
for key,value in header.items():
    elem=(key,value)
    head.append(elem)
opener.addheaders=head
#打开一次网页让opener具备Cookie
opener.open(url)

#首先获取相关链接从KindLinks
_kls=kls._FirstPageLinkToGetUrl(opener)
#书籍的链接数据
bdata=_kls.getDifferentSeriesBookUrl()

bdata_url=bdata[0]          #包含所有需要用的url
bdata_gd=bdata[1]           #大体描述
#bdata_count=bdata[2]        #每取出多少个url,创建一个表格
#把字典转换为list存储
bdata_url_name=[]
bdata_url_url=[]
print((list(bdata_url[0].values())))
for key in range(len(bdata_url)):
    bdata_url_url.append(list(bdata_url[key].values()))
    bdata_url_name.append(list(bdata_url[key].keys()))
print(bdata_url_name)
print(bdata_url_url[0])
#实例化对象
bio=bookInfo._GetBookInfo(opener)
#在excel中存储的格式
StyleinfoInExcel=["书名","评论数","作者","出版社","价格","出版日期"]
book=xlwt.Workbook(encoding="utf-8")
#用于统计总计书的数量
count=0

for _gd in range(len(bdata_url)):
    for _bdata in range(len(bdata_url_name[_gd])):
        page = bio.getPage(bdata_url_url[_gd][_bdata])           #获取页码数
        #
        sheetname=bdata_url_name[_gd][_bdata].replace("/", "-")
        try:
            sheet=book.add_sheet(sheetname=sheetname)
        except:continue
        print(sheetname+"正在写入...")
        for i in range(len(StyleinfoInExcel)):
            sheet.write(0,i,StyleinfoInExcel[i])
        #进行数据的读取和写入
        temp=0
        for CurrentPage in range(1,page,1):                                             #CurrentPage为实际爬取到的网页页码
            try:
                data=bio.getInfo(getCorrectUrl(bdata_url_url[_gd][_bdata],CurrentPage))          #数据保存到data中
                #将数据写入到Excel
                for i in range(len(data)):
                    temp+=1
                    for j in range (len(data[i])):
                        #print(data[i][j],end=" ")
                        sheet.write(temp,j,data[i][j])
                    count+=1
            except:continue
        print("已写入"+str(count)+"本书")
        print(sheetname+"写入完成...\r\n")
        
        if _bdata==len(bdata_url_name[_gd])-1:
            book.save(bdata_gd[_gd].replace("/","-")+".xls")
            book = xlwt.Workbook(encoding="utf-8")
            print("--------已完成"+bdata_gd[_gd])
print("写入完成，共计"+str(count)+"本书")



