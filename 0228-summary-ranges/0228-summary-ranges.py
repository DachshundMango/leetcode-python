class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        result = []

        first = None
        second = None

        for i in range(len(nums)):
            
            if first == None:
                first = nums[i]
            
            elif nums[i] > (first + 1):
                
                if second == None:
                    result.append(f"{first}")
                    first = nums[i]
                    
                
                elif nums[i] == (second + 1): 
                    second = nums[i]
                    
                
                else:
                    result.append(f"{first}->{second}")
                    first = nums[i]
                    second = None
                    
            
            elif nums[i] == (first + 1):
                second = nums[i]
                
            if i == len(nums) - 1:
                if second == None:
                    result.append(f"{first}")
                else:
                    result.append(f"{first}->{second}")
                break
            else:
                continue

        return result

            