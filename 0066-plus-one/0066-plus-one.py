class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new=0
        new=digits[-1]+1
        digits[-1]=new
        if (digits[-1]%10==0):
             r=digits[-1]%10
             n=digits[-1]/10
             digits.append(r)
             digits[len(digits)-2]=int(n)
        
        return digits
