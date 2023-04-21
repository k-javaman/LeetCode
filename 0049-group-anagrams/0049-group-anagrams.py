class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {} # create an empty dictionary to store the anagrams
        for word in strs: # loop through each word in the input list
            sortedWord = ''.join(sorted(word)) # sort the characters in the word                                             and join them back into a string
            if sortedWord not in h: # if the sorted word is not in the dictionary
                h[sortedWord] = [word] # create a new key in the dictionary with        the sorted word as the key and the original wordas the value (in a list) 
            else: # if the sorted word is already in the dictionary
                h[sortedWord].append(word) # append the original word to the list                       of values for the key that corresponds to the sorted word
        final = [] # create an empty list to store the final output
        for value in h.values(): # loop through the values (which are lists of                                     anagrams) in the dictionary
            final.append(value) # append the list of anagrams to the final output                                  list
        return final # return the final output list of anagram lists