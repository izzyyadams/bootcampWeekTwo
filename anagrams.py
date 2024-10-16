class Solution(object):
    def findAnagrams(self, s, p):
        targetDict = {}
        checkDict = {}
        indReturn = []

        if len(p) > len(s):
            return indReturn

        for letter in p:
            if letter in targetDict:
                targetDict[letter] += 1
            else:
                targetDict[letter] = 1
        
        for ind in range(len(p)):
            if s[ind] in checkDict:
                checkDict[s[ind]] += 1
            else:
                checkDict[s[ind]] = 1
        
        if checkDict == targetDict:
            indReturn.append(0)
        
        # Start sliding the window
        for i in range(len(p), len(s)):
            outgoing_char = s[i - len(p)]
            checkDict[outgoing_char] -= 1
            if checkDict[outgoing_char] == 0:
                del checkDict[outgoing_char]
            
            incoming_char = s[i]
            if incoming_char in checkDict:
                checkDict[incoming_char] += 1
            else:
                checkDict[incoming_char] = 1
            
            if checkDict == targetDict:
                indReturn.append(i - len(p) + 1)
        
        return indReturn

          
