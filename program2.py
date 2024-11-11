class Solution(object):
    def __init__(self):
        # define conversions here so that it can be used everywhere
        self.conversions = {
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
        prevValue = 0
        
        for char in reversed(s):
            value = self.conversions[char]
            if value < prevValue:  # we must subtract in these cases IV- is the example.
                total -= value
            else:  # we can add example VI
                total += value
            prevValue = value
        
        return total
