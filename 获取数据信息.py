#当当网商品种类链接，获取不同种类的所有图书

from bs4 import BeautifulSoup
import re
class _GetBookInfo():
    def __init__(self,opener):
        self.opener=opener

    def getPage(self,url):
        html = self.opener.open(url)
        html = html.read().decode("gbk")  # 网页数据
        with open("test.txt","w") as f:
            f.write(html)
        regex=re.compile("<span>/\d+</span>")
        valueNum=re.findall("\d+",regex.findall(html)[0])
        return int(valueNum[0])

    def getInfo(self,url):

        html = self.opener.open(url).read().decode("gbk")

        soup = BeautifulSoup(html,"html.parser")

        ulTag=soup.find("ul",class_="list_aa listimg",id=True)

        liTag=ulTag.find_all("li",id=True)

        data1=[]
        #遍历liTag
        temp=0
        for li in liTag:
            data = []
            try:
                data.append(li.find("p",class_="name").string)
                data.append(li.find("p",class_="star").a.string)
                data.append(li.find("p",class_="author").a.string)
                data.append(li.find("p",class_="publishing").a.string)
                data.append(li.find("p",class_="price").span.string)
                data.append(re.findall(r"/ .+ ",str(li.find("p", class_="publishing_time")))[0].replace(" ","").replace("/",""))
                data1.append(data)
            except:continue
        #print(data)
        return data1



'''
    def getDifferentSeriesBookUrl(self):
        html=self.opener.open(self.url).read().decode("gbk")

        soup=BeautifulSoup(html)
        #类别
        LB = []
        # 字典存储小类别对应的URL
        dictUrl = {}
        #outside  ---外层的div
        #_li      ---li层
        for outsideDiv in soup.find("div", class_="classify_books", id="floor_1").find_all("div", class_="classify_kind"):
            LB.append(outsideDiv.div.a.string)
            for _li in outsideDiv.find("ul").find_all("li"):
                if _li.a.string == "更多":
                    continue
                else:
                   # print(s.a.get("href"), s.a.string)
                    dictUrl[_li.a.string] = _li.a.get("href")

        return dictUrl,LB
'''