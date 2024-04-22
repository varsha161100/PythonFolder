import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hrs=int(time.strftime('%H'))
print(hrs)
# timestamp=time.strftime('%M min')
# print(timestamp)
# timestamp=time.strftime('%S sec')
# print(timestamp)

if (hrs>=1 and hrs<12):
    print("Good morning Dear!!!")
elif(hrs>=12 and hrs<17):
    print("good Afternoon Dear!!!")
elif(hrs>=17 and hrs<20):
    print("Good Evening dear!!!")
else:
    print("Good Night Dear!!!")