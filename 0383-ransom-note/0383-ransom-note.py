from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine_dict = Counter(magazine)

        ransom_list = list(ransomNote)

        for i in range(len(ransom_list)):
            if magazine_dict[ransom_list[i]] == 0:
                return False
            else:
                magazine_dict[ransom_list[i]] -= 1

        return True