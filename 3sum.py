def threeSum(self, nums: List[int]) -> List[List[int]]:
        list1=[]
        result=[]
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                for k in range(2,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        list1.append(i)
                        list1.append(j)
                        list1.append(k)

                    result.append(list1)
                    list1.clear()
        
        return result
