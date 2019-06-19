import re
import datetime
currenttime=int('2019-06-07 10:18:18.398917')

#for xy in currenttime:
print(re.sub("\.", " ", currenttime))
lt1 = re.sub("\."," ",currenttime)
li1 = len(lt1)-7
print(lt1[0:li1])
current_time = lt1[0:li1]
current_time =datetime.datetime(current_time)
print(current_time)
"""    
for x in a:
    print(re.sub("\.", " ", x))
    lt=re.sub("\."," ",x)
    li=len(lt)-7
    print(lt[0:li])
"""
