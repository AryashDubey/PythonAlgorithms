# 0414 - Third Maximum Number
class Solution:
    def thirdMax( nums=[]) -> int:
        nums= input("Please enter Numbers separated with a space").split() #asks for numbers and store it in a array
        nums.sort()
        print(nums[-3])
    thirdMax()
