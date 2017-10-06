import math
import random
import matplotlib.pyplot as plt
from collections import OrderedDict

monthDays= OrderedDict([('January' ,31),('February' ,28),('March' ,31),('April' ,30),('May' ,31),('June' ,30),('July' ,31),
    ('August' ,31), ('September' ,30), ('October' ,31),('November' ,30),('December' ,31)])

monthlyTemp= OrderedDict()
tempMean = OrderedDict()

for month, days in monthDays.items():
    monthlyTemp[month] = random.sample(range(-4,30),days)
    tempMean[month] = sum(monthlyTemp[month]) / len(monthDays)

variances = OrderedDict()

for month,mean in tempMean.items():
    varianceList = list()
    for days in monthlyTemp[month]:
        varianceList.append(((mean - days) ** 2))
    
    variances[month] = sum(varianceList)


sd = OrderedDict({})
for month,variance in variances.items():
    sd[month] = math.sqrt(variance / monthDays[month])


colors = ("blue", "yellow", "green")

months = [1,2,3,4,5,6,7,8,9,10,11,12]



plt.scatter(months ,list(sd.values()),  c=colors)
plt.title('Temperature Standard deviation for each Month in a year  ')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.show()