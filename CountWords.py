import string # import for string manipulation
import re

def CountWord(Text):
    """
    count the word freq from a Text string

    """

    # Count the Words with the Frequency from the Text list
    # print(Text[1]) -- check the structure of the Text var

    # STEP:1 Initialize the word_count dictionary
    word_count ={}

    # STEP:2 Add "." at the end of TEXT to make sure text ends
    if(Text[-1] != "."):
        Text = Text + "."
    
    # STEP:3 Split the Text in list of Lines? 
    # - could be used if Text need to be split into lines 
    # - Here not required as directly we can remove specific chars and get the final list of words
    
    # lines_of_Text = list(Text.splitlines())
    # lines_of_Text = [x for x in lines_of_Text if x!= ''] # remove '' elem from the list
    # print(lines_of_Text)

    # STEP:4 get all the words in a single list - still contain some ", ", "\", "."-"
    # all_words = [x.split() for x in lines_of_Text]
    # flat_list_all_words = [x for sublist in all_words for x in sublist]
    # print(flat_list_all_words)

    # STEP:5 remove specific characters from the flat list of words
    final_flat_list_of_words = re.sub('[-.\,:;/]', '', Text).split()
    #print(final_flat_list_of_words)

    # STEP:6 record the number of Occurence of the words from the "All text" list final_flat_list_of_words
    for word in final_flat_list_of_words:
        if word in word_count.keys(): # check if the word exist in the dict before
            word_count[word] = word_count[word]+1
        else:
            word_count[word] = 1
    
    return word_count



# 1. Program Begin here..
if(__name__ == "__main__"):

    # Read the text from the file Poem.txt
    TextFile = open("C:\\Users\\Prateek\\Anaconda3\\CodePrateek\\PythonBibleCode\\PythonBible\\Poem.txt", "r")
    Text = TextFile.read()
    TextFile.close()

    # Call to CountWords function
    words_dictionary  = CountWord(Text)
    key_words = words_dictionary.keys()
    sorted(words_dictionary)

    # Print output
    for word in key_words:
        print(word, words_dictionary[word])





