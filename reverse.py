class Solution(object):
    def reverseWords(self, s):
        start = 0
        end = 0
        tempList = []
        while end < len(s):
            if s[start] == " " and s[end] == " ":
                start += 1
                end += 1
            elif s[end] == " ":
                tempList.append(s[start:end])
                start = end
            elif end == len(s)-1 and s[end] != " ":
                tempList.append(s[start:end+1])
                end += 1
            else :
                end += 1
        
        tempList.reverse()
        return  " ".join(tempList)

            
        
