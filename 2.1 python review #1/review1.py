import random
temperatures = []
for i in range(7):
	temperatures.append(random.randint(26, 41)) 

days_of_the_week=["Sunday","Monday","Tuesday","Wendsday","Thursday","Friday","Saturday"]
print(days_of_the_week[3])
print(temperatures)



def check_even(temperatures):
	count = 0
	for x in range(len(temperatures)):
		if(temperatures[x]%2!=0):
			count+=1

	return count


even_days = check_even(temperatures)
print(even_days)


good_days_count = even_days
index = 0

for temp in range(len(temperatures)-1):
	if(temperatures[temp]>temperatures[temp+1]):
		index = temp


highest_temp = temperatures[index]
highest_temp_day = days_of_the_week[index]

index =0
for temp in range(len(temperatures)-1):
	if(temperatures[temp]<temperatures[temp+1]):
		index = temp


lowest_temp = temperatures[index]
lowest_temp_day = days_of_the_week[index]


sum1=0
avg=0
for a in range(len(temperatures)):
	sum1+=temperatures[a]

avg = sum1/len(temperatures)

above_avg =0
for f in range(len(temperatures)):
	if(temperatures[f]>avg):
		above_avg+=1



	
for day in range(len(days_of_the_week)):
	print(days_of_the_week[day],":",temperatures[day])
print()
print("shelly had ",good_days_count," good days this week")


print("the lowest temperature ",lowest_temp)
print("the lowest temperature day ", lowest_temp_day)
print()
print("the highest temperature ",highest_temp)
print("the highest temperature day ", highest_temp_day)
print()
print("the average temperature is ",avg)


aboveavg = []
for f in range(len(temperatures)):
	if(temperatures[f]>avg):
		aboveavg.append(temperatures[f])

print("days above avg were: ",aboveavg)
