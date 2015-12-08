nums = []
for i in range(1,1001):
	nums.append(i)
relations = []
while True:
	if len(nums) > 0:
		number = nums[0]
		nums.remove(number)
		for i in nums:
			relations.append(str(number)+" -> "+str(i))
	else:
		break
for i in relations:
	print(i)