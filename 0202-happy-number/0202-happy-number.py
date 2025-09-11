class Solution:
    def isHappy(self, n: int) -> bool:

        happy_num_dict = {}

        target = n

        while (True):

            sum_result = 0

            while (target != 0):
    
                sum_result += (target % 10) ** 2
                target = target // 10
                
            target = sum_result
            
            if target == 1:
                return True

            hash_value = target % 10

            if happy_num_dict.get(hash_value) is None:
                happy_num_dict[hash_value] = []
                happy_num_dict[hash_value].append(target)
                continue

            else:
                for i in range(len(happy_num_dict[hash_value])):
                    if happy_num_dict[hash_value][i] == target:
                        return False
                happy_num_dict[hash_value].append(target)
                continue

        
 
        