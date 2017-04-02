# dangdangwang
爬取当当网图书，未使用框架

main是主函数

KindLinks.py和 获取数据信息.py 是2个封装的类

KindLinks只有一个方法，它返回的是  listUrl---(name（小分类名称）,url（小分类对应的链接）) LB---(总的分类)

获取数据信息有2个方法，---getpage(),getinfo()  getpage()返回的是页码数，getinfo()返回的是每本书中的信息（书名，评论数，作者，出版社，价格，出版日期）
书名我没有进行进一步的解析，可能比较杂乱
