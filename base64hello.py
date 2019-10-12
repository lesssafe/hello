import base64
print("base64加密，解密")
while True:
    nm=int(input("加密选择1，解密选择2:\n"))
    if nm==1:
        cmd = input("请输入要加密的内容:\n")
        command = base64.b64encode(cmd.encode('utf-8'))
        print ("加密结果",str(command,'utf-8'))
    elif nm==2:
        cmd = input("请输入要解密的内容:\n")
        command = base64.b64decode(cmd.encode('utf-8'))
        print ("解密结果：",str(command,'utf-8'))
    else:
        print("输入有误")
