import requests
import re
print("**********lesssafe制作**********")
url = 'http://www.myxsw.com/book/250/chapter.html'
response = requests.get(url)
html = response.text
dl = re.findall(r'<ul class="clearfix chapter-list">.*?</ul>',html,re.S)[0]
chapter_info_list = re.findall(r'href="(.*?)" title="(.*?),更新',dl)
for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = 'http://www.myxsw.com%s'%chapter_url
    #print(chapter_url,chapter_title)
    chapter_response = requests.get(chapter_url)
    chapter_html = chapter_response.text
    chapter_content = re.findall(r'<div class="article-con">(.*?)</div>',chapter_html,re.S)[0]#正则匹配
    chapter_content = chapter_content.replace(' ','')#清洗
    chapter_content = chapter_content.replace('</p>','')
    chapter_content = chapter_content.replace('<p>','')
    chapter_txt = open('%s.txt'%chapter_title,'w',encoding='utf-8')#建一个文本
    chapter_txt.write(chapter_content)#把内容写进去
    print("*已经完成下载：",chapter_title)
