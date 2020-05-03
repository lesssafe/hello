#!/usr/bin/env python
# coding: utf-8
#2020/5/3
#Less is More
import requests
import re
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
nums=['25','50','75','100','125']#设置爬取页数
urls=['https://www.douban.com/group/beijingzufang/discussion?start=']#设置要爬取的豆瓣小组
for url in urls:
    for num in nums:
        urlget=url+num
        zfweb=requests.get(urlget,headers=headers)
        zfinfos=re.findall(r'<a href="(.*?)" title="(.*?)" class="">',zfweb.text)
        chapter_txt = open('/root/zf.txt','a+',encoding='utf-8')#建一个文本
        chapter_txt.write(str(zfinfos))#把内容写进去
        chapter_txt.close
        #print(zfinfos)
        for zfinfo in zfinfos:
            zfurl,zftitle=zfinfo
            zfcontent=requests.get(zfurl,headers=headers)
            zfrecontent=re.findall(r'"text": "(.*?)",',zfcontent.text)
            baocun=[zfurl,zftitle,zfrecontent]
            chapter_txt = open('/root/zfcontent.txt','a+',encoding='utf-8')#建一个文本
            chapter_txt.write(str(baocun)+'\n')#把内容写进去
            chapter_txt.close
print("爬取完成！")


# In[ ]:





# In[ ]:





# In[ ]:




