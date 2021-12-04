nums = [3,1, 2,4,5, 3,1, 2,4,5]
mylist = list(dict.fromkeys(nums))
print(dict.fromkeys(nums))
print(mylist)
if nums == mylist:
    print('No duplicate')
else:
    print('duplicate')

print(range(6)[4:3])

for i in nums[4:1]:
    print(i,2)