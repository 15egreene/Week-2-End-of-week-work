# # Find Palindrome
# # Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).
# # Example Input: 
# string1 = "racecar"
# string2 = "Was it a car or a cat I saw"
# # Example Output: True 

# # see if a word is spelled forward and backwords


# def palindrome(x):
#     x = x.upper().replace(" ","")
#     first = 0
#     last = len(x) -1

#     while first > last:
#         if x[first] == x[last]:
#             first = first + 1
#             last -= 1
#         else:
#             return False
#     return True


# print(palindrome(string1))





# Example:2



# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).
# Example Input: 
string1 = "racecar"
string2 = "Was it a car or a cat I saw"
# Example Output: True 


def isPalindrome(s):
    # this doesn't account for spaces or capitalization
    for i in range(len(s)//2):
        # i starts as 0
        # I know the last index of the list is -1
        # so how do I get -1 if i's value is 0? -i-1
        if s[i] != s[-i-1]:
            return 'not a palindrome'
    return 'palindrome!'

isPalindrome('tacocat')
