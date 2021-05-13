import string
class Solution:
    def isNumber(self, s):
        # if s == "1E9": return True

        Delta=[

            [0,1,2,3,9,9],
            [9,9,2,3,9,9],
            [8,9,2,4,5,9],
            [9,9,4,9,9,9],
            [8,9,4,9,5,9],
            [9,6,7,9,9,9],
            [9,9,7,9,9,9],
            [8,9,7,9,9,9],
            [8,9,9,9,9,9],
            [9,9,9,9,9,9]

        ]
        
        def char_to_input(c):
            if c in string.whitespace: return 0
            if c in '+-': return 1
            if c in '0123456789': return 2
            if c == '.': return 3
            if c == 'E': return 4
            if c == 'e': return 4
            return 5
        
        state=0
        for c in s:
            inp=char_to_input(c)
            state=Delta[state][inp]
            if state == 9: return False
        
        state=Delta[state][0]
        return state == 8

        




# s = "0"
s="1E9"
# s = "e"
# s = "."
# s = ".1"
# s="+6e-1"



sl=Solution()
print(sl.isNumber(s))
