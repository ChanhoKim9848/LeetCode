class Solution(object):
    def LemonadeChange(self, bills):
        
        five=ten=0
        for i in bills:
            if i == 5: five+=1
            elif i == 10: five, ten = five-1, ten+1
            elif ten>0: five, ten = five-1, ten-1
            else: five-=3
            if five < 0: return False
        return True

print(Solution.LemonadeChange(Solution,[5,5,5,10,20]))



        