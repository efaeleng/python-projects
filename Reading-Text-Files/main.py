# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename
from lib2to3.pgen2.token import COMMENT


def read_file_content(filename):
    #read the file content
   
    filename = './story.txt'
    with open(filename, 'r') as open_file: #open the file
        read_file = open_file.read() #read the file
    return read_file #print the file
# read_file_content(filename) #call the function

def count_words():
    words = read_file_content(filename) #call the function
    words_split = words.split() #split the words
    # print(words_split) #print the words
    words_dict = {} #create an empty dictionary
    for word in words_split: #for each word in the list
        if word in words_dict: #if the word is in the dictionary
            words_dict[word] += 1 #add 1 to the value
        else:
            words_dict[word] = 1
    return words_dict #return the dictionary
print(count_words()) #call the function and print the dictionary

#     return {"as": 10, "would": 20}