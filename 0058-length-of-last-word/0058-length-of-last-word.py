class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        last_word = ""
        idx = len(s) - 1
                
        while (idx >= 0):
            if (s[idx] == " " and last_word == ""):
                idx -= 1
                continue
            elif (s[idx] == " " and last_word != ""):
                break
            else:           
                last_word = last_word + s[idx]
                idx -= 1

        return len(last_word)

