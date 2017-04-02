#当当网商品种类链接，获取不同种类的所有图书

from bs4 import BeautifulSoup

class _FirstPageLinkToGetUrl():
    def __init__(self,opener):
        self.opener=opener
        self.url="http://category.dangdang.com/?ref=www-0-C"


    def getDifferentSeriesBookUrl(self):
        html=self.opener.open(self.url).read().decode("gbk")

        soup=BeautifulSoup(html,"html.parser")
        #类别
        LB = []
        # 字典存储小类别对应的URL
        dictUrl = {}
        #
        temp=0
        count=[]
        #outside  ---外层的div
        #_li      ---li层
        for outsideDiv in soup.find("div", class_="classify_books", id="floor_1").find_all("div", class_="classify_kind"):
            LB.append(outsideDiv.div.a.string)
            temp=0
            for _li in outsideDiv.find("ul").find_all("li"):
                temp+=1
                if _li.a.string == "更多":
                    continue
                else:
                   # print(s.a.get("href"), s.a.string)
                    dictUrl[_li.a.string] = _li.a.get("href")
            count.append(temp)
        return dictUrl,LB,count
