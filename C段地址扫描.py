import subprocess
import time
def subping():
   for i in range(1,256):
      ip_r=print_ip
      ip_r = ip_r+"%d"%i
      ret = subprocess.call("ping -n 1 %s"%ip_r,stdout=subprocess.PIPE)
      if ret == 0:
         print('%s is up'%ip_r,"  当前时间是：",time.ctime())
      elif ret == 1:
         print('%s is dowm'%ip_r,"  当前时间是：",time.ctime())
if __name__ == "__main__":
   print("***********C段扫描程序************lesssafe制作**************\n")
   print("输入实列：如果扫描192.168.1.0/24段，请输入192.168.1.\n")
   print_ip = input("请输入ip:")
   subping()
