class Solution(object):
    def isValid(self, s):
        stack = []
        for e in s:
            if e in '[{(':
                stack.append(e)
            elif e == ')':
                if stack and stack[-1] == 







    



  

