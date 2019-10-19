import random
import time
people=['王','王1','王2','王3','王4','王5','王6']
zjr=random.sample(people,4)
a=0
for i in zjr:
    a=a+1
    time.sleep(1)
    print('第%d名是:'%a,i)
