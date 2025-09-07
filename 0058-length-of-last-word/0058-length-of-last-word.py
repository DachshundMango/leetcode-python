class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        result = 0
        idx = len(s) - 1
                
        while (idx >= 0):
            if (s[idx] == " "):
                if result == 0:
                    idx -= 1
                    continue
                else:
                    break
            else:           
                result += 1 
                idx -= 1

        return result

