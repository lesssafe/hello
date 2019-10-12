import hashlib
while True:
    a = input('输入加密的字符:')   #python3为input
    hashlib.md5().update(a.encode(encoding='utf-8'))
    print ('MD5加密前：'+ a)
    print ('MD5加密后：'+hashlib.md5().hexdigest())
