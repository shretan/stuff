import time
import datetime
lis=[]
for _ in range(int(input("number of queies"))):
    
    try:
        date_string = input("enter departure time in H:M format: ")
        x= time.strptime(date_string, '%H:%M')
    except ValueError :
        date_string = input("enter departure time in H:M format: ")
        x= time.strptime(date_string, '%H:%M')
    delay1=int(input("enter travel time expected"))
    date_second=input("enter reaching time in H:M format: ")
    y= time.strptime(date_second, '%H:%M')
    delay2=int(input("enter delay in reaching location"))
    ans=datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min).total_seconds()
    bans=datetime.timedelta(hours=y.tm_hour,minutes=y.tm_min).total_seconds()
    diff= (bans-ans)/60
    
    if int(diff) <= delay1+delay2:
        lis.append("reaches in time")
    else:
        lis.append("dos not reach in time")
print('\n\n'.join(lis))
