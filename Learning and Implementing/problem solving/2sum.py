nums = [3, 3]
target = 6

for index, num in enumerate(nums):
    for nest_index, nest_num in enumerate(nums):
        if num + nest_num == target:
            if index == nest_index:
                continue
            print(index, nest_index) #  return
