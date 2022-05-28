# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



#         ANSWER
# =======================

# def find_anagram(word, anagram):

#     word = word.lower()
#     anagram = anagram.lower()

# # check if length is same
#     if(len(word) == len(anagram)):
#     # sort the strings
#         sorted_str1 = sorted(word)
#         sorted_str2 = sorted(anagram)	
# 	# the sorted strings are checked
#     if(sorted(sorted_str1)== sorted(sorted_str2)):
# 	    print("The strings are anagrams.")
#     else:
#         print("The strings are not anagrams.")		

# find_anagram("hello", "check")


def find_anagram(word, anagram):
    word = word.lower()
    anagram = anagram.lower()

# check if length is same
    if(len(word) == len(anagram)):
    # sort the strings
        sorted_str1 = sorted(word)
        sorted_str2 = sorted(anagram)

    if(sorted(sorted_str1)== sorted(sorted_str2)):
	    return True
    else:
        return False		

find_anagram("below", "elbow")
find_anagram("hello", "check")







