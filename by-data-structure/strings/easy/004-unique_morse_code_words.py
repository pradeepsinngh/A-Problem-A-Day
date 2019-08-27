# Prob: Unique Morse Code Words
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, 
# as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)
