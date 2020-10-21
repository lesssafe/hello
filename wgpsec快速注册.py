import requests,json,time

url='https://plat.wgpsec.org/api/user/register'

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
,'Accept':'application/json, text/plain, */*'
,'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
,'Accept-Encoding':'gzip, deflate'
,'Content-Type':'application/json;charset=utf-8'
,'Content-Length':'139'
,'Origin':'https://plat.wgpsec.org'
,'Connection':'close'
,'Referer':'https://plat.wgpsec.org/user/register'
,'Cookie':'_ga=GA1.2.1599219593.1599029682; __cfduid=d00b003603d24f763d13d807ccca2a3e31601451889; Hm_lvt_d31977bd4b59af272381996d54181816=1603250068; _gid=GA1.2.1929137260.1603250077; Hm_lvt_a6e73021b45476cfaee1302caada08c1=1603250252,1603266010; Hm_lpvt_a6e73021b45476cfaee1302caada08c1=1603266010'
}
code=input("请输入邀请码：")
data=json.dumps({"username":"","email":"","password":"","password2":"","inviteCode":code,"protocol":'true'})

r_post=requests.post(url,data,headers=headers)
print(r_post.text)
time.sleep(15)