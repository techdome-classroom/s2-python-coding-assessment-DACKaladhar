class Solution(object):
    def __init__(self):
        self.d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s):
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = self.d[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total
