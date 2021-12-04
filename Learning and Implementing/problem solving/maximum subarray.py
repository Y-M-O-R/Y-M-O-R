nums =  [1,1,-2]

if len(nums)<=1:
    #return nums[0]
    pass
else:
    subarray_sum = {}
    #single index
    for index in nums:
        subarray_sum[f'{index}'] = index

    for first_index in range(len(nums)):
        for second_index in range(len(nums)):
            if nums[first_index]!=nums[second_index]:
                sum=0        
                
                index_gap = nums[first_index:second_index+1]
            
                
                if len(index_gap)!=0:
    
                    for index in index_gap:
                        sum += index
                    subarray_sum[f'{first_index}-{second_index}'] = sum
                        
    
    max = int(list(subarray_sum.values())[0])
    
    
    for value in subarray_sum.values():
        if value>=max:
            max = value
            

    print(max)
print(subarray_sum)