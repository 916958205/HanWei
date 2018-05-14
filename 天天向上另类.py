#python 天天向上 1-5工作，6-7休息
dayup, dayfactor = 1.0, 0.01
for i in range (365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 + dayfactor)
    else:
        dayup = dayup * (1 - dayfactor)
print ("otherdayup:{:.2f}.".format(dayup))