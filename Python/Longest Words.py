"""
Given a dictionary, find all of the longest words in the dictionary.

Example
Given

{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
the longest words are(is) ["internationalization"].

Given

{
  "like",
  "love",
  "hate",
  "yes"
}
the longest words are ["like", "love", "hate"].

Challenge
It's easy to solve it in two passes, can you do it in one pass?
"""

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        max_length, result = -1, []
        for i, word in enumerate(dictionary):
            if max_length == -1 or max_length < len(word):
                max_length = len(word)
                result = [i]
            elif max_length == len(word):
                result.append(i)
        return [dictionary[result[i]] for i in range(len(result))]
