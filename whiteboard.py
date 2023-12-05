# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

# Case insensitive
# only letters

# Given a Case insensitive string
# We want to check if the string forward is the same as the string backwards

def solution(some_string): # Always call the name of the function "solution"
    # Create a reversed copy of the string
    reversed_some_string = some_string[::-1]
    # Check if the lower cased version of reversed copy is equal to the lower cased version of original string
    if reversed_some_string.lower() == some_string.lower():
        # if it is, return True, 
        return True
    else:
        # if not return False
        return False

# def solution(string):
#     return string.lower() == string[::-1].lower()
