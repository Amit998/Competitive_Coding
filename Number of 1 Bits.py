class Solution:
    def hammingWeight(self, n: int) -> int:
        n=list(str(bin(n)))
        # print(n)
        return n.count("1")

# n = 00000000000000000000000000001011
# n = 00000000000000000000000010000000
n=int(input())
sl=Solution()
print(sl.hammingWeight(n))
