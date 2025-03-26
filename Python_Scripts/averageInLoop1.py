count = 0
sum = 0
print ('Before count:',count,' sum:',sum)
for value in [9,41,12,3,74,15]:
    count += 1
    sum += value
    print (count,sum,value)
print('After count:',count,' sum:',sum,' average:',sum/count)
