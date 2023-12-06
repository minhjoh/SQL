class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = j = 0
        string = str()
        while i < len(word1) and j < len(word2):
            string = string + word1[i] + word2[j]
            i += 1
            j += 1
        while i < len(word1):
            string += word1[i]
            i += 1
        while j < len(word2):
            string += word2[j]
            j += 1
        return string 