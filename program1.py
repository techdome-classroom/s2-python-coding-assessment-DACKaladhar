class Solution(object):
    def isValid(self, s):
        stack = []
        for e in s:
            if e in '[{(':
                stack.append(e)
            else:
                if not stack or stack[-1] != '(':
                    







    



  

