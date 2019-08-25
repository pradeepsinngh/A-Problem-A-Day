# Prob: You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

class Solution(object):

    def countCharacters(self, words, chars):
        total = 0
        dictChar = {}
        for char in chars:
            if char not in dictChar:
                dictChar[char] = 1
            else:
                dictChar[char] += 1
            
        for word in words:
            count = 0
            for letter in word:
                validChar = True
            
                if letter not in dictChar.keys():
                    validChar = False
                    break
                else:
                    # the case when the character in the word is more than the available character
                    if word.count(letter) > dictChar[letter]:
                        validChar = False
                        break
                    else:
                        count += 1
                    
            if validChar and len(word) <= len(chars):
                total += count
            
        return total
