# Return the number of different transformations among all words we have
import string
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        keys = list(string.ascii_lowercase)
        values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = dict(zip(keys, values))
        translation = []
        for word in words:
            temp_word = list(word)
            temp_morse = ""
            translation.append(''.join([morse[x]for x in temp_word]))
        translation = set(translation)
        num_transformation = len(translation)
        return num_transformation
myobject = Solution()
num_transformation = myobject.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print num_transformation