class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            sum_digit = 0
            while num > 0:
                sum_digit += num % 10
                num = num // 10
            num = sum_digit
        return num
        